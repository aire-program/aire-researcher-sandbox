# Architecture

The Sandbox is structured as a modular Python application with distinct components for frontend interaction, data processing, and API simulation.

## Components

### 1. Streamlit App (`app/`)
The user interface is built with Streamlit, providing an interactive dashboard to browse data and test tools.
- `main.py`: Entry point.
- `pages/`: Individual modules (Overview, Pipeline Gallery, etc.).

### 2. Jupyter Pipelines (`pipelines/`)
Standalone notebooks that demonstrate specific research workflows.
- `text/`: NLP workflows.
- `tabular/`: Data cleaning and analysis.
- `rag/`: Retrieval-Augmented Generation patterns.

### 3. Synthetic Data (`data/`)
All data is generated programmatically to ensure privacy and safety.
- `scripts/generate_synthetic_data.py`: The source of truth for data generation.
- `schemas/`: JSON schemas defining the data structure.

### 4. Governance (`governance/`)
Templates and checklists to ensure responsible AI use.

### 5. CI/CD (`.github/`)
Automated testing ensures that the environment remains stable and reproducible.
