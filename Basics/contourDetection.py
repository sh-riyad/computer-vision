import cv2 as cv
import numpy as  np

img = cv.imread("Photos/cats.jpg")

# cv.imshow("Orginal Image", img)

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# # cv.imshow("Gray Image", gray)

# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT )

# # canny = cv.Canny(img, 125, 175)
# canny = cv.Canny(blur, 125, 175)
# cv.imshow("Canny Image", canny)

# contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# print(f"{len(contours)} contours found!")

# Binarizing the image using threshold method
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# the the value of a pixel is less then 125 it will converted into 0
cv.imshow("Threshold Image", thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f"{len(contours)} contours found!")

 
# Drawing Contours on an blank image
blank = np.zeros(img.shape, dtype='uint8')
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow("Contours Drawn", blank)

cv.waitKey(0)


# good pratc --> use canny(blur) before finding contours rather then using threshold