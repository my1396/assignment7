'''
Created on Nov 3, 2015

@author: ds-ga-1007
'''
import numpy as np
class Question1st:
    def __init__(self):
        self.origin=np.array(np.arange(1,16)).reshape(3,5).transpose()
        print "The original array is:\n",self.origin
    def first(self):
        a=self.origin[1:4:2,:]
        return a
    def second(self):
        b=self.origin[:,1]
        return b
    def third(self):
        c=self.origin[1:3,:]
        return c
    def forth(self):
        d=list()
        for element in self.origin.flat:
            if (element >=3 ) & (element<=11):
                d.append(element)
        d.sort()
        return d
            
    
    
    
    
    
