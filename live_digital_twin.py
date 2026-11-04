
import random
import time


class MachineTwin:

    def __init__(self, machine_id):
        self.machine_id = machine_id
        self.temperature = 0
        self.vibration = 0
        self.speed = 0
        self.status = "Starting"

    # Update virtual machine with new sensor readings
    def update(self, temperature, vibration, speed):

        self.temperature = temperature
        self.vibration = vibration
        self.speed = speed

        if temperature > 90:
            self.status = "WARNING"
        else:
            self.status = "NORMAL"

    # Display current machine condition
    def display(self):

        print("\n========== LIVE DIGITAL TWIN ==========")
        print("Machine ID:", self.machine_id)
        print("Temperature:", self.temperature, "°C")
        print("Vibration:", self.vibration, "mm/s")
        print("Speed:", self.speed, "RPM")
        print("Machine Status:", self.status)
        print("=======================================")


# Create virtual machine
machine = MachineTwin("M001")

print("Starting Live Digital Twin...")
print("Press CTRL + C to stop.\n")

try:

    while True:

        # Simulate sensor readings
        temperature = random.randint(60, 110)
        vibration = round(random.uniform(2.0, 8.0), 2)
        speed = random.randint(1000, 1800)

        # Update virtual machine
        machine.update(temperature, vibration, speed)

        # Display updated condition
        machine.display()

        time.sleep(2)

except KeyboardInterrupt:

    print("\nLive Digital Twin stopped.")
