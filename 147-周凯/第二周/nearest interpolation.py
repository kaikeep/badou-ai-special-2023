#!/usr/bin/env python
# coding: utf-8

# In[6]:


import cv2
import numpy as np
def function(img):
    height,width,channels=img.shape
    emptyImage=np.zeros((800,1000,channels),np.uint8)
    sh=800/height
    sw=1000/width
    for i in range(800):
        for j in range(1000):
            x=int(i/sh+0.5)
            y=int(j/sw+0.5)
            emptyImage[i,j]=img[x,y]
    return emptyImage
img=cv2.imread("lenna.png")
zoom=function(img)
print("%s"%zoom)
print(zoom.shape)
print(zoom.shape[0])
print(zoom.size)
cv2.imshow("nearest interp",zoom)
cv2.imshow("image",img)
cv2.waitKey(0)







