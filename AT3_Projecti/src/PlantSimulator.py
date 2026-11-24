import csv
import math
import os
import random
from datetime import datetime, timedelta

random.seed(42)

PLANTS = {
    "Peikonlehti": {"start_moisture": 65.0, "dry_rate": 0.45, "water_at": 35.0},
    "Kaktus":   {"start_moisture": 30.0, "dry_rate": 0.15, "water_at": 15.0},
    "Basilika":    {"start_moisture": 75.0, "dry_rate": 0.85, "water_at": 40.0},
}

DAYS = 7
HOURS = DAYS * 24
GLITCH_CHANCE = 0.03

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_PATH = os.path.join(BASE_DIR, "data", "raw_sensor_data.csv")


def simulate_sensor_data():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    start_time = datetime.now().replace(minute=0, second=0, microsecond=0) - timedelta(hours=HOURS)

    rows = []

    for plant_name, cfg in PLANTS.items():
        moisture = cfg["start_moisture"]

        for hour_idx in range(HOURS):
            timestamp = start_time + timedelta(hours=hour_idx)
            hour_of_day = timestamp.hour

            moisture -= cfg["dry_rate"] + random.uniform(-0.1, 0.2)
            is_final_days = hour_idx >= (HOURS - 48)
            if moisture <= cfg["water_at"] and not (plant_name == "Basilika" and is_final_days):
                moisture = min(90.0, moisture + random.uniform(35.0, 45.0))
            moisture = max(5.0, round(moisture, 1))
            light_wave = max(0.0, math.sin((hour_of_day - 6) * math.pi / 12))
            light = round(800.0 * light_wave + random.uniform(0, 30), 0) if light_wave > 0 else 0.0

            recorded_moisture = moisture
            recorded_light = light

            if random.random() < GLITCH_CHANCE:
                glitch_type = random.choice(["bad_moisture", "bad_light", "missing_value"])
                if glitch_type == "bad_moisture":
                    recorded_moisture = random.choice([-15.0, 150.0])
                elif glitch_type == "bad_light":
                    recorded_light = -50.0
                elif glitch_type == "missing_value":
                    recorded_moisture = ""

            rows.append({
                "timestamp": timestamp.isoformat(),
                "plant": plant_name,
                "moisture_pct": recorded_moisture,
                "light_lux": recorded_light,
            })

    with open(OUTPUT_PATH, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f, fieldnames=["timestamp", "plant", "moisture_pct", "light_lux"]
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"Generated {len(rows)} rows in {OUTPUT_PATH}")


if __name__ == "__main__":
    simulate_sensor_data()