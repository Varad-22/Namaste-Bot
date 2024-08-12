import cv2 as cv

img = cv.imread('Screenshot(4).png')
img = cv.resize(img, (700,500))

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')
face_rect = haar_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=10)

for (x,y,z,w) in face_rect:
    cv.rectangle(img, (x,y), (x+z,y+w), color=(0,255,0), thickness=3)

cv.imshow('detected', img)

cv.waitKey(0)