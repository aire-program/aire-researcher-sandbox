"""Tests for API client helpers."""

from __future__ import annotations

from typing import Any, Dict

import numpy as np

from api.python.client_embeddings import EmbeddingsClient
from api.python.client_rest_api import ResearchAPIClient


class DummyResponse:
    def __init__(self, payload: Dict[str, Any]):
        self._payload = payload

    def raise_for_status(self) -> None:
        return None

    def json(self) -> Dict[str, Any]:
        return self._payload


class DummySession:
    def __init__(self, payload: Dict[str, Any]):
        self.payload = payload
        self.last_request = None

    def request(self, method: str, url: str, timeout: int = 5, **kwargs: Any) -> DummyResponse:
        self.last_request = {"method": method, "url": url, "kwargs": kwargs, "timeout": timeout}
        return DummyResponse(self.payload)


def test_rest_api_client_get_and_post() -> None:
    session = DummySession({"ok": True})
    client = ResearchAPIClient(base_url="https://example.test", session=session)

    health = client.health()
    assert health["status"] == "online"

    result_get = client.get_json("/path", params={"q": "test"})
    assert result_get["ok"] is True
    assert session.last_request["method"] == "GET"

    result_post = client.post_json("/path", payload={"name": "demo"})
    assert result_post["ok"] is True
    assert session.last_request["method"] == "POST"


def test_embeddings_client_similarity_and_search() -> None:
    client = EmbeddingsClient(max_features=16)
    texts = [
        "Synthetic research abstract about reproducibility.",
        "Notes on experimental design and treatment arms.",
        "Overview of responsible AI documentation practices.",
    ]

    embeddings = client.embed(texts)
    assert isinstance(embeddings, np.ndarray)
    assert embeddings.shape[0] == len(texts)

    similarity = client.similarity(texts[:2])
    assert similarity.shape == (2, 2)

    results = client.search("reproducibility", texts, top_k=2)
    assert len(results) == 2
    assert isinstance(results[0][1], float)
