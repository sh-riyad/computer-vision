import cv2 as cv
import mediapipe as mp
import HandTrackingModule as htm


capture = cv.VideoCapture(0)
detector = htm.handDetector()
while True: 
    isTrue, img = capture.read()
    img = detector.findHands(img)
    detector.findPositon(img, 0)
    cv.imshow("Web feed", img)
        
    if cv.waitKey(1) == ord('q'):
        break