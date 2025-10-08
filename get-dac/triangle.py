import r2r_dac as r2r
import signal_generator as sg
import time
import math

def triangle(freq,time):
    res = (2/3.14*math.asin(math.sin(2*3.14*freq*time))+1)/2
    return res

amplitude = 3.16
signal_frequency = 5
sampling_frequency = 1000

gpio_bits = [16, 20,21,25,26,17,27,22]

if __name__ == "__main__":
    try:
        dac = r2r.R2R_DAC(gpio_bits, amplitude, True)
        while True:
            sg.wait_for_sampling_period(sampling_frequency)
            voltage = triangle(signal_frequency,time.time())
            dac.set_voltage(voltage*amplitude)
    finally:
        dac.deinit()
