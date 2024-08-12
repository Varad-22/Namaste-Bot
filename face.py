import cv2

def camera_detection(frame):
    # kit = ServoKit(channels = 8)

    # piCam=Picamera2()
    # disph=480
    # dispw=720
    # piCam.preview_configuration.main.size=(dispw,disph)
    # piCam.preview_configuration.main.format="RGB888"
    # piCam.preview_configuration.controls.FrameRate=30
    # piCam.preview_configuration.align()
    # piCam.configure("preview")
    # piCam.start()
    # fps=0
    # pos=(30,60)
    # font=cv2.FONT_HERSHEY_SIMPLEX
    # height=1.5
    # myColor=(0,0,255)
    # weight=3
        # tStart=time.time()
        # frame=piCam.capture_array()


        #ROI=frame[:int(disph/2),:int(dispw/2)]
        #frame[:int(disph/2),:int(dispw/2)]=[0,0,255]
        #frame[:int(disph/2),int(dispw/2):]=[255,0,0]
        #frame[int(disph/2):,int(dispw/2):]=[0,255,0]
        #frame[int(disph/2):,:int(dispw/2)]=[0,125,125]
        
        #frame[:int(disph/2),int(dispw/2):] = ROI
        #frame[int(disph/2):,int(dispw/2):] = ROI
        #frame[int(disph/2):,:int(dispw/2)] = ROI

        # face detection 
    haar_cascade = cv2.CascadeClassifier('haar_face.xml')
    frame = cv2.flip(frame,1)
    gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # result = model(frame)
    # annotated_frame = result[0].plot()
    face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)
    detect = False

    for (x,y,z,w) in face_rect:
        # cv2.rectangle(frame, (x,y), (x+z,y+w), color=(0,255,0), thickness=3)
        detect = True

    cv2.imshow('detected',frame)
    print(detect)

#     cv2.putText(frame,str(int(fps)),pos,font,height,myColor,weight)
    # cv2.imshow("piCam",frame)
#     #cv2.imshow("ROI",ROI)
#     if cv2.waitKey(1)==ord('q'):
#         break
#     tEnd=time.time()
#     loopTime=tEnd-tStart
#     fps = .9*fps + .1*(1/loopTime)
    # cv2.destroyAllWindows()

    return (detect,face_rect)


