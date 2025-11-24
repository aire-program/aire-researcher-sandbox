"""Generate reproducible synthetic datasets for the sandbox."""

from __future__ import annotations

import os
import random
from datetime import datetime, timedelta
from typing import List

import numpy as np
import pandas as pd

# Set fixed random seed for reproducibility
SEED = 42
np.random.seed(SEED)
random.seed(SEED)

DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))
TEXT_DIR = os.path.join(DATA_DIR, "sample_texts")
TABULAR_DIR = os.path.join(DATA_DIR, "sample_tabular")


def ensure_dirs() -> None:
    """Ensure destination directories exist."""
    os.makedirs(TEXT_DIR, exist_ok=True)
    os.makedirs(TABULAR_DIR, exist_ok=True)


def _generate_text(index: int, adjectives: List[str], domains: List[str]) -> str:
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
    output_path = os.path.join(TEXT_DIR, "articles_sample.csv")
    df.to_csv(output_path, index=False)
    print(f"Saved {len(df)} rows to {output_path}")


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
    output_path = os.path.join(TEXT_DIR, "notes_sample.csv")
    df.to_csv(output_path, index=False)
    print(f"Saved {len(df)} rows to {output_path}")


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
    output_path = os.path.join(TABULAR_DIR, "experiments_sample.csv")
    df.to_csv(output_path, index=False)
    print(f"Saved {len(df)} rows to {output_path}")


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
    output_path = os.path.join(TABULAR_DIR, "metrics_sample.csv")
    df.to_csv(output_path, index=False)
    print(f"Saved {len(df)} rows to {output_path}")


def main() -> None:
    """Generate all synthetic datasets and print a concise summary."""
    ensure_dirs()
    generate_articles(150)
    generate_notes(120)
    generate_experiments(180)
    generate_metrics(200)
    print("Synthetic data generation complete.")


if __name__ == "__main__":
    main()
