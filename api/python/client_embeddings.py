"""Local TF-IDF embeddings client for demonstrations."""

from __future__ import annotations

from typing import Iterable, Sequence

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class EmbeddingsClient:
    """Generate embeddings using a local TF-IDF vectorizer."""

    def __init__(self, max_features: int = 512) -> None:
        self.vectorizer = TfidfVectorizer(max_features=max_features, stop_words="english")
        self._is_fitted = False

    def fit(self, corpus: Sequence[str]) -> None:
        """Fit the vectorizer on the provided corpus."""
        self.vectorizer.fit(corpus)
        self._is_fitted = True

    def embed(self, texts: Iterable[str]) -> np.ndarray:
        """Embed text into numeric vectors."""
        texts_list = list(texts)
        if not self._is_fitted:
            self.fit(texts_list)
        matrix = self.vectorizer.transform(texts_list)
        return matrix.toarray()

    def similarity(self, texts: Sequence[str]) -> np.ndarray:
        """Compute pairwise cosine similarity for the given texts."""
        embeddings = self.embed(texts)
        return cosine_similarity(embeddings)
