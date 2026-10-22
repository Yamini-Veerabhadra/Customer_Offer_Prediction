# Project summary for interviews

**Problem:** Predict term-deposit subscription responses from historical bank campaign contact features, and summarize campaign performance with reproducible business metrics.

**My approach:** Validate source records, compute campaign-level SQL/Power BI-ready KPIs, select only features available before contact, compare two interpretable classification approaches, evaluate on an untouched chronological holdout, explore simple campaign-history clusters, and expose a probability score through a local API.

**Why exclude duration?** Call duration becomes known only after the phone call. Using it for a pre-call scoring use case would overstate model accuracy through target-time leakage.

**Why PR-AUC?** Responses are relatively rare, so accuracy can mask missed positives; PR-AUC is useful for model selection in imbalanced classifications.

**What are limitations?** This is an older Portuguese term-deposit dataset, not current US banking data. It lacks customer IDs, unique customer identities, and treatment/control data. A probability score cannot claim causal improvement in marketing conversion. Model fairness and stability should be assessed before deployment.

**What I would improve with production data:** unique customer IDs, stable timestamps, repeat-contact controls, fair-model auditing, drift detection, outreach costs and a randomized campaign measurement design.

**Demo status:** Synthetic data demonstrates a working technical pipeline. Do not quote synthetic model performance as historical UCI results.
