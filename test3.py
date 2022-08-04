from machine import Pin
from esp32_gpio_lcd import GpioLcd
import time

lcd = GpioLcd(rs_pin=Pin(0), rw_pin=Pin(1), enable_pin=Pin(2),
              d4_pin=Pin(4), d5_pin=Pin(5), d6_pin=Pin(6),d7_pin=Pin(7))

Counter = 0
while True:
    lcd.clear()
    lcd.putstr(str(Counter))