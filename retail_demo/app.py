from pathlib import Path
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

st.set_page_config(page_title='Retail Explorer', layout='wide')
st.title('Retail Explorer')
st.caption('Synthetic retail transactions • Educational demonstration')
df = pd.read_csv(Path(__file__).parent / 'data.csv')
missing = int(df.isna().sum().sum())
df = df.drop_duplicates().dropna()
q1, q3 = df.sales.quantile([.25, .75])
outliers = df.sales > q3 + 1.5 * (q3 - q1)
st.sidebar.header('Explore transactions')
regions = st.sidebar.multiselect('Region', sorted(df.region.unique()), default=sorted(df.region.unique()))
categories = st.sidebar.multiselect('Category', sorted(df.category.unique()), default=sorted(df.category.unique()))
months = st.sidebar.slider('Month range', 1, 12, (1, 12))
remove = st.sidebar.checkbox('Exclude high-sales IQR outliers')
st.sidebar.caption(f'{missing} missing cells; {int(outliers.sum())} high-sales outliers. Outliers are retained by default.')
if remove:
    df = df.loc[~outliers]
d = df[df.region.isin(regions) & df.category.isin(categories) & df.month.between(*months)].copy()
if len(d) < 10:
    st.warning('Select more transactions to display charts and models.')
    st.stop()
a, b, c = st.columns(3)
a.metric('Transactions', len(d))
b.metric('Sales', f'${d.sales.sum():,.0f}')
c.metric('Profit', f'${d.profit.sum():,.0f}')

def show(fig, explanation):
    fig.update_layout(template='plotly_white', margin=dict(t=60, b=30))
    st.plotly_chart(fig, use_container_width=True)
    st.caption(explanation)

show(px.treemap(d, path=['region', 'category'], values='sales', title='1. Sales hierarchy — treemap'), 'Area represents sales. Click a region to explore its categories.')
show(px.sunburst(d, path=['segment', 'category', 'channel'], values='sales', title='2. Customer and channel mix — sunburst'), 'Nested rings reveal the sales mix within each customer segment.')
flows = d.groupby(['region', 'category'], as_index=False).sales.sum()
labels = list(d.region.unique()) + list(d.category.unique())
show(go.Figure(go.Sankey(node=dict(label=labels), link=dict(source=[labels.index(x) for x in flows.region], target=[labels.index(x) for x in flows.category], value=flows.sales))).update_layout(title='3. Region-to-category sales — Sankey'), 'Link width represents sales flowing from regions to categories. Nodes can be dragged.')
show(px.parallel_coordinates(d, dimensions=['quantity', 'discount', 'sales', 'profit'], color='profit', title='4. Transaction profiles — parallel coordinates'), 'Brush an axis to inspect how transaction characteristics occur together.')
show(px.density_heatmap(d, x='discount', y='profit', nbinsx=12, nbinsy=20, title='5. Discount and profit density'), 'Cell intensity shows transaction counts. Discount relationships are partly encoded by the synthetic generator.')
show(px.violin(d, x='category', y='profit', color='category', box=True, title='6. Profit distributions — violin'), 'Distribution width indicates concentration. Compare typical profit and variability.')
show(px.line(d.groupby('month', as_index=False).sales.sum(), x='month', y='sales', markers=True, title='7. Monthly sales'), 'Compare total sales across the selected months.')
show(px.bar(d.groupby('channel', as_index=False).profit.sum(), x='channel', y='profit', title='8. Profit by channel'), 'Compare total contribution by sales channel.')
show(px.scatter(d, x='sales', y='profit', color='category', size='quantity', hover_data=['region', 'discount'], title='9. Sales versus profit'), 'Hover for transaction details. Large revenue can coexist with low or negative profit.')
st.header('Machine learning')
st.caption('Models use the current filtered data. Synthetic patterns demonstrate methods and do not support real business conclusions.')
features = ['quantity', 'discount', 'sales', 'profit']
k = st.slider('Number of clusters', 2, 5, 3)
d['cluster'] = KMeans(n_clusters=k, random_state=42, n_init=10).fit_predict(StandardScaler().fit_transform(d[features])).astype(str)
show(px.scatter(d, x='sales', y='profit', color='cluster', title='K-means transaction segments'), 'Inputs are standardized before clustering. Cluster labels have no inherent ordering.')
x = pd.get_dummies(d[['quantity', 'discount', 'category', 'region', 'channel']], drop_first=True)
x_train, x_test, y_train, y_test = train_test_split(x, d.sales, test_size=.25, random_state=42)
model = LinearRegression().fit(x_train, y_train)
prediction = model.predict(x_test)
st.write(f'Linear regression — held-out MAE: ${mean_absolute_error(y_test, prediction):.2f}; R²: {r2_score(y_test, prediction):.3f}')
st.caption('Predicts sales using quantity, discount, category, region and channel. Evaluation uses a 25% held-out split.')
st.download_button('Download filtered transactions', d.to_csv(index=False), 'filtered.csv', 'text/csv')
