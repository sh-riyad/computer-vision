import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')
# cv.imshow("Blank image", blank)

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(),(200,200), 200 , 255, -1)

# cv.imshow("Rectangle", rectangle)
# cv.imshow("Circle", circle)

# 1. Bitwase AND
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("Bitwise And", bitwise_and)

# 2. Bitwase OR
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("Bitwise OR", bitwise_or)


# 3. Bitwase XOR
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("Bitwise XOR", bitwise_xor)

# 4. Bitwase NOT
bitwise_not = cv.bitwise_not(rectangle)
# bitwise not is the inverse of the image. It will make the black pixels white and white pixels black
cv.imshow("Bitwise NOT", bitwise_not)


cv.waitKey(0)