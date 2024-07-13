import cv2 as cv

img = cv.imread("Photos/cat.jpg")

cv.imshow("Orginal Image", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Image", gray)

canny = cv.Canny(img, 125, 175)
cv.imshow("Canny Image", canny)

cv.waitKey(0)