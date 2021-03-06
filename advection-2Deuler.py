#advecion equation 1d euler scheme
from mpl_toolkits.mplot3d import axes3d
import numpy as np
import matplotlib.pyplot as plt



z=np.arange(0,7,0.1)
m1=np.arange(-1,1,0.1)
m2=np.arange(-1,1,0.1)

X=np.zeros([len(m1),len(m2)])
Y=np.zeros([len(m1),len(m2)])

u_1=np.zeros((len(z),len(m1),len(m2)))


v=0.5
t=0;
z=0
for i in np.arange(0,7,0.1):
    m1=0
    for j in np.arange(-7,7,0.1):
        m2=0
        for k in np.arange(-7,7,0.1):
            u_1[z,m1,m2]=np.exp(-(((j)**2)+((k)**2))-v*i)
            m2=m2+1
        m1=m1+1
    z=z+1
print(u_1)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(u_1[0,:,:],u_1[0,1,:],u_1[0,2,:])
plt.show()