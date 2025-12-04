from machine import Pin
import time

# Set up our LED names and GPI pin numbers
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

counter = 1
while counter < 11:
    print(counter)

    # Red on
    red.value(1)
    amber.value(0)
    green.value(0)

    time.sleep(0.5)

    # Amber on
    red.value(0)
    amber.value(1)
    green.value(0)

    time.sleep(0.5)

    # Green on
    red.value(0)
    amber.value(0)
    green.value(1)

    time.sleep(0.5)

    counter += 1
