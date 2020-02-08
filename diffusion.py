#Diffusion equation 1d euler scheme
import numpy as np
import matplotlib.pyplot as plt

x=np.arange(-2,2,0.1)
t=np.arange(0,2,0.1)
c_1=np.zeros([len(t),len(x)])

t1=0.1
j2=0
k_h=0.4
for t1 in np.arange(0,2,0.1):
    x2=0
    for x1 in np.arange(-2,2,0.1):
        c_1[j2,x2]=(1/(np.sqrt(4*np.pi*k_h*t1)))*np.exp(-(((x1)**2)/(4*k_h*t1)))
        x2=x2+1
    t=t+1
    j2=j2+1
print (c_1)
