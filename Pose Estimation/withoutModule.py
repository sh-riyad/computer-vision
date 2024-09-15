import cv2 as cv
import mediapipe as mp

capture = cv.VideoCapture("Pose Estimation\dance.mp4")

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()


while True:
    isTrue, frame = capture.read()
    
    frame = cv.resize(frame, (800,600), interpolation=cv.INTER_CUBIC)
    
    results = pose.process(frame)
    
    if results.pose_landmarks:
        mpDraw.draw_landmarks(frame, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        
    cv.imshow("Dancing", frame)
    
    if cv.waitKey(1) & 0xFF == ord("q"):
        break
    
capture.release()
cv.destroyAllWindows()