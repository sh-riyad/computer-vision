import cv2 as cv
import mediapipe as mp
import time

class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode=self.mode, 
                                        max_num_hands=self.maxHands, 
                                        min_detection_confidence=self.detectionCon, 
                                        min_tracking_confidence=self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
    
    def findHands(self, img):
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        
        
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                # for id, lm in enumerate(handLms.landmark):
                #     h, w, c = img.shape
                #     cx, cy = int(lm.x * w), int(lm.y * h)
                #     cv.circle(img, (cx, cy), 20, (255,0,255), cv.FILLED)
                
                self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
    
        return img              
        
    def findPositon(self, img, handNo=0, draw=False):
        if self.results.multi_hand_landmarks:
            myHands = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHands.landmark):
                # print(f"hand Number {handNo} ")
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 8:
                    cv.circle(img, (cx, cy), 20, (255,0,255), 2)
            
        
    
    
def main():
        capture = cv.VideoCapture(0)
        detector = handDetector()
        while True: 
            isTrue, img = capture.read()
            img = detector.findHands(img)
            detector.findPositon(img, 0)
            cv.imshow("Web feed", img)
            
            if cv.waitKey(1) == ord('q'):
                break


if __name__ == "__main__":
    main()