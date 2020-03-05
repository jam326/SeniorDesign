"""
class EncoderReader:
    position = 0
    encoderStatus = 1

    def __init__(self, a, b):
        self.PinA = a
        self.PinB = b

    # function to be called during interrupts
    def updateposition(self, channel):
        # bitwise shift to left by  1 bit
        self.encoderStatus <<= 1
        # read channel A and put that value into the rightmost bit of encoderStatus
        self.encoderStatus |= 0
        # bitwise shift to left by 1 bit
        self.encoderStatus <<= 1
        # read channel B and put that value into the
        self.encoderStatus |= 0
        # truncate encoder status to rightmost 4 bits
        self.encoderStatus &= 15
        # if encoder status matches pattern for counting up by one, add one to motorPosition
        if self.encoderStatus == 2 or self.encoderStatus == 4 or self.encoderStatus == 11 or self.encoderStatus == 13:
            self.position += 1
        else:
            # otherwise subtract one (since function is only called if something changes)
            self.position -= 1

motor = EncoderReader(1,2)
print(motor.position)
print(motor.encoderStatus)
motor.updateposition(5)
print(motor.position)
print(motor.encoderStatus)
motor.updateposition(5)
print(motor.position)
print(motor.encoderStatus)
"""

class xy:
    x = 0
    y = 1

    def add(self):
        return self.x+self.y

    def add2times(self):
        return 2*self.add()
