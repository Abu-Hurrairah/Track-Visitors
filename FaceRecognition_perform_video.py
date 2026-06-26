import pickle

import cv2
import face_recognition
import numpy as np

file = open('EncodeFile.p','rb')
encodeListVisitorsWithIds = pickle.load(file)
visitorsEncodingList, visitor_ids = encodeListVisitorsWithIds

cap = cv2.VideoCapture('testing/video3.mp4')
frameCounter = 1;
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        frameCounter+=1
        if frameCounter % 30 == 0:
            #frameS = cv2.resize(frame,(0,0),None,0.75,0.75)
            faceCurFrame = face_recognition.face_locations(frame)

            encodeCurFrame = face_recognition.face_encodings(frame, faceCurFrame)
            for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
                matches = face_recognition.compare_faces(visitorsEncodingList, encodeFace,tolerance=0.5)
                faceDis = face_recognition.face_distance(visitorsEncodingList, encodeFace)
                matchIndex = np.argmin(faceDis)

                if matches[matchIndex]:
                    print("Visitor face Detected", visitor_ids[matchIndex])
                else:
                    print("No match found....")
    else:
        break

cap.release()