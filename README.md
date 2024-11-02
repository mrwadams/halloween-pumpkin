# Motion-Activated Halloween Pumpkin

A CircuitPython project that creates spooky lighting effects in a carved pumpkin when motion is detected. Perfect for Halloween decorations that interact with trick-or-treaters!

![Pumpkin Demo](pumpkin.gif)

## Features

- Motion detection using a PIR sensor
- Multiple LED control with PWM for smooth brightness transitions
- Various lighting effects:
  - Lightning flashes with random patterns
  - Eerie flickering glow
  - Smooth pulsing effects
  - Fade transitions
- Cooldown timer to prevent effect spam

## Hardware Requirements

- Raspberry Pi Pico (or similar CircuitPython-compatible board)
- PIR motion sensor
- 3x LEDs
- Resistors appropriate for your LEDs
- Jumper wires
- USB cable for programming
- A carved pumpkin 🎃

## Pin Configuration

- LED 1: GP15
- LED 2: GP14
- LED 3: GP13
- PIR Sensor: GP22

## Installation

1. Install CircuitPython on your board if you haven't already
2. Copy the code.py file to your CircuitPython device

## Circuit Setup

1. Connect LEDs to pins GP15, GP14, and GP13 through appropriate resistors
2. Connect PIR sensor to GP22
3. Ensure all components share a common ground
4. Power the circuit through USB or battery pack

## Usage

1. Place the assembled circuit inside your carved pumpkin
2. Power on the device
3. The pumpkin will activate its spooky light show whenever someone walks past!
4. A 5-second cooldown prevents the effect from triggering too frequently

## Customisation

You can modify several parameters in the code to customize the effects:

- Adjust `cooldown` value to change the delay between triggers
- Modify timing in `halloween_effect()` to change effect durations
- Adjust brightness levels in individual effects
- Add or remove effects from the sequence

## Contributing

Feel free to fork this project and submit pull requests with your own spooky effects!

## License

This project is released under the Apache License 2.0.

## Acknowledgments

- Built using CircuitPython
- Thanks to the Adafruit community for their excellent libraries and documentation