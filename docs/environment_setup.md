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
