import pandas as pd
import os

def load_data(file_path: str) -> pd.DataFrame:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"CSV file not found: {file_path}")
    df = pd.read_csv(file_path, dtype=str)
    if "TITLE" not in df.columns or "DESCRIPTION" not in df.columns:
        raise ValueError("CSV must contain 'TITLE' and 'DESCRIPTION' columns")
    df.fillna("", inplace=True)
    return df