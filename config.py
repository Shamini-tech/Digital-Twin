"""Shared settings for the Machine Digital Twin project."""

MACHINE_ID = "M001"

# A reading is a WARNING if any of these limits is crossed
TEMP_LIMIT = 90         # degrees C
VIBRATION_LIMIT = 7.0   # mm/s


def get_status(temperature, vibration):
    """Return 'WARNING' or 'NORMAL' for one reading."""
    if temperature > TEMP_LIMIT or vibration > VIBRATION_LIMIT:
        return "WARNING"
    return "NORMAL"
