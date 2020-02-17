# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 22:25:52 2020

@author: Jenna
"""
'''
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
'''

#Set variables
motorPosition = 0
encoderStatus = 0

#Assign pins
Pin_motor_encoderA = 13
Pin_motor_encoderB = 6

#create function for edge detect
def updateMotorPosition(motorPosition,encoderStatus):
    #bitwise shift to left by  1 bit
    encoderStatus <<= 1
    #read channel A and put that value into the rightmost bit of encoderStatus
    encoderStatus |= GPIO.input(Pin_motor_encoderA)
    #bitwise shift to left by 1 bit
    encoderStatus <<= 1
    #read channel B and put that value into the 
    encoderStatus |= GPIO.input(Pin_motor_encoderB)
    #truncate encoder status to rightmost 4 bits
    encoderStatus &= 15
    #if encoder status matches pattern for counting up by one, add one to motorPosition
    if encoderStatus == 2 or encoderStatus == 4 or encoderStatus == 11 or encoderStatus == 13:
         motorPosition += 1
    else:
        #otherwise subtract one (since function is only called if something changes)
        motorPosition -= 1

#Set up -run once
GPIO.setup(Pin_motor_encoderA,GPIO.IN,pull_up_down = GPIO.PUD_UP) #change to GPIO.IN
GPIO.setup(Pin_motor_encoderB,GPIO.IN,pull_up_down = GPIO.PUD_UP) #change to GPIO.IN


#interrupt for encoder pins
GPIO.add_event_detect(Pin_motor_encoderA,BOTH,updateMotorPosition) #add GPIO.BOTH, add callback = 
GPIO.add_event_detect(Pin_motor_encoderB,BOTH,updateMotorPosition) #add GPIO.BOTH, add callback = 

try:
    while True:
        updateMotorPosition(motorPosition,encoderStatus)
        print(motorPosition)
except KeyboardInterrupt:
        GPIO.cleanup()
        

