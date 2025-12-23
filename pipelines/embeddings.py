"""TF-IDF embedding utilities for text vectorization."""

from __future__ import annotations

import pickle
from pathlib import Path
from typing import Any, Sequence

from sklearn.feature_extraction.text import TfidfVectorizer


def fit_tfidf(texts: Sequence[str], stop_words: str = "english") -> TfidfVectorizer:
    """Fit a TF-IDF vectorizer on the given texts."""
    vectorizer = TfidfVectorizer(stop_words=stop_words)
    vectorizer.fit(texts)
    return vectorizer


def save_index(
    path: str | Path,
    vectorizer: TfidfVectorizer,
    matrix: Any,
    ids: Sequence[str],
) -> None:
    """
    Persist a vector index to disk.

    Warning: Uses pickle serialization. Only load indexes from trusted sources.
    """
    payload = {
        "vectorizer": vectorizer,
        "tfidf_matrix": matrix,
        "article_ids": list(ids),
    }
    with open(path, "wb") as f:
        pickle.dump(payload, f)


def load_index(path: str | Path) -> dict[str, Any]:
    """
    Load a vector index from disk.

    Warning: Uses pickle deserialization. Only load indexes from trusted sources.
    """
    with open(path, "rb") as f:
        return pickle.load(f)