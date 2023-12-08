#!/usr/bin/env python
# coding: utf-8

# In[17]:


import numpy as np


class CPCA(object):
    
    def __init__(self,X,K):
        
        self.X = X
        self.K = K
        self.centreX = []
        self.C = []
        self.U = []
        self.Z = []
        
        self.centreX = self._centralized()
        self.C = self._cov()
        self.U = self._U()
        self.Z = self._Z()
        
    #矩阵中心化    
    def _centralized(self):
        
        centreX = []
        mean = np.array([np.mean(attr) for attr in self.X.T])
        centreX = self.X - mean
        return centreX
    #求协方差
    def _cov(self):
        ns = np.shape(self.X)[0]
        C = np.dot(self.centreX.T,self.centreX)/(ns-1)
        return C
    
    #求特征矩阵
    def _U(self):
        a,b = np.linalg.eig(self.C)
        ind = np.argsort(-1*a)
        U = b[:,ind[:self.K]]
        return U
    #求降维后的矩阵
    def _Z(self):
        
        Z = np.dot(self.X,self.U)
        print('降维矩阵为:',Z)
        return Z
    
if __name__ == '__main__':
    X = np.array([[10, 15, 29],
                  [15, 46, 13],
                  [23, 21, 30],
                  [11, 9,  35],
                  [42, 45, 11],
                  [9,  48, 5],
                  [11, 21, 14],
                  [8,  5,  15],
                  [11, 12, 21],
                  [21, 20, 25]])
    K = np.shape(X)[1]-1
    print('样本：',X)
    pca = CPCA(X,K)


# In[ ]:




