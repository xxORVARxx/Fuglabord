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
