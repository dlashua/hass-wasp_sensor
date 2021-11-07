"""Constants for integration_blueprint."""
# Base component constants
NAME = "Wasp Sensor"
DOMAIN = "wasp_sensor"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "0.0.1"
ISSUE_URL = "http://google.com"

# Device classes
BINARY_SENSOR_DEVICE_CLASS = "occupancy"

# Platforms
BINARY_SENSOR = "binary_sensor"
PLATFORMS = [BINARY_SENSOR]

# Services
SERVICE_RELOAD = "reload"

# Defaults
DEFAULT_NAME = DOMAIN

# Config Elements
CONF_WASP_SENSORS = "wasp_sensors"
CONF_WASP_INV_SENSORS = "wasp_inv_sensors"
CONF_BOX_SENSORS = "box_sensors"
CONF_BOX_INV_SENSORS = "box_inv_sensors"
CONF_TIMEOUT = "timeout"
CONF_NAME = "name"

# Configuration
SENSOR_CHANGE_DELAY = 1
DEFAULT_WASP_TIMEOUT = 5


STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""
