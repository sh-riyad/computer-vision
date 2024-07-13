import cv2 as cv

def scale(frame, scale_rate = 0.75):
    width = int(frame.shape[1] * scale_rate)
    height = int(frame.shape[0] * scale_rate)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)

# img = cv.imread("Photos/cat_large.jpg")

# scaled_image = scale(img, scale_rate=0.5)
# cv.imshow("Car large Image", scaled_image)

# cv.waitKey(0)


capture = cv.VideoCapture("Videos/kitten.mp4")

while True:
    isTrue, frame = capture.read()
    
    cv.imshow("Kitten Video", frame)
    
    if cv.waitKey(10) & 0xFF ==  ord('d'):
        break
    
capture.release()
cv.destroyAllWindows()