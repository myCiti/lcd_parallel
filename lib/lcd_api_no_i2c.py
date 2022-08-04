from machine import Pin
from time import sleep_ms, sleep_us

class Lcd:
    """Implements the API for talking with HD44780 compatible character LCDs without I2C protocol."""
    def __init__(self, rs, enable, d4, d5, d6, d7):
        self.rs_pin = Pin(rs, Pin.OUT)
        self.enable_pin = Pin(enable, Pin.OUT)
        self.d4_pin = Pin(d4, Pin.OUT)
        self.d5_pin = Pin(d5, Pin.OUT)
        self.d6_pin = Pin(d6, Pin.OUT)
        self.d7_pin = Pin(d7, Pin.OUT)
        self.setUpLCD()
    
    def pulseE(self):
        self.enable_pin.high()
        sleep_us(40)
        self.enable_pin.low()
        sleep_us(40)

    
    def returnHome(self):
        self.rs_pin.low()
        self.send2LCD8(0b00000010)
        self.rs_pin.high()
        sleep_ms(2)
    
    def moveCursorRight(self):
        self.rs_pin.low()
        self.send2LCD8(0b00010100)
        self.rs_pin.high()
        sleep_us(2)

    def setCursor(self, line, col):
        b = 0
        if line == 1:
            b = 0
        elif line == 2:
            b = 40
        self.returnHome()
        for _ in range(0, b+col):
            self.moveCursorRight()
    
    def send2LCD4(self, BinNum):
        self.d4_pin.value((BinNum & 0b00000001) >>0)
        self.d5_pin.value((BinNum & 0b00000010) >>1)
        self.d6_pin.value((BinNum & 0b00000100) >>2)
        self.d7_pin.value((BinNum & 0b00001000) >>3)
        self.pulseE()
    
    def send2LCD8(self, BinNum):
        self.d4_pin.value((BinNum & 0b00010000) >>4)
        self.d5_pin.value((BinNum & 0b00100000) >>5)
        self.d6_pin.value((BinNum & 0b01000000) >>6)
        self.d7_pin.value((BinNum & 0b10000000) >>7)
        self.pulseE()
        self.d4_pin.value((BinNum & 0b00000001) >> 0)
        self.d5_pin.value((BinNum & 0b00000010) >> 1)
        self.d6_pin.value((BinNum & 0b00000100) >> 2)
        self.d7_pin.value((BinNum & 0b00001000) >> 3)
        self.pulseE()
    
    def setUpLCD(self):
        self.rs_pin.value(0)
        self.send2LCD4(0b0011)#8 bit
        self.send2LCD4(0b0011)#8 bit
        self.send2LCD4(0b0011)#8 bit
        self.send2LCD4(0b0010)#4 bit
        self.send2LCD8(0b00101000)#4 bit,2 lines?,5*8 bots
        self.send2LCD8(0b00001100)#lcd on, blink off, cursor off.
        self.send2LCD8(0b00000110)#increment cursor, no display shift
        self.send2LCD8(0b00000001)#clear screen
        sleep_ms(2)#clear screen needs a long delay
    
    def write_line(self, msg:str, line:int, col:int):
        self.setCursor(line, col)
        for c in msg:
            self.send2LCD8(ord(c))

def main():
    import time
    lcd = Lcd(rs=16, enable=17, d4=18, d5=19, d6=20, d7=21)
    while True:
        start = time.ticks_ms()
        lcd.write_line('H', 1, 5)
        elapsed = time.ticks_diff(time.ticks_ms(), start)
        print(f'Delai: {elapsed:,}')
        time.sleep_ms(500)

if __name__ == '__main__':
    main()
