import cv2 as cv
import numpy as np

img = cv.imread("Photos/cats.jpg")
# cv.imshow("Original Image", img)

blank = np.zeros(img.shape[:2], dtype='uint8')
# cv.imshow("Blank Image", blank)

mask = cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 100, 255, -1)
# cv.imshow("circle", circle)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow("Masked image", masked)

cv.waitKey(0)