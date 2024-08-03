import cv2 as cv
import numpy as np
import os

people = []
for i in os.listdir(r'Face Recognition\Faces\train'):
    people.append (i)
    
# print(people)

features =  []
labels = []

DIR = r'Face Recognition\Faces\train'
haar_cascade = cv.CascadeClassifier("Face Detection/haarcascade_frontalface_default.xml")

def create_train():
    for person in people:
        path = os.path.join(DIR,person)
        label = people.index(person)
        
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
            
            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                # cv.imshow("", faces_roi)
                # if cv.waitKey(0) == ord('q'):
                #     break
                
                features.append(faces_roi)
                labels.append(label)

create_train()

features = np.array(features, dtype='object')
labels = np.array(labels)

print(f"Length of features {len(features)}")
print(f"Length of features {len(labels)}")

np.save("Face Recognition/features.npy",features)
np.save("Face Recognition/labels.npy", labels)
