#!/bin/bash

if [ ! -d res ]; then
	mkdir res
fi

curl https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_eye.xml > res/haarcascade_eye.xml
curl https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml > res/haarcascade_frontalface_default.xml
curl -o res/default_img.jpg https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fb%2Fbf%2FGwyneth_Paltrow_face.jpg
