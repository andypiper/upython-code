# Waveshare DHT11 sensor

from machine import Pin
import dht
import utime

sensor = dht.DHT11(Pin(2))

while True:
    sensor.measure()
    print('Temperature: %3.1f C' %sensor.temperature())
    print('Humidity: %3.1f %%' %sensor.humidity())
    utime.sleep(3)
