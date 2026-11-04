import os

import altair as alt
import pandas as pd
import streamlit as st

from config import get_status

# ---------- Settings ----------
DATA_FILES = ["machine_data.csv", "live_machine_data.csv"]

st.set_page_config(page_title="Machine Digital Twin", page_icon="🏭", layout="wide")


# ---------- Load data ----------
def load_data():
    for path in DATA_FILES:
        if os.path.exists(path):
            df = pd.read_csv(path)
            break
    else:
        st.error("No data file found. Run the sensor simulation first.")
        st.stop()

    # Make column names flexible (works with 'temperature', 'Temperature', 'Machine Status', etc.)
    rename = {}
    for col in df.columns:
        key = col.strip().lower().replace("_", " ")
        if key in ("machine id", "machineid", "machine"):
            rename[col] = "Machine ID"
        elif key.startswith("temp"):
            rename[col] = "Temperature"
        elif key.startswith("vib"):
            rename[col] = "Vibration"
        elif key.startswith("speed"):
            rename[col] = "Speed"
        elif key in ("machine status", "status"):
            rename[col] = "Machine Status"
    df = df.rename(columns=rename)

    if "Machine ID" not in df.columns:
        df["Machine ID"] = "M001"

    # Always compute status from the shared thresholds in config.py
    df["Machine Status"] = df.apply(
        lambda r: get_status(r["Temperature"], r["Vibration"]), axis=1
    )
    return df


df = load_data()
latest = df.iloc[-1]
recent = df.tail(100).reset_index(drop=True)


def trend_chart(data, column, title):
    st.subheader(title)
    chart = (
        alt.Chart(data.reset_index())
        .mark_line()
        .encode(
            x=alt.X("index:Q", title="Reading"),
            y=alt.Y(f"{column}:Q", scale=alt.Scale(zero=False), title=column),
        )
    )
    st.altair_chart(chart, width="stretch")


# ---------- Header ----------
st.title("🏭 Machine Digital Twin Dashboard")
st.caption("Live Machine Condition Monitoring System (simulated data)")

# ---------- Current status ----------
st.header("Current Machine Status")
if latest["Machine Status"] == "NORMAL":
    st.success("Machine Operating Normally")
else:
    st.warning("Warning: Machine readings are outside the normal range")

# ---------- Sensor readings ----------
st.header("Machine Sensor Readings")
c1, c2, c3 = st.columns(3)
c1.metric("🌡️ Temperature", f"{latest['Temperature']:.0f} °C")
c2.metric("〰️ Vibration", f"{latest['Vibration']:.2f} mm/s")
c3.metric("⚙️ Machine Speed", f"{latest['Speed']:.0f} RPM")

st.divider()

# ---------- Charts ----------
st.header("Sensor Monitoring Charts (last 100 readings)")
trend_chart(recent, "Temperature", "Temperature Trend")
trend_chart(recent, "Vibration", "Vibration Trend")
trend_chart(recent, "Speed", "Machine Speed Trend")

st.divider()

# ---------- Recent readings ----------
st.header("Recent Machine Readings")
st.dataframe(
    df[["Machine ID", "Temperature", "Vibration", "Speed", "Machine Status"]].tail(10),
    width="stretch",
)

# ---------- Summary ----------
st.header("Machine Status Summary (all readings)")
s1, s2 = st.columns(2)
s1.metric("Normal Readings", int((df["Machine Status"] == "NORMAL").sum()))
s2.metric("Warning Readings", int((df["Machine Status"] == "WARNING").sum()))

st.divider()
st.caption(f"Digital Twin Learning Project | Machine ID: {latest['Machine ID']}")