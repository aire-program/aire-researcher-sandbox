import pandas as pd
from pathlib import Path

def load_articles(data_dir: Path = Path("data")) -> pd.DataFrame:
    return pd.read_csv(data_dir / "sample_texts" / "articles_sample.csv")

def load_experiments(data_dir: Path = Path("data")) -> pd.DataFrame:
    return pd.read_csv(data_dir / "sample_tabular" / "experiments_sample.csv")