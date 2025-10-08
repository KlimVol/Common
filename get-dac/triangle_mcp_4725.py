import mcp4725_driver
import signal_generator as sg
import time
import math

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

def triangle(freq,time):
    res = (2/3.14*math.asin(math.sin(2*3.14*freq*time))+1)/2
    return res

if __name__ == "__main__":
    try:
        dac = mcp4725_driver.MCP4725(amplitude)
        while True:
            sg.wait_for_sampling_period(sampling_frequency)
            voltage = triangle(signal_frequency,time.time())
            dac.set_voltage(voltage*amplitude)
    finally:
        dac.deinit()
