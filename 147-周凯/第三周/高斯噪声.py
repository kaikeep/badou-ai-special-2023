#!/usr/bin/env python
# coding: utf-8

# In[34]:


import cv2
import random
import numpy as np
def Gauss_Noise(src,aver,sigma,percetage):
    NoiseImg=src
    NoiseNum=int(percetage*NoiseImg.shape[0]*NoiseImg.shape[1])
    
    for i in range(NoiseNum):
        randx=random.randint(0,NoiseImg.shape[0]-1)
        randy=random.randint(0,NoiseImg.shape[1]-1)
    
        NoiseImg[randx,randy]=NoiseImg[randx,randy]+random.gauss(aver,sigma)
        if NoiseImg[randx,randy]<0:
            NoiseImg[randx,randy]=0
        elif NoiseImg[randx,randy]>255:
            NoiseImg[randx,randy]=255
    return NoiseImg
img=cv2.imread("lenna.png",0)
print(img)
img1=Gauss_Noise(img,2,4,0.8)
img=cv2.imread("lenna.png",1)

img2=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("source gauss",np.hstack([img2,img1]))
cv2.waitKey(0)


# In[ ]:





# In[ ]:




