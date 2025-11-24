"""Validate synthetic datasets against JSON Schemas and constraints."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable

import jsonschema
import pandas as pd

from paths import ARTICLES_PATH, EXPERIMENTS_PATH, METRICS_PATH, NOTES_PATH, SCHEMA_DIR


def load_schema(name: str) -> dict:
    schema_path = Path(SCHEMA_DIR) / name
    with open(schema_path, "r", encoding="utf-8") as f:
        return json.load(f)


def validate_dataframe(df: pd.DataFrame, schema: dict) -> None:
    records = df.to_dict(orient="records")
    for record in records:
        jsonschema.validate(instance=record, schema=schema)


def expect_non_empty(df: pd.DataFrame, columns: Iterable[str]) -> None:
    for col in columns:
        assert (df[col].astype(str).str.len() > 0).all(), f"Column {col} contains empty values"


def expect_unique(df: pd.DataFrame, column: str) -> None:
    assert df[column].is_unique, f"Duplicate values detected in {column}"


def expect_row_count(df: pd.DataFrame, minimum: int = 50, maximum: int = 200) -> None:
    assert minimum <= len(df) <= maximum, f"Row count {len(df)} outside [{minimum}, {maximum}]"


def test_articles_schema() -> None:
    df = pd.read_csv(ARTICLES_PATH)
    expect_row_count(df)
    expect_unique(df, "article_id")
    expect_non_empty(df, ["article_id", "title", "abstract"])
    schema = load_schema("articles_schema.json")
    validate_dataframe(df, schema)


def test_notes_schema() -> None:
    df = pd.read_csv(NOTES_PATH)
    expect_row_count(df)
    expect_unique(df, "note_id")
    expect_non_empty(df, ["note_id", "note_text"])
    schema = load_schema("notes_schema.json")
    validate_dataframe(df, schema)


def test_experiments_schema() -> None:
    df = pd.read_csv(EXPERIMENTS_PATH)
    expect_row_count(df)
    expect_unique(df, "experiment_id")
    expect_non_empty(df, ["experiment_id", "condition", "timestamp"])
    assert df["metric_value"].between(0, 100).all(), "metric_value outside 0-100 range"
    schema = load_schema("experiments_schema.json")
    validate_dataframe(df, schema)


def test_metrics_schema() -> None:
    df = pd.read_csv(METRICS_PATH)
    expect_row_count(df)
    expect_unique(df, "record_id")
    expect_non_empty(df, ["record_id", "category"])
    schema = load_schema("metrics_schema.json")
    validate_dataframe(df, schema)
