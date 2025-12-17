# SHL Product Catalog Ingestion

To build the recommendation engine, the SHL Product Catalog was ingested and stored locally.

## Data Source

https://www.shl.com/solutions/products/product-catalog/

## Scope

-   Only **Individual Test Solutions** were included
-   **Pre-packaged Job Solutions** were explicitly excluded
-   Final dataset contains **377+ assessments**

## Ingestion Approach

Due to the dynamic nature of the SHL catalog website (JavaScript-rendered content),
a controlled ingestion approach was used:

1. The catalog pages were explored and filtered using the SHL UI.
2. Relevant assessment metadata was collected:
    - Assessment name
    - URL
    - Description
    - Test type (K / P / C)
3. The extracted data was normalized and stored locally as:
