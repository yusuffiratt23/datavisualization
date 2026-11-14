# Retail Explorer — Report Draft

This educational dashboard explores 3,000 synthetic retail transactions across 10 attributes. The included generator uses random seed 42. The dataset is artificial and has no external commercial source. Its purpose is to demonstrate exploratory visualization and reproducible analysis.

The analysis examines sales composition, profit distributions, discount relationships and monthly variation. Preprocessing removes duplicate and incomplete rows, identifies high-sales outliers using the 1.5-IQR rule and offers optional exclusion. The supplied generated data contains no missing cells.

Nine methods are implemented: treemap, sunburst, Sankey, parallel coordinates, density heatmap, violin, line, bar and scatter. Shared filters select regions, categories and months. Chart-specific interactions include hover, zoom, hierarchy navigation and axis brushing.

The generator assigns different price levels to categories and makes discount reduce revenue relative to costs. Consequently, category sales differences and negative-profit transactions illustrate designed patterns rather than independent discoveries. Use the dashboard to calculate and discuss the specific results for your chosen filters.

K-means explores standardized transaction profiles. Linear regression predicts sales and reports held-out MAE and R² using a 25% test set. Results depend on filters and synthetic assumptions and cannot be generalized to real retail operations.

GitHub repository: [ADD YOUR PUBLIC REPOSITORY URL]
Contributions: [ADD EACH MEMBER'S ACTUAL CONTRIBUTION]
