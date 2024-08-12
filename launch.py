import cv2
# from picamera2 import Picamera2
import time
# from ultralytics import YOLO
# model = YOLO("yolov8n.pt")
from Namaste_Ki_Audio import audio
import face
import servos
# kit = ServoKit(channels = 16)

vid = cv2.VideoCapture(0)
# piCam=Picamera2()
disph=720
dispw=720
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
    cam = face.camera_detection(frame)
    detect = cam[0]
    for (x,y,z,w) in cam[1]:
        cv2.rectangle(frame, (x,y), (x+z,y+w), color=(0,255,0), thickness=3)
        # detect = True
    cv2.putText(frame,str(int(fps)),pos,font,height,myColor,weight)
    # frame = cv2.flip(frame,1)
    # result = model.track(frame, persist=True)
    # annotated_frame = result[0].plot()
    # cv2.imshow('detected', frame)
    if detect:
        #servos.servo(0)
        servos.servo()
        isTrue, frame2 = vid.read()
        cam_check = face.camera_detection(frame2)
        for (x,y,z,w) in cam[1]:
            cv2.rectangle(frame2, (x,y), (x+z,y+w), color=(0,255,0), thickness=3)
            # detect = True
        cv2.putText(frame2,str(int(fps)),pos,font,height,myColor,weight)
        detect_feedback = cam_check[0] 
        cnt=0
        while detect_feedback:
            print("namaste")
            audio()
            time.sleep(3)
            cnt += 1
            isTrue, frame3 = vid.read()
            cam_check = face.camera_detection(frame3)
            detect_feedback = cam_check[0]
            if cnt>=2:
                break
        servos.servo_back()
    else:
        #qservos.servo_back(0)         
        continue

    if cv2.waitKey(1)==ord('q'):
        break
    tEnd=time.time()
    loopTime=tEnd-tStart
    fps = .99*fps + .01*(1/loopTime)

vid.release()
cv2.destroyAllWindows()


