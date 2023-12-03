#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 19:57:23 2020

@author: nicolas
"""
import cv2
import numpy as np
import wave
import contextlib
#fname = '/tmp/test.wav'


video_path = '/home/nicolas/Universidad/códigos/Proyecto/Video3.mp4'
cap = cv2.VideoCapture(video_path)

length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps    = cap.get(cv2.CAP_PROP_FPS)
duraciont = length/fps
duracionfps= duraciont/length
print( length )
print( fps )
print( duraciont )
print( duracionfps)

img_index =0
# threshold =0.8

while (cap.isOpened()):
    ret, frame = cap.read()
    
    if ret ==False:
        break
    img_rotate_90_clockwise = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    cv2.imwrite('/home/nicolas/Universidad/códigos/Proyecto/' + str(img_index) + '.png', img_rotate_90_clockwise)
    img_index += 1
    
    
    # template = cv2.imread('/home/nicolas/Universidad/códigos/Proyecto/objeto.png',0)
    # face_w, face_h = template.shape[::-1]
    # img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    # loc = np.where(res >= threshold)
    # for pt in zip(*loc[::-1]):
    #     #puting  rectangle on recognized erea 
    #     cv2.rectangle(frame, pt, (pt[0] + face_w, pt[1] + face_h), (0,0,255), 2)

# cv2.imshow("detected", frame)
cap.release()
# cv2.waitKey(10000)
cv2.destroyAllWindows()
