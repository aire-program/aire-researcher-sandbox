"""Example script demonstrating text processing pipeline usage."""

from __future__ import annotations

from pipelines.text_processing import clean_text


def main() -> None:
    """Run a simple text cleaning demonstration."""
    sample_text = "This is a TEST article."
    cleaned = clean_text(sample_text)
    print(f"Original: {sample_text}")
    print(f"Cleaned:  {cleaned}")


if __name__ == "__main__":
    main()