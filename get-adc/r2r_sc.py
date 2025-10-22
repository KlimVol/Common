import RPi.GPIO as GPIO
import adc_plot
import r2r_adc 
import time

if(__name__=="__main__"):
    dynamic_range = 3
    gpio_bits = [11,25,12,13,16,19,20,26]
    gpio_bits = gpio_bits[::-1]
    comp_pin = 21
    adc = r2r_adc.R2R_ADC(gpio_bits, dynamic_range,comp_pin, True)
    voltage_values = []
    time_values = []
    duration = 3.0
    exp_time = 100
    try:
        start = time.time()
        while(time.time()-start<exp_time):
            voltage=adc.bit_finder()
            voltage_values.append(voltage)
            time_values.append(time.time()-start)
        adc_plot.plot_voltage_vs_time(voltage_values,time_values,dynamic_range)
    finally:
        adc.deinit()