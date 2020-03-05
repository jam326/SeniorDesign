
# ------------------------------------------CLASS FOR MOTOR--------------------------------------------
GPIO = Gpio()

class Motor:
    position = 0               # [encoder counts]
    encoderStatus = 0          # [binary (4 bits)] rightmost bits = current status, leftmost bits = previous status 
    maximumPosition = 0        # [encoder counts]
    min_vel_comp_count = 2     # [encoder counts] update velocity if position moves 2 encoder counts
    min_vel_comp_time = 10000  # [microseconds] update velocity after 10000 microseconds
    prevPosition = 0           # [encoder counts] store previous position for velocity computation
    prev_vel_comp_time = datetime.now()  #store previous time for velocity computation
    velocity = 0               # [encoder counts\sec]

    def __init__(self, a, b, pwm, dir1, dir2):
        self.PinEncoderA = a
        self.PinEncoderB = b
        self.PinPWM = pwm
        self.PinDIR1 = dir1
        self.PinDIR2 = dir2

    # function to be called during interrupts
    def updateposition(self, channel):
        # bitwise shift to left by  1 bit
        self.encoderStatus <<= 1
        # read channel A and put that value into the rightmost bit of encoderStatus
        self.encoderStatus |= GPIO.input(self.PinEncoderA)
        # bitwise shift to left by 1 bit
        self.encoderStatus <<= 1
        # read channel B and put that value into the
        self.encoderStatus |= GPIO.input(self.PinEncoderB)
        # truncate encoder status to rightmost 4 bits
        self.encoderStatus &= 15
        # if encoder status matches pattern for counting up by one, add one to motorPosition
        if self.encoderStatus == 2 or self.encoderStatus == 4 or self.encoderStatus == 11 or self.encoderStatus == 13:
            self.position += 1
        else:
            # otherwise subtract one (since function is only called if something changes)
            self.position -= 1


    #check these
    # function to move in dir1 at full speed
    def move_forward(self):
        GPIO.output(self.PinPWM, GPIO.HIGH)
        GPIO.output(self.PinDIR1, GPIO.HIGH)
        GPIO.output(self.PinDIR2, GPIO.LOW)

     # move dir2 in dir 2 at full speed
    def move_backward(self):
        GPIO.output(self.PinPWM, GPIO.HIGH)
        GPIO.output(self.PinDIR1, GPIO.LOW)
        GPIO.output(self.PinDIR2, GPIO.HIGH)

    # hard stop
    def hard_stop(self):
        GPIO.output(self.PinPWM, GPIO.HIGH)
        GPIO.output(self.PinDIR1, GPIO.LOW)
        GPIO.output(self.PinDIR2, GPIO.LOW)

    def speed_computation(self):
        now = datetime.now()
        # update speed if motor travels through minimum angle or minimum time has passed
        if abs(self.position - self.prevPosition) > self.min_vel_comp_count or \
                (now - self.prev_vel_comp_time).microseconds > self.min_vel_comp_time:
            #calculate velocity
            self.velocity = (self.position - self.prevPosition)*100000/(now - self.prev_vel_comp_time).microseconds
            print(self.velocity)
            # remember this position and time for next iteration
            self.prevPosition = self.position
            self.prev_vel_comp_time = now


 
# ------------------------------------------LINEAR ACTUATOR CLASS------------------------------------------------


class LinearActuator:
    position = 0
    maximumPosition = 0
    min_vel_comp_count = 2  # min encoder counts to recompute the velocity
    min_vel_comp_time = 0.01  # seconds
    prevPosition = 0
    prev_vel_comp_time = 0
    velocity = 0

    def __init__(self, encoder, pwm, dir1, dir2):
        self.PinEncoder = encoder
        self.PinPWM = pwm
        self.PinDIR1 = dir1
        self.PinDIR2 = dir2

    # function to be called during interrupt (only activated if encoder pin changes)
    def updateposition(self, channel):
        if GPIO.input(self.PinDIR1):   # if moving in direction 1
            self.position += 1
        else:                         # if moving in direction 2
            self.position -= 1

    # check these
    # function to move dir 1 at full speed
    def move_forward(self):
        GPIO.output(self.PinPWM, GPIO.HIGH)
        GPIO.output(self.PinDIR1, GPIO.HIGH)
        GPIO.output(self.PinDIR2, GPIO.LOW)

    #  move dir 2 at full speed
    def move_backward(self):
        GPIO.output(self.PinPWM, GPIO.HIGH)
        GPIO.output(self.PinDIR1, GPIO.LOW)
        GPIO.output(self.PinDIR2, GPIO.HIGH)

    # hard stop
    def hard_stop(self):
        GPIO.output(self.PinPWM, GPIO.HIGH)
        GPIO.output(self.PinDIR1, GPIO.LOW)
        GPIO.output(self.PinDIR2, GPIO.LOW)
