
import pandas as pd
import matplotlib.pyplot as plt

# Read sensor data
data = pd.read_csv("live_machine_data.csv")

# Select the latest 100 readings
data = data.tail(100).reset_index(drop=True)

print("Latest Sensor Readings:", len(data))

print("\nMachine Status Summary:")
print(data["Machine Status"].value_counts())

plt.figure(figsize=(12, 8))

# Temperature
plt.subplot(3, 1, 1)
plt.plot(data["Temperature"], linewidth=1.5)
plt.axhline(y=90, linestyle="--", label="Warning Limit")
plt.title("Machine Temperature")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)

# Vibration
plt.subplot(3, 1, 2)
plt.plot(data["Vibration"], linewidth=1.5)
plt.title("Machine Vibration")
plt.ylabel("Vibration (mm/s)")
plt.grid(True)

# Speed
plt.subplot(3, 1, 3)
plt.plot(data["Speed"], linewidth=1.5)
plt.title("Machine Speed")
plt.ylabel("Speed (RPM)")
plt.xlabel("Latest 100 Readings")
plt.grid(True)

plt.tight_layout()
plt.show()
