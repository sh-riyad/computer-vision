import cv2 as cv

img = cv.imread('Photos\cat.jpg')
cv.imshow("Cat Image", img)

cv.waitKey(0)