# Usage Patterns for Researchers

## 1. Exploratory Data Analysis (EDA)
Use the `01_Overview` page in the app to quickly inspect dataset statistics. Then, open `pipelines/tabular/tabular_cleaning.ipynb` to start working with the data programmatically.

## 2. Prototyping RAG Systems
If you are interested in building a chatbot for your literature review:
1. Run `pipelines/rag/build_index.ipynb` to index the synthetic articles.
2. Use `pipelines/rag/rag_query.ipynb` to test queries.
3. Use the **RAG Workbench** in the Streamlit app to visualize results interactively.

## 3. API Integration
Use the mock clients in `api/python/` to simulate connecting to external services. This allows you to write your data ingestion code before you have access to the real API keys.
