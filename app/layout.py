"""Reusable Streamlit layout helpers."""

from __future__ import annotations

import streamlit as st


def render_header(title: str, description: str | None = None) -> None:
    """Render a consistent page header."""
    st.markdown(f"## {title}")
    if description:
        st.markdown(description)
    st.markdown("---")


def render_sidebar() -> None:
    """Render sidebar content with navigation tips."""
    with st.sidebar:
        st.markdown("### AI Researcher Developer Sandbox")
        st.caption("Minimal research workbench for synthetic workflows.")
        st.markdown("---")
        st.markdown(
            "Use the navigation at the top to explore text, tabular, RAG, and API resources."
        )
        st.markdown(
            "[Documentation](https://github.com/aire-program/aire-researcher-sandbox/tree/main/docs)"
        )
