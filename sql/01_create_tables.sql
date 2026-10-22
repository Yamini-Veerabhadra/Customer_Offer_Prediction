-- Example PostgreSQL table for raw UCI bank-additional-full campaign contacts.
-- Not a unique-customer table.
CREATE SCHEMA IF NOT EXISTS marketing;
CREATE TABLE IF NOT EXISTS marketing.campaign_contacts (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    age INT, job TEXT, marital TEXT, education TEXT, "default" TEXT,
    housing TEXT, loan TEXT, contact TEXT, month TEXT, day_of_week TEXT,
    duration INT, campaign INT, pdays INT, previous INT, poutcome TEXT,
    emp_var_rate DECIMAL, cons_price_idx DECIMAL, cons_conf_idx DECIMAL,
    euribor3m DECIMAL, nr_employed DECIMAL,
    y TEXT CHECK (y IN ('yes','no'))
);
-- Use a staging COPY command with the original UCI columns in CSV order;
-- the generated id must be excluded from the COPY column list.
