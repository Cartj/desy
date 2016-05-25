__author__ = 'Igor Zagorodnov'

from ocelot.cpbd.wake3D import *
from ocelot.gui import *


filename='WakeXFEL0.1600.001'
Ps0, q, z0, gamref = astraBeam2particleArray(filename)

#
Ps = Ps0.particles.view()
Np = len(Ps)/6
Ps.shape = (Np, 6)

y0=0
x0=0.1e-3
Ps[:,2]=Ps[:,2]+y0
Ps[:,0]=Ps[:,0]+x0
Ns=500              # wake sampling
NF=20               # smoothing filter order       
wakeFile='wake_vert_1m.txt'
THv=LoadWakeTable (wakeFile)
Px,Py,Pz,I00=AddTotalWake (Ps[:,0],Ps[:,2],Ps[:,4],q,THv,Ns,NF)
wakefile='WakeLQD.txt'
w1=np.loadtxt(wakefile,comments='%')
s=-w1[:,0]*1e3+1


P = exact_xxstg_2_xp(Ps, gamref)
sp=P[:,2]*1e6

plt.figure(1)
koef=np.min(Pz)/np.max(I00[:,1])
plt.plot(sp,Pz*1e-6,'.',s,w1[:,1]*1e12/4*1e-6,I00[:,0]*1e6,-I00[:,1]*koef*1e-6)
plt.figure(2)
koef=np.max(Px)/np.max(I00[:,1]);
plt.plot(sp,Px*1e-6,'.',s,w1[:,2]*1e15/2*1e-6*x0,I00[:,0]*1e6,I00[:,1]*koef*1e-6)
plt.show()
