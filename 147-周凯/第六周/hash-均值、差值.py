#!/usr/bin/env python
# coding: utf-8

# In[8]:


import cv2
import numpy as np

#均值哈希
def ahash(img):
    img = cv2.resize(img,(8,8),interpolation=cv2.INTER_CUBIC)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    
    s = 0
    hash_str = ''
    for i in range(8):
        for j in range(8):
            s = s + gray[i,j]
    avg = s/64
    for i in range(8):
        for i in range(8):
            if gray[i,j] > avg:
                hash_str = hash_str + '1'
                
            else:
                hash_str = hash_str + '0'
    return hash_str

#差值算法
def shash(img):
    img = cv2.resize(img,(9,8),interpolation=cv2.INTER_CUBIC)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    hash_str = ''
    for i in range(8):
        for j in range(8):
            if gray[i,j] > gray[i,j+1]:
                hash_str = hash_str + '1'
                
            else:
                hash_str = hash_str + '0'
    return hash_str

def cmphash(hash1,hash2):
    n = 0
    if len(hash1) != len(hash2):
        return -1
    
    for i in range(len(hash1)):
        if hash1[i] != hash2[i]:
            n = n + 1
    return float(n)/len(hash1)


img1 = cv2.imread('lenna.png')
img2 = cv2.imread('lenna_noise.png')

hash1 = ahash(img1)
hash2 = ahash(img2)
print(hash1)
print(hash2)
n = cmphash(hash1,hash2)
print('均值哈希相似度：',n)


hash1 = shash(img1)
hash2 = shash(img2)
print(hash1)
print(hash2)
n = cmphash(hash1,hash2)
print('差值哈希相似度：',n)


    


# In[ ]:




