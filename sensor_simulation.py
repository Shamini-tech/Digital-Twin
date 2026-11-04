import csv
import random

from config import MACHINE_ID, get_status

NUM_READINGS = 200        # how many readings to generate
ANOMALY_CHANCE = 0.06     # about 6% of readings are faults (spikes)

with open("machine_data.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Column headings
    writer.writerow(["Machine ID", "Temperature", "Vibration", "Speed", "Machine Status"])

    warnings = 0

    for i in range(NUM_READINGS):
        # Normal operation: values stay close to a typical level
        temperature = random.gauss(72, 5)
        vibration = random.gauss(4.0, 0.7)
        speed = random.gauss(1450, 60)

        # Occasionally the machine develops a fault: temperature and vibration spike
        if random.random() < ANOMALY_CHANCE:
            temperature += random.uniform(18, 35)
            vibration += random.uniform(2.5, 4.0)
            speed -= random.uniform(100, 300)

        temperature = round(temperature)
        vibration = round(max(vibration, 0.5), 2)
        speed = round(speed)

        status = get_status(temperature, vibration)
        if status == "WARNING":
            warnings += 1

        writer.writerow([MACHINE_ID, temperature, vibration, speed, status])

print(f"Saved {NUM_READINGS} readings to machine_data.csv")
print(f"Warning readings: {warnings} ({warnings / NUM_READINGS:.0%})")