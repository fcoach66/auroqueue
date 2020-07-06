#!/usr/bin/env python3
from gpiozero import Button, OutputDevice
import RPi.GPIO as GPIO
from time import sleep
import os

button24 = Button(24)

Relay_Ch1 = 26
Relay_Ch2 = 20
Relay_Ch3 = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(Relay_Ch1,GPIO.OUT)
GPIO.setup(Relay_Ch2,GPIO.OUT)
GPIO.setup(Relay_Ch3,GPIO.OUT)

GPIO.output(Relay_Ch1,GPIO.HIGH)
GPIO.output(Relay_Ch2,GPIO.HIGH)
GPIO.output(Relay_Ch3,GPIO.HIGH)

while True:
    if button24.is_pressed:
        os.system('curl http://localhost:8000/api/advance/1 &')
        GPIO.output(Relay_Ch1,GPIO.LOW)
        sleep(5)
        GPIO.output(Relay_Ch1,GPIO.HIGH)
    sleep(0.5)
