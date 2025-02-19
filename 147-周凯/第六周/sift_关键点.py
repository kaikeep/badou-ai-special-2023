#!/usr/bin/env python
# coding: utf-8

# In[5]:


import cv2
import numpy as np

img = cv2.imread("lenna.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#找出关键点
sift = cv2.xfeatures2d.SIFT_create()
keypoints,descriptor = sift.detectAndCompute(gray,None)

#对图像的每个关键点进行关键点绘制方向
img = cv2.drawKeypoints(image=img,outImage=img,keypoints=keypoints,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS,color=(51,163,236))

cv2.imshow('sift-keypoints',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




