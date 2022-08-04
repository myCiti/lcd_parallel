# alcdtest.py Test program for LCD class
# Author: Peter Hinch
# Copyright Peter Hinch 2017-2020 Released under the MIT license
# Updated for uasyncio V3
# runs for 20s
import uasyncio as asyncio
import utime as time
from alcd import LCD

PINLIST = [16, 17, 18, 19, 20, 21]

lcd = LCD(PINLIST, cols = 16)

async def lcd_task():
    for secs in range(20, -1, -1):
        lcd[0] = 'MicroPython {}'.format(secs)
        lcd[1] = "{:11d}uS".format(time.ticks_us())
        await asyncio.sleep(1)


def test1():
    import time
    while True:
        start = time.ticks_ms()
        # lcd.write_line('Hello World', 0)
        # lcd.write_line('Hello', 0)
        lcd.write_line2('K'*4, 1, 1)
        elapsed = time.ticks_diff(time.ticks_ms(), start)
        print(f'Delai: {elapsed}')
        time.sleep_ms(500)

if __name__ == '__main__':
    # asyncio.run(lcd_task())
    test1()