import cv2 as cv

capture = cv.VideoCapture(0)

while True:
    # ret is a boolean that checks if the webcam is being read  
    ret, frame = capture.read()
    fliped = cv.flip(frame, 0)
    
    cv.imshow('Webcam', fliped)
    
    if cv.waitKey(1) == ord('q'):
        break

capture.release()
cv.destroyAllWindows()

