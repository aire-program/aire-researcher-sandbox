"""Build a simple TF-IDF index over synthetic article abstracts."""

from __future__ import annotations

import pickle
from pathlib import Path
from typing import Any, Dict, Tuple

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
ARTICLES_PATH = DATA_DIR / "sample_texts" / "articles_sample.csv"
INDEX_PATH = DATA_DIR / "vector_index.pkl"


def build_vector_index() -> Tuple[TfidfVectorizer, Any, pd.Series]:
    """Construct a TF-IDF index for article abstracts."""
    if not ARTICLES_PATH.exists():
        raise FileNotFoundError("Articles CSV not found. Run scripts/generate_synthetic_data.py first.")

    articles = pd.read_csv(ARTICLES_PATH)
    abstracts = articles["abstract"].fillna("")

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(abstracts)

    return vectorizer, tfidf_matrix, articles["article_id"]


def save_index(vectorizer: TfidfVectorizer, tfidf_matrix: Any, ids: pd.Series) -> Path:
    """Persist the index to disk using pickle."""
    payload: Dict[str, object] = {
        "vectorizer": vectorizer,
        "tfidf_matrix": tfidf_matrix,
        "article_ids": ids.tolist(),
    }
    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(INDEX_PATH, "wb") as fh:
        pickle.dump(payload, fh)
    return INDEX_PATH


def main() -> None:
    """Build and save the TF-IDF index, reporting basic stats."""
    vectorizer, tfidf_matrix, ids = build_vector_index()
    index_path = save_index(vectorizer, tfidf_matrix, ids)
    print(f"Vector index created with {tfidf_matrix.shape[0]} documents and {tfidf_matrix.shape[1]} features.")
    print(f"Saved index to {index_path}")


if __name__ == "__main__":
    main()
