"""Lightweight environment validation for the sandbox."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Iterable

import pandas as pd
import pkg_resources

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"
SCHEMA_DIR = DATA_DIR / "schemas"

REQUIRED_FILES = {
    "articles": DATA_DIR / "sample_texts" / "articles_sample.csv",
    "notes": DATA_DIR / "sample_texts" / "notes_sample.csv",
    "experiments": DATA_DIR / "sample_tabular" / "experiments_sample.csv",
    "metrics": DATA_DIR / "sample_tabular" / "metrics_sample.csv",
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
    for schema_name in ["articles.schema.json", "notes.schema.json", "experiments.schema.json", "metrics.schema.json"]:
        schema_path = SCHEMA_DIR / schema_name
        if not schema_path.exists():
            raise SystemExit(f"Missing schema file: {schema_path}")
        with open(schema_path, "r", encoding="utf-8") as handle:
            json.load(handle)


def main() -> None:
    print(f"Python version: {sys.version.split()[0]}")
    _check_packages(["pandas", "numpy", "streamlit", "scikit-learn", "jsonschema", "pytest", "requests"])
    _check_files()
    _validate_schema_presence()
    _validate_sample_counts()
    print("Environment validation successful.")


if __name__ == "__main__":
    main()
