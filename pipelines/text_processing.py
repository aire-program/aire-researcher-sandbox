"""Text preprocessing utilities for NLP pipelines."""

from __future__ import annotations

import re

import pandas as pd


def clean_text(text: str) -> str:
    """Normalize text by lowercasing and removing special characters."""
    if not isinstance(text, str):
        return ""
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return " ".join(text.split())


def load_and_clean_articles(path: str) -> pd.DataFrame:
    """Load articles CSV and apply text cleaning to abstracts."""
    df = pd.read_csv(path)
    if "abstract" in df.columns:
        df["cleaned_abstract"] = df["abstract"].apply(clean_text)
    return df