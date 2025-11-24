"""Project-level paths for datasets and artifacts."""

from __future__ import annotations

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

ARTICLES_PATH = DATA_DIR / "sample_texts" / "articles_sample.csv"
NOTES_PATH = DATA_DIR / "sample_texts" / "notes_sample.csv"
EXPERIMENTS_PATH = DATA_DIR / "sample_tabular" / "experiments_sample.csv"
METRICS_PATH = DATA_DIR / "sample_tabular" / "metrics_sample.csv"
SCHEMA_DIR = DATA_DIR / "schemas"
VECTOR_INDEX_PATH = DATA_DIR / "vector_index.pkl"
