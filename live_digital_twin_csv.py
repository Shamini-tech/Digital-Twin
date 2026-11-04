
import random
import time
import csv
import os

class MachineTwin:
    def __init__(self, machine_id):
        self.machine_id = machine_id
        self.temperature = 0
        self.vibration = 0
        self.speed = 0
        self.status = "Starting"

    def update(self, temperature, vibration, speed):
        self.temperature = temperature
        self.vibration = vibration
        self.speed = speed

        if temperature > 90:
            self.status = "WARNING"
        else:
            self.status = "NORMAL"

    def display(self):
        print("\n========== LIVE DIGITAL TWIN ==========")
        print("Machine ID:", self.machine_id)
        print("Temperature:", self.temperature, "°C")
        print("Vibration:", self.vibration, "mm/s")
        print("Speed:", self.speed, "RPM")
        print("Machine Status:", self.status)
        print("=======================================")


# Create the digital twin
machine = MachineTwin("M001")

# CSV file name
file_name = "live_machine_data.csv"

# Add column headings if the file is new or empty
file_exists = os.path.exists(file_name) and os.path.getsize(file_name) > 0

with open(file_name, "a", newline="") as file:
    writer = csv.writer(file)

    if not file_exists:
        writer.writerow([
            "Machine ID",
            "Temperature",
            "Vibration",
            "Speed",
            "Machine Status"
        ])

    print("Starting Live Digital Twin...")
    print("Sensor data is being saved to CSV.")
    print("Press CTRL + C to stop.\n")

    try:
        while True:
            temperature = random.randint(60, 110)
            vibration = round(random.uniform(2.0, 8.0), 2)
            speed = random.randint(1000, 1800)

            machine.update(temperature, vibration, speed)
            machine.display()

            # Save each reading to CSV
            writer.writerow([
                machine.machine_id,
                machine.temperature,
                machine.vibration,
                machine.speed,
                machine.status
            ])

            file.flush()

            print("Reading saved to CSV.")

            time.sleep(2)

    except KeyboardInterrupt:
        print("\nLive Digital Twin stopped.")
