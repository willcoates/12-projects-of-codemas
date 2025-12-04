from machine import Pin
from utime import sleep

onboardLED = Pin(25, Pin.OUT)
enabled = True

while True:
    onboardLED.value(enabled)
    enabled = not enabled
    sleep(0.5)
