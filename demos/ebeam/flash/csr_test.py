import numpy as np
import matplotlib.pyplot as plt

from arcline import arcline
from ocelot.cpbd.csr_old import *
import matplotlib
font = {'size'   : 20}
matplotlib.rc('font', **font)
#
# define trajectory (= arc + line)
#

SRE = np.transpose([[0, 0, 0, 0, 0, 0, 1]])
Delta_S = 0.5
d_S=0.0002
R_vect = np.array([0, 10., 0])
SRE = arcline(SRE, Delta_S, d_S, R_vect)
#print SRE
Delta_S=2.5
d_S=0.0002
R_vect=[]
SRE=arcline(SRE,Delta_S, d_S, R_vect)
Delta_S=0.5
d_S=0.0002
R_vect=[0, -1, 0]
SRE=arcline(SRE, Delta_S, d_S, R_vect)
Delta_S=3.5
d_S=0.0002
R_vect=[]
SRE=arcline(SRE, Delta_S, d_S, R_vect)
#SRE_m = np.loadtxt("SRE.txt", unpack=True)


plt.figure(1)
plt.title("Trajectory")
plt.xlabel("z, m")
plt.ylabel("x, m")
plt.grid(True)
plt.plot(SRE[0,:], SRE[1,:], "r")
plt.plot(SRE[0, 499], SRE[2,499], "bo")
plt.show()



#%--------------------------------------------------------------------------
i= np.where(SRE[0,:]<0.1)[0][-1]
print i
Ndw=[2000, 1E-6]
gamma = 100
K1 = CSR_K1(i, SRE, Ndw, gamma=None)
w_range = np.arange(-Ndw[0], 1)*Ndw[1]

plt.figure(2)
plt.plot(w_range, K1, 'r')
plt.xlabel("s, m")
plt.ylabel("V/C")
#plt.yscale("log")
#plt.plot(w_range_m, K1_m, 'b')
#plt.show()

#%--------------------------------------------------------------------------
sigma=50E-6
qtot=1E-9
lamb = lambda w: qtot/np.sqrt(2*np.pi)/sigma*np.exp(-0.5*(w/sigma)**2)
Ns = np.ceil(5*sigma/Ndw[1])
s=np.arange(-Ns, Ns+1)*Ndw[1]
lam = lamb(s)
plt.figure(4)
plt.ticklabel_format(style='sci', axis='y', scilimits=(1,1))
plt.plot(s, lam)
plt.xlabel("s, m")
plt.ylabel(r"$\lambda$")
#%--------------------------------------------------------------------------
print("len lam/K1: ", len(lam), len(K1))
lam_K1 = np.convolve(lam, K1 )
Nend = len(lam_K1)
#Nend=size(lam_K1, 2)
plt.figure(3)
x = np.arange(Ns+1-Nend,Ns+1)*Ndw[1]
#x2, K2 = np.loadtxt("lam_K1.txt", unpack=True)
plt.plot(x, lam_K1/1000)
plt.xlabel("s, m")
plt.ylabel("W, keV")
plt.show()