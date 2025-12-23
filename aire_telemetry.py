"""Telemetry logging to Google Sheets for event tracking."""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from typing import Any

import gspread
from google.oauth2.service_account import Credentials

_sheet_cache: gspread.Worksheet | None = None


def _get_sheet() -> gspread.Worksheet | None:
    """
    Initialize and return a gspread worksheet using credentials from env.

    Returns None if credentials are missing or initialization fails.
    Uses module-level caching to avoid re-authenticating on every call.
    """
    global _sheet_cache
    if _sheet_cache is not None:
        return _sheet_cache

    raw_creds = os.environ.get("AIRE_TELEMETRY_CREDENTIALS")
    if not raw_creds:
        return None

    try:
        config = json.loads(raw_creds)
        service_account_info = config.get("service_account")
        spreadsheet_id = config.get("spreadsheet_id")
        worksheet_name = config.get("worksheet_name", "Sheet1")
        if not service_account_info or not spreadsheet_id:
            return None

        scopes = ["https://www.googleapis.com/auth/spreadsheets"]
        credentials = Credentials.from_service_account_info(
            service_account_info, scopes=scopes
        )
        client = gspread.authorize(credentials)
        sheet = client.open_by_key(spreadsheet_id).worksheet(worksheet_name)
        _sheet_cache = sheet
        return sheet
    except (json.JSONDecodeError, KeyError, gspread.exceptions.GSpreadException) as exc:
        print(f"Telemetry initialization failed: {exc}")
        return None


def log_event(
    event_name: str,
    user_id: str | None = None,
    metadata: dict[str, Any] | None = None,
    timestamp: str | None = None,
) -> None:
    """Append a telemetry row if a worksheet is available; otherwise no-op."""
    sheet = _get_sheet()
    if sheet is None:
        return

    ts = timestamp or datetime.now(timezone.utc).isoformat()
    metadata_json = json.dumps(metadata or {})

    try:
        sheet.append_row([ts, event_name, user_id or "", metadata_json])
    except gspread.exceptions.GSpreadException as exc:
        print(f"Telemetry logging failed: {exc}")
