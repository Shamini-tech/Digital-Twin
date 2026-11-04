
import streamlit as st
import pandas as pd

# --------------------------------
# 1. PAGE CONFIGURATION
# --------------------------------

st.set_page_config(
    page_title="Machine Digital Twin",
    page_icon="🏭",
    layout="wide"
)

# --------------------------------
# 2. DASHBOARD TITLE
# --------------------------------

st.title("🏭 Machine Digital Twin Dashboard")
st.caption("Live Machine Condition Monitoring System")

# --------------------------------
# 3. LOAD SENSOR DATA
# --------------------------------

try:
    data = pd.read_csv("live_machine_data.csv")

    if data.empty:
        st.warning("No sensor readings available.")
        st.stop()

except FileNotFoundError:
    st.error("live_machine_data.csv not found!")
    st.stop()

# Select latest 100 readings
latest = data.tail(100).reset_index(drop=True)

# Get latest reading
current = latest.iloc[-1]

temperature = current["Temperature"]
vibration = current["Vibration"]
speed = current["Speed"]
status = current["Machine Status"]

# --------------------------------
# 4. MACHINE STATUS
# --------------------------------

st.subheader("Current Machine Status")

if temperature > 90:
    st.error("⚠️ WARNING: High Temperature Detected!")
else:
    st.success("✅ Machine Operating Normally")

# --------------------------------
# 5. SENSOR METRICS
# --------------------------------

st.subheader("Machine Sensor Readings")

col1, col2, col3 = st.columns(3)

col1.metric(
    label="🌡️ Temperature",
    value=f"{temperature} °C"
)

col2.metric(
    label="〰️ Vibration",
    value=f"{vibration} mm/s"
)

col3.metric(
    label="⚙️ Machine Speed",
    value=f"{speed} RPM"
)

st.divider()

# --------------------------------
# 6. SENSOR VISUALIZATION
# --------------------------------

st.subheader("Sensor Monitoring Charts")

st.write("Temperature Trend")
st.line_chart(latest["Temperature"])

st.write("Vibration Trend")
st.line_chart(latest["Vibration"])

st.write("Machine Speed Trend")
st.line_chart(latest["Speed"])

# --------------------------------
# 7. MACHINE DATA HISTORY
# --------------------------------

st.divider()

st.subheader("Recent Machine Readings")

st.dataframe(
    latest.tail(10),
    use_container_width=True
)

# --------------------------------
# 8. MACHINE STATUS SUMMARY
# --------------------------------

st.subheader("Machine Status Summary")

status_counts = data["Machine Status"].value_counts()

col1, col2 = st.columns(2)

col1.metric(
    "Normal Readings",
    int(status_counts.get("NORMAL", 0))
)

col2.metric(
    "Warning Readings",
    int(status_counts.get("WARNING", 0))
)

st.divider()

st.caption("Digital Twin Learning Project | Machine ID: M001")
