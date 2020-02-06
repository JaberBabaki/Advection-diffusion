#advecion equation 1d euler scheme
import numpy as np
import matplotlib.pyplot as plt

x=np.arange(-5,5,0.1)
t=np.arange(0,7,0.1)
u_1=np.zeros([len(t),len(x)])

v=0.5
t1=0;
j2=0
for j in np.arange(0,7,0.1):
    x2=0
    for x1 in np.arange(-5,5,0.1):
        u_1[j2,x2]=np.exp(-((x1+0.3-v*t1)**2))
        x2=x2+1
    t=t+1
    j2=j2+1
#print(u_1)
#plt.plot(x,u_1[0,:])
#plt.show()



x=np.arange(-5,5,0.1)
t=np.arange(0,7,0.1)
u_2=np.zeros([len(t),len(x)])
t1=0;
v=0.5
x2=0
for x1 in np.arange(-5,5,0.1):
    u_2[0,x2]=np.exp(-((x1+0.3-v*t1)**2))
    x2=x2+1
#print(u_2)
#plt.plot(x,u_2[0,:])
#plt.show()



v=0.5
delta_t=0.05
delta_x=0.05
a=(v*delta_t)/(2*delta_x)
l=1
for g in np.arange(len(t)-1):
    n=1
    for s in np.arange(len(x)-2):
        u_2[l,n]=u_2[g,s+1]-a*(u_2[g,s+2]-u_2[g,s])
        #u_2[l,n]=u_2[g,s+1]+u_2[g,s+2]+u_2[g,s]
        #print(n,l,s,0)
        n=n+1
    u_2[l,0]=u_2[l,len(x)-2]   #i
    u_2[l,len(x)-1]=u_2[l,1]   #i
    l=l+1
print(u_1)
print("******")
print(u_2)

plt.plot(x,u_1[5,:])
plt.plot(x,u_2[5,:])
plt.show()

print(1.84519524e-01-a*(5.04176026e-03-9.13931185e-01))