"""Semantic search utilities using cosine similarity."""

from __future__ import annotations

from typing import Any

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def search(
    query_vec: Any,
    index_matrix: Any,
    top_k: int = 5,
) -> tuple[np.ndarray, np.ndarray]:
    """Retrieve top-k documents using cosine similarity.

    Args:
        query_vec: Query vector (1, n_features).
        index_matrix: Document index matrix (n_docs, n_features).
        top_k: Number of results to return.

    Returns:
        Tuple of (indices, scores) for the top-k matches.
    """
    sims = cosine_similarity(query_vec, index_matrix).flatten()
    indices = sims.argsort()[::-1][:top_k]
    return indices, sims[indices]