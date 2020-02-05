#advecion equation 1d euler scheme
import numpy as np
import matplotlib.pyplot as plt

i=np.arange(-10,10,0.01)
j=np.arange(-10,10,0.01)

u_1=np.zeros([len(j),len(i)])


def exact_solution(j,x):
    v=0
    t=0
    u_1[0,j]=np.exp(-((x+0.3)**2-v*t))


def euler_scheme1(n,l,j,i):
    v=0.5
    delta_t=0.05
    delta_x=0.05
    a=(v*delta_t)/(2*delta_x)
    u_1[n,l]=u_1[j+1,i]-a*(u_1[j+2,i]-u_1[j,i])
    #print(u_1[j,i+1])


t=0
for z in np.arange(-10,10,0.01):
    exact_solution(t,z)
    t=t+1

plt.plot(j,u_1[0,:])
plt.show()
print(u_1)

