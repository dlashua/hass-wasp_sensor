# Home Assistant Wasp Sensor

This is a Wasp Sensor for Home Assistant. It is installable as a `custom_component` or via [HACS](https://hacs.xyz/).

To install via HACS add the repository URL `https://github.com/dlashua/hass-wasp_sensor` as a custom resposity. It should then show up on the Inegrations Installation page.

# Wasp Sensor

PIR Motion Sensors aren't perfect. If you enter a room and are sitting quietly -- working, reading, sleeping, watching Television -- a PIR Motion Sensor will eventually see no motion. Using such a sensor as the sole source of information to determine if a room is occupied can leave undesired behavior -- lights turning off while you're still in the room, HVAC no longer adjusting temperature for that room, etc. A Wasp Sensor is one solution to that problem.

The name "Wasp in a Box" has been used many times in reference to the logic contained in this Integration. The idea is, if motion is seen in a room (the Wasp) while all the doors are closed, then, even if motion stops, people (the Wasp) are still in there. Once a door opens, the logic resets.

This can also be used if you have motion sensors at all of the exits for a room. If motion happened inside the room and no motion has happened at the exits of a room, then someone is still inside the room.

# Usage

This integration is configurable with YAML in `configuration.yaml`. Here's an example configuration:

```yaml
wasp_sensor:
  - name: office
    wasp_sensors:
      - binary_sensor.office_motion_front
      - binary_sensor.office_motion_rear
    box_sensors:
      - binary_sensor.office_door

  - name: office_motion
    wasp_sensors:
      - binary_sensor.office_motion_front
      - binary_sensor.office_motion_rear
    box_sensors:
      - binary_sensor.halldown_motion
```

# Configuration Details

## name
User Defined name for the `binary_sensor`

## wasp_sensors
A List of `entity_id`s that indicate motion in the room. These Entities should have an on/off state and should be `on` when motion is detected.

## wasp_inv_sensors
The same as `wasp_sensors` but `off` indicates motion.

## box_sensors
A list of `entity_id`s that indicate when the room is open or when an exit is being used. These Entities should have an on/off state and should be `on` to indicate that the room is exitable or being exited.

## box_inv_sensors
The same as `box_sensors` but `off` indicates that the room is exitable or being exited.

## timeout
The number of seconds that `wasp_sensors` and `wasp_inv_sensors` should be in the motion detected state to indicate that the room is truly occupied. This defaults to 180.

# Logic

If the "box" is closed and THEN motion is detected, the wasp sensor will immediately turn on.

If the "box" is opened the wasp sensor will immediate turn off. It will stay off until the "box" is closed.

If the "box" becomes closed WHILE motion is detected, the wasp sensor will wait for `timeout` to elapse before checking to ensure that motion is still detected. If it is, the wasp sensor will turn on.

# Best Use Cases
With the above configuration, I recommend setting up a template `binary_sensor` to indicate room occupancy.

```yaml
template:
  - binary_sensor:
      - name: "Office Occupied"
        device_class: occupancy
        state: >
          {{
          is_state('binary_sensor.office_motion','on')
          or is_state('binary_sensor.wasp_office', 'on')
          or is_state('binary_sensor.wasp_office_motion','on')
          }}
```

With the above, when `binary_sensor.office_occupied` is `on` your automations can take the desired actions when the room is occupied.

If you don't have "door sensors" or have a room without doors, you can leave that part out of your configuration and out of the template `binary_sensor`. The same is true if you do not have "exit motion sensors". By setting these sensors in an `or` configuration using the template `binary_sensor` you ensure that occupancy will be indicated if any of these sensors have an `on` state.

