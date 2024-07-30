import cv2 as cv


# capture is a instance of the VideoCapture class
capture = cv.VideoCapture('Videos/dog.mp4')

# isTrue is a boolean that checks if the video is being read
# frame is the current frame of the video
# The while loop reads the video frame by frame
# cv.imshow() displays the frame
# cv.waitKey() waits for a key press to break the loop
# capture.release() releases the video file
# cv.destroyAllWindows() closes the window
count = 0
while True:
    isTrue, frame = capture.read() # capture.read() returns a tuple of isTrue and frame 
    
    # isTrue return boolean value
    # if there are no frame available it return None. it is NoneType
    
    cv.imshow('Video',frame)
    
    if cv.waitKey(30) & 0xFF == ord('d'):   # Press 'd' to break the loop
        break
    
capture.release()
cv.destroyAllWindows()