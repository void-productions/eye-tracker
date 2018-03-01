#!/usr/bin/python3 -B

# sauce: https://docs.opencv.org/trunk/d7/d8b/tutorial_py_face_detection.html

import numpy as np
import cv2 as cv

face_cascade = cv.CascadeClassifier('res/haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('res/haarcascade_eye.xml')

def show_img_eyes(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    cv.imshow('img',img)

def get_eye_borders(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    eye_borders = []

    for (x,y,w,h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            eye_borders.append((ex, ey, ew, eh))

    return eye_borders
