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


def Prenta_innganga(innganga_listi):
    stada_skynjara = []
    for inngangur in innganga_listi:
        stada_skynjara.append(GPIO.input(inngangur))
    print("Stada Skynjara:", stada_skynjara)


def Bera_saman_fugla_og_skynjara(innganga_listi, fugla_listi):
    stada_skynjara = []
    for inngangur in innganga_listi:
        stada_skynjara.append(GPIO.input(inngangur))
    fugl_nr = 0
    for fugl in fugla_listi:
        fugl_nr += 1
        if fugl == stada_skynjara:
            #print("Spila Fuglahljóð nr:", fugl_nr)
            return fugl_nr
            break
    return 0
    
    
innganga_listi = [16, 18, 19, 21, 22, 23, 24, 26]
GPIO.setup(innganga_listi, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# The GPIO-pins NEED to have 'pull-ups'!
# The sensors are wired in such a way that when it sense something,
# it will connect the GPIO-pin to ground(GND).
# NO 3V3 OR 5V ARE NEED FOR THE SENSORS AND SHOULD NOT BE CONNECTED!


fugla_listi = [[0,0,0,0,0,0,0,0],  # Fálki.
               [0,1,0,1,0,1,0,1],  # Stokkönd.
               [1,0,1,0,1,0,1,0],  # Auðnutitlingur.
               [1,1,1,1,1,1,1,1]]  # Stelkur.


try:
    print("Main Loop Byrjar.")
    while(True):
        #Prenta_innganga(innganga_listi)
        fugl_nr = Bera_saman_fugla_og_skynjara(innganga_listi, fugla_listi)
        if fugl_nr > 0:
            print("Spila Fuglahljóð nr:", fugl_nr)
        time.sleep(0.2)
except Exception as e:
    print("VILLA!", e)
finally:
    GPIO.cleanup()
    print("Cleanup.")
