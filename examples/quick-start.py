from GPIOEmulator.EmulatorGUI import GPIO
from GPIOEmulator.EmulatorGUI import app

#import RPi.GPIO as GPIO
import time
import traceback
 
def Main():
    try:
        GPIO.setmode(GPIO.BCM)

        GPIO.setwarnings(False)

        GPIO.setup(15, GPIO.IN)
        GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP)
        GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

        GPIO.setup(14, GPIO.OUT)
        GPIO.setup(17, GPIO.OUT, initial = GPIO.LOW)

        while(True):

            if (GPIO.input(15) == True):
                GPIO.output(14,GPIO.HIGH)
            else:
                GPIO.output(14,GPIO.LOW)

            if (GPIO.input(23) == False):
                GPIO.output(17,GPIO.HIGH)
                time.sleep(1)

            if (GPIO.input(24) == True):
                GPIO.output(17,GPIO.LOW)
                time.sleep(1)

    except Exception as ex:
        traceback.print_exc()
    finally:
        GPIO.cleanup() #this ensures a clean exit
    
Main()
    