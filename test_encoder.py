import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
from helper import Motor

pinA =
pinB =
pinPWM =
pinDIR1 =
pinDIR2 =

motor = Motor(pinA,pinB,pinPWM,pinDIR1,pinDIR2)
GPIO.add_event_detect(pinA, GPIO.BOTH, callback = motor.updateposition)  # add GPIO.BOTH, add callback =
GPIO.add_event_detect(pinB, GPIO.BOTH, callback = motor.updateposition)  # add GPIO.BOTH, add callback =

try: 
    while True:
        print(motor.position)
except: KeyboardInterrupt
    pass
