import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

if face_cascade.empty():
    raise IOError('Unable to load the face cascade classifier xml file')

cap = cv2.VideoCapture(0)

scaling_factor = 0.5

while True:

    _, frame = cap.read()

    frame = cv2.resize(frame,
                       None,
                       fx=scaling_factor,
                       fy=scaling_factor,
                       interpolation=cv2.INTER_AREA)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_rects = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in face_rects:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 3)

    cv2.imshow('Face Detection', frame)

    c = cv2.waitKey(1)

    if c == 27:
        break

cap.release()

cv2.destroyAllWindows()