# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 18:09:08 2020

@author: Jenna
"""
import time
from GPIO import Gpio
from helper import Motor
# from GPIO import PWM
GPIO = Gpio()
# -----------------------------------------PIN SET UP---------------------------------------------------
# assign pin numbers to variables
PinMotorEncoderA = 0
PinMotorEncoderB = 0
PinMotor_PWM = 0
PinMotor_DIR1 = 0
PinMotor_DIR2 = 0

# set pins as input or output
# inputs: add pull-up or pull-down resistor if needed
"""
# set to input or output and turn on pullup resistors for input channels
GPIO.setup(PinMotorEncoderA, GPIO.IN, pull_up_down = GPIO.PUD_UP)  
GPIO.setup(PinMotorEncoderB, GPIO.IN, pull_up_down = GPIO.PUD_UP)   
"""
GPIO.setup(PinMotor_PWM, GPIO.OUT)
GPIO.setup(PinMotor_DIR1, GPIO.OUT)
GPIO.setup(PinMotor_DIR2, GPIO.OUT)

# ----------------------------------------STATE VARIABLES--------------------------------------------------
# set state variables
weighLaundry = 0
home = 1
setVolume = 2
h2o_1 = 3
move2dispense = 4
h2o_2 = 5
move2compress = 6
compress = 7
push2surface = 8
kickPod = 9

# set initial state
state = weighLaundry
old_state = weighLaundry
start_time = time.time()
count = 0

# --------------------------------------MOTOR SET-UP------------------------------------------------
# create motor object
motor = Motor(PinMotorEncoderA, PinMotorEncoderB, PinMotor_PWM, PinMotor_DIR1, PinMotor_DIR2)

# set position constants for the motor
dispensePosition = 0
compressPosition = 0
kickEndPosition = 0

# set interrupt for encoder pins
GPIO.add_event_detect(PinMotorEncoderA, GPIO.BOTH, motor.updateposition)  # add GPIO.BOTH, add callback =
GPIO.add_event_detect(PinMotorEncoderB, GPIO.BOTH, motor.updateposition)  # add GPIO.BOTH, add callback =

# start PWM for the motor PWM pin that is outputted to the H-bridge


# -------------------------------------LINEAR ACTUATOR SET-UP-------------------------------------------------


# -------------------------------------STATE MACHINE LOOP----------------------------------------------------
try:
    while True:
        if state == weighLaundry:
            if time.time() - start_time > 2:
                print('Weighing Laundry')
                state = setVolume
                old_state = weighLaundry
                start_time = time.time()
                '''
                get input from load cell
                do formula to determine # and size of load
                do formula to get # pods and volume per pod needed (depth needed)
                determine amount of water needed
                '''
            else:
                pass

        elif state == home:
            if time.time() - start_time > 2:  # GPIO.input(limSwitchPin) == GPIO.HIGH:
                print('HOME - move towards limit switch')
                # motor.hard_stop()                     # stop motor
                start_time = time.time()
                if old_state == move2dispense:
                    state = h2o_2
                elif old_state == compress:
                    state = push2surface
                elif old_state == kickPod:  # cycle is completed, break from while loop
                    print('COMPLETE CYCLE')
                    break
            else:
                pass
                # motor.move_backward()

        elif state == setVolume:
            if time.time() - start_time > 2:
                print('Move linear actuator to set the volume')
                state = h2o_1
                old_state = setVolume
                start_time = time.time()
                '''
                read inputs from lin actuator encoder and output to move accordingly
                stop when reach desired position
                s
                '''
            else:
                pass

        elif state == h2o_1:
            '''
            turn on pump for amount of time needed then turn off
            '''
            if time.time() - start_time > 2:
                print('Dispensing water 1')
                state = move2dispense
                old_state = h2o_1
                start_time = time.time()
            else:
                pass

        elif state == move2dispense:
            if motor.position == dispensePosition:
                # motor.hard_stop()
                print('MOVE TO DISPENSE')
                time.sleep(2)
                state = home
                old_state = move2dispense
            else:
                pass

                # motor.move_forward()

        elif state == h2o_2:
            '''
            turn on pump for amount of time needed then turn off
            '''
            if time.time() - start_time > 2:
                print('Dispensing water')
                state = move2compress
                old_state = h2o_2
                start_time = time.time()
            else:
                pass

        elif state == move2compress:
            if motor.position == compressPosition:
                # motor.hard_stop()
                print('MOVE TO COMPRESS')
                time.sleep(2)
                state = compress
                old_state = move2compress
            else:
                pass
                # motor.move_forward()

        elif state == compress:
            if time.time() - start_time > 2:
                print('Move Linear actuator to compress')
                state = home
                old_state = compress
                start_time = time.time()
            else:
                pass

        elif state == push2surface:
            if time.time() - start_time > 2:
                print('Move Linear actuator push pod up to surface')
                state = kickPod
                old_state = push2surface
                start_time = time.time()
            else:
                pass

        elif state == kickPod:
            if motor.position == kickEndPosition:
                # motor.hard_stop()
                print('KICK POD')
                state = home
                old_state = kickPod
                time.sleep(2)
        else:
            # shouldnt get here
            print('State machine has reached state that it cannot handle, ABORT!!!')
            print('Current Unkown State = ')
            print(state)
            # motor.move_forward()


# END OF STATE MACHINE ------------------------------------------------------------------------------
# POSITION CONTROL----------------------------------------------------------------------------------

except KeyboardInterrupt:
    print('done')
