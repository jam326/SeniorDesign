import RPi.GPIO as GPIO
from helper import Motor
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pinA = 20
pinB = 21
#need to fix for BCM
pinPWM = 14
pinDIR1 = 15
pinDIR2 = 18

GPIO.setup(pinA, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pinA, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pinPWM,GPIO.OUT)
GPIO.setup(pinDIR1,GPIO.OUT)
GPIO.setup(pinDIR2,GPIO.OUT)

motor = Motor(pinA,pinB,pinPWM,pinDIR1,pinDIR2)
motor.move_forward()
time.sleep(1)
motor.hard_stop()
time.sleep(1)
motor.move_backward()
time.sleep(1)
motor.hard_stop()
time.sleep(1)

GPIO.cleanup()



