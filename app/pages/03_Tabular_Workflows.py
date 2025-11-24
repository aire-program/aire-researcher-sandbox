"""Tabular workflow exploration page."""

from __future__ import annotations

import pandas as pd
import streamlit as st

from app import utils
from app.layout import render_header


def _prepare(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df


def main() -> None:
    render_header("Tabular Workflows", "Sanity checks and quick summaries for synthetic experiment data.")
    st.markdown(
        "Use this page to understand the shape and health of the tabular datasets. "
        "Researchers rely on quick stats to decide if data is ready for modeling or if more cleaning is needed. "
        "Browse the tables below, then jump into the tabular notebooks for hands-on feature work."
    )

    experiments = _prepare(utils.load_experiments())
    metrics = utils.load_metrics()

    st.markdown("### Experiments: summary statistics")
    st.dataframe(experiments.describe(include="all"))

    st.markdown("### Mean metric by condition (table view)")
    condition_means = experiments.groupby("condition")["metric_value"].mean().reset_index(name="mean_metric_value")
    st.dataframe(condition_means)

    st.markdown("### Sample of metric values over time")
    sample = experiments.sort_values("timestamp").head(20)[["timestamp", "experiment_id", "condition", "metric_value"]]
    st.dataframe(sample)

    st.markdown("### Metrics by category (table view)")
    category_summary = metrics.groupby("category")["value"].mean().reset_index(name="mean_value")
    st.dataframe(category_summary)

    st.info(
        "The tabular cleaning and feature engineering steps are detailed in the `pipelines/tabular` "
        "notebooks. This page provides a quick preview using the same synthetic dataset."
    )
    st.caption(
        "Next steps: run pipelines/tabular/tabular_cleaning.ipynb then pipelines/tabular/feature_engineering.ipynb "
        "to extend these checks; Colab links are in docs/colab_index.md."
    )


if __name__ == "__main__":
    main()
