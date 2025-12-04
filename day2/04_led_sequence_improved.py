from machine import Pin
import time

# Set up our LED names and GPI pin numbers
leds = [
    Pin(18, Pin.OUT),
    Pin(19, Pin.OUT),
    Pin(20, Pin.OUT),
]

# Make sure all LEDs are off at start
for led in leds:
    led.value(0)

for counter in range(10):
    print(counter + 1)
    # Cycle through all LEDs
    for led in leds:
        led.value(1)
        time.sleep(0.5)
        led.value(0)
    