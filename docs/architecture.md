# Architecture

The repository is organized to keep notebook-first experimentation clear and reproducible while mirroring the structure of the internal AIRE sandbox and aligning with other AIRE Program resources.

## Components
- **app/**: Minimal Streamlit workbench used to preview synthetic data, retrieval demos, and governance links.
- **pipelines/**: Jupyter notebooks for text, tabular, RAG, and prototype workflows. Each notebook includes a Colab-friendly setup cell and runs against local synthetic data.
- **api/**: Example clients plus notebooks showing simple REST interactions and local embedding generation.
- **data/**: Programmatically generated CSVs plus explicit JSON Schemas that document every column and type.
- **governance/**: Templates for provenance, model cards, release checklists, and responsible use guidance.
- **scripts/**: Utilities to generate data, build vector indexes, and validate the environment.
- **tests/**: Pytest suite covering schema validation, API utilities, and retrieval indexing.
- **.github/workflows/**: CI pipelines for full tests and lightweight smoke checks.
