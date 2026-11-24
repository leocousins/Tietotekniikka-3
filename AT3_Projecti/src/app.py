import streamlit as st
from PlantSimulator import simulate_sensor_data
from processor import load_raw_data, clean_sensor_data
from analyzer import analyze_plants, THRESHOLDS

st.set_page_config(page_title="Plant Monitor", page_icon="🌿", layout="wide")

st.title("🌿 Smart Plant Monitor")


st.sidebar.header("Controls")
if st.sidebar.button("🔄 Regenerate Sensor Data"):
    simulate_sensor_data()
    st.rerun()

st.sidebar.subheader("Moisture Alert Thresholds (%)")
custom_thresholds = {}
for plant_name, defaults in THRESHOLDS.items():
    min_m = st.sidebar.slider(
        f"{plant_name} min moisture",
        min_value=5.0,
        max_value=80.0,
        value=float(defaults["min_moisture"]),
        step=1.0,
    )
    custom_thresholds[plant_name] = {"min_moisture": min_m}

raw_df = load_raw_data()
clean_df, removed_count = clean_sensor_data(raw_df)
plant_statuses = analyze_plants(clean_df, custom_thresholds=custom_thresholds)

st.sidebar.divider()
st.sidebar.header("Pipeline Status")
st.sidebar.metric("Raw Readings", len(raw_df))
st.sidebar.metric("Glitches Filtered", removed_count)
st.sidebar.metric("Clean Readings", len(clean_df))

st.subheader("Current Plant Status")
cols = st.columns(len(plant_statuses))

for col, item in zip(cols, plant_statuses):
    with col:
        if item["status"] == "ALERT":
            st.error(f"**{item['plant']} — ALERT**")
        else:
            st.success(f"**{item['plant']} — OK**")

        st.metric("Soil Moisture", f"{item['latest_moisture']}%", f"Min: {item['min_moisture']}%")
        st.metric("Light", f"{int(item['latest_light'])} lux")

        if item["hours_since_watered"] is not None:
            st.caption(f"💧 Last watered: **{item['hours_since_watered']} hours ago**")
        else:
            st.caption("💧 Last watered: **Not detected in last 7 days**")

        for alert in item["alerts"]:
            st.warning(f"⚠️ {alert}")

st.divider()

st.subheader("7-Day Sensor Trends")
plant_names = [p["plant"] for p in plant_statuses]
selected_plant = st.selectbox("Select a plant to inspect:", plant_names)

plant_df = clean_df[clean_df["plant"] == selected_plant].set_index("timestamp")

tab1, tab2 = st.tabs(["Soil Moisture (%)", "Light (lux)"])

with tab1:
    moisture_chart = plant_df[["moisture_pct"]].copy()
    moisture_chart["Min Threshold"] = custom_thresholds[selected_plant]["min_moisture"]
    st.line_chart(moisture_chart)
with tab2:
    st.line_chart(plant_df["light_lux"])