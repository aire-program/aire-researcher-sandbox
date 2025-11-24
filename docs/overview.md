# Overview

The AI Researcher Developer Sandbox mirrors the internal Michigan State University environment used by the Applied AI Innovation & Research Enablement (AIRE) Program. It provides a safe, synthetic-data workspace where researchers can rehearse AI-enabled workflows without touching institutional or sensitive data.

**Who this is for:** Researchers, faculty, and staff who are comfortable with basic Python/Jupyter but new to applied AI workflows. No prior production experience required—this is a hands-on virtual lab with synthetic data.

## Purpose
- Offer a reproducible, notebook-first sandbox that aligns with institutional governance practices.
- Demonstrate text, tabular, retrieval, and API patterns using only synthetic datasets.
- Lower the barrier to experimentation for faculty, graduate researchers, and research staff who need documented examples before scaling to production environments.

## Synthetic mirror of the internal environment
All datasets are generated programmatically via `scripts/generate_synthetic_data.py`. The schemas, file layouts, and pipelines mirror the internal GitLab project while removing any real data. This ensures researchers can explore workflows locally or in Colab with full transparency.

## How to use
1. Create a virtual environment and install dependencies from `requirements.txt`.
2. Run `python scripts/generate_synthetic_data.py` to materialize the CSV files.
3. Explore notebooks in `pipelines/` or open the Streamlit workbench with `streamlit run app/main.py`.
4. Adapt the governance templates in `governance/` to document your own projects.

## Example end-to-end walkthrough
1. **Ingest and clean**: `pipelines/text/ingest_and_clean.ipynb` for text normalization; `pipelines/tabular/tabular_cleaning.ipynb` for tabular sanity checks.
2. **Explore and cluster**: `pipelines/text/clustering_and_topics.ipynb` to group abstracts; review clusters in the Streamlit **Text Workflows** page.
3. **Retrieve and answer**: Build an index with `pipelines/rag/build_index.ipynb`, query with `pipelines/rag/rag_query.ipynb`, and prototype answers in `pipelines/prototypes/minimal_research_assistant.ipynb`; mirror retrieval in the Streamlit **RAG Workbench**.
4. **Document governance**: Capture provenance with `governance/data_provenance_template.md` and summarize models in `governance/model_card_template.md` before sharing outputs.

## Flow at a glance
- **Data generation** → `scripts/generate_synthetic_data.py`
- **Notebooks** → `pipelines/` (clean, cluster, retrieve, prototype assistants)
- **App** → `streamlit run app/main.py` (overview, text/tabular previews, retrieval workbench, governance links)
- **Governance** → `governance/` templates applied alongside or after each workflow
