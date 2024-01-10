#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import matplotlib.pyplot as plt

def zero_one(x):
    
    return [(float(i) - min(x)) / float(max(x) - min(x)) for i in x]

def one_one(x):
    
    return [(float(i) - np.mean(x)) / (max(x) - min(x)) for i in x]

def z_score(x):
    
    s2 = sum([(i - np.mean(x)) * (i - np.mean(x)) for i in x]) / len(x)
    return [(i - np.mean(x)) / s2 for i in x]

l=[-10, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 15, 15, 30]

cs = []
for i in l:
    c = l.count(i)
    cs.append(c)
p = zero_one(l)    
n = one_one(l)
z = z_score(l)

plt.plot(l,cs)
plt.plot(p,cs)
plt.plot(n,cs)
plt.plot(z,cs)


# In[ ]:




