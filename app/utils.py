"""Shared utilities for the Streamlit workbench."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Iterable, List, Tuple

import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from app import config


def _load_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Expected data file not found: {path}")
    return pd.read_csv(path)


@st.cache_data
def load_articles() -> pd.DataFrame:
    """Load synthetic articles."""
    return _load_csv(config.ARTICLES_PATH)


@st.cache_data
def load_notes() -> pd.DataFrame:
    """Load synthetic notes."""
    return _load_csv(config.NOTES_PATH)


@st.cache_data
def load_experiments() -> pd.DataFrame:
    """Load synthetic experiment records."""
    return _load_csv(config.EXPERIMENTS_PATH)


@st.cache_data
def load_metrics() -> pd.DataFrame:
    """Load synthetic metrics."""
    return _load_csv(config.METRICS_PATH)


def clean_text(text: str) -> str:
    """Lightweight text cleaning for demonstrations."""
    return " ".join(text.lower().strip().split())


def build_tfidf_index(texts: Iterable[str]) -> Tuple[TfidfVectorizer, Any]:
    """Build a TF-IDF index for arbitrary text collection."""
    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform(list(texts))
    return vectorizer, matrix


def query_index(query: str, vectorizer: TfidfVectorizer, matrix: Any) -> List[float]:
    """Return cosine similarity scores for a query over an index."""
    query_vector = vectorizer.transform([query])
    scores = cosine_similarity(query_vector, matrix).flatten()
    return scores.tolist()
