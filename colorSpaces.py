import cv2 as cv

img = cv.imread("Photos/cat.jpg")
cv.imshow("Orginal Image", img)

# # BGR to Gray
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray Image", gray)

# # BGR to HSV
# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow("HSV Image", hsv)

# # BGR to L*A*B
# lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow("LAB Image", lab)



# # cv read images in BGR formet but matplotlib read images in RGB formet
# import matplotlib.pyplot as plt
# plt.imshow(img)
# plt.show()
# # Colors are completely imversed because of the color spaces
# # So we have to convert BGR to RGB
# rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# plt.imshow(rgb)
# plt.show()


# # HSV to BGR
# hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
# cv.imshow("HSV to BGR Image", hsv_bgr)

# Simillary we can convert GRAY to BGR, LAB to BGR but we cant directly convert Gray to HSV or similar operations


cv.waitKey(0) 