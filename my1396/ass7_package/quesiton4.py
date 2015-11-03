'''
Created on Nov 3, 2015

@author: ds-ga-1007
'''
import numpy as np
import matplotlib.pyplot as plt
def Q4():
    N_max = 50
    some_threshold = 50
    Interval=1000
    x_array=np.linspace(-2,1,Interval)
    y_array=np.linspace(-1.5,1,5,Interval)
    c=np.empty([Interval,Interval],dtype=complex)
    for i in range(Interval):
        for k in range(Interval):
            c[i,k]=x_array[i]+1j*y_array[k]
    z=c
    for v in range(N_max):
        z = z**2 + c
    mask=abs(z)<some_threshold
    plt.imshow(mask.T, extent=[-2, 1, -1.5, 1.5])
    plt.gray()
    plt.savefig('mandelbrot.png')
    
    
    

    
        
    