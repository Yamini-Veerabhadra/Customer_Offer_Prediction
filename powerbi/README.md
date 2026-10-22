# Power BI Dashboard

This folder contains the Power BI dashboard created for the **Customer Offer Prediction and Analysis** project.

I built the dashboard in Power BI Desktop to analyze bank marketing campaign performance, explore customer response patterns, and visualize the results of the machine learning model.

## Dashboard Pages

The report contains four pages:

1. **Campaign Overview** – Displays total marketing contacts, subscriptions, response rates, and campaign performance across job categories.

2. **Customer Analysis** – Explores response rates by education, job, age group, and previous campaign outcomes.

3. **Prediction & Model Performance** – Presents classification metrics, actual versus predicted outcomes, probability distributions, and validation versus test performance.

4. **Business Insights & Recommendations** – Summarizes key findings, potential business actions, and model limitations.

## Files

| File | Description |
|---|---|
| `Customer_Offer_Prediction.pbix` | Complete four-page Power BI Desktop report |
| `TestPredictions.csv` | Held-out test predictions used for model visualizations |
| `ModelMetrics.csv` | Validation and test performance metrics |
| `CAMPAIGN_DASHBOARD_PREVIEW.html` | Separate offline HTML dashboard preview |
| `DAX_MEASURES.txt` | Reference DAX calculations |

The campaign reporting data comes from `../outputs/powerbi_campaign_contacts.csv`.

Screenshots of all four Power BI pages are available in the [Screenshots folder](../Screenshots/).

## Opening the Dashboard

1. Open `Customer_Offer_Prediction.pbix` using Power BI Desktop.
2. Navigate through the four report pages.
3. Use the available filters and charts to explore campaign results.
4. If the CSV data sources are unavailable after moving the project to another computer, update their paths through **Transform data → Data source settings** in Power BI Desktop.

## Notes

The Power BI report uses historical UCI Bank Marketing data and model evaluation outputs generated through the Python pipeline.

The HTML dashboard preview is provided as an additional way to explore the project results. It is separate from the actual Power BI `.pbix` report.

The dashboard is intended for portfolio demonstration and exploratory analysis, not as a production banking decision system.