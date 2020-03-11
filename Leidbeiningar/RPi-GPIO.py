
###
### https://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/
###



# Import the module and check to see if it is successful:
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("""Error importing RPi.GPIO! This is probably because you need superuser privileges.  
    You can achieve this by using 'sudo' to run your script""")


# To discover information about your RPi:
GPIO.RPI_INFO
# To discover the Raspberry Pi board revision:
GPIO.RPI_INFO['P1_REVISION']
# To discover the version of RPi.GPIO:
GPIO.VERSION


# Using the BOARD numbering system. This refers to the pin numbers on the P1 header of
# the Raspberry Pi board. Using This your hardware will always work, regardless of the
# revision of the RPi board. 
GPIO.setmode(GPIO.BOARD)
# Using the channel numbers on the Broadcom SOC. You have to always work with a diagram of
# which channel number goes to which pin on the RPi board. Your script could break
# between revisions of RPi boards.
GPIO.setmode(GPIO.BCM)

# To detect which pin numbering system has been set:
mode = GPIO.getmode()
print(mode)
# The mode will be 'GPIO.BOARD', 'GPIO.BCM' or 'None'.


# To checking for a function of a RPi-GPIO channel:
func = GPIO.gpio_function(pin)
# Will return a value from:
# GPIO.IN, GPIO.OUT, GPIO.SPI, GPIO.I2C, GPIO.HARD_PWM, GPIO.SERIAL, GPIO.UNKNOWN


# If other scripts/circuits has made changes to the GPIO of your RPi board,
# you get a warning. To disable:
GPIO.setwarnings(False)



###################################### BASIC USAGE ######################################

# You need to set up every 'channel' you are using as an input or an output.
GPIO.setup(channel, GPIO.IN)
GPIO.setup(channel, GPIO.OUT)
# 'channel' is the pin number based on 'BOARD' or 'BCM'.

# Pull-up - 10K resistor between the input channel and 3.3V (pull-up):
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# Pull-down - 10K resistor between the input channel and 0V (pull-down):
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# An input pin not connected to anything will 'float', and it can change value a lot
# as a result of receiving interference.

# You can set up more than one channel, using 'list' or 'tuples':
chan_list = [11,12]
GPIO.setup(chan_list, GPIO.OUT)
chan_tub = (11,12)
GPIO.setup(chan_tub, GPIO.IN)



# Input - To read the value of a GPIO pin:
GPIO.input(channel)
# This will return either:
#   0 / GPIO.LOW / False.
#   1 / GPIO.HIGH / True.

# Testing inputs (polling)
if GPIO.input(channel):
    print('Input was HIGH')
else:
    print('Input was LOW')
    
# To wait for a button press by polling in a loop:
while GPIO.input(channel) == GPIO.LOW:
    time.sleep(0.01)  # wait 10 ms to give CPU chance to do other things



# Output - To set the output state of a GPIO pin:
GPIO.output(channel, state)
# State can be:
#   0 / GPIO.LOW / False.
#   1 / GPIO.HIGH / True.

# 'channel' is the pin number based on 'BOARD' or 'BCM'.



# You can output to many channels, using 'list' or 'tuples':
chan_list = [11,12]                           # <- Also works with tuples.
GPIO.output(chan_list, GPIO.LOW)              # <- Sets all to GPIO.LOW.
GPIO.output(chan_list, (GPIO.HIGH, GPIO.LOW)) # <- Sets first HIGH and second LOW.


# For example to toggle an output:
GPIO.output(12, not GPIO.input(12))



# Cleanup - It returns all channels you have used back to inputs with no pull up/down.
# It also clears the pin numbering system in use.
GPIO.cleanup()
# You dont have to clean up every channel, you can some set-up when your program exits.
# You can clean up individual channels, a list or a tuple of channels:
GPIO.cleanup(channel)
GPIO.cleanup( (channel1, channel2) )
GPIO.cleanup( [channel1, channel2] )



###################################### EVENTS ###########################################

# Polling - Is to manually check the input value at a point in time.
# Interrupt (edge detection) - Is when the input value transition from
#                               HIGH to LOW (falling edge) or LOW to HIGH (rising edge).


# Event is a change in state of an input, but not necessary its value at a point in time.
# You can use 'Events' To avoid missing a button press while your program is busy doing
# something else:

# This function will stop your program until an edge is detected: (good for the CPU)
GPIO.wait_for_edge(channel, GPIO.RISING)
# You can detect edges of type:
#   'GPIO.RISING', 'GPIO.FALLING', 'GPIO.BOTH'.

# Wait for up to 5 seconds for a rising edge (timeout is in milliseconds)
channel = GPIO.wait_for_edge(channel, GPIO_RISING, timeout=5000)
if channel is None:
    print('Timeout occurred')
else:
    print('Edge detected on channel', channel)
# 'channel' is the pin number based on 'BOARD' or 'BCM'.



# Add rising edge detection on a channel, this can be used in a loop with other things:
GPIO.add_event_detect(channel, GPIO.FALLING)
...
do_something()
...
if GPIO.event_detected(channel):
    print('Button pressed', channel)
# You can detect edges of type:
#   'GPIO.RISING', 'GPIO.FALLING', 'GPIO.BOTH'.


# RPi.GPIO can run a second thread for callback-functions.
def My_callback(channel):
    print('This is run in a different thread to your main program')

GPIO.add_event_detect(channel, GPIO.RISING, callback=My_callback)


# Switch debounce - Is When callbacks are called more than once for each button press.
# You can fix this by add a 0.1uF capacitor across your switch.
# Or you can use software debouncing and wait for some milliseconds:
GPIO.add_event_detect(channel, GPIO.RISING, callback=my_callback, bouncetime=200)
# or:
GPIO.add_event_callback(channel, my_callback, bouncetime=200)


# If your program no longer needs event detection, you can remove it:
GPIO.remove_event_detect(channel)



###################################### PWM ##############################################

# Using PWM in RPi.GPIO, To create a PWM instance:
p = GPIO.PWM(channel, frequency)
# 'channel' is the pin number based on 'BOARD' or 'BCM'.

# To start PWM:
p.start(dc)
# 'dc' is the duty-cycle, a float between 0 and 100 (0.0 <= dc <= 100.0).

# To change the frequency:
p.ChangeFrequency(freq)
# 'freq' is the new frequency in Hz.

# To change the duty-cycle:
p.ChangeDutyCycle(dc)
# 0.0 <= dc <= 100.0

# To stop PWM:
p.stop()
# Note that PWM will also stop if the instance variable 'p' goes out of scope.
