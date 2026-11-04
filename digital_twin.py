
import pandas as pd


class MachineTwin:

    def __init__(self, machine_id):
        self.machine_id = machine_id
        self.temperature = 0
        self.vibration = 0
        self.speed = 0
        self.status = "Unknown"

    # Update the virtual machine
    def update(self, temperature, vibration, speed):

        self.temperature = temperature
        self.vibration = vibration
        self.speed = speed

        if self.temperature > 90:
            self.status = "Warning"
        else:
            self.status = "Normal"

    # Display current machine condition
    def display(self):

        print("\nDIGITAL TWIN - MACHINE STATUS")
        print("Machine ID:", self.machine_id)
        print("Temperature:", self.temperature, "°C")
        print("Vibration:", self.vibration, "mm/s")
        print("Speed:", self.speed, "RPM")
        print("Status:", self.status)
        print("-----------------------------")


# Read sensor data
data = pd.read_csv("machine_data.csv")

# Create virtual machine
machine = MachineTwin("M001")

# Update virtual machine using sensor readings
for index, row in data.iterrows():

    machine.update(
        row["Temperature"],
        row["Vibration"],
        row["Speed"]
    )

    machine.display()
