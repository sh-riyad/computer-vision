import cv2 as cv
import numpy as np

img = cv.imread("Photos/park.jpg")

# cv.imshow("Original Image", img)

# # spliting color channels
# blue, green, red = cv.split(img)
# # split function split the image into 3 channels and return grayscale images
# # more white means more intensity of that color and more black means less intensity of that color


# cv.imshow("Blue", blue)
# cv.imshow("Green", green)
# cv.imshow("Red", red)

# print(f"Original Image shape {img.shape}")
# print(f"Blue Image shape {blue.shape}")
# print(f"Green Image shape {green.shape}")
# print(f"Red Image shape {red.shape}")

# # We can merge the images
# merged = cv.merge([blue, green, red])
# cv.imshow("Merged Image", merged)



# # we can also show the colors in a blank image instead of grayscale
# blank = np.zeros(img.shape[:2] ,dtype='uint8')
# cv.imshow("Blank Image", blank)
# b,g,r = cv.split(img)
# blue = cv.merge([b, blank, blank])
# green = cv.merge([blank, g, blank])
# red = cv.merge([blank, blank, r])

# cv.imshow("Blue", blue)
# cv.imshow("Green", green)
# cv.imshow("Red", red)


cv.waitKey(0) 