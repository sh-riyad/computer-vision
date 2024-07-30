import cv2 as cv
import numpy as np

img = cv.imread("Photos/park.jpg")
# cv.imshow("Park Image", img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray image", gray)

# 2. Lablacian
lab = cv.Laplacian(gray, cv.CV_64F) # lablacian may return regative pixel values
lab = np.uint8(np.absolute(lab)) # so we make them positive and then convert it to image formet
# cv.imshow("Lablacian Image", lab)

# 2. Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

# cv.imshow("Sobel X", sobelx)
# cv.imshow("Sobel Y", sobely)
cv.imshow("Sobel Combined", combined_sobel)

# 3. Canny
canny = cv.Canny(gray, 150, 175)
cv.imshow("Canny Image", canny)

cv.waitKey(0)