'''
Created on 27.03.2015
@author: Igor Zagorodnov @ Martin Dohlus
'''
import matplotlib.pyplot as plt
import numpy as np
import time
from math import *


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
    c=299792458;    mue0=4*pi*1e-7;   eps0=1/(c*c*mue0)
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

t0=time.time()
xres=0.1
yres=0.2
zres=0.3
hxyz=(xres,yres,zres)
nxyz=(60,60,60)
kern=Sym_Kernel(nxyz,hxyz)
q=np.zeros((60,60,60))
for i in range(60):
    for j in range(60):
        for k in range(60):
            q[i,j,k]=i+j+k+3
out,kern=Phi(q,kern,hxyz)
t1=time.time()-t0
print t1, out[0,1,2]
