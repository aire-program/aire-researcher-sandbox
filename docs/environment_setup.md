# Environment Setup

Follow these steps to run the sandbox locally.

1. **Clone the repository**
   ```bash
git clone https://github.com/aire-program/aire-researcher-sandbox.git
cd aire-researcher-sandbox
```
2. **Create and activate a virtual environment**
   ```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```
3. **Install dependencies**
   ```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```
4. **Generate synthetic data**
   ```bash
python scripts/generate_synthetic_data.py
```
5. **Run tests**
   ```bash
pytest
```
6. **Launch the Streamlit workbench**
   ```bash
streamlit run app/main.py
```

You can also open notebooks directly in Jupyter or via the Colab badges listed in `docs/colab_index.md`. Each notebook contains a first-cell setup to install requirements automatically when running in Google Colab.

## Verify your setup
- Confirm data files exist: `data/sample_texts/articles_sample.csv`, `data/sample_tabular/experiments_sample.csv`, etc.
- Run `pytest` to validate schemas, API clients, and retrieval indexing.
- Import the app to check dependencies: `python -c "import app.main"`.
- GitHub Actions smoke tests mirror these steps automatically on pushes affecting app, pipelines, data, scripts, or requirements.

## Common setup issues and quick fixes
- **CSV files missing**: Rerun `python scripts/generate_synthetic_data.py`.
- **Import errors (app/api)**: Ensure the repo root is on `PYTHONPATH`; running from repo root with `pytest` handles this, or use `python -c "import app.main"` to confirm.
- **Dependency errors in Colab**: Rerun the first cell of any notebook; it installs required packages.
- **Slow installs in Colab**: Wait for the first cell to finish before running later cells.
