#!/usr/bin/env python
# coding: utf-8

# In[12]:


import cv2
import random
import numpy as np

def fun1(src,percetage):
    pepperImg=src
    pepperNum=int(percetage*pepperImg.shape[0]*pepperImg.shape[1])
    for i in range(pepperNum):
        randx=random.randint(0,pepperImg.shape[0]-1)
        randy=random.randint(0,pepperImg.shape[1]-1)
        
        if random.random()>0.5:
            pepperImg[randx,randy]=255
        else:
            pepperImg[randx,randy]=0
    return pepperImg

img=cv2.imread("lenna.png",0)
img1=fun1(img,0.2)
img=cv2.imread("lenna.png")
img2=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("source pepperandsalt",np.hstack([img2,img1]))
cv2.waitKey(0)


# In[ ]:





# In[ ]:




