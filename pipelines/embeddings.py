import pickle
from typing import Any, Dict, List
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def fit_tfidf(texts: List[str], stop_words: str = "english") -> TfidfVectorizer:
    """Fit a TF-IDF vectorizer."""
    vectorizer = TfidfVectorizer(stop_words=stop_words)
    vectorizer.fit(texts)
    return vectorizer

def save_index(path: str, vectorizer: Any, matrix: Any, ids: List[str]) -> None:
    """Save the vector index to disk."""
    payload = {
        "vectorizer": vectorizer,
        "tfidf_matrix": matrix,
        "article_ids": ids,
    }
    with open(path, "wb") as f:
        pickle.dump(payload, f)

def load_index(path: str) -> Dict[str, Any]:
    """Load the vector index from disk."""
    with open(path, "rb") as f:
        return pickle.load(f)