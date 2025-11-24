# Overview

The AIRE Researcher Sandbox mirrors the internal Michigan State University environment used by the Applied AI Innovation & Research Enablement (AIRE) Program. It provides a safe, synthetic-data workspace where researchers can rehearse AI-enabled workflows without touching institutional or sensitive data. This public mirror keeps the internal structure intact to support transparency and reproducibility across the AIRE Program, the Applied AI Literacy Hub, and the AIRE Impact Dashboard.

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
1. **Ingest and clean**: `notebooks/text_cleaning.ipynb` for text normalization; `notebooks/tabular_basics.ipynb` for tabular sanity checks.
2. **Explore and cluster**: `notebooks/text_classification.ipynb` to group abstracts; review clusters in the Streamlit **Text Workflows** page.
3. **Retrieve and answer**: Build an index with `notebooks/rag_build_index.ipynb`, query with `notebooks/rag_query.ipynb`, and prototype answers in `notebooks/minimal_research_assistant.ipynb`; mirror retrieval in the Streamlit **RAG Workbench**.
4. **Document governance**: Capture provenance with `governance/data_provenance_template.md` and summarize models in `governance/model_card_template.md` before sharing outputs.

## Flow at a glance
- **Data generation** → `scripts/generate_synthetic_data.py`
- **Notebooks** → `notebooks/` (clean, cluster, retrieve, prototype assistants)
- **App** → `streamlit run app/main.py` (overview, text/tabular previews, retrieval workbench, governance links)
- **Governance** → `governance/` templates applied alongside or after each workflow

## Program alignment
- Part of the AIRE Program’s research enablement portfolio.
- Complements the Applied AI Literacy Hub (pedagogy) and the AIRE Impact Dashboard (reporting and analytics).
- Provides a transparent, synthetic-data mirror of the internal MSU deployment for collaboration and reproducibility.
