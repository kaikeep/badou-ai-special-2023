#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
img = cv2.imread("lenna.png")
h,w=img.shape[:2]
img_gray=np.zeros([h,w],img.dtype)
for i in range(h):
        for j in range(w):
            m=img[i,j]
            img_gray[i,j]=int(m[0]*0.11 + m[1]*0.59 + m[2]*0.3 )
print(img_gray)
print("image show gray:%s"%img_gray)
cv2.imshow("image show gray",img_gray)
cv2.waitKey(0)

rows,cols=img_gray.shape
for i in range(rows):
    for j in range(cols):
        if(img_gray[i,j] <= 122):
            img_gray[i,j]=0
        else:
            img_gray[i,j]=255
print(img_gray)

print("image show binary:%s"%img_gray)
cv2.imshow("image show binary",img_gray)
cv2.waitKey(0)





