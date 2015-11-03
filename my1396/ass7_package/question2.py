'''
Created on Nov 3, 2015

@author: ds-ga-1007
'''
import numpy as np
class Q2:
    def __init__(self):
        self.a=np.arange(25).reshape(5, 5)
        self.b=np.array([1., 5, 10, 15, 20])
        self.c=np.zeros((5,5))
    def divide_col_elewise(self):
        for i in range(5):
            self.c[:,i]=np.divide(self.a[:,i],self.b)
        return self.c
            
                
        
        
