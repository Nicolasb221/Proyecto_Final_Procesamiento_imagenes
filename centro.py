#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 11:32:41 2020

@author: nicolas
"""

import numpy as np
import cv2 
x_datos=[]
y_datos=[]
var=0

img_index =2
while img_index <= 116:

    image = cv2.imread('/home/nicolas/Universidad/códigos/Proyecto/detected/Frame_detected' + str(img_index) + '.png') 
    # image= cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    lower_yellow = np.array([15,100,20],np.uint8)#definan dependiendo del color de su marcador
    upper_yellow = np.array([45,255,255],np.uint8)
    
    maskyellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
    # cv2.imshow('puta', maskyellow)
    # Your code to threshold
    # ret,binaria = cv2.threshold(img_grey, 225, 255, cv2.THRESH_BINARY_INV)  
    
    contornos,hierarchy = cv2.findContours(maskyellow, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    
    img_index +=1
    
    for c in contornos:
        area=cv2.contourArea(c) #area de cada contorno
        if area > 1500:  #detecta lo que esta más cerca a la cámara
            M=cv2.moments(c) #haller el centroide
            if (M["m00"]==0): M["m00"]=1 #evitar denominador cero, es decir, infinito
            x=int(M["m10"]/M["m00"])
            y=int(M["m01"]/M["m00"])
            
            x_datos.append(x)
            y_datos.append(y)
            
            var +=1
            # cómo será el punto en el centro, radio, color, posición
            font = cv2.FONT_HERSHEY_SIMPLEX 
            #ubicacion del texto en el video, tamaño, ancho, color, etc.
            cv2.putText(image, '{},{}'.format(x,y), (x,y+40), font, 0.40, (255,0,0),1, cv2.LINE_AA)
            cv2.circle(image,(x,y),2,(0,0,255), -1)
            imagen1=cv2.drawContours(image, contornos, -1, (0,255,0), 2)
            encabezado='x'
            enca='y'
            np.savetxt('/home/nicolas/Universidad/códigos/Proyecto/datos_x', x_datos, fmt ='%d', header=encabezado)
            np.savetxt('/home/nicolas/Universidad/códigos/Proyecto/datos_y', y_datos, fmt ='%d', header=enca)
            cv2.imwrite('/home/nicolas/Universidad/códigos/Proyecto/centro/Area_imagen' + str(img_index) + '.png',image)
# print(x_datos)
# print(y_datos)

# cv2.imshow('111', imagen1)
# cv2.imwrite('/home/nicolas/Universidad/códigos/Proyecto/Frame89.png', imagen1) 
cv2.waitKey(10000)
cv2.destroyAllWindows()