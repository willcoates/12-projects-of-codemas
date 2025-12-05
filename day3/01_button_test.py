from machine import Pin
import time

# Set up our LED names and GPI pin numbers
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)

while True:
    time.sleep(0.2)

    if button1.value() == 1:
        print("Button 1 pressed")
