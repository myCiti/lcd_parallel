from math import trunc
from machine import Pin
from gpio_lcd import GpioLcd
import time

lcd = GpioLcd(rs_pin=Pin(16),
                enable_pin=Pin(17),
                d4_pin=Pin(18),
                d5_pin=Pin(19),
                d6_pin=Pin(20),
                d7_pin=Pin(21),
                num_lines=4, num_columns=20
                )

# lcd = GpioLcd(rs_pin=Pin(16),
#                 enable_pin=Pin(17),
#                 d0_pin=Pin(15),
#                 d1_pin=Pin(14),
#                 d2_pin=Pin(13),
#                 d3_pin=Pin(12),
#                 d4_pin=Pin(18),
#                 d5_pin=Pin(19),
#                 d6_pin=Pin(20),
#                 d7_pin=Pin(21),
#                 num_lines=2, num_columns=16
#                 )

# lcd4bit.move_to(0, 0)
# lcd.blink_cursor_on()
# lcd4bit.putstr('Micropython')
# lcd8bit.putstr('Micro 8bits')
# lcd.putstr('LCD16x2display')
lcd.clear()
while True:
    start = time.ticks_ms()
    lcd.move_to(0,0)
    lcd.putstr('A'*20)
    lcd.move_to(0,3)
    lcd.putstr('B'*20)
    elapsed = time.ticks_diff(time.ticks_ms(), start)
    print(f'Delai: {elapsed}')
    time.sleep_ms(500)