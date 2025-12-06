from machine import ADC, Pin, PWM
import time

red = PWM(Pin(18))

potentiometer = ADC(Pin(27))

red.freq(1000)

while True:
    reading = potentiometer.read_u16()
    print(reading)

    red.duty_u16(reading)

    time.sleep(0.001)

