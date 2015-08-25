'''
Created on 27.03.2015
@author: Igor Zagorodnov @ Martin Dohlus
'''
import matplotlib.pyplot as plt
import numpy as np
import time
from math import *

q0=1.60217733e-19
me=9.10938188e-31
c=299792458
mue0=4*pi*1e-7   
eps0=1/(c*c*mue0)
E_ele_eV=me*c*c/q0


def Sym_Kernel(ijk2,hxyz):
    i2=ijk2[0]; j2=ijk2[1]; k2=ijk2[2]
    hx=hxyz[0]; hy=hxyz[1]; hz=hxyz[2]
    x=hx*np.r_[0:i2+1]-hx/2;y=hy*np.r_[0:j2+1]-hy/2
    z=hz*np.r_[0:k2+1]-hz/2
    x,y,z=np.ix_(x,y,z)
    r=np.sqrt(x*x+y*y+z*z)
    IG=(-x*x*0.5*np.arctan(y*z/(x*r))+y*z*np.log(x+r)
        -y*y*0.5*np.arctan(z*x/(y*r))+z*x*np.log(y+r)
        -z*z*0.5*np.arctan(x*y/(z*r))+x*y*np.log(z+r))
    out=(IG[1:i2+1,1:j2+1,1:k2+1]-IG[0:i2,1:j2+1,1:k2+1]
         -IG[1:i2+1,0:j2,1:k2+1]+IG[0:i2,0:j2,1:k2+1]
         -IG[1:i2+1,1:j2+1,0:k2]+IG[0:i2,1:j2+1,0:k2]
         +IG[1:i2+1,0:j2,0:k2]-IG[0:i2,0:j2,0:k2])
    return out

def Phi(q,kern,steps):
    hx=steps[0];    hy=steps[1];    hz=steps[2]
    Nx=q.shape[0];    Ny=q.shape[1];    Nz=q.shape[2]
    out=np.zeros((2*Nx-1,2*Ny-1,2*Nz-1))
    out[:Nx,:Ny,:Nz]=q
    if kern.shape>=q.shape:
        K1=kern[:Nx,:Ny,:Nz]
    else:
        print 'size(q)= ', q.shape ,'; calculate kernel'
        K1=Sym_Kernel(q.shape,steps)
    K2=np.zeros((2*Nx-1,2*Ny-1,2*Nz-1))
    K2[0:Nx,0:Ny,0:Nz]=K1
    K2[0:Nx,0:Ny,Nz:2*Nz-1]=K2[0:Nx,0:Ny,Nz-1:0:-1] #z-mirror
    K2[0:Nx,Ny:2*Ny-1,:]=K2[0:Nx,Ny-1:0:-1,:]       #y-mirror
    K2[Nx:2*Nx-1,:,:]=K2[Nx-1:0:-1,:,:]             #x-mirror
    out=np.real(np.fft.ifftn(np.fft.fftn(out)*np.fft.fftn(K2)))
    out[:Nx,:Ny,:Nz]=out[:Nx,:Ny,:Nz]/(4*pi*eps0*hx*hy*hz)
    return out[:Nx,:Ny,:Nz], K1

def exact_xp_2_xxstg(xp,gamref):
    N=xp.shape[0]
    xxstg=np.zeros((N,6))
    pref=E_ele_eV*sqrt(gamref**2-1)
    u=np.c_[xp[:,3],xp[:,4],xp[:,5]+pref]
    gamma=np.sqrt(1+np.sum(u*u,1)/E_ele_eV**2)
    beta=np.sqrt(1-gamma**-2)
    norm=np.linalg.norm(u,2,1);
    norm=norm.reshape((N,1))
    u=u/norm;
    cdt=-xp[:,2]/(beta*u[:,2])
    xxstg[:,0]=xp[:,0]+beta*u[:,0]*cdt;
    xxstg[:,2]=xp[:,1]+beta*u[:,1]*cdt;
    xxstg[:,4]=cdt
    xxstg[:,1]=u[:,0]/u[:,2]
    xxstg[:,3]=u[:,1]/u[:,2]
    xxstg[:,5]=gamma/gamref-1
    return xxstg

P=np.loadtxt('D:/MyTools/MartinsTracker/2ASTRA/test.ast')

Q=-P[:,7]*1e-9 #charge in nC -> in C 
xp=P[:,:6] 
z00=xp[0,2] 
pz00=xp[0,5] 
xp[0,2]=0; xp[0,5]=0;
zav=np.mean(xp[:,2]); 
z0=z00+zav; 
xp[:,2]=xp[:,2]-zav;
pav=np.mean(xp[:,5]); 
pz0=pz00+pav; 
xp[:,5]=xp[:,5]-pav;

Pref=pz0; 
gamref=sqrt((Pref/E_ele_eV)**2+1);
xxstg0=exact_xp_2_xxstg( xp,gamref);

np.savetxt('D:/pytest.ast',xxstg0)


