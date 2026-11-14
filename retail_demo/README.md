# Retail Explorer

An educational Streamlit dashboard for 3,000 synthetic retail transactions with 10 columns. Data is generated reproducibly by generate_data.py (seed 42). It represents no real retailer. Confirm that synthetic data is acceptable before using this example for your assignment.

## Run (Python 3.10+)

```sh
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

The included CSV allows offline data loading. Recreate it with `python generate_data.py`.

## Visualizations

Nine distinct methods: treemap, sunburst, Sankey, parallel coordinates, density heatmap, violin, line, bar and scatter. The first six are proposed advanced methods; confirm your instructor's classification. Every chart responds to sidebar filters. Plotly charts provide hover and/or direct selection, zoom or brushing as supported by the chart type.

Filters include region, category, month range and outlier exclusion. Missing rows and duplicate rows are removed; high-sales outliers are identified by the upper 1.5-IQR rule and optionally excluded. The supplied generated data has no missing values. Extreme valid transactions are retained by default.

K-means uses standardized quantity, discount, sales and profit. Linear regression predicts sales with a reproducible 75/25 train/test split and reports MAE and R². Synthetic relationships and filtered samples limit interpretation.

## Contributions — fill with actual work

- Member 1: [name and actual contributions]
- Member 2: [name and actual contributions]
- Member 3: [name and actual contributions]

## Submission preparation

Replace these placeholders, upload the project to a public GitHub repository, insert its link in report.md and prepare your English presentation. Check whether the instructor accepts synthetic data. The report is a draft and should be formatted to one page for submission.
