# Environment Setup

## Prerequisites
- Python 3.10 or later
- Git

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/aire-researcher-sandbox.git
   cd aire-researcher-sandbox
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Generate synthetic data**
   ```bash
   python scripts/generate_synthetic_data.py
   ```

## Running the App
```bash
streamlit run app/main.py
```

## Running Tests
```bash
pytest
```
