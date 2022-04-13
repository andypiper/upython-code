# Waveshare MQ5 sensor

from machine import Pin, ADC
import utime

# Select ADC input 0 (GPIO26)
ADC_ConvertedValue = machine.ADC(0)
DIN = Pin(2,Pin.IN)
conversion_factor = 3.3 / (65535)

while True:
    if (DIN.value() == 1):
        print("No gas leak")
    else:
        print("Gas leak!")
        AD_value = ADC_ConvertedValue.read_u16() * conversion_factor
        print("Current AD value = ", AD_value, "V")
    utime.sleep(0.5)
