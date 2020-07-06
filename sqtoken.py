#!/usr/bin/env python3
from gpiozero import Button
from time import sleep
import os

button23 = Button(23)

while True:
    if button23.is_pressed:
        os.system('curl http://localhost:8000/api/token &')
    sleep(0.5)
