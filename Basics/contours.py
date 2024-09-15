import cv2 as cv
import numpy as np

img = cv.imread("Photos/cats.jpg")

# cv.imshow("Orginal Image", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# cv.imshow("Gray Image", gray)

# finding controus 
 res, 

cv.waitKey(0)