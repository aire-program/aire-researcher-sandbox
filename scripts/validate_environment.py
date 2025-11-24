"""Lightweight environment validation for the AIRE Researcher Sandbox synthetic mirror."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Iterable

import pandas as pd
import pkg_resources

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from paths import (  # noqa: E402
    ARTICLES_PATH,
    DATA_DIR,
    EXPERIMENTS_PATH,
    METRICS_PATH,
    NOTES_PATH,
    SCHEMA_DIR,
)

REQUIRED_FILES = {
    "articles": ARTICLES_PATH,
    "notes": NOTES_PATH,
    "experiments": EXPERIMENTS_PATH,
    "metrics": METRICS_PATH,
}


def _check_packages(packages: Iterable[str]) -> None:
    missing = []
    for pkg in packages:
        try:
            pkg_resources.get_distribution(pkg)
        except pkg_resources.DistributionNotFound:
            missing.append(pkg)
    if missing:
        raise SystemExit(f"Missing required packages: {', '.join(missing)}")


def _check_files() -> None:
    missing = [name for name, path in REQUIRED_FILES.items() if not path.exists()]
    if missing:
        raise SystemExit(f"Missing data files: {', '.join(missing)}. Run scripts/generate_synthetic_data.py")


def _validate_sample_counts() -> None:
    for name, path in REQUIRED_FILES.items():
        df = pd.read_csv(path)
        print(f"{name}: {len(df)} rows loaded from {path}")


def _validate_schema_presence() -> None:
    for schema_name in ["articles_schema.json", "notes_schema.json", "experiments_schema.json", "metrics_schema.json"]:
        schema_path = SCHEMA_DIR / schema_name
        if not schema_path.exists():
            raise SystemExit(f"Missing schema file: {schema_path}")
        with open(schema_path, "r", encoding="utf-8") as handle:
            json.load(handle)


def main() -> None:
    print(f"Python version: {sys.version.split()[0]}")
    _check_packages(["pandas", "numpy", "scikit-learn", "jsonschema", "requests", "pydantic", "jupyter"])
    _check_files()
    _validate_schema_presence()
    _validate_sample_counts()
    print("Environment validation successful.")


if __name__ == "__main__":
    main()
