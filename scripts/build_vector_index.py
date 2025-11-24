"""Build a simple TF-IDF index over synthetic article abstracts."""

from __future__ import annotations

import pickle
import sys
from pathlib import Path
from typing import Any, Dict, Tuple

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from paths import ARTICLES_PATH, VECTOR_INDEX_PATH  # noqa: E402


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
    VECTOR_INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(VECTOR_INDEX_PATH, "wb") as fh:
        pickle.dump(payload, fh)
    return VECTOR_INDEX_PATH


def main() -> None:
    """Build and save the TF-IDF index, reporting basic stats."""
    vectorizer, tfidf_matrix, ids = build_vector_index()
    index_path = save_index(vectorizer, tfidf_matrix, ids)
    print(f"Vector index created with {tfidf_matrix.shape[0]} documents and {tfidf_matrix.shape[1]} features.")
    print(f"Saved index to {index_path}")


if __name__ == "__main__":
    main()
