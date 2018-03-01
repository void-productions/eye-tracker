#!/usr/bin/python3 -B

# sauce: https://stackoverflow.com/questions/604749/how-do-i-access-my-webcam-in-python#606154

import cv2

vc = cv2.VideoCapture(0)

def get():
	if vc.isOpened():
		rval, frame = vc.read()
	else:
		rval = False

	if rval:
		return frame
	else:
		return None
