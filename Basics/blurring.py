import cv2 as cv

img = cv.imread("Photos/cats.jpg")

cv.imshow("Original Image", img)

# We can reduce the noise in the image by applying a blur filter
# kernel size must be odd numbers
# The larger the kernel size, the more blur the image will be


# 1. Averaging Blur
average = cv.blur(img, (7,7))
# In averaging method it calculate the average of all the pixels in the kernel area and replace the central pixel with the average value
# cv.imshow("Average Blur", average)

# 2. Gaussian Blur
gaussian = cv.GaussianBlur(img, (7,7), 0)
# In Gaussian blur method each surrounding pixel is given a weight and the central pixel is replaced with the weighted average
# The weight of the surrounding pixels decreases as the distance from the central pixel increases
# The weight of the surrounding pixels is calculated using the Gaussian function
# cv.GaussianBlur(image, kernel_size, sigmaX) here sigmaX is the standard deviation in the x direction
# Gaussian blur give less blur than average blur but it is more natural
# cv.imshow("Gaussian Blur", gaussian)

# 3. Median Blur
median = cv.medianBlur(img, 7)
# In median blur method the central pixel is replaced with the median value of the surrounding pixels
# Median blur is very effective in removing salt-and-pepper noise
# salt-and-pepper basically means white and black dots in the image
# it is very effective in removing noise
# cv.imshow("Median Blur", median)

# 4. Bilateral Blur
bilateral = cv.bilateralFilter(img, 10, 35, 25)
# cv.bilateralFilter(image, diameter, sigmaColor, sigmaSpace) where diameter is the diameter of each pixel neighborhood, sigmaColor is the standard deviation in the color space, sigmaSpace is the standard deviation in the coordinate space
# Bilateral filter is very effective in noise removal while keeping the edges sharp
# Bilateral filter is very slow compared to other filters
cv.imshow("Bilateral Blur", bilateral)



cv.waitKey(0)