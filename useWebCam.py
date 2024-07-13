import cv2 as cv

capture = cv.VideoCapture(0)

while True:
    # ret is a boolean that checks if the webcam is being read  
    ret, frame = capture.read()
    cv.imshow('Webcam', frame)
    
    if cv.waitKey(1) == ord('q'):  # cv.waitKey(10000) waits for 10 seconds before breaking the loop 
        break

capture.release()
cv.destroyAllWindows()

