import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')

# cv.imshow('Black image', blank)

# img = cv.imread("Photos/cat.jpg")
# cv.imshow('Cat',img)

# 1. Changing the blank image color

# red
# blank[:] = 0,0,255
# cv.imshow("Red Image", blank)

# # Green
# blank[:] = 0,255,0
# cv.imshow("Green Image", blank)

# # 2. paint the image a certain point
# blank[200:300, 300:400] = 0,0,255
# cv.imshow("",blank);

# # 3. Draw a line
# cv.line(blank, (200,0),(300,500), (0,0,255), thickness=2)
# cv.imshow("Line", blank);

# # 4. Draw a rectangle
# cv.rectangle(blank,(50,50),(200,400), (0,0,255))
# cv.rectangle(blank, (0,0), (250,500), (0,0,255), thickness=cv.FILLED); #Fill the rectangle inner body. we can also use thickness=-1
# cv.rectangle(blank,(50,50),(blank.shape[1]//2, blank.shape[0]//2), (0,0,255))

# cv.imshow("Rectangle",blank)

# # 5. Draw a Circle
# cv.circle(blank, (250,250), 100, (0,0,255), thickness=2);
# cv.imshow("Circle", blank);

# # 6. Draw a text on a image
# cv.putText(blank, "ক", (200,200), cv.FONT_HERSHEY_TRIPLEX, 1.0 , (0,255,0), 1)
# # cv.putText(image, text, starting point, font, scale, color, thinkness)
# cv.imshow("Text", blank)


# # Exercise: Draw a rectangle using line
# cv.line(blank,(50,50), (300,50), (0,0,255), thickness=1)
# cv.line(blank,(50,50), (50,250), (0,0,255), thickness=1)
# cv.line(blank,(50,250), (300,250), (0,0,255), thickness=1)
# cv.line(blank,(300,50), (300,250), (0,0,255), thickness=1)
# cv.imshow("Rectangle using line", blank)


# # Exercise: Triangle using line
# cv.line(blank, (250,50), (50,250), (0,0,255), thickness=1)
# cv.line(blank, (250,50), (450,250), (0,0,255), thickness=1)
# cv.line(blank, (50,250), (450,250), (0,0,255), thickness=1)
# cv.imshow("Triangle using line", blank)

cv.waitKey(0) 