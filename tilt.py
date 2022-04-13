# Waveshare Tilt sensor
# not very sensitive...

from machine import Pin
import utime

DIN = Pin(2, Pin.IN)

while True:
     if (DIN.value() == 1):
         print("Stable")
     else:
         print("Vibration!")
     utime.sleep(0.1)
