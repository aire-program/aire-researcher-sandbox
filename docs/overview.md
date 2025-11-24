# Overview

The AI Researcher Developer Sandbox mirrors the internal Michigan State University environment used by the Applied AI Innovation & Research Enablement (AIRE) Program. It provides a safe, synthetic-data workspace where researchers can rehearse AI-enabled workflows without touching institutional or sensitive data.

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
