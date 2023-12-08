#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
class PCA():
    def __init__(self,k):
        self.k = k
        
    def fit_transform(self,X):
        self.K_rows = X.shape[1]
        #求方差
        X = X - X.mean(axis=0)
        self.convariance = np.dot(X.T,X)/X.shape[0]
        #求特征值和特征向量
        eig_vals,eig_vectors = np.linalg.eig(self.convariance)
        #求降维矩阵
        idx = np.argsort(-eig_vals)
        self.components = eig_vectors[:,idx[:self.k]]
        #对X进行降维
        return np.dot(X,self.components)
    
pca = PCA(2)
X = np.array([[-1,2,66,-1], [-2,6,58,-1], [-3,8,45,-2], [1,9,36,1], [2,10,62,1], [3,5,83,2]])
newX = pca.fit_transform(X)
print(newX)


# In[ ]:




