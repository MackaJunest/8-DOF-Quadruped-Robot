#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#JimmyChen V3.0 by MackaJunest COPYRIGHT 2022
'''
                            front
                   leg  leg1|    |leg2
    4 groups: 1,2  -|1      |    |
              3,4  -|2_____Jimmychen
              5,6  -|3      |    |
              7,8  -|4  leg3|    |leg4
                             back
'''
import numpy as np
import cv2
face_cascade=cv2.CascadeClassifier('face1.xml')
cap=cv2.VideoCapture(0)

def FD():
    ret,img =cap.read()
    img=cv2.flip(img,-1)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    for(x,y,w,h)in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=img[y:y+h,x:x+w]
        print(int(x+w/2),int(y+h/2))
    cv2.imshow('img',img)
    k=cv2.waitKey(30) & 0xff

