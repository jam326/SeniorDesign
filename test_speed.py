from helper import Motor
from datetime import datetime
import time
motor = Motor(1,2,3,4,5)
time_limit = .2
motor.position = 0
count = 0
start_time = datetime.now()
while (datetime.now() - start_time).total_seconds() < time_limit:
    motor.speed_computation()
    motor.position = count
    count += 1
    #time.sleep(.00000001)
    print(motor.position)
