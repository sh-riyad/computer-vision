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
    # we can use the isTrue variable to check if the video is being read aslo we can use it to break the loop
    cv.imshow('Video',frame)
    count += 1
    
    if cv.waitKey(30) & 0xFF == ord('d'):   # Press 'd' to break the loop
        break
    
capture.release()
cv.destroyAllWindows()
print(count) # prints the number of frames in the video

