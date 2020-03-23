#!/usr/bin/env python3


###
###  Til að kveikja á forrit:
###  python3 ./Fuglabord_main.py "~/path/to/program/"
###


### Import Modules:
import sys
import time
# Import the python-vlc module:
# https://www.olivieraubert.net/vlc/python-ctypes/doc/
import vlc
# Import the GPIO module and check to see if it is successful:
# https://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    time_string = time.strftime("%M:%H-%d.%m.%Y", time.localtime())
    print(time_string, """| Python:  Error importing RPi.GPIO! This 
                       is probably because you need superuser privileges.
                       You can achieve this by using 'sudo' to run 
                       your script""", flush=True)
# Command-line argument:
try:
    directory = str(sys.argv[1])
except:
    time_string = time.strftime("%M:%H-%d.%m.%Y", time.localtime())
    print(time_string, """| Python:  Aðvörun!  Vantar "command-line argument"
                       sem á að inni halda staðsetninguna á forritinu. Til að 
                       kveikja á forrit:  
                       python3 ./Fuglabord_main.py "~/path/to/program/" """,
          flush=True)


# Using the BOARD numbering system. This refers to the pin numbers on
# the P1 header of the Raspberry Pi board.
GPIO.setmode(GPIO.BOARD)


def Stilla_vlc(fugla_hljod):
    vlc_spilarar = []
    for hljod in fugla_hljod:
        time_string = time.strftime("%M:%H-%d.%m.%Y", time.localtime())
        print(time_string, "| Python:  VLC: ",
              vlc_spilarar.append(vlc.MediaPlayer(hljod)), hljod)
    for spilari in vlc_spilarar:
        spilari.audio_set_volume(100)
    return vlc_spilarar


def Prenta_innganga(innganga_listi):
    stada_skynjara = []
    for inngangur in innganga_listi:
        stada_skynjara.append(GPIO.input(inngangur))
    time_string = time.strftime("%M:%H-%d.%m.%Y", time.localtime())
    print(time_string, "| Python:  Stada Skynjara:", stada_skynjara)


def Bera_saman_fugla_og_skynjara(innganga_listi, fugla_listi):
    stada_skynjara = []
    for inngangur in innganga_listi:
        stada_skynjara.append(GPIO.input(inngangur))
    fugl_nr = 0
    for fugl in fugla_listi:
        if fugl == stada_skynjara:
            #print("Spila Fuglahljóð nr:", fugl_nr)
            return fugl_nr
            break
        fugl_nr += 1
    return -1


def Spila_hljod(spilari, fugl):
    if not spilari.is_playing():
        spilari.stop()
        spilari.play()
        time_string = time.strftime("%M:%H-%d.%m.%Y", time.localtime())
        print(time_string, "| Python:  Play:", fugl)



innganga_listi = [16, 18, 19, 21, 22, 23, 24, 26]
GPIO.setup(innganga_listi, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# The GPIO-pins NEED to have 'pull-ups'!
# The sensors are wired in such a way that when it sense something,
# it will connect the GPIO-pin to ground(GND).
# NO 3V3 OR 5V ARE NEED FOR THE SENSORS AND SHOULD NOT BE CONNECTED!


fugla_listi = [[0,0,0,0,0,0,0,0],  # Fálki.
               [0,1,0,1,0,1,0,1],  # Stokkönd.
               [1,0,1,0,1,0,1,0],  # Auðnutittlingur.
               [1,1,1,1,1,1,1,1]]  # Stelkur.
fugla_hljod = [directory +"falki.ogg",
               directory +"stokkond.ogg",
               directory +"audnutittlingur.ogg",
               directory +"stelkur.ogg"]
vlc_spilarar = Stilla_vlc(fugla_hljod)


time.sleep(5)
var_ad_spila = -1
try:
    time_string = time.strftime("%M:%H-%d.%m.%Y", time.localtime())
    print(time_string, "| Python:  Main Loop Byrjar.")
    while(True):
        #Prenta_innganga(innganga_listi)
        fugl_nr = Bera_saman_fugla_og_skynjara(innganga_listi, fugla_listi)
        if fugl_nr >= 0:
            if fugl_nr != var_ad_spila:
                #print("Spila Fuglahljóð nr:", fugl_nr)
                Spila_hljod(vlc_spilarar[fugl_nr], fugla_hljod[fugl_nr])
                var_ad_spila = fugl_nr
        else:
            var_ad_spila = -1
        time.sleep(0.2)
except Exception as e:
    time_string = time.strftime("%M:%H-%d.%m.%Y", time.localtime())
    print(time_string, "| Python:  VILLA!", e)
finally:
    GPIO.cleanup()
    time_string = time.strftime("%M:%H-%d.%m.%Y", time.localtime())
    print(time_string, "| Python:  GPIO Cleanup done.")
