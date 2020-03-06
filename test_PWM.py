import RPi.GPIO as GPIO
import time
from helper import Motor

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pinA = 20
pinB = 21
#need to fix for BCM
pinPWM = 14
pinDIR1 = 15
pinDIR2 = 18

motor = Motor(pinA,pinB,pinPWM,pinDIR1,pinDIR2)

GPIO.setup(pinA, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(pinB, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(pinPWM,GPIO.OUT)
GPIO.setup(pinDIR1,GPIO.OUT)
GPIO.setup(pinDIR2,GPIO.OUT)

GPIO.add_event_detect(pinA, GPIO.BOTH, callback=motor.updateposition)  # add GPIO.BOTH, add callback =
GPIO.add_event_detect(pinB, GPIO.BOTH, callback=motor.updateposition)


mode = 'forward'
motor.move_forward()
try:
    while True:
        print(motor.position)
        if mode == 'forward' and motor.position > 100:
            mode = 'backwards'
            motor.move_backward()
        if mode == 'backwards' and motor.position < 0:
            mode = 'forward'
            motor.move_forward()
          
except KeyboardInterrupt:
    motor.hard_stop()
    pass

GPIO.cleanup


