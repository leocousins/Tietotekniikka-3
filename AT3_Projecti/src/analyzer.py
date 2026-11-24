import pandas as pd

THRESHOLDS = {
    "Peikonlehti": {"min_moisture": 35.0},
    "Kaktus":   {"min_moisture": 15.0},
    "Basilika":    {"min_moisture": 40.0},
}


def analyze_plants(clean_df, custom_thresholds=None):
    """
    Analyzes the latest readings for each plant:
    - Checks 'Needs Water' (below min_moisture for last 3 readings)
    - Detects 'Last Watered' by finding the most recent moisture jump > 20%
    """
    active_thresholds = custom_thresholds if custom_thresholds is not None else THRESHOLDS
    results = []

    for plant_name, group in clean_df.groupby("plant"):
        plant_df = group.sort_values("timestamp")
        latest = plant_df.iloc[-1]
        rules = active_thresholds.get(plant_name, {"min_moisture": 30.0})

        alerts = []

        recent_moisture = plant_df["moisture_pct"].tail(3)
        if len(recent_moisture) >= 3 and (recent_moisture < rules["min_moisture"]).all():
            alerts.append(f"Needs Water (below {rules['min_moisture']}% for 3+ hours)")

        moisture_jumps = plant_df[plant_df["moisture_pct"].diff() > 20.0]
        if not moisture_jumps.empty:
            last_watered_ts = moisture_jumps.iloc[-1]["timestamp"]
            hours_since_watered = int((latest["timestamp"] - last_watered_ts).total_seconds() // 3600)
        else:
            hours_since_watered = None

        results.append({
            "plant": plant_name,
            "status": "ALERT" if alerts else "OK",
            "alerts": alerts,
            "latest_moisture": round(float(latest["moisture_pct"]), 1),
            "latest_light": round(float(latest["light_lux"]), 0),
            "min_moisture": rules["min_moisture"],
            "hours_since_watered": hours_since_watered,
        })

    return results