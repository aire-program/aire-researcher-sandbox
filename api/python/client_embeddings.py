"""TF-IDF based embeddings client for text similarity demonstrations."""

from __future__ import annotations

from typing import Sequence

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class EmbeddingsClient:
    """Generate embeddings using a local TF-IDF vectorizer."""

    def __init__(self, max_features: int = 512) -> None:
        self._vectorizer = TfidfVectorizer(max_features=max_features, stop_words="english")
        self._is_fitted = False

    def fit(self, corpus: Sequence[str]) -> None:
        """Fit the vectorizer on the provided corpus."""
        self._vectorizer.fit(corpus)
        self._is_fitted = True

    def embed(self, texts: Sequence[str]) -> np.ndarray:
        """Transform texts into TF-IDF vectors."""
        texts_list = list(texts)
        if not self._is_fitted:
            self.fit(texts_list)
        return self._vectorizer.transform(texts_list).toarray()

    def similarity(self, texts: Sequence[str]) -> np.ndarray:
        """Compute pairwise cosine similarity for the given texts."""
        embeddings = self.embed(texts)
        return cosine_similarity(embeddings)

    def search(
        self,
        query: str,
        corpus: Sequence[str],
        top_k: int = 3,
    ) -> list[tuple[str, float]]:
        """Return top-k corpus entries most similar to the query."""
        if not self._is_fitted:
            self.fit(corpus)
        corpus_vectors = self._vectorizer.transform(corpus)
        query_vec = self._vectorizer.transform([query])
        scores = cosine_similarity(query_vec, corpus_vectors).flatten()
        ranked = sorted(zip(corpus, scores), key=lambda x: x[1], reverse=True)
        return ranked[:top_k]
