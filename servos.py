import time 
from adafruit_servokit import ServoKit


import time 
from adafruit_servokit import ServoKit
kit = ServoKit(channels = 16)
shldr_up = 0
shldr_down = 1
elbow = 2
wrist = 3

# kit.servo[0].angle=70
# kit.servo[1].angle=90
# kit.servo[2].angle= 150
# kit.servo[3].angle=20

# kit.servo[4].angle = 60
# kit.servo[5].angle = 80
# kit.servo[6].angle = 0
# kit.servo[7].angle = 140

def servo():
    for i in range(35):

        kit.servo[0].angle=70+i
        kit.servo[1].angle=90-(2*i)
        kit.servo[2].angle= 150-(3.65*i)
        kit.servo[3].angle= 20+(1.90*i)

        kit.servo[4].angle = 60-(0.85*i)
        kit.servo[5].angle = 80+(1.57*i)
        kit.servo[6].angle = 0+(3.20*i)
        kit.servo[7].angle = 140-(2.72*i)

        time.sleep(0.02)


def servo_back():
    for i in range(35):
        
        kit.servo[0].angle=105-i
        kit.servo[1].angle=20+(2*i)
        kit.servo[2].angle= 22+(3.65*i)
        kit.servo[3].angle= 85-(1.85*i)

        kit.servo[4].angle = 30+(0.85*i)
        kit.servo[5].angle = 135-(1.57*i)
        kit.servo[6].angle = 110-(3.20*i)
        kit.servo[7].angle = 50+(2.57*i)

        time.sleep(0.02)
# servo_back()
