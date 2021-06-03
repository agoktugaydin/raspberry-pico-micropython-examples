from machine import Pin
import time

led = Pin(25, Pin.OUT)

start = time.time()
c = 0


while (True):
    if (time.time() - start == 1):
        start = time.time()
        led.toggle()
        print("pass")
        c += 1
    if (c == 5):
        print("pass_5")
        c = 0
        
