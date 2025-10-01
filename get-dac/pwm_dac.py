import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

dynamic_range = 3.16
dac_bits = [16, 20,21,25,26,17,27,22]
gpio_pin = 12
pwm_frequency = 500


class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.pwm_frequency = pwm_frequency
        GPIO.setup(self.gpio_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.gpio_pin, self.pwm_frequency)
        self.pwm.start(0)
    def deinit(self):
        GPIO.output(self.gpio_pin, 0)
        GPIO.cleanup()
    def set_voltage(self, voltage):
        self.pwm.ChangeDutyCycle(voltage/self.dynamic_range*100)
if __name__ == "__main__":
    try:
        dac = PWM_DAC(gpio_pin, pwm_frequency, dynamic_range, True)
        while True:
            try:
                voltage = float(input("Введите напряжение в вольтах: "))
                dac.set_voltage(voltage)
            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")
    finally:
        dac.deinit()
