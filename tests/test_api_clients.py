"""Tests for API client helpers."""

from __future__ import annotations

import numpy as np

from api.python.client_embeddings import EmbeddingsClient
from api.python.client_rest_api import ResearchAPIClient


def test_rest_api_client() -> None:
    client = ResearchAPIClient()
    status = client.get_status()
    assert status["status"] == "online"
    assert "timestamp" in status

    projects = client.get_projects()
    assert isinstance(projects, list)
    assert {"id", "name", "owner"}.issubset(projects[0].keys())

    dataset_meta = client.get_dataset("TEST-123")
    assert dataset_meta["id"] == "TEST-123"
    assert dataset_meta["format"] == "csv"


def test_embeddings_client() -> None:
    client = EmbeddingsClient(max_features=16)
    texts = ["Hello world", "Test sentence", "Another sentence"]
    embeddings = client.embed(texts)

    assert isinstance(embeddings, np.ndarray)
    assert embeddings.shape[0] == len(texts)
    assert embeddings.shape[1] > 0

    similarities = client.similarity(texts[:2])
    assert similarities.shape == (2, 2)
    assert np.allclose(np.diag(similarities), 1.0)
