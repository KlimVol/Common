import RPi.GPIO as GPIO
import time
import math
GPIO.setwarnings(False)

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)
voltage = 100
period = 1
leds = [8,11,7,1,0,5,12,6]
GPIO.setup(leds, GPIO.OUT)
while True:
    GPIO.output(leds, dec2bin(abs(int(voltage))))
    voltage=127 + 128*math.sin(float(2*3.14*time.time()/period))