"""Tests for vector indexing utilities."""

from __future__ import annotations

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

from paths import ARTICLES_PATH
from scripts.build_vector_index import build_vector_index


def test_vector_index_build_and_query() -> None:
    df = pd.read_csv(ARTICLES_PATH)
    vectorizer, matrix, ids = build_vector_index()

    assert matrix.shape[0] == len(df) == len(ids)
    assert matrix.shape[1] > 0

    query_vec = vectorizer.transform(["reproducible research methods"])
    scores = cosine_similarity(query_vec, matrix).flatten()
    assert len(scores) == len(df)
    assert scores.max() >= 0
