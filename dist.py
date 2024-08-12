from gpiozero import DistanceSensor
us = DistanceSensor(echo=17, trigger=4)
while True:
    print(us.distance)