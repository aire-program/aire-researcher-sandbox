from pathlib import Path

import pandas as pd


def load_articles(data_dir: Path = Path("data")) -> pd.DataFrame:
    """Load synthetic articles."""
    return pd.read_csv(data_dir / "sample_texts" / "articles_sample.csv")


def load_experiments(data_dir: Path = Path("data")) -> pd.DataFrame:
    """Load synthetic experiments."""
    return pd.read_csv(data_dir / "sample_tabular" / "experiments_sample.csv")
