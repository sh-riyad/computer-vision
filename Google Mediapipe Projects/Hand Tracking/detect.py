import cv2 as cv
import mediapipe as mp
import time

# for calculating frame reate
pTime = 0
cTime = 0

capture = cv.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    isTrue, frame = capture.read()
    frameRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    results = hands.process(frameRGB)
    # print(results.multi_hand_landmarks)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            
            for id, lm in enumerate(handLms.landmark):
                # print(id, lm)
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                
                if id == 8:
                    cv.circle(frame, (cx,cy), 30, (0,255,0), 1)
                
            
            
            mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)
    
    
    # calculate frame Rate
    cTime = time.time()
    fps = 1 / (cTime-pTime)
    pTime = cTime
    cv.putText(frame, str(int(fps)), (10,20), cv.FONT_HERSHEY_SIMPLEX, 0.5 , (255, 0, 255), 1)
    
    cv.imshow("WebCam", frame)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
capture.release()
cv.destroyAllWindows()