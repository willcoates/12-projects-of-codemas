from machine import ADC, Pin, PWM
import time

potentiometer = ADC(Pin(27))

class LED:
    def __init__(self, led: PWM):
        self._led = led
        self._lit = False
        self._duty = 0

        led.freq(1000)
        led.duty_u16(0)

    @property
    def lit(self) -> bool:
        return self._lit
    
    @lit.setter
    def lit(self, value: bool):
        self._lit = value
        if value:
            self._led.duty_u16(self._duty)
        else:
            self._led.duty_u16(0)
    
    @property
    def duty(self) -> int:
        return self._duty
    
    @duty.setter
    def duty(self, value: int):
        self._duty = value
        if self._lit:
            self._led.duty_u16(value)


leds = [
    LED(PWM(Pin(18))),
    LED(PWM(Pin(19))),
    LED(PWM(Pin(20))),
]

button_onoff = Pin(21, Pin.IN, Pin.PULL_DOWN)
button_set_brightness = Pin(22, Pin.IN, Pin.PULL_DOWN)
button_next = Pin(26, Pin.IN, Pin.PULL_DOWN)

current_led = 0

def debounce(period_ms = 200):
    """
    Debounces a function, ignoring future calls until period_ms has passed.
    """
    def decorator(fn):
        last_invoke = time.ticks_add(time.ticks_ms(), -period_ms)

        def wrapper(*args, **kwargs):
            nonlocal last_invoke
            now = time.ticks_ms()
            if time.ticks_diff(now, last_invoke) > period_ms:
                last_invoke = now
                fn(*args, **kwargs)
        return wrapper
    return decorator

@debounce()
def toggle_led(pin):
    global current_led
    led = leds[current_led]
    led.lit = not led.lit

@debounce()
def set_brightness(pin):
    global current_led
    led = leds[current_led]
    led.duty = potentiometer.read_u16()

@debounce()
def next_led(pin):
    global current_led
    current_led += 1
    if current_led >= 3:
        current_led = 0

button_onoff.irq(toggle_led, trigger=Pin.IRQ_RISING)
button_set_brightness.irq(set_brightness, trigger=Pin.IRQ_RISING)
button_next.irq(next_led, trigger=Pin.IRQ_RISING)
