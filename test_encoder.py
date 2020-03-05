import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
from helper import Motor


pinA = 38
pinB = 40
pinPWM = 8
pinDIR1 = 10
pinDIR2 = 12

motor = Motor(pinA,pinB,pinPWM,pinDIR1,pinDIR2)
GPIO.setup(pinA, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(pinB, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.add_event_detect(pinA, GPIO.BOTH, callback = motor.updateposition)  # add GPIO.BOTH, add callback =
GPIO.add_event_detect(pinB, GPIO.BOTH, callback = motor.updateposition)  # add GPIO.BOTH, add callback =

try:
    while True:
        print(motor.position)
except KeyboardInterrupt:
    pass
