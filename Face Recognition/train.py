import cv2 as cv
import numpy as np

features = np.load("Face Recognition/features.npy",allow_pickle=True)
labels = np.load("Face Recognition/labels.npy")

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(features, labels)

face_recognizer.save("Face Recognition/faces_trained.yml")