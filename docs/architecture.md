# Architecture

The repository mirrors the internal AIRE research environment to keep analytics, data generation, and governance aligned between MSU’s secured environment and this public synthetic-data mirror.

## Components
- **notebooks/**: Jupyter notebooks that replicate calculations for adoption-style indicators, workshop engagement, confidence deltas, and retrieval.
- **pipelines/**: Reusable Python modules for text processing, embeddings, and supporting logic.
- **api/**: Example clients and notebooks demonstrating REST interactions and local embedding generation against synthetic data.
- **data/**: Programmatically generated CSVs plus explicit JSON Schemas that document every column and type.
- **governance/**: Templates for provenance, model cards, release checklists, and responsible use guidance.
- **scripts/**: Utilities to generate data, build vector indexes, and validate the environment.
- **tests/**: Pytest suite covering schema validation, API utilities, and retrieval indexing.
- **.github/workflows/**: CI pipelines for linting, notebook execution, structural checks, and tests to keep the mirror reproducible.
