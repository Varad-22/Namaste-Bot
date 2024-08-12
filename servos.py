import time 
from adafruit_servokit import ServoKit

#
kit = ServoKit(channels = 8)

# kit.servo[1].angle = 180
# time.sleep(1)

# kit.servo[1].angle = 0
# time.sleep(1)

def servo():
    kit.servo[1].angle = 90
    # time.sleep(0.5)
    # kit.servo[1].angle = 180
    # time.sleep(0.5)
def servo_back():
    kit.servo[1].angle = 180