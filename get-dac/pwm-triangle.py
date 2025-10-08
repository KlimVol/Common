import pwm_dac
import signal_generator as sg
import time
import math

def triangle(freq,time):
    res = math.fabs((2/3.14*math.asin(math.sin(2*3.14*freq*time))+1)/2)
    return res

amplitude = 3.16
signal_frequency = 10
sampling_frequency = 10000
gpio_pin = 12

if __name__ == "__main__":
    try:
        dac = pwm_dac.PWM_DAC(gpio_pin, sampling_frequency, amplitude, True)
        while True:
            sg.wait_for_sampling_period(sampling_frequency)
            voltage = triangle(signal_frequency,time.time())
            dac.set_voltage(voltage*amplitude%amplitude)
    finally:
        dac.deinit()
