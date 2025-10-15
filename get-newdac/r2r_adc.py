import RPi.GPIO as GPIO
import r2r_dac 
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
dynamic_range = 3
gpio_bits = [11,25,12,13,16,19,20,26]
gpio_bits = gpio_bits[::-1]
comp_pin = 21
GPIO.setup(comp_pin, GPIO.IN)

if __name__ == "__main__":
    adc = r2r_dac.R2R_DAC(gpio_bits, dynamic_range, True)
    try:
        
        while True:
            l0 = 0
            r = 255
            while( r-l0 > 1):
                adc.set_number((r+l0)//2)
                time.sleep(0.005)
                if(GPIO.input(comp_pin)):
                    r = (r+l0)//2
                else:
                    l0 = (r+l0)//2
            print(((r+l0)/510)*3)
    finally:
        adc.deinit()
