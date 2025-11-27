import json
import os
from datetime import datetime, timezone
from typing import Any, Dict, Optional

import gspread
from google.oauth2.service_account import Credentials


def _get_sheet():
    """
    Safely initialize and return a gspread worksheet using credentials from env.
    Returns None if credentials are missing or any error occurs.
    """
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
        return client.open_by_key(spreadsheet_id).worksheet(worksheet_name)
    except Exception:
        return None


def log_event(
    event_name: str,
    user_id: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    timestamp: Optional[str] = None,
) -> None:
    """
    Append a telemetry row if a worksheet is available; otherwise no-op.
    """
    sheet = _get_sheet()
    if sheet is None:
        return

    ts = timestamp or datetime.now(timezone.utc).isoformat()
    metadata_json = json.dumps(metadata or {})

    try:
        sheet.append_row([ts, event_name, user_id or "", metadata_json])
    except Exception:
        # Telemetry should never break application flow.
        return
