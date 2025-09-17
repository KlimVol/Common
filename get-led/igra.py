import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
leds = [24,22,23,27,17,25,12,16]
buttonup = 9
buttondown = 10
exitbutt = 13
currnum = 0
ornum = 0
light_time = 0.1
sum = 0
GPIO.setup(exitbutt, GPIO.IN)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(buttonup, GPIO.IN)
GPIO.setup(buttondown, GPIO.OUT)
GPIO.output(leds, 0)
time1 = time.time()
while True:
    if(time.time() - time1 > 5):
        sum+=1
        time1 = time.time()
        print(currnum)
        if(currnum!=ornum):
            GPIO.output(leds, 1)
            time.sleep(1)
            GPIO.output(leds, 0)
            break
        currnum = 0
        ornum = random.randint(0,7)
        print(ornum)
        for i in range(len(leds)):
            if(i != ornum):
                GPIO.output(leds[i], 1)
                time.sleep(light_time)
                GPIO.output(leds[i], 0)
        for i in range(len(leds)):
            if(7-i != ornum):
                GPIO.output(leds[7-i], 1)
                time.sleep(light_time)
                GPIO.output(leds[7-i], 0)
    if(GPIO.input(buttondown)):
        currnum=currnum - 1
        if(currnum<0):
            currnum = 7
        time.sleep(0.2)
    if(GPIO.input(buttonup)):
        currnum=currnum + 1
        if(currnum>7):
            currnum = 0
        time.sleep(0.2)
    flag = False
    if(GPIO.input(exitbutt)):
        GPIO.output(leds, 1)
        time.sleep(1)
        GPIO.output(leds, 0)
        break
    if(sum==5):
        for led in leds:
            GPIO.output(led, 1)
            time.sleep(0.01)
            GPIO.output(led, 0)
        for led in reversed(leds):
            GPIO.output(led, 1)
            time.sleep(0.01)
            GPIO.output(led, 0)
        break
    

    