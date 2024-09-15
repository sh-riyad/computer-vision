import cv2 as cv

img = cv.imread("Photos/cats.jpg")

# cv.imshow("Cats Image", img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray Image", gray)

# 1. Simple Thresholding or Binary Threshold
threshold, thresh = cv.threshold(gray, 130, 255, cv.THRESH_BINARY)
# cv.imshow("Threshold Image", thresh)

# inverse threshold
threshold, thresh_inv = cv.threshold(gray, 130, 255, cv.THRESH_BINARY_INV)
# cv.imshow("Inversed Threshold Image", thresh_inv)


# 2. Adaptive Threshold
thresh_ada = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 3, 4)
# cv.imshow("Adaptive Threshold", thresh_ada)

thresh_ada = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 3, 4)
cv.imshow("Adaptive Threshold", thresh_ada)

cv.waitKey(0)