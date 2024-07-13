import cv2 as cv
import numpy as np

img = cv.imread("Photos/cat.jpg")

cv.imshow("Original Image", img)


# # 1. Translation
# def translate(img, x, y):
#     transMat = np.float32([[1,0,x],[0,1,y]])
#     dimensions = (img.shape[1], img.shape[0])
#     return cv.warpAffine(img, transMat, dimensions)
    
# # -x --> left
# # x --> right
# # y --> up
# # -y --> down

# translated = translate(img, 50, 50)
# cv.imshow("translated Image", translated);

# # 2. Rotation Image
# def rotate(img, angle, rotPoint=None):
#     (height,width) = img.shape[:2]
    
#     if rotPoint is None:
#         rotPoint = (width//2, height//2)
    
#     rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
#     dimensions = (width, height)
    
#     return cv.warpAffine(img, rotMat, dimensions)

# rotated = rotate(img, 45)
# cv.imshow("Roted Image", rotated);


# # 3. Resizing Image
# resized = cv.resize(img,(500,500), interpolation=cv.INTER_CUBIC)
# cv.imshow("Resized", resized)


# # 4. Flipping Image
# fliped = cv.flip(img, 0)
# cv.imshow("Horizontally fliped Image", fliped)

# fliped = cv.flip(img, 1)
# cv.imshow("Vartically fliped Image", fliped)

# fliped = cv.flip(img, -1)
# cv.imshow("Both Horizontally and Vartically Fliped Image", fliped)

# # 5. Cropping 
# cropped = img[100:400, 100:400] 
# cv.imshow("Cropped Image", cropped)
  
cv.waitKey(0)