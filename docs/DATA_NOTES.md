# Original UCI Bank Marketing: data notes

The project uses the `bank-additional-full.csv` **additional** variant (20 attributes plus target `y`, 41,188 records). Do not accidentally use the older 16-feature bank-full variant. Column names with dots are valid in Pandas; the SQL schema uses underscores.

- `y`: whether a contact led to a term-deposit subscription, yes/no.
- `duration`: call duration (post-contact leakage for pre-contact targeting), excluded from predictive inputs.
- `pdays=999`: no previous campaign contact recorded; this is not a literal 999-day gap.
- `unknown`: categorical unknown value; not necessarily missing numeric data.
- `contact`, `month`, `day_of_week`, `campaign`: contact-time information conservatively excluded from pre-contact prediction, but useful for descriptive campaign reporting.
- No customer IDs and no exact dates exist in this release. We cannot count unique customers or guarantee grouping by person. Original full variant is described by UCI as ordered by date.
- Predictive correlation ≠ increased conversions caused by targeting. Without randomized trial data, model outputs alone cannot measure targeting uplift.
- Demographic features require fairness review in any real application.

Source: https://archive.ics.uci.edu/dataset/222/bank+marketing ; Moro, Rita & Cortez (2014), CC BY 4.0.
