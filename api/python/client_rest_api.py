"""Simple REST client utilities for synthetic mirror demonstrations."""

from __future__ import annotations

from typing import Any, Dict, Optional

import requests

DEFAULT_TIMEOUT = 5


class ResearchAPIClient:
    """Lightweight client with GET/POST helpers and basic error handling."""

    def __init__(self, base_url: str = "https://example.invalid", session: Optional[requests.Session] = None):
        self.base_url = base_url.rstrip("/")
        self.session = session or requests.Session()

    def _request(self, method: str, path: str, **kwargs: Any) -> Dict[str, Any]:
        url = f"{self.base_url}/{path.lstrip('/')}"
        timeout = kwargs.pop("timeout", DEFAULT_TIMEOUT)
        try:
            response = self.session.request(method=method, url=url, timeout=timeout, **kwargs)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as exc:  # pragma: no cover - network is mocked in tests
            raise RuntimeError(f"Request failed for {url}") from exc

    def get_json(self, path: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Perform a GET request and return JSON."""
        return self._request("GET", path, params=params)

    def post_json(self, path: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Perform a POST request with JSON body and return JSON."""
        return self._request("POST", path, json=payload)

    def health(self) -> Dict[str, Any]:
        """Return a synthetic health payload without network dependency."""
        return {"status": "online", "base_url": self.base_url}
