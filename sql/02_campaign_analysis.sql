-- Contact-level conversion, NOT unique-customer conversion.
SELECT COUNT(*) contacts, SUM((y='yes')::int) subscriptions,
       ROUND(100.0*AVG((y='yes')::int),2) response_pct
FROM marketing.campaign_contacts;

SELECT job, COUNT(*) contacts, SUM((y='yes')::int) subscriptions,
       ROUND(100.0*AVG((y='yes')::int),2) response_pct
FROM marketing.campaign_contacts GROUP BY job ORDER BY contacts DESC;

SELECT poutcome, COUNT(*) contacts,
       ROUND(100.0*AVG((y='yes')::int),2) response_pct
FROM marketing.campaign_contacts GROUP BY poutcome ORDER BY contacts DESC;

SELECT month, contact, COUNT(*) contacts,
       ROUND(100.0*AVG((y='yes')::int),2) response_pct
FROM marketing.campaign_contacts GROUP BY month,contact ORDER BY contacts DESC;
