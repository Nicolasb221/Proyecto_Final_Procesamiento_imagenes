#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 09:34:35 2020

@author: nicolas
"""

import cv2
import numpy as np
import glob

img_index =0
while img_index <= 116:
    
    img_rgb = cv2.imread('/home/nicolas/Universidad/códigos/Proyecto/' + str(img_index) + '.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    
    # image = cv2.adaptiveThreshold(img_rgb, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 45, 0)
    
    template = cv2.imread('/home/nicolas/Universidad/códigos/Proyecto/object.png',0)
    # template1 = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('xxx',template1)
    # cv2.waitKey(10000)
    w, h = template.shape[::-1]
    
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    # min_v, max_v, min_pt, max_pt = cv2.minMaxLoc(res)
        
    threshold = 0.90
    loc = np.where( res >= threshold)
    
    # mask = np.zeros(image.shape[:2], np.uint8)
    # cv2.drawContours(mask, cnt, -1, 255, -1)
    # contornos,hierarchy = cv2.findContours(maskred, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
        
        # area=cv2.contourArea(res) #area de cada contorno
        # if area > 100:
        # M=cv2.moments(loc) #haller el centroide
        # if (M["m00"]==0): M["m00"]=1 #evitar denominador cero, es decir, infinito
        # x=int(M["m10"]/M["m00"])
        # y=int(M["m01"]/M["m00"])
        # # cómo será el punto en el centro, radio, color, posición
        # cv2.circle(img_rgb,(x,y),4,(0,0,255), -1)
        
    cv2.imwrite('/home/nicolas/Universidad/códigos/Proyecto/detected/Frame_detected' + str(img_index) + '.png', img_rgb)
    img_index +=1
# cv2.imshow('Detected',img_rgb)

# cv2.waitKey(10000)
cv2.destroyAllWindows()