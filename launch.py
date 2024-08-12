import cv2
# from picamera2 import Picamera2
import time
from ultralytics import YOLO
model = YOLO("yolov8n.pt")

# import face
import servos
# kit = ServoKit(channels = 16)

vid = cv2.VideoCapture(0)
# piCam=Picamera2()
# disph=720
# dispw=720
# piCam.preview_configuration.main.size=(dispw,disph)
# piCam.preview_configuration.main.format="RGB888"
# piCam.preview_configuration.controls.FrameRate=30
# piCam.preview_configuration.align()
# piCam.configure("preview")
# piCam.start()
fps=0
pos=(30,60)
font=cv2.FONT_HERSHEY_SIMPLEX
height=1.5
myColor=(0,0,255)
weight=3
while True:
    tStart=time.time()
    isTrue , frame = vid.read()
    # frame=piCam.capture_array()
    cv2.putText(frame,str(int(fps)),pos,font,height,myColor,weight)
    frame = cv2.flip(frame,1)
    result = model.track(frame, persist=True)
    annotated_frame = result[0].plot()
    cv2.imshow('detected', annotated_frame)
    # if detect:
    #     servos.servo()
    # else:         
    #     servos.servo_back()


    
    # cv2.imshow("piCam",frame)
    #cv2.imshow("ROI",ROI)
    if cv2.waitKey(1)==ord('q'):
        break
    tEnd=time.time()
    loopTime=tEnd-tStart
    fps = .99*fps + .01*(1/loopTime)

vid.release()
cv2.destroyAllWindows()


