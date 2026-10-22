# Power BI report guide

The completed report is `powerbi/Customer_Offer_Prediction.pbix`. It contains these pages:

1. **Campaign Overview** — total contacts, subscriptions, response rate, contact volume and response by job, dropdown filters.
2. **Customer Analysis** — subscription response rates by education, occupation, age group and previous campaign outcome.
3. **Prediction & Model Performance** — held-out Random Forest evaluation KPIs, actual versus predicted outcomes, probability bands, and validation/test comparison.
4. **Business Insights & Recommendations** — evidence-based findings, proposed investigations, and limitations.

The report uses `outputs/powerbi_campaign_contacts.csv`, `powerbi/TestPredictions.csv`, and `powerbi/ModelMetrics.csv`. Import source file paths are local to the original computer, so they may require updates in Power BI Desktop under **Transform data > Data source settings** when the project is moved.

**Metrics:** 41,188 campaign-contact records, 4,640 positive responses (11.27%). The model metrics on Page 3 relate to the 8,238-row held-out test period, not the full dataset.

`powerbi/CAMPAIGN_DASHBOARD_PREVIEW.html` is a separate web preview, not the native report. `powerbi/BUILD_REPORT_IN_POWER_BI_DESKTOP.md` is optional reconstruction/reference documentation.

Four report screenshots are provided in `Screenshots/`.
