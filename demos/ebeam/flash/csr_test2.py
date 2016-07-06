import numpy as np
import matplotlib.pyplot as plt

from arcline import arcline
from ocelot.cpbd.csr_old import *

#from IPython import display
#
# define trajectory (= arc + line)
#

SRE = np.transpose([[0, 0, 0, 0, 0, 0, 1 ]])
Delta_S = 0.5
d_S=0.0002
R_vect = np.array([0, 1.5, 0])
SRE = arcline(SRE, Delta_S, d_S, R_vect)
#print SRE
Delta_S=2.5
d_S=0.0002
R_vect=[]
SRE=arcline(SRE,Delta_S,d_S,R_vect)
Delta_S=0.5
d_S=0.0002
R_vect=[0, -1.5, 0]
SRE=arcline(SRE,Delta_S,d_S,R_vect)
Delta_S=3.5
d_S=0.0002
R_vect=[]
SRE=arcline(SRE,Delta_S,d_S,R_vect)
plt.plot(SRE[3,:], SRE[1,:], "r.")
plt.show()



#%--------------------------------------------------------------------------
i=np.where(SRE[0,:]<7)[0][-1]
print i
Ndw=[2000, 1E-6]
gamma=100;
#K1 =CSR_K1(i,SRE,Ndw,gamma)
#K1i=CSR_K1(i,SRE,Ndw)
w_range=np.arange(-Ndw[0],1)*Ndw[1]
#plt.figure(2);
#plt.plot(w_range,K1,w_range,K1i);
#plt.figure(5);
#plt.plot(w_range,K1);
#plt.figure(6)
#plt.plot(w_range, K1i);
#%--------------------------------------------------------------------------
sigma=50E-6;
qtot=1E-9;
lambd= lambda w: qtot/np.sqrt(2*np.pi)/sigma*np.exp(-0.5*(w/sigma)**2)
Ns = np.ceil(5*sigma/Ndw[1]);
s = np.arange(-Ns, Ns+1)*Ndw[1];
lam=lambd(s);
#plt.figure(4)
#plt.plot(s, lam)
#%--------------------------------------------------------------------------
gamma=100;
Ndw=[2000, 1E-6]

i=np.where(SRE[0,:]<=0.05)[0][-1]
print i
K1 =CSR_K1(i, SRE, Ndw, gamma)
lam_K1 = np.convolve(lam, K1 )
Nend=len(lam_K1)
x = np.arange(Ns+1-Nend, Ns+1)*Ndw[1]

plt.ion()
f=plt.figure()
ax = f.add_subplot(111)
line, = ax.plot(x[::10], lam_K1[::10])
plt.ylim([-2.5e6, 2e6])
plt.grid(True)
#plt.show()
print("s", SRE[0,-1])

for s in np.linspace(0.05, SRE[0,-1], num=500):
    i=np.where(SRE[0,:]<=s)[0][-1]
    print s, i
    K1 =CSR_K1(i, SRE, Ndw, gamma)
    lam_K1 = np.convolve(lam, K1 )
    Nend=len(lam_K1)
    x = np.arange(Ns+1-Nend, Ns+1)*Ndw[1]

    line.set_ydata(lam_K1[::10])
    line.set_xdata(x[::10])
    #plt.draw()
    plt.pause(0.001)
    f.canvas.draw()


#lam_K1i=np.convolve(lam,K1i);
#plt.figure(3);

