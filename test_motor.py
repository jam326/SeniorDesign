import RPi.GPIO as GPIO
from helper import Motor
import time


motor = Motor(1, 2, 3, 4, 5)
motor.move_forward()
time.sleep(1)
motor.hard_stop()
time.sleep(1)
motor.move_backward()
time.sleep(1)
motor.hard_stop()
time.sleep(1)



