"""Lightweight REST client used for demonstration purposes."""

from __future__ import annotations

import time
from typing import Any, Dict, List, Optional

import requests


class ResearchAPIClient:
    """Simple client that simulates calls to a research API."""

    def __init__(self, base_url: str = "https://api.example.research.msu.edu", session: Optional[requests.Session] = None):
        self.base_url = base_url.rstrip("/")
        self.session = session or requests.Session()

    def get_status(self) -> Dict[str, Any]:
        """Return a lightweight status payload."""
        return {"status": "online", "timestamp": time.time(), "base_url": self.base_url}

    def get_projects(self) -> List[Dict[str, str]]:
        """Return a synthetic list of projects without external calls."""
        return [
            {"id": "PROJ-001", "name": "AI in Education", "owner": "Research Group A"},
            {"id": "PROJ-002", "name": "Climate Modeling", "owner": "Research Group B"},
        ]

    def get_dataset(self, dataset_id: str) -> Dict[str, Any]:
        """Return synthetic dataset metadata."""
        return {
            "id": dataset_id,
            "size_mb": 128,
            "format": "csv",
            "access_level": "public",
            "description": "Synthetic dataset used for demonstration purposes.",
        }

    def fetch_json(self, path: str) -> Dict[str, Any]:
        """Attempt to GET a JSON payload; primarily for demonstration."""
        url = f"{self.base_url}/{path.lstrip('/') }"
        try:
            response = self.session.get(url, timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as exc:  # pragma: no cover - network optional
            raise RuntimeError(f"Request to {url} failed") from exc
