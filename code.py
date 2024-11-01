import board
import pwmio
import digitalio
import time
import random
import math

# Define multiple LED pins
led_pins = [board.GP15, board.GP14, board.GP13]
leds = [pwmio.PWMOut(pin, frequency=1000, duty_cycle=0) for pin in led_pins]

# Setup PIR sensor
pir = digitalio.DigitalInOut(board.GP22)
pir.direction = digitalio.Direction.INPUT

def set_brightness(led, brightness):
    led.duty_cycle = int(brightness * 65535)

def set_all_brightness(brightness):
    for led in leds:
        set_brightness(led, brightness)

def set_individual_brightness(brightnesses):
    for led, brightness in zip(leds, brightnesses):
        set_brightness(led, brightness)

def lightning_flash():
    flash_count = random.randint(3, 7)  # Variable number of flashes
    for _ in range(flash_count):
        # Randomize which LEDs flash for more natural effect
        flash_pattern = [random.uniform(0.8, 1.0) for _ in leds]
        set_individual_brightness(flash_pattern)
        time.sleep(0.05)
        set_all_brightness(0)
        time.sleep(random.randint(20, 150) / 1000)

def flicker_effect(duration, base_brightness=0.3):
    start_time = time.monotonic()
    while time.monotonic() - start_time < duration:
        # Create random flicker for each LED
        flicker = [base_brightness + random.uniform(-0.2, 0.2) for _ in leds]
        flicker = [max(0, min(1, f)) for f in flicker]  # Clamp values
        set_individual_brightness(flicker)
        time.sleep(0.05)

def pulse_effect(duration, min_brightness=0.1, max_brightness=0.6):
    start_time = time.monotonic()
    while time.monotonic() - start_time < duration:
        # Sine wave pulsing
        phase = ((time.monotonic() - start_time) * 2)
        brightness = min_brightness + (max_brightness - min_brightness) * (
            (math.sin(phase) + 1) / 2
        )
        set_all_brightness(brightness)
        time.sleep(0.05)

def fade_transition(start_brightnesses, end_brightnesses, duration):
    steps = 20
    step_time = duration / steps
    for step in range(steps + 1):
        fraction = step / steps
        current = [
            start + (end - start) * fraction
            for start, end in zip(start_brightnesses, end_brightnesses)
        ]
        set_individual_brightness(current)
        time.sleep(step_time)

def halloween_effect():
    # Start with lightning
    lightning_flash()
    
    # Fade into an eerie glow
    fade_transition([0, 0, 0], [0.4, 0.3, 0.5], 1.0)
    
    # Flicker for a while
    flicker_effect(3.0, base_brightness=0.4)
    
    # Pulse effect
    pulse_effect(2.0)
    
    # Intense flicker building up
    flicker_effect(2.0, base_brightness=0.6)
    
    # Final lightning flash
    lightning_flash()
    
    # Slow fade to darkness
    fade_transition([0.4, 0.3, 0.5], [0, 0, 0], 2.0)

# Main loop
last_trigger = 0
cooldown = 5  # Seconds between triggers

while True:
    current_time = time.monotonic()
    if pir.value and (current_time - last_trigger) >= cooldown:
        print("Motion detected! Triggering spooky effect!")
        halloween_effect()
        last_trigger = current_time
    else:
        set_all_brightness(0)
    time.sleep(0.1)