
import pandas as pd

# Read sensor data
data = pd.read_csv("machine_data.csv")

print("MACHINE SENSOR DATA")
print(data)

print("\nMACHINE STATISTICS")

print("Average Temperature:",
      data["Temperature"].mean())

print("Maximum Temperature:",
      data["Temperature"].max())

print("Minimum Temperature:",
      data["Temperature"].min())

print("\nMACHINE STATUS SUMMARY")

print(data["Machine Status"].value_counts())
