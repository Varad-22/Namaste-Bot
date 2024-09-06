import cv2

import time

from Namaste_Ki_Audio import audio
import face
from dist import distance
from servos import servo, servo_back


vid = cv2.VideoCapture(0)

fps=0
pos=(30,60)
font=cv2.FONT_HERSHEY_SIMPLEX
height=1.5
myColor=(0,0,255)
weight=3
pos=0
mean=1
while True:
    # d = distance()
    # if d <= 150:
    tStart=time.time()
    # time.sleep(1)
    isTrue , frame = vid.read()
    cam = face.camera_detection(frame)
    detect = cam[0]
    print(detect)
    # for (x,y,z,w) in cam[1]:
    #     cv2.rectangle(frame, (x,y), (x+z,y+w), color=(0,255,0), thickness=3)
    #     # detect = True
    # cv2.putText(frame,str(int(fps)),pos,font,height,myColor,weight)
    # frame = cv2.flip(frame,1)

    # cv2.imshow('detected', frame)
    # if detect:
        # isTrue, frame2 = vid.read()
        # cam_check = face.camera_detection(frame2)
        # for (x,y,z,w) in cam[1]:
        #     cv2.rectangle(frame2, (x,y), (x+z,y+w), color=(0,255,0), thickness=3)
        #     # detect = True
        # cv2.putText(frame2,str(int(fps)),pos,font,height,myColor,weight)
        # detect_feedback = cam_check[0] 

        
        # d = distance()
    # d=100
    # if d<=150:
    cnt=0
    
    if detect:
        if pos==0:
            servo()
            audio()
            time.sleep(3.5)
            pos=1
            mean=0
        while cnt<2:
            isTrue, frame3 = vid.read()
            cam_check = face.camera_detection(frame3)
            detect = cam_check[0]
            print("baad mai", detect)
            if detect:
                cnt+=1
            else:
                # servo_back()
                break
    elif pos==1 and mean==0:
        servo_back()
        mean=1
        pos=0
        # if cnt>=2:
        #     # break
        #     servo_back()
        #     time.sleep(1)
    # servo_back()
    # else:
    #     servo_back()
    #     pos=0
            # time.sleep(1)

#     if cv2.waitKey(1)==ord('q'):
#         break
#     tEnd=time.time()
#     loopTime=tEnd-tStart
#     fps = .99*fps + .01*(1/loopTime)
#     # else:
#     #     continue

# vid.release()
# cv2.destroyAllWindows()


