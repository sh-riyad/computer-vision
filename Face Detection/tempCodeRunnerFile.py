import cv2 as cv

img = cv.imread("Photos/lady.jpg")
cv.imshow("Lady Image", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray Image", gray)

haar_cascade = cv.CascadeClassifier("Face Detection/haarcascade_frontalface_default.xml")

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print(f"Total Faces {len(faces_rect)}")
print(faces_rect)
for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)
    
cv.imshow("Face Detecction", img)

cv.waitKey(0)
