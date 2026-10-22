# Final pre-upload checklist

**Already completed in this packaged revision**

- [x] Official UCI dataset included, attributed (CC BY 4.0).
- [x] 41,188 records processed; model trained and test results saved in `outputs/evaluation.json`.
- [x] Charts exported into `docs/real_data_preview/` and displayed from README.
- [x] All three project tests passed.
- [x] `api.main.health()` and a real model prediction validated.
- [x] Reporting-ready CSVs and original SQL queries included.

**You should check before making this a public portfolio**

1. Extract the ZIP, open the folder and read `README.md`.
2. Verify screenshots display and dataset citation appears on GitHub.
3. Optionally run `py -3 -m venv .venv`, activate it, install `requirements.txt`, `python -m pytest -q`.
4. Optionally run `python -m uvicorn api.main:app --reload` and open `http://127.0.0.1:8000/docs`.
5. The native four-page Power BI Desktop-authored report **is included** at `powerbi/Customer_Offer_Prediction.pbix`. Reopen and inspect all four pages after moving the project, and update local CSV source paths as required.
6. Public cloud API deployment has **not** been performed. Do not call this a production or deployed service.
7. Upload *contents* of `customer-offer-prediction/` to GitHub, including hidden `.github` and `.gitignore`. Note `outputs/model.joblib` is ~14MB and is a trusted locally generated binary; GitHub can store it, but do not load untrusted joblib files.
8. On GitHub inspect README, images and Actions status.

Do not invent ML accuracy, model lift, paid-company use cases or professional AI experience.
