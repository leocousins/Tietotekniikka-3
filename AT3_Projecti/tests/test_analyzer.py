import pandas as pd
from src.analyzer import analyze_plants


def test_needs_water_alert_after_3_dry_hours():
    df = pd.DataFrame([
        {"timestamp": pd.Timestamp("2026-11-18 10:00"), "plant": "Basilika", "moisture_pct": 38.0, "light_lux": 300.0},
        {"timestamp": pd.Timestamp("2026-11-18 11:00"), "plant": "Basilika", "moisture_pct": 36.0, "light_lux": 350.0},
        {"timestamp": pd.Timestamp("2026-11-18 12:00"), "plant": "Basilika", "moisture_pct": 34.0, "light_lux": 400.0},
    ])

    Basilika = analyze_plants(df)[0]
    assert Basilika["status"] == "ALERT"
    assert any("Needs Water" in alert for alert in Basilika["alerts"])


def test_no_water_alert_if_only_1_dry_hour():
    df = pd.DataFrame([
        {"timestamp": pd.Timestamp("2026-11-18 10:00"), "plant": "Basilika", "moisture_pct": 50.0, "light_lux": 300.0},
        {"timestamp": pd.Timestamp("2026-11-18 11:00"), "plant": "Basilika", "moisture_pct": 45.0, "light_lux": 350.0},
        {"timestamp": pd.Timestamp("2026-11-18 12:00"), "plant": "Basilika", "moisture_pct": 38.0, "light_lux": 400.0},
    ])

    Basilika = analyze_plants(df)[0]
    assert Basilika["status"] == "OK"
    assert Basilika["alerts"] == []


def test_last_watered_detection():
    df = pd.DataFrame([
        {"timestamp": pd.Timestamp("2026-11-18 10:00"), "plant": "Peikonlehti", "moisture_pct": 35.0, "light_lux": 200.0},
        {"timestamp": pd.Timestamp("2026-11-18 11:00"), "plant": "Peikonlehti", "moisture_pct": 75.0, "light_lux": 250.0},
        {"timestamp": pd.Timestamp("2026-11-18 12:00"), "plant": "Peikonlehti", "moisture_pct": 74.0, "light_lux": 300.0},
        {"timestamp": pd.Timestamp("2026-11-18 13:00"), "plant": "Peikonlehti", "moisture_pct": 73.0, "light_lux": 300.0},
    ])

    Peikonlehti = analyze_plants(df)[0]
    assert Peikonlehti["hours_since_watered"] == 2