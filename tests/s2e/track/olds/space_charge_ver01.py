'''
Created on 27.03.2015
@author: Igor Zagorodnov @ Martin Dohlus
'''
import matplotlib.pyplot as plt
import numpy as np
import time
from math import *

#def IGreen(x,y,z):
#    xx=x*x; yy=y*y; zz=z*z
#    xy=x*y; zx=z*x; yz=y*z
#    r=sqrt(xx+yy+zz)
    #out=(-xx*0.5*atan(yz/(x*r))+yz*log(x+r)
    #-yy*0.5*atan(zx/(y*r))+zx*log(y+r)
    #-zz*0.5*atan(xy/(z*r))+xy*log(z+r))
#    out=-xx*0.5*atan(yz/(x*r))
#    return out

def Sym_Kernel(ijk2,hxyz):
    #t0=time.time()
    i2=ijk2[0]; j2=ijk2[1]; k2=ijk2[2]
    hx=hxyz[0]; hy=hxyz[1]; hz=hxyz[2]
    x=hx*np.r_[0:i2+1]-hx/2
    y=hy*np.r_[0:j2+1]-hy/2
    z=hz*np.r_[0:k2+1]-hz/2
    #IG=np.zeros((i2+1,j2+1,k2+1))
    #for i in range(i2+1):
    #    for j in range(j2+1):
    #        for k in range(k2+1):
    #            IG[i,j,k]=IGreen(x[i],y[j],z[k])
    x=x.reshape(i2+1,1,1);y=y.reshape(1,j2+1,1);z=z.reshape(1,1,k2+1)
    r=np.sqrt(x*x+y*y+z*z)
    IG=(-x*x*0.5*np.arctan(y*z/(x*r))+y*z*np.log(x+r)
        -y*y*0.5*np.arctan(z*x/(y*r))+z*x*np.log(y+r)
        -z*z*0.5*np.arctan(x*y/(z*r))+x*y*np.log(z+r))
    #print IG.shape, rd.shape,x.shape, y.shape, z.shape
    #IG1=IGreen(xx,yy,zz)
    
    #xx=np.zeros(x.shape); xx=x*x;
    #yy=np.zeros(y.shape); yy=y*y;
    
    #xx=x*x; yy=y*y; zz=z*z
    #xy=x*y; zx=z*x; yz=y*z
    #r=sqrt(xx+yy+zz)
    #out=(-xx*0.5*atan(yz/(x*r))+yz*log(x+r)
    #-yy*0.5*atan(zx/(y*r))+zx*log(y+r)
    #-zz*0.5*atan(xy/(z*r))+xy*log(z+r))
    #t1=time.time()-t0
    #print t1
   
    # out=np.zeros((i2,j2,k2));
    # t0=time.time()
    out=(IG[1:i2+1,1:j2+1,1:k2+1]-IG[0:i2,1:j2+1,1:k2+1]
         -IG[1:i2+1,0:j2,1:k2+1]+IG[0:i2,0:j2,1:k2+1]
         -IG[1:i2+1,1:j2+1,0:k2]+IG[0:i2,1:j2+1,0:k2]
         +IG[1:i2+1,0:j2,0:k2]-IG[0:i2,0:j2,0:k2])
    #for i in range(i2):
    #    for j in range(j2):
    #        for k in range(k2):
    #            out[i,j,k]= (IG[i+1,j+1,k+1]-IG[i,j+1,k+1]
    #            -IG[i+1,j,k+1]+IG[i,j,k+1]
    #            -IG[i+1,j+1,k]+IG[i,j+1,k]
    #            +IG[i+1,j,k]-IG[i,j,k])
    #t1=time.time()-t0
    #print t1            
    return out

def Phi(q,kern,steps):
    c=299792458;    mue0=4*pi*1e-7;   eps0=1/(c*c*mue0)
    #--------------------------------------------------------------------
    hx=steps[0];    hy=steps[1];    hz=steps[2]
    Nx=q.shape[0];    Ny=q.shape[1];    Nz=q.shape[2]
    out=np.zeros((2*Nx-1,2*Ny-1,2*Nz-1))
    out[:Nx,:Ny,:Nz]=q
    #--------------------------------------------------------------------
    if kern.shape>=q.shape:
        K1=kern[:Nx,:Ny,:Nz]
    else:
        print 'size(q)= ', q.shape ,'; calculate kernel'
        K1=Sym_Kernel(q.shape,steps)
    
    K2=np.zeros((2*Nx-1,2*Ny-1,2*Nz-1))
    K2[0:Nx,0:Ny,0:Nz]=K1
    K2[0:Nx,0:Ny,Nz:2*Nz-1]=K2[0:Nx,0:Ny,Nz-1:0:-1]
    K2[0:Nx,Ny:2*Ny-1,:]=K2[0:Nx,Ny-1:0:-1,:]
    K2[Nx:2*Nx-1,:,:]=K2[Nx-1:0:-1,:,:]
    #for nx in range(Nx):
    #    nx2=0 
    #    if nx>0:
    #        nx2=2*Nx-1-nx 
    #    for ny in range(Ny):
    #        ny2=0 
    #        if ny>0: 
    #            ny2=2*Ny-1-ny 
    #        for nz in range(Nz):
    #            nz2=0 
    #            if nz>0: 
    #                nz2=2*Nz-1-nz 
    #            h=K1[nx,ny,nz]
    #            K2[nx ,ny ,nz]=h
    #            K2[nx2,ny ,nz]=h
    #            K2[nx ,ny2,nz]=h
    #            K2[nx2,ny2,nz]=h
    #            K2[nx ,ny ,nz2]=h
    #            K2[nx2,ny ,nz2]=h
    #            K2[nx ,ny2,nz2]=h
    #            K2[nx2,ny2,nz2]=h
    #--------------------------------------------------------------------
    #t0=time.time()
    out=np.real(np.fft.ifftn(np.fft.fftn(out)*np.fft.fftn(K2)))
    #out=np.real(np.fft.ifft(np.fft.ifft(np.fft.ifft(
    #            np.fft.fft(np.fft.fft(np.fft.fft(out,axis=0),axis=1),axis=2)
    #            *np.fft.fft(np.fft.fft(np.fft.fft(K2,axis=0),axis=1),axis=2),axis=2),
    #            axis=1),axis=0))
    #t1=time.time()-t0
    #print t1
    out[:Nx,:Ny,:Nz]=out[:Nx,:Ny,:Nz]/(4*pi*eps0*hx*hy*hz)
    return out[:Nx,:Ny,:Nz], K1

t0=time.time()
xres=0.1
yres=0.2
zres=0.3
hxyz=(xres,yres,zres)
nxyz=(60,60,60)
#t0=time.time() 
kern=Sym_Kernel(nxyz,hxyz)
#t1=time.time()-t0 
#print t1
q=np.zeros((60,60,60))
for i in range(60):
    for j in range(60):
        for k in range(60):
            q[i,j,k]=i+j+k+3

#t0=time.time()   
out,kern=Phi(q,kern,hxyz)
t1=time.time()-t0
print t1, out[0,1,2]
