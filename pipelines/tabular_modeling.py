"""Tabular data preprocessing utilities."""

from __future__ import annotations

import pandas as pd


def normalize_metrics(df: pd.DataFrame, column: str) -> pd.Series:
    """Compute Z-score normalization for a numeric column."""
    col = df[column]
    return (col - col.mean()) / col.std()


def add_date_features(df: pd.DataFrame, date_col: str) -> pd.DataFrame:
    """Add day-of-week feature from a datetime column."""
    df = df.copy()
    df[date_col] = pd.to_datetime(df[date_col])
    df["day_of_week"] = df[date_col].dt.day_name()
    return df