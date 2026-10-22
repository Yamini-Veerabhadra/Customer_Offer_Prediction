// Power BI Desktop: Home > Transform data > New Source > Blank Query > Advanced Editor.
// Replace the path below with the actual local absolute path of your extracted project.
let
    Source = Csv.Document(File.Contents("C:\YOUR_PATH\customer-offer-prediction\outputs\powerbi_campaign_contacts.csv"),[Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    PromotedHeaders = Table.PromoteHeaders(Source,[PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(PromotedHeaders,{{"contact_record_id",Int64.Type},{"age",Int64.Type},{"subscribed",Int64.Type},{"campaign",Int64.Type},{"previous",Int64.Type}})
in
    Typed
