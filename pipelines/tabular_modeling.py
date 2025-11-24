import pandas as pd

def normalize_metrics(df: pd.DataFrame, column: str) -> pd.Series:
    """Compute Z-score normalization for a column."""
    return (df[column] - df[column].mean()) / df[column].std()

def add_date_features(df: pd.DataFrame, date_col: str) -> pd.DataFrame:
    """Add day_of_week and other date features."""
    df[date_col] = pd.to_datetime(df[date_col])
    df["day_of_week"] = df[date_col].dt.day_name()
    return df