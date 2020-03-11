#!/usr/bin/env python3


###
###  To Run Script Do:
###  python3 ./Fuglabord_main.py 
###


### Import Modules:
import math
import time

# Import the python-vlc module
# https://www.olivieraubert.net/vlc/python-ctypes/doc/
import vlc

# Import the GPIO module and check to see if it is successful:
# https://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("""Error importing RPi.GPIO! This is probably because you need superuser privileges.  
    You can achieve this by using 'sudo' to run your script""")
    
# Using the BOARD numbering system. This refers to the pin numbers on the P1 header of
# the Raspberry Pi board.
GPIO.setmode(GPIO.BOARD)


GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def Callback_22(channel):
    print("Callback_22", channel, GPIO.input(22))

def Callback_24():
    print("Callback_24")

def Callback_26():
    print("Callback_26")

    
GPIO.add_event_detect(22, GPIO.BOTH)
GPIO.add_event_detect(24, GPIO.BOTH)
GPIO.add_event_detect(26, GPIO.BOTH)
 
GPIO.add_event_callback(22, Callback_22)
GPIO.add_event_callback(24, Callback_24)
GPIO.add_event_callback(26, Callback_26)


try:
    print("Loop.")
    while(True):
        time.sleep(0.2)
except:
    GPIO.cleanup()
    print("Cleanup.")




"""
GPIO.output(5, GPIO.LOW)
for i in range(5):
    GPIO.output(5, not GPIO.input(5))
    print("Working", i)
    time.sleep(3)
"""
