"""REST API client utilities for demonstration purposes."""

from __future__ import annotations

from typing import Any

import requests

_DEFAULT_TIMEOUT = 5


class ResearchAPIClient:
    """Lightweight REST client with GET/POST helpers and error handling."""

    def __init__(
        self,
        base_url: str = "https://example.invalid",
        session: requests.Session | None = None,
    ) -> None:
        self._base_url = base_url.rstrip("/")
        self._session = session or requests.Session()

    def _request(
        self,
        method: str,
        path: str,
        **kwargs: Any,
    ) -> dict[str, Any]:
        url = f"{self._base_url}/{path.lstrip('/')}"
        timeout = kwargs.pop("timeout", _DEFAULT_TIMEOUT)
        try:
            response = self._session.request(
                method=method, url=url, timeout=timeout, **kwargs
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as exc:
            raise RuntimeError(f"Request failed for {url}") from exc

    def get_json(
        self,
        path: str,
        params: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Perform a GET request and return JSON response."""
        return self._request("GET", path, params=params)

    def post_json(
        self,
        path: str,
        payload: dict[str, Any],
    ) -> dict[str, Any]:
        """Perform a POST request with JSON body and return JSON response."""
        return self._request("POST", path, json=payload)

    def health(self) -> dict[str, Any]:
        """Return a synthetic health payload for testing."""
        return {"status": "online", "base_url": self._base_url}
