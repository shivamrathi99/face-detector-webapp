import csv

import cv2
import numpy as np
import face_recognition
import os
import pickle
import pandas as pd
import datetime


#path = 'ImageAttendance'
#images = []
classNames = ['shivam', 'shivam', 'shivam', 'shivam', 'vinay', 'vinay', 'vinay', 'vinay', 'vinay', 'vinay', 'vinay']
#myList = os.listdir(path)

# for cl in myList:
#     lst = os.listdir(path + '/' + cl)
#     for person in lst:
#         currentImg = cv2.imread(f'{path}/{cl}/{person}')
#         images.append(currentImg)
#         classNames.append(os.path.splitext(cl)[0])
# print(classNames)
# print('clasename done..')



def findEncodings(argimages):
    n = 0
    encodeList = []
    x = 0
    for img in argimages:
        x += 1
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        print(x)
        encodeList.append(encode)
    return encodeList


res=[]
def markAttendance(name):
    now = datetime.date.today()
    tareek = str(now)

    df = pd.read_csv("actual.csv")
    if tareek not in df:
        df[tareek] = ""

    with open("Attendance.csv", "r") as f:
        reader = csv.reader(f, delimiter="\t")
        for i, line in enumerate(reader):
            if line[0] == name:
                df[tareek][i - 1] = "PRESENT"
                res.append(name)
    df.to_csv("actual.csv", index=False)
    return res


def Encoding():
    encodeList = findEncodings(images)
    with open('encodings', 'wb') as f:
        pickle.dump(encodeList, f)
    print("Encoding Completed")


def webcam(a):
    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLocation in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDistance = face_recognition.face_distance(encodeListKnown, encodeFace)
            matchIndex = np.argmin(faceDistance)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                y1, x2, y2, x1 = faceLocation
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            # markAttendance(name)

        cv2.imshow('Webcam', img)

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


def inputImage(path,encodeListKnown):
        img=cv2.imread(path)
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)


        for encodeFace, faceLocation in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDistance = face_recognition.face_distance(encodeListKnown, encodeFace)
            matchIndex = np.argmin(faceDistance)

            if matches[matchIndex]:
                name = classNames[matchIndex]
                y1, x2, y2, x1 = faceLocation
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                img = cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                img = cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                img = cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1,
                                  (255, 255, 255), 2)
                ans=markAttendance(name)
        img = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))
        #cv2.imshow("Output", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return ans


def initialize(path):
    #Encoding()
    with open('encodings', 'rb') as f:
        encodeListKnown = pickle.load(f)
    #path="C:\\Users\\win\\Documents\\project\\4.jpeg"
    return inputImage(path,encodeListKnown)
