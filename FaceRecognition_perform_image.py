import pickle
import cv2
import face_recognition
import numpy as np

file = open('EncodeFile.p','rb')
encodeListVisitorsWithIds = pickle.load(file)
visitorsEncodingList, visitor_ids = encodeListVisitorsWithIds

image = cv2.imread('testing/images.jpeg')
#imgS = cv2.resize(image,(0,0),None,0.25,0.25)
imgS = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

faceCurFrame = face_recognition.face_locations(imgS)
encodeCurFrame = face_recognition.face_encodings(imgS,faceCurFrame)

for encodeFace,faceLoc in zip(encodeCurFrame,faceCurFrame):
    matches = face_recognition.compare_faces(visitorsEncodingList,encodeFace,tolerance=0.5)
    faceDis = face_recognition.face_distance(visitorsEncodingList, encodeFace)

    matchIndex = np.argmin(faceDis)
    if matches[matchIndex]:
        print("Visitor face Detected",visitor_ids[matchIndex])
    else:
       print("No match found....")
