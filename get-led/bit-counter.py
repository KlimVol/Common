import RPi.GPIO as GPIO
import time 

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

sleep_time = 0.2

GPIO.setmode(GPIO.BCM)
leds = [16,12,25,17,27,23,22,24]
buttonup = 9
buttondown = 10
num = 0
nump = 0
GPIO.setup(buttonup, GPIO.IN)
GPIO.setup(buttondown, GPIO.IN)
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)
while True:
    if(GPIO.input(buttonup)):
        nump = num
        num-=1
        if(num<0):
            num = 7
        print(dec2bin(num))
        time.sleep(sleep_time)
    if(GPIO.input(buttondown)):
        nump = num
        num+=1
        if(num>7):
            num = 0
        print(dec2bin(num))
        time.sleep(sleep_time)
    GPIO.output(leds[num], 1)
    GPIO.output(leds[nump], 0)
     