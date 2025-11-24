# AIRE Researcher Sandbox

A synthetic-data mirror of an internal Michigan State University GitLab deployment that supported research teams experimenting with safe, reproducible AI workflows. This repository is part of the AIRE Program and complements the Applied AI Literacy Hub by providing a technical, notebook-first sandbox with governance and testing baked in.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](docs/colab_index.md)

## Purpose and context
- Enable researchers to prototype AI-powered workflows using only synthetic data.
- Mirror institutional structures for responsible data handling without exposing sensitive information.
- Provide clear governance templates and testing patterns alongside runnable notebooks and a minimal Streamlit workbench.
- Make it easy to start in minutes with local or Colab execution; every notebook includes a first-cell dependency installer for Colab.

## 10-minute quickstart
- Install: `pip install -r requirements.txt`
- Generate data: `python scripts/generate_synthetic_data.py`
- Smoke check: `pytest` (schema, API client, and retrieval tests)
- Explore: `streamlit run app/main.py` or open any notebook via the Colab badge above or in `docs/colab_index.md`

## Components
- **Notebook-first architecture**: Jupyter pipelines for text, tabular, retrieval, and prototype workflows, runnable locally or in Google Colab.
- **Synthetic datasets + schemas**: Programmatically generated CSVs with explicit JSON Schemas to validate structure.
- **Streamlit workbench**: Minimal UI (`app/`) to preview data, run simple retrieval demos, and surface governance resources.
- **API examples**: Local clients and notebooks demonstrating REST calls and TF-IDF embeddings without external dependencies.
- **Governance toolkit**: Templates for responsible use, provenance, model cards, and release checklists.
- **CI and tests**: Pytest suite for schemas, API clients, and vector indexing; GitHub Actions for continuous validation.

## Relationship to AIRE Program and Applied AI Literacy Hub
This sandbox is the research-facing counterpart to the AIRE Program’s educational resources. While the Applied AI Literacy Hub focuses on pedagogy, this repository provides reproducible technical workflows, synthetic data, and governance assets for research teams. Together, they align responsible AI practice with practical experimentation.

## Synthetic data and safety
All datasets are generated via `scripts/generate_synthetic_data.py` and contain no real records. JSON Schemas in `data/schemas/` document every column, and tests enforce conformance.

## Streamlit workbench
Run `streamlit run app/main.py` after generating data to explore:
- Overview of dataset counts
- Text workflow previews (cleaning, clustering)
- Tabular summaries
- TF-IDF retrieval workbench
- API and governance resources

## Running locally
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Generate synthetic data:
   ```bash
   python scripts/generate_synthetic_data.py
   ```
3. Run tests:
   ```bash
   pytest
   ```
4. Launch Streamlit:
   ```bash
   streamlit run app/main.py
   ```

## CI and testing
- `.github/workflows/ci.yml` runs pytest on push/PR.
- `.github/workflows/smoke-tests.yml` regenerates data, checks required files, and imports the app.

## Colab access
Use the Colab launch buttons in `docs/colab_index.md` for one-click execution in Google Colab. Each notebook includes a setup cell to install dependencies when running in Colab.
