#!/usr/bin/python3 -B

# sauce: https://stackoverflow.com/questions/604749/how-do-i-access-my-webcam-in-python#606154

import cv2
import eye_detector

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    eye_detector.show_img_eyes(frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
cv2.destroyAllWindows()
