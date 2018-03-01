#!/usr/bin/python3 -B

# sauce: https://stackoverflow.com/questions/604749/how-do-i-access-my-webcam-in-python#606154

import cv2
import cam
import eye_detector
import numpy

cv2.namedWindow("preview")

while True:
    frame = cam.get()
    if frame is None:
       	break
    eye_detector.show_img_eyes(frame)
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
cv2.destroyAllWindows()
