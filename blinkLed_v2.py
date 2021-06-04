from machine import Pin
import time

led = Pin(25, Pin.OUT)
i = 0
c = int(input("Led kaç kez yansın ? \nLütfen tam sayı olarak girin: "))

while (i<c):
    i += 1
    led.toggle()
    time.sleep(1)
    led.toggle()
    time.sleep(1)
