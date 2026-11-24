import pandas as pd
from src.processor import clean_sensor_data


def test_clean_sensor_data_removes_glitches():
    sample_data = pd.DataFrame([
        # Good row
        {"timestamp": "2026-11-18T10:00:00", "plant": "Peikonlehti", "moisture_pct": 55.0, "light_lux": 300.0},
        # Glitch 1: Negative light
        {"timestamp": "2026-11-18T11:00:00", "plant": "Peikonlehti", "moisture_pct": 54.0, "light_lux": -50.0},
        # Glitch 2: Moisture over 100%
        {"timestamp": "2026-11-18T12:00:00", "plant": "Peikonlehti", "moisture_pct": 150.0, "light_lux": 350.0},
        # Glitch 3: Missing moisture value
        {"timestamp": "2026-11-18T13:00:00", "plant": "Peikonlehti", "moisture_pct": "", "light_lux": 350.0},
    ])

    cleaned_df, removed_count = clean_sensor_data(sample_data)

    assert len(cleaned_df) == 1
    assert removed_count == 3
    assert cleaned_df.iloc[0]["moisture_pct"] == 55.0