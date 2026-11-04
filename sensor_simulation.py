
import random
import time
import csv

machine_id = "M001"

# Create and open the CSV file
with open("machine_data.csv", "w", newline="") as file:

    writer = csv.writer(file)

    # Add column headings
    writer.writerow([
        "Machine ID",
        "Temperature",
        "Vibration",
        "Speed",
        "Machine Status"
    ])

    # Generate 10 sensor readings
    for i in range(10):

        temperature = random.randint(60, 110)
        vibration = round(random.uniform(2.0, 8.0), 2)
        speed = random.randint(1000, 1800)

        if temperature > 90:
            status = "Warning"
        else:
            status = "Normal"

        print("Reading:", i + 1)
        print("Temperature:", temperature, "°C")
        print("Vibration:", vibration, "mm/s")
        print("Speed:", speed, "RPM")
        print("Machine Status:", status)
        print("------------------------")

        # Save readings into CSV
        writer.writerow([
            machine_id,
            temperature,
            vibration,
            speed,
            status
        ])

        time.sleep(2)

print("All 10 sensor readings saved successfully!")
