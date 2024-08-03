import cv2 as cv

capture = cv.VideoCapture(0)
haar_cascate = cv.CascadeClassifier("Face Detection/haarcascade_frontalface_default.xml")


while True:
    isTrue, frame = capture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces_rect = haar_cascate.detectMultiScale(gray, scaleFactor=1.1,  minNeighbors=4)
    
    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), thickness=2)
    
    cv.imshow("Web Cam", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
capture.release()
cv.destroyAllWindows()
