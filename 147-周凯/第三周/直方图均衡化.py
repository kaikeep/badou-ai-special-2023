#!/usr/bin/env python
# coding: utf-8

# In[28]:


import cv2
import matplotlib.pyplot as plt
import numpy as np

#灰度图直方图均值化
img=cv2.imread('lenna.png',1)
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_gray_equalize=cv2.equalizeHist(img_gray)
hist_img_gray=cv2.calcHist([img_gray_equalize],[0],None,[256],[0,256])
plt.figure()
plt.hist(img_gray_equalize.ravel(), 256)
plt.show()
cv2.imshow("gray  equalize",np.hstack([img_gray,img_gray_equalize]))
cv2.waitKey(0)

#彩色图直方图均值化

chans=cv2.split(img)
print(chans)
bH=cv2.equalizeHist(b)
gH=cv2.equalizeHist(g)
rH=cv2.equalizeHist(r)
result=cv2.merge((bH,gH,rH))
cv2.imshow("img histogram",np.hstack([img,result]))
cv2.waitKey(0)
colors=['b','g','r']
plt.figure()
plt.title("colorful histogram")
plt.xlabel("bins")
plt.ylabel("# of Pixels")

for color,chan in zip(colors,chans):
    color_hist=cv2.calcHist([chan],[0],None,[256],[0,256])
    plt.plot(color_hist,color=color)
    plt.xlim=([0,256])
plt.show()


# In[ ]:




