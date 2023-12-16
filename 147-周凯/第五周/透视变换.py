#!/usr/bin/env python
# coding: utf-8

# In[5]:


import cv2
import numpy as np

img = cv2.imread('photo1.jpg')
result = img.copy()


src = np.float32([[207,151],[517,285],[17,601],[343,731]])
dst = np.float32([[0,0],[337,0],[0,488],[337,488]])
print(img.shape)

m = cv2.getPerspectiveTransform(src,dst)
print("warpMatrix:")
print(m)
result_img = cv2.warpPerspective(result,m,(337,488))
cv2.imshow("src_img",img)
cv2.imshow("result_img",result_img)
cv2.waitKey(0)


# In[ ]:





# In[ ]:




