# SHL Assessment Recommendation System – Approach Document

## 1. Problem Understanding

Recruiters often struggle to identify the most relevant SHL assessments for a given job role due to reliance on keyword-based search and manual filtering. The objective of this project is to build an intelligent recommendation system that accepts a natural language hiring query or job description and returns a balanced set of relevant SHL assessments.

The solution must handle:

-   Free-text queries and job descriptions
-   Multiple skill domains (technical, behavioral, cognitive)
-   Efficient retrieval from a large catalog of assessments

---

## 2. Data Pipeline

The SHL Product Catalog was ingested from:
https://www.shl.com/solutions/products/product-catalog/

Only Individual Test Solutions were included, explicitly excluding Pre-packaged Job Solutions. The final catalog contains over 377 assessments. Each assessment record includes:

-   Assessment name
-   URL
-   Description
-   Test type (Knowledge, Personality, Cognitive)

The catalog is stored locally as `shl_catalog.csv` and used consistently across all stages of the pipeline.

---

## 3. Query Understanding and Retrieval Strategy

The system follows a retrieval-based approach:

1. User query or job description is received.
2. The query is optionally enriched using a lightweight LLM (Gemini) for intent clarification.
3. Both the query and assessment descriptions are converted into vector embeddings using `all-MiniLM-L6-v2`.
4. Cosine similarity is used to retrieve the most relevant assessments.

This approach enables semantic matching beyond keyword overlap.

---

## 4. Recommendation Balancing

Many hiring queries span multiple skill domains. To address this, recommendations are explicitly balanced across:

-   Knowledge & Skills (K)
-   Personality & Behavior (P)
-   Cognitive Ability (C)

The system ensures that when a query involves multiple domains (e.g., technical skills and collaboration), the output contains a mix of relevant assessment types.

Fallback logic is applied if a balanced split is not possible for a given query.

---

## 5. Evaluation Methodology

The system is evaluated using the provided labeled training dataset. Performance is measured using Mean Recall@10, defined as the fraction of relevant assessments retrieved in the top 10 results, averaged across all queries.

This evaluation is applied at the retrieval stage to ensure that the system retrieves relevant assessments before balancing.

Initial experiments used pure semantic similarity. Performance was improved by:

-   Query normalization
-   Balanced ranking across test types
-   Schema normalization of catalog data

---

## 6. API and System Design

The system exposes a REST API using FastAPI:

-   `/health` endpoint for service validation
-   `/recommend` endpoint for assessment recommendations

Responses follow the format specified in the assignment appendix, including assessment metadata and attributes.

A lightweight frontend is provided to allow interactive testing of the system.

---

## 7. Conclusion

The final solution provides a modular, scalable, and explainable recommendation system that satisfies all requirements of the SHL GenAI assignment. It combines semantic retrieval, balanced recommendation logic, and measurable evaluation to deliver relevant and reliable assessment recommendations.
