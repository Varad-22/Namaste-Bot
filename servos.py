import time 
from adafruit_servokit import ServoKit

kit = ServoKit(channels = 8)

# kit.servo[0].angle = 180
# time.sleep(1)

# kit.servo[0].angle = 0
# time.sleep(1)

def servo():
    # kit.servo[n].angle = 90
    for i in range(180):
        kit.servo[1].angle = i/2
        kit.servo[2].angle = i
        time.sleep(0.040)
def servo_back():
    # kit.servo[n].angle = 180
    for i in range(179,-1,-1):
        kit.servo[1].angle = i/2
        kit.servo[2].angle = i
        time.sleep(0.040)

# servo()
# servo_back()
# time.sleep(1)
# servo(2)
# time.sleep(1)
# servo_back(1)
# time.sleep(1)
# servo_back(2)
# time.sleep(1)