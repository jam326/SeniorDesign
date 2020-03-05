import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
from helper import Motor
GPIO.setwarnings(False)
import time


pinA = 20
pinB = 21
#need to fix for BCM
pinPWM = 8
pinDIR1 = 10
pinDIR2 = 12

motor = Motor(pinA,pinB,pinPWM,pinDIR1,pinDIR2)
GPIO.setup(pinA, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pinB, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(pinA, GPIO.BOTH, callback=motor.updateposition)  # add GPIO.BOTH, add callback =
GPIO.add_event_detect(pinB, GPIO.BOTH, callback=motor.updateposition)  # add GPIO.BOTH, add callback =

try:
    while True:
        print(motor.position)
except KeyboardInterrupt:
    pass

GPIO.cleanup()