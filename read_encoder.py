# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 22:25:52 2020

@author: Jenna
"""

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)


#Set variables
motorPosition = 0
encoderStatus = 0

#Assign pins
Pin_motor_encoderA = 13
Pin_motor_encoderB = 6

#create function for edge detect
def updateMotorPosition(position,status):
    #bitwise shift to left by  1 bit
    status <<= 1
    #read channel A and put that value into the rightmost bit of encoderStatus
    status |= GPIO.input(Pin_motor_encoderA)
    #bitwise shift to left by 1 bit
    status <<= 1
    #read channel B and put that value into the 
    status |= GPIO.input(Pin_motor_encoderB)
    #truncate encoder status to rightmost 4 bits
    status &= 15
    #if encoder status matches pattern for counting up by one, add one to motorPosition
    if status == 2 or status == 4 or status == 11 or status == 13:
         position += 1
    else:
        #otherwise subtract one (since function is only called if something changes)
        position -= 1
    return [position,status]


#Set up -run once
GPIO.setup(Pin_motor_encoderA,GPIO.IN,pull_up_down = GPIO.PUD_UP) #change to GPIO.IN
GPIO.setup(Pin_motor_encoderB,GPIO.IN,pull_up_down = GPIO.PUD_UP) #change to GPIO.IN


#interrupt for encoder pins
GPIO.add_event_detect(Pin_motor_encoderA,GPIO.BOTH,callback = updateMotorPosition) #add GPIO.BOTH, add callback = 
GPIO.add_event_detect(Pin_motor_encoderB,GPIO.BOTH,callback = updateMotorPosition) #add GPIO.BOTH, add callback = 


try:
    while True:
        [motorPosition,encoderStatus] = updateMotorPosition(motorPosition,encoderStatus)
        print(motorPosition)
        print(encoderStatus)
except KeyboardInterrupt:
        print('done')
        

