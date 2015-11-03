'''
Created on Nov 3, 2015

@author: ds-ga-1007
'''
import numpy as np
class Q3:
    def __init__(self):
        np.random.seed(1234)
        self.a=np.random.rand(10,3)
    def pick(self):
        self.b=abs(self.a-.5)
        self.c=np.argsort(self.b,axis=1)
        idx=self.c[:,0]
        result=self.a[range(10),idx]
        return result
                
