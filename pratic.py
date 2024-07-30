import cv2 as cv

capture = cv.VideoCapture(0)


while True:
    isTrue, frame = capture.read()
    
    
    cv.imshow("Web Cam", frame)
    
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
capture.release()
cv.destroyAllWindows()