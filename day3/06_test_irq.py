from machine import Pin
import time

# Try using an IRQ (interrupt) to read from buttons
# Feels better than a time.sleep loop...

# Set up our LED names and GPI pin numbers
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(3, Pin.IN, Pin.PULL_DOWN)

def on_button1_press(pin):
    red.toggle()

button1.irq(on_button1_press, trigger=Pin.IRQ_RISING)
