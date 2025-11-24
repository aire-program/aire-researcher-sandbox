# Overview

The AIRE Researcher Sandbox summarizes adoption-style signals, workshop engagement, confidence deltas, and usage patterns using synthetic data. This repository is the public, synthetic-data mirror of the internal MSU environment, preserving structure and calculations while keeping all information non-sensitive.

**What**: Notebook and pipeline walkthroughs with aligned tests.  
**Why**: Provides consistent indicators to guide AI literacy efforts and resource planning without exposing operational data.  
**How**: Run the notebooks or pipelines to reproduce calculations; all views operate on synthetic data generated from the same schemas as the internal system.

## Purpose
- Provide a transparent, reproducible mirror of the internal AIRE research environment.
- Document how adoption indices, workshop metrics, confidence deltas, and usage patterns are derived.
- Support analytics staff, faculty, and research teams with clear WHAT/WHY/HOW framing and governance templates.

## Synthetic mirror of the internal environment
All datasets are generated via `scripts/generate_synthetic_data.py`. The schemas, file layouts, and pipelines match the internal MSU deployment without exposing operational records. Tests in `tests/` confirm schema alignment.

## How to use
1. Create a virtual environment and install dependencies from `requirements.txt`.
2. Run `python scripts/generate_synthetic_data.py` to materialize the CSV files.
3. Open notebooks in `notebooks/` to verify calculations or adapt them for local analytics.
4. Use governance templates in `governance/` to document provenance, confidence deltas, and release checks.

## Example end-to-end walkthrough
1. **Readiness check**: Run `pytest` to confirm schemas and utilities align with the synthetic mirror.
2. **Tabular indicators**: Use `notebooks/tabular_basics.ipynb` to inspect adoption and usage aggregates; extend features in `notebooks/tabular_modeling.ipynb`.
3. **Workshop narratives**: Explore `notebooks/text_cleaning.ipynb` and `notebooks/text_classification.ipynb` to summarize engagement notes.
4. **Retrieval-assisted insights**: Build and query the index with `notebooks/rag_build_index.ipynb` and `notebooks/rag_query.ipynb`.
5. **Governance**: Capture provenance with `governance/data_provenance_template.md` and summarize assumptions in `governance/model_card_template.md` before sharing outputs.

## Flow at a glance
- **Data generation** → `scripts/generate_synthetic_data.py`
- **Notebooks** → `notebooks/` (adoption, workshops, retrieval, prototype assistants)
- **Governance** → `governance/` templates applied alongside each workflow

## Program alignment
- Official component of the AIRE Program’s analytics portfolio.
- Complements the Applied AI Literacy Hub (pedagogy) and reports into program leadership.
- Provides a transparent, synthetic-data mirror of the internal MSU deployment for reproducibility and collaboration.
