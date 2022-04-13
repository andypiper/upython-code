# Waveshare UV sensor

from machine import Pin, ADC
import utime

# Select ADC input 0 (GPIO26)
ADC_ConvertedValue = machine.ADC(0)

while True:
    AD_value = ADC_ConvertedValue.read_u16()

    if (AD_value > 500) :
        print("UV above average ", AD_value)
    else :
        print("UV below average ", AD_value)
        
    utime.sleep(0.5)
