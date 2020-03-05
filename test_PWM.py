import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

pinA =
pinB =
pinPWM =
pinDIR1 =
pinDIR2 =

GPIO.setup(pinA, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(pinB, GPIO.IN, pull_up_down = GPIO.PUD_UP)


GPIO.setup(pinPWM,GPIO.OUT)
GPIO.setup(pinDIR1,GPIO.OUT)
GPIO.setup(pinDIR2,GPIO.OUT)

p = GPIO.PWM(pinPWM, 207)
p.start(0)
try:
    while True:
        for i in range(0,100):
            p.ChangeDutyCycle(i)
            time.sleep(0.02)
        for i in range(0,100):
            p.ChangeDutyCycle(100-i)
            time.sleep(0.02)
except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup


