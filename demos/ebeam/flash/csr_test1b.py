import numpy as np
import matplotlib.pyplot as plt

from arcline import arcline
from ocelot.cpbd.csr_old import *

#
# define trajectory (= arc + line)
#

SRE = np.transpose([[0, 0, 0, 0, 1, 0, 0 ]])
Delta_S = 0.5
d_S=0.002
R_vect = np.array([0, 0, 1.5])
SRE = arcline(SRE, Delta_S, d_S, R_vect)
#print SRE
Delta_S=2.5
d_S=0.002
R_vect=[]
SRE=arcline(SRE,Delta_S,d_S,R_vect)
Delta_S=0.5
d_S=0.002
R_vect=[0, 0, -1.5]
SRE=arcline(SRE,Delta_S,d_S,R_vect)
Delta_S=3.5
d_S=0.002
R_vect=[]
SRE=arcline(SRE,Delta_S,d_S,R_vect)
#SRE_m = np.loadtxt("SRE.txt", unpack=True)
#print SRE[3,:]
plt.plot(SRE[0,:], SRE[2,:], "r.")
#plt.plot(SRE_m[0,:], SRE_m[5,:], "b.")
plt.show()



#%--------------------------------------------------------------------------
i=np.where(SRE[0,:]<7)[0][-1]
print i
Ndw=[2000, 1E-6]
gamma=100000;
K1 =CSR_K1(i,SRE,Ndw,gamma)
K1i=CSR_K1(i,SRE,Ndw)
w_range=np.arange(-Ndw[0],1)*Ndw[1]
plt.figure(2);
plt.plot(w_range,K1,w_range,K1i);
plt.figure(5);
plt.plot(w_range,K1);
plt.figure(6)
plt.plot(w_range, K1i);
#%--------------------------------------------------------------------------
sigma=50E-6;
qtot=1E-9;
lambd= lambda w: qtot/np.sqrt(2*np.pi)/sigma*np.exp(-0.5*(w/sigma)**2)
Ns = np.ceil(5*sigma/Ndw[1]);
s = np.arange(-Ns, Ns+1)*Ndw[1];
lam=lambd(s);
plt.figure(4)
plt.plot(s, lam)
#%--------------------------------------------------------------------------

lam_K1 =np.convolve(lam,K1 );
Nend=len(lam_K1);
lam_K1i=np.convolve(lam,K1i);
plt.figure(3);
x = np.arange(Ns+1-Nend, Ns+1)*Ndw[1]
plt.plot(x,lam_K1,x,lam_K1i);
plt.figure(7);
plt.plot(x,lam_K1);
plt.figure(8);
plt.plot(x,lam_K1i);
plt.show()