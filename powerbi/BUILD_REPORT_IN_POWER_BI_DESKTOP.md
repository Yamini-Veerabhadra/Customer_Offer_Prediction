# Power BI report build — exact instructions

**Important:** `.pbix` is authored and saved by Microsoft Power BI Desktop (Windows). This package includes a standalone interactive HTML dashboard preview, real CSV data, ready DAX measures, a theme, and page-by-page visual directions. **A four-page Power BI Desktop-saved `.pbix` exists in this package. These instructions remain for rebuilding or changing the report.**

## Step 1 — Start the report
1. Download **Power BI Desktop** from Microsoft if not installed, then open it.
2. Home → Get data → Text/CSV → select `outputs/powerbi_campaign_contacts.csv`. Click **Transform Data** and rename the query `CampaignContacts`. Set `subscribed`, `age`, `campaign`, `previous`, `contact_record_id` to Whole number. **Close & Apply**.
3. Import `powerbi/TestPredictions.csv` and `powerbi/ModelMetrics.csv` via Text/CSV. Rename to `TestPredictions` and `ModelMetrics`. Set probability and Value to Decimal number; `actual_subscription`, `predicted_positive_50pct` to Whole number.
4. Do **not** automatically link `TestPredictions` to `CampaignContacts`: there is no shared contact ID in the test export. Disable automatically detected relationships for these three tables.
5. View → Themes → Browse for themes → select `powerbi/Campaign_Report_Theme.json`.
6. Modeling → New measure: add DAX formulas from `DAX_MEASURES.txt` **one at a time**, using the target table identified in the comments.

## Step 2 — Build four report pages

### Page 1 — Campaign overview
- 3 Cards: `[Campaign Contacts]`, `[Subscriptions]`, `[Response Rate]` (format response as % with one decimal).
- Clustered bar: Axis `job`, Values `[Campaign Contacts]`; sort descending.
- Clustered bar: Axis `education`, Values `[Response Rate]`.
- Bar: Axis `poutcome`, Values `[Response Rate]`.
- Slicers: `contact`, `marital`, `education`.
- Title: **Customer Offer Prediction — Campaign Overview**.

### Page 2 — Campaign patterns
- Clustered columns: X `month`, Y `[Campaign Contacts]`.
- Line chart: X `campaign`, Y `[Response Rate]` (contact attempt analysis, **not** chronological forecasting).
- Clustered columns: X `contact`, Y `[Response Rate]`.
- Scatter: X `age`, Y `campaign`, Size `[Campaign Contacts]` (optional).
- Text note: `Month is a text category covering records across years, not a full date.`

### Page 3 — Model performance (held-out data ONLY)
- Import `TestPredictions.csv` as directed in Step 1.
- Cards: `[Heldout Records]`, `[Heldout Precision]`, `[Heldout Recall]`.
- Clustered column: X `probability_band`, Y `Count of probability` (change aggregation to **Count**, then sort by band as needed).
- Clustered column: X `probability_band`, Legend `y`, Y `Count of y`.
- Table: `ModelMetrics[Split]`, `ModelMetrics[Metric]`, `ModelMetrics[Value]` (disable aggregation on Value).
- Text box: Held-out ROC-AUC 0.6794; PR-AUC 0.4895; F1 0.4770. These values are from `outputs/evaluation.json`, not estimates.
- Text note: `Training and validation results are separate from held-out test metrics. Contact duration was excluded from predictors to prevent leakage.`

### Page 4 — Data and limitations
- Cards: `[Average Age]`, `[Average Contact Attempts]`, `[Prior Campaign Share]`.
- Matrix: Rows `job`, Columns `poutcome`, Values `[Campaign Contacts]`, `[Response Rate]`.
- Text notes:
  - One row is a marketing **contact**, not necessarily a distinct individual customer.
  - Portuguese bank telemarketing data covers 2008–2010, not current live banking operations.
  - No evidence of causality or incremental offer uplift is claimed.
  - AI classifications are historical contact-response estimates, not credit decisions.
  - Full raw record includes `duration`, but it is excluded from pre-contact ML predictors.

## Step 3 — Save and verify
1. File → Save As → `powerbi/Customer_Offer_Prediction.pbix`.
2. Close and reopen the `.pbix` to confirm the report actually opens, cards and visuals populate, and no source paths are broken.
3. File → Export → PDF (optional) or take clear PNG screenshots of all four pages; store images under `docs/powerbi_screenshots/`.
4. In `README.md`, add links to the `.pbix` file and screenshots **only after these files exist**.
5. If source CSV files move, Power BI Desktop → File → Options and settings → Data source settings → Change Source.

## Notes
- A `.pbix` file cannot be converted reliably from an HTML page or CSV by changing the filename.
- Model metrics are from this project's chronological test and validation pipeline; do not call the model production-ready.
- Power BI Desktop's visual placement is a manual activity. The charts here are specified so the finished report is reproducible.
