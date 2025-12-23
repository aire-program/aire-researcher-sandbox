"""Data loading utilities for sample datasets."""

from __future__ import annotations

import pandas as pd

from paths import ARTICLES_PATH, EXPERIMENTS_PATH


def load_articles() -> pd.DataFrame:
    """Load synthetic articles dataset."""
    return pd.read_csv(ARTICLES_PATH)


def load_experiments() -> pd.DataFrame:
    """Load synthetic experiments dataset."""
    return pd.read_csv(EXPERIMENTS_PATH)
