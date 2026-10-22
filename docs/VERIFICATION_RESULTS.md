# Verification results — official UCI dataset

Data: `data/raw/bank-additional-full.csv` (41,188 historical marketing-contact records).

- Test suite: `3 passed`.
- Training: completed with no errors.
- Selected model: Random Forest, validation selection by PR-AUC.
- Held-out final chronological 20%: ROC-AUC 0.6794, PR-AUC 0.4895, precision 0.4748, recall 0.4791, F1 0.4770, Brier score 0.2114.
- Response count: 4,640 positive outcomes, response rate 11.265%.
- API `health()`: `status=ok`, `model_ready=true`.
- Example `/predict` function: returned estimated response probability 0.5898 for the sample request in `docs/EXAMPLE_API_REQUEST.json`.
- Preview charts: created from official UCI records in `docs/real_data_preview/`.

Still missing: Power BI Desktop-authored `.pbix`, public cloud API deployment, professional application UI, automated fair-use/fairness assessment. These are optional extensions, not claimed completed deliverables.
