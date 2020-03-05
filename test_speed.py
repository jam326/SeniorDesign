import RPi.GPIO as GPIO
from helper import Motor
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pinA = 20
pinB = 21
#need to fix for BCM
pinPWM = 8
pinDIR1 = 10
pinDIR2 = 12

motor = Motor(pinA,pinB,pinPWM,pinDIR1,pinDIR2)
motor = Motor(pinA,pinB,pinPWM,pinDIR1,pinDIR2)
GPIO.setup(pinA, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pinB, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(pinA, GPIO.BOTH, callback=motor.updateposition)  # add GPIO.BOTH, add callback =
GPIO.add_event_detect(pinB, GPIO.BOTH, callback=motor.updateposition)

try:
    while True:
        motor.speed_computation()
        time.sleep(.05)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
        
