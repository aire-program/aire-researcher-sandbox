"""Generate reproducible synthetic datasets for notebook-based workflows."""

from __future__ import annotations

import json
import random
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

import jsonschema
import numpy as np
import pandas as pd

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

SEED = 42
np.random.seed(SEED)
random.seed(SEED)

TEXT_DIR = DATA_DIR / "sample_texts"
TABULAR_DIR = DATA_DIR / "sample_tabular"


def ensure_dirs() -> None:
    """Ensure destination directories exist."""
    TEXT_DIR.mkdir(parents=True, exist_ok=True)
    TABULAR_DIR.mkdir(parents=True, exist_ok=True)


def _generate_text(index: int, adjectives: list[str], domains: list[str]) -> str:
    """Create a short synthetic title fragment."""
    adjective = random.choice(adjectives)
    domain = random.choice(domains)
    return f"{adjective} Study of {domain}: {index}"


def generate_articles(n: int = 150) -> None:
    """Generate synthetic articles with unique IDs and non-empty fields."""
    print(f"Generating {n} articles...")
    data = []
    for i in range(n):
        article_id = f"ART-{i:04d}"
        title = _generate_text(
            index=random.randint(1, 10_000),
            adjectives=["Advanced", "Novel", "Comparative", "Longitudinal"],
            domains=["AI", "Biology", "Sociology", "Economics", "Public Health"],
        )
        abstract = (
            f"This paper explores {title.lower()} with a focus on method {random.randint(1, 10)}. "
            f"Findings highlight reproducible patterns in synthetic research workflows."
        )
        data.append({"article_id": article_id, "title": title, "abstract": abstract})

    df = pd.DataFrame(data)
    df.to_csv(ARTICLES_PATH, index=False)
    print(f"Saved {len(df)} rows to {ARTICLES_PATH}")


def generate_notes(n: int = 120) -> None:
    """Generate synthetic research notes with clear, unique identifiers."""
    print(f"Generating {n} notes...")
    data = []
    for i in range(n):
        note_id = f"NOTE-{i:04d}"
        note_text = (
            f"Observation {i}: The session showed {random.choice(['high', 'low', 'moderate'])} engagement. "
            f"Next review scheduled for {random.choice(['Monday', 'Tuesday', 'Wednesday'])}."
        )
        data.append({"note_id": note_id, "note_text": note_text})

    df = pd.DataFrame(data)
    df.to_csv(NOTES_PATH, index=False)
    print(f"Saved {len(df)} rows to {NOTES_PATH}")


def generate_experiments(n: int = 180) -> None:
    """Generate tabular experiment records within specified ranges."""
    print(f"Generating {n} experiment records...")
    data = []
    start_date = datetime(2023, 1, 1)
    for i in range(n):
        experiment_id = f"EXP-{i:04d}"
        condition = random.choice(["control", "treatment_A", "treatment_B"])
        metric_value = round(random.uniform(0, 100), 2)
        timestamp = start_date + timedelta(
            days=random.randint(0, 365),
            hours=random.randint(0, 23),
            minutes=random.randint(0, 59),
            seconds=random.randint(0, 59),
        )
        data.append(
            {
                "experiment_id": experiment_id,
                "condition": condition,
                "metric_value": metric_value,
                "timestamp": timestamp.isoformat(timespec="seconds"),
            }
        )

    df = pd.DataFrame(data)
    df.to_csv(EXPERIMENTS_PATH, index=False)
    print(f"Saved {len(df)} rows to {EXPERIMENTS_PATH}")


def generate_metrics(n: int = 200) -> None:
    """Generate auxiliary metric records with bounded numeric values."""
    print(f"Generating {n} metric records...")
    data = []
    for i in range(n):
        record_id = f"REC-{i:04d}"
        category = random.choice(["throughput", "accuracy", "latency", "error_rate"])
        value = round(random.uniform(0, 100), 4)
        data.append({"record_id": record_id, "category": category, "value": value})

    df = pd.DataFrame(data)
    df.to_csv(METRICS_PATH, index=False)
    print(f"Saved {len(df)} rows to {METRICS_PATH}")


def _load_schema(name: str) -> dict[str, Any]:
    schema_path = SCHEMA_DIR / name
    with open(schema_path, encoding="utf-8") as handle:
        return json.load(handle)


def validate_outputs() -> None:
    """Validate generated datasets against schemas and report summary."""
    schemas = {
        "articles": _load_schema("articles_schema.json"),
        "notes": _load_schema("notes_schema.json"),
        "experiments": _load_schema("experiments_schema.json"),
        "metrics": _load_schema("metrics_schema.json"),
    }

    datasets = {
        "articles": pd.read_csv(ARTICLES_PATH),
        "notes": pd.read_csv(NOTES_PATH),
        "experiments": pd.read_csv(EXPERIMENTS_PATH),
        "metrics": pd.read_csv(METRICS_PATH),
    }

    for name, df in datasets.items():
        records = df.to_dict(orient="records")
        for record in records:
            jsonschema.validate(instance=record, schema=schemas[name])
        print(f"{name}: {len(df)} rows validated against {name} schema")


def main() -> None:
    """Generate all synthetic datasets and print a concise summary."""
    ensure_dirs()
    generate_articles(150)
    generate_notes(120)
    generate_experiments(180)
    generate_metrics(200)
    validate_outputs()
    print("Synthetic data generation complete.")


if __name__ == "__main__":
    main()
