# Machine Digital Twin Dashboard

A learning project that builds a **digital twin** of an industrial machine (ID: `M001`). It simulates sensor data, stores it in CSV files, analyses it, and shows the machine's condition on a Streamlit dashboard.

> **Note:** All sensor data is **simulated**. No real machine is connected.

## What is a digital twin?

A digital twin is a virtual copy of a physical asset that is kept in sync with sensor data. It lets you monitor the asset's condition, spot problems early and test what-if scenarios without touching the real machine.

## Features

- Simulated sensor readings: temperature (°C), vibration (mm/s) and machine speed (RPM)
- Mostly normal operation with occasional simulated faults (spikes)
- Rule-based status classification: `NORMAL` / `WARNING`, with thresholds kept in one place (`config.py`)
- Streamlit dashboard with:
  - Current machine status banner
  - Latest sensor readings
  - Trend charts for temperature, vibration and machine speed (last 100 readings)
  - Table of recent readings
  - Normal vs warning reading summary
- Offline analysis and visualization scripts

## Architecture

```
config.py (thresholds + status rule)
      |
sensor_simulation.py  ->  machine_data.csv  ->  app.py (Streamlit dashboard)
                                            ->  analyze_machine.py / visualize_machine.py (offline analysis)
```

## Project structure

| File / Folder | Purpose |
|---------------|---------|
| `config.py` | Machine ID, warning thresholds and the `get_status()` rule |
| `sensor_simulation.py` | Generates 200 simulated readings into `machine_data.csv` |
| `digital_twin.py` | Core twin logic |
| `live_digital_twin.py` | Continuously updating twin |
| `live_digital_twin_csv.py` | Live twin that writes readings to `live_machine_data.csv` |
| `analyze_machine.py` | Summary statistics of the machine data |
| `visualize_machine.py` | Generates charts into the `visualizations/` folder |
| `app.py` | Streamlit dashboard |
| `machine_data.csv` | Generated sample dataset |
| `screenshots/` | Dashboard screenshots used in this README |
| `requirements.txt` | Python dependencies |

## Getting started

```bash
# 1. Clone the repository
git clone https://github.com/Shamini-tech/Digital-Twin.git
cd Digital-Twin

# 2. (Optional) create a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux

# 3. Install dependencies
python -m pip install -r requirements.txt

# 4. Generate the sensor data
python sensor_simulation.py

# 5. Run the dashboard
python -m streamlit run app.py
```

Then open http://localhost:8501 in your browser.

## Status rules

A reading is flagged `WARNING` when temperature is above `TEMP_LIMIT` (90 °C) or vibration is above `VIBRATION_LIMIT` (7.0 mm/s). Otherwise it is `NORMAL`. The thresholds and the rule are defined in `config.py`, so the simulation and the dashboard always use the same logic.

## Screenshots

### Dashboard overview
![Dashboard](screenshots/dashboard.png)

### Temperature trend
![Temperature Trend](screenshots/Trend_1.png)

### Vibration trend
![Vibration Trend](screenshots/Trend_2.png)

### Machine speed trend
![Machine Speed Trend](screenshots/Trend_3.png)

## Tech stack

Python, Pandas, NumPy, Matplotlib, Streamlit, Altair

## Future improvements

- Anomaly detection (rolling z-score or Isolation Forest)
- Predictive-maintenance risk score
- Support for multiple machines
- Real sensor input via MQTT

## Author

**Shamini S** — [GitHub](https://github.com/Shamini-tech)