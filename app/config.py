"""Configuration constants for the Streamlit workbench."""

from __future__ import annotations

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
ARTICLES_PATH = DATA_DIR / "sample_texts" / "articles_sample.csv"
NOTES_PATH = DATA_DIR / "sample_texts" / "notes_sample.csv"
EXPERIMENTS_PATH = DATA_DIR / "sample_tabular" / "experiments_sample.csv"
METRICS_PATH = DATA_DIR / "sample_tabular" / "metrics_sample.csv"
VECTOR_INDEX_PATH = DATA_DIR / "vector_index.pkl"
PIPELINES_DIR = BASE_DIR / "pipelines"
GOVERNANCE_DIR = BASE_DIR / "governance"

COLAB_BASE = "https://colab.research.google.com/github/aire-program/aire-researcher-sandbox/blob/main/"
