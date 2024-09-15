import cv2 as cv
import numpy as np

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

haar_cascate = cv.CascadeClassifier("Face Detection/haarcascade_frontalface_default.xml")

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read("Face Recognition/faces_trained.yml")

img = cv.imread("Face Recognition/Faces/val/jerry_seinfeld/2.jpg")
# cv.imshow("Original Image", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Detect Face in the image
img_rect = haar_cascate.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

for (x,y,w,h) in img_rect:
    img_roi = gray[y:y+h, x:x+w]
    label, confidence = face_recognizer.predict(img_roi)
    
    print(f"{people[label]} with a confidence of {confidence}")
    
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 1)
    cv.putText(img, people[label], (x, y-5), cv.FONT_HERSHEY_COMPLEX, 0.5, (0,255,0), 1)
    
    cv.imshow(people[label], img)
    
    
    
 

cv.waitKey(0)