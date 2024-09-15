import cv2 as cv

img = cv.imread("Photos/lady.jpg")
cv.imshow("Orginal Image", img)

# # converting to grayscale
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("Gray Image", gray)

# # Blur a Image 
# blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow("Blur Image", blur)


# # Edge Cascade
# canny = cv.Canny(img, 125, 175)
# cv.imshow("canny Edges 125, 175", canny)
# # We can reduce edges by passing blur image

# # Dilating the image
# dilated = cv.dilate(img, (21,21), iterations=5)
# cv.imshow("Dialated Image", dilated)

# # Eroding Image
# eroded = cv.erode(dilated,(3,3),iterations=3)
# cv.imshow("Eroded Image", img)

# # Resizin an image
# resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
# cv.imshow("Resized Image INTER_AREA", resized)
# resized = cv.resize(img, (500,500), interpolation=cv.INTER_LINEAR)
# cv.imshow("Resized Image INTER_LINEAR", resized)
# resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
# cv.imshow("Resized Image INTER_CUBIC", resized)


# # Croping an image 
# croped = img[50:200,200:400]
# cv.imshow("Croped Imagee", croped)


cv.waitKey(0)