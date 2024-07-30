import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt

img = cv.imread("Photos/cats.jpg")
cv.imshow("Cats Image", img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray Image", gray)

# 1. Grayscale Histogram
gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])
# cv.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]]) where images is the source image of type uint8 or float32. channels is the index of channel for which we calculate histogram. For grayscale image, its value is [0] and for color image, you can pass [0], [1] or [2] to calculate histogram of blue, green or red channel respectively. mask is the optional mask. histSize is the number of bins. ranges is the range of intensity values you want to measure. For grayscale intensity range is [0, 256].

# plt.figure() # to plot in new window instead of the same window as the image
# plt.title("Grayscale Histogram")
# plt.xlabel("Bins")
# plt.ylabel("# of pixels")
# plt.xlim([0,256]) # x-axis range from 0 to 256
# plt.plot(gray_hist)
# plt.show()


# # we can calculate histogram for masked image as well
# blank = np.zeros(img.shape[:2], dtype='uint8')
# circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
# masked = cv.bitwise_and(gray, gray, mask=circle) # Applying mask on grayscale image for simplicity
# cv.imshow("Masked Image", masked)
# masked_hist = cv.calcHist([gray], [0], masked, [256], [0,256])
# plt.figure()
# plt.title("Grayscale Histogram for masked Image")
# plt.xlabel("Bins")
# plt.ylabel("# of pixels")
# plt.xlim([0,256])
# plt.plot(masked_hist)
# plt.show()


# 2. Color Histogram
plt.figure()
plt.xlabel("Bins")
plt.ylabel("# of pixels")
plt.title("Color histogram")
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    plt.xlim([0,256])
    plt.plot(hist)
plt.show()
# we can also calculate color histogram for masked image

cv.waitKey(0)