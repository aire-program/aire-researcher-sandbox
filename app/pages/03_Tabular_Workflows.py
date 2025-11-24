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
    render_header("Tabular Workflows", "Sanity checks and quick visual summaries.")

    experiments = _prepare(utils.load_experiments())
    metrics = utils.load_metrics()

    st.markdown("### Experiments: summary statistics")
    st.dataframe(experiments.describe(include="all"))

    st.markdown("### Mean metric by condition")
    condition_means = experiments.groupby("condition")["metric_value"].mean()
    st.bar_chart(condition_means)

    st.markdown("### Metric values over time (sample)")
    sample = experiments.sort_values("timestamp").head(50).set_index("timestamp")
    st.line_chart(sample["metric_value"], height=200)

    st.markdown("### Metrics by category")
    category_summary = metrics.groupby("category")["value"].mean()
    st.bar_chart(category_summary)

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
