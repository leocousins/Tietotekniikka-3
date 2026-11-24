import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "raw_sensor_data.csv")


def load_raw_data(filepath=RAW_DATA_PATH):
    """Loads the raw CSV file into a pandas DataFrame."""
    return pd.read_csv(filepath)


def clean_sensor_data(df):
    """
    Cleans sensor glitches:
    - Converts timestamps and numeric columns
    - Removes impossible moisture (< 0% or > 100%) and negative light (< 0 lux)
    - Drops rows with missing values
    Returns: (cleaned_df, removed_count)
    """
    cleaned = df.copy()
    initial_rows = len(cleaned)

    cleaned["timestamp"] = pd.to_datetime(cleaned["timestamp"], errors="coerce")
    cleaned["moisture_pct"] = pd.to_numeric(cleaned["moisture_pct"], errors="coerce")
    cleaned["light_lux"] = pd.to_numeric(cleaned["light_lux"], errors="coerce")

    valid_moisture = cleaned["moisture_pct"].between(0, 100)
    valid_light = cleaned["light_lux"] >= 0

    cleaned = cleaned[valid_moisture & valid_light]
    cleaned = cleaned.dropna(subset=["timestamp", "plant", "moisture_pct", "light_lux"])

    removed_count = initial_rows - len(cleaned)
    return cleaned.reset_index(drop=True), removed_count