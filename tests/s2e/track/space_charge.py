'''
Created on 27.03.2015
@author: Igor Zagorodnov @ Martin Dohlus
'''
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as ndimage 
import time
from math import *
from PhysConsts import *

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
    kern=(IG[1:i2+1,1:j2+1,1:k2+1]-IG[0:i2,1:j2+1,1:k2+1]
         -IG[1:i2+1,0:j2,1:k2+1]+IG[0:i2,0:j2,1:k2+1]
         -IG[1:i2+1,1:j2+1,0:k2]+IG[0:i2,1:j2+1,0:k2]
         +IG[1:i2+1,0:j2,0:k2]-IG[0:i2,0:j2,0:k2])
    return kern

def Phi(q,steps):
    hx=steps[0];    hy=steps[1];    hz=steps[2]
    Nx=q.shape[0];    Ny=q.shape[1];    Nz=q.shape[2]
    out=np.zeros((2*Nx-1,2*Ny-1,2*Nz-1))
    out[:Nx,:Ny,:Nz]=q
    K1=Sym_Kernel(q.shape,steps)
    K2=np.zeros((2*Nx-1,2*Ny-1,2*Nz-1))
    K2[0:Nx,0:Ny,0:Nz]=K1
    K2[0:Nx,0:Ny,Nz:2*Nz-1]=K2[0:Nx,0:Ny,Nz-1:0:-1] #z-mirror
    K2[0:Nx,Ny:2*Ny-1,:]=K2[0:Nx,Ny-1:0:-1,:]       #y-mirror
    K2[Nx:2*Nx-1,:,:]=K2[Nx-1:0:-1,:,:]             #x-mirror
    t0=time.time()
    out=np.real(np.fft.ifftn(np.fft.fftn(out)*np.fft.fftn(K2)))
    t1=time.time()
    print 'fft time:', t1-t0,' sec'
    out[:Nx,:Ny,:Nz]=out[:Nx,:Ny,:Nz]/(4*pi*eps0*hx*hy*hz)
    return out[:Nx,:Ny,:Nz]

def exact_xp_2_xxstg(xp, gamref):
    N=xp.shape[0]
    xxstg=np.zeros((N,6))
    pref=E_ele_eV*sqrt(gamref**2-1)
    u=np.c_[xp[:,3],xp[:,4],xp[:,5]+pref]
    gamma=np.sqrt(1+np.sum(u*u,1)/E_ele_eV**2)
    beta=np.sqrt(1-gamma**-2)
    u=u/np.linalg.norm(u,2,1).reshape((N,1))
    cdt=-xp[:,2]/(beta*u[:,2])
    xxstg[:,0]=xp[:,0]+beta*u[:,0]*cdt;
    xxstg[:,2]=xp[:,1]+beta*u[:,1]*cdt;
    xxstg[:,4]=cdt
    xxstg[:,1]=u[:,0]/u[:,2]
    xxstg[:,3]=u[:,1]/u[:,2]
    xxstg[:,5]=gamma/gamref-1
    return xxstg

def exact_xxstg_2_xp(xxstg,gamref):
    N=xxstg.shape[0]
    xp=np.zeros((N,6))
    pref=E_ele_eV*sqrt(gamref**2-1);
    gamma=gamref*(1+xxstg[:,5])
    beta=np.sqrt(1-gamma**-2);
    u=np.c_[xxstg[:,1],xxstg[:,3],np.ones(N)]
    norm=np.linalg.norm(u,2,1).reshape((N,1))
    u=u/norm
    xp[:,0]=xxstg[:,0]-u[:,0]*beta*xxstg[:,4]
    xp[:,1]=xxstg[:,2]-u[:,1]*beta*xxstg[:,4]
    xp[:,2]=-u[:,2]*beta*xxstg[:,4]
    xp[:,3]=u[:,0]*gamma*beta*E_ele_eV
    xp[:,4]=u[:,1]*gamma*beta*E_ele_eV
    xp[:,5]=u[:,2]*gamma*beta*E_ele_eV-pref
    return xp
    
def EField(X,Q,gamma,nxyz):
    N=X.shape[0];
    X[:,2]=X[:,2]*gamma
    XX=np.max(X,axis=0)-np.min(X,axis=0)
    XX=XX*np.random.uniform(low=1.0,high=1.1)
    print 'mesh steps:', XX
    steps=XX/(nxyz-3)
    X=X/steps
    X_min=np.min(X,axis=0)
    X_mid=np.dot(Q,X)/np.sum(Q);
    X_off=np.floor(X_min-X_mid)+X_mid;
    X=X-X_off  
    nx=nxyz[0];ny=nxyz[1];nz=nxyz[2];nzny=nz*ny
    Xi=np.int_(np.floor(X)+1)
    inds=np.int_(Xi[:,0]*nzny+Xi[:,1]*nz+Xi[:,2]) # 3d -> 1d
    print inds.shape, nxyz
    q=np.bincount(inds,Q,nzny*nx).reshape(nxyz)
    p=Phi(q,steps)
    Ex=np.zeros(p.shape);Ey=np.zeros(p.shape);Ez=np.zeros(p.shape);
    Ex[:nx-1,:,:]=(p[:nx-1,:,:]-p[1:nx,:,:])/steps[0]
    Ey[:,:ny-1,:]=(p[:,:ny-1,:]-p[:,1:ny,:])/steps[1]
    Ez[:,:,:nz-1]=(p[:,:,:nz-1]-p[:,:,1:nz])/steps[2]
    Exyz=np.zeros((N,3))
    Exyz[:,0]=ndimage.map_coordinates(Ex,np.c_[X[:,0],X[:,1]+0.5,X[:,2]+0.5].T,order=1)*gamma
    Exyz[:,1]=ndimage.map_coordinates(Ey,np.c_[X[:,0]+0.5,X[:,1],X[:,2]+0.5].T,order=1)*gamma
    Exyz[:,2]=ndimage.map_coordinates(Ez,np.c_[X[:,0]+0.5,X[:,1]+0.5,X[:,2]].T,order=1)
    return Exyz

def SC_xxstg_update(xxstg,Q,gamref,dS,L0,nxyz):
    # L0 = true : use low order approximation for kick
    #Lorentz transformation with z-axis and gamref
    betref2=1-gamref**-2
    betref=sqrt(betref2)
    Eref=gamref*E_ele_eV
    pref=Eref*betref
    Exyz=EField( np.c_[xxstg[:,0],xxstg[:,2],-betref*xxstg[:,4]],Q,gamref,nxyz)
    cdT=dS/betref
    if L0:
    #-- 0te Ordnung -------------------------------------------------------
        xxstg[:,1]=xxstg[:,1]+(cdT/pref/gamref**2)*Exyz[:,0]
        xxstg[:,3]=xxstg[:,3]+(cdT/pref/gamref**2)*Exyz[:,1]
        xxstg[:,5]=xxstg[:,5]+(dS/Eref)*Exyz[:,2]
    else:
    #-- 1te Ordnung -------------------------------------------------------
        betax=betref*xxstg[:,1]
        betay=betref*xxstg[:,3]
        betaz=betref*(1+xxstg[:,5]/(gamref**2-1))
        dpxyz_q_pref_x=(cdT/pref)*(1-betref*betaz)*Exyz[:,0]
        dpxyz_q_pref_y=(cdT/pref)*(1-betref*betaz)*Exyz[:,1]
        dpxyz_q_pref_z=(cdT/pref)*(Exyz[:,2]+betref*(betax*Exyz[:,0]+betay*Exyz[:,1]))
        xxstg[:,1]=(1-dpxyz_q_pref_z)*(xxstg[:,1]+dpxyz_q_pref_x)
        xxstg[:,3]=(1-dpxyz_q_pref_z)*(xxstg[:,3]+dpxyz_q_pref_y)
        xxstg[:,5]=xxstg[:,5]+dpxyz_q_pref_z*betref2;
        
        
def SC_xp_update(xp, Q, gamref, dS, nxyz):
    #Lorentz transformation with z-axis and gamref
    betref2=1-gamref**-2
    betref=sqrt(betref2)
    Eref=gamref*E_ele_eV
    pref=Eref*betref
    Exyz=EField(np.c_[xp[:,0],xp[:,1],xp[:,2]],Q,gamref,nxyz)
    u=np.c_[xp[:,3],xp[:,4],xp[:,5]+pref]
    gamma=np.sqrt(1+np.sum(u*u,1)/E_ele_eV**2).reshape((xp.shape[0],1))
    cdT=dS/betref
    u=u/(gamma*E_ele_eV)
    xp[:,3]=xp[:,3]+cdT*(1-betref*u[:,2])*Exyz[:,0]
    xp[:,4]=xp[:,4]+cdT*(1-betref*u[:,2])*Exyz[:,1]
    xp[:,5]=xp[:,5]+cdT*(Exyz[:,2]+betref*(u[:,0]*Exyz[:,0]+u[:,1]*Exyz[:,1]))
    
        
if __name__ == "__main__":
    P=np.loadtxt('D:/MyTools/MartinsTracker/2ASTRA/test.ast')
    #P=np.loadtxt('D:/MyTools/MartinsTracker/2ASTRA/bc1_out.ast')
    Q=-P[:,7]*1e-9 #charge in nC -> in C 
    xp=P[:,:6] 
    z00=xp[0,2] 
    pz00=xp[0,5] 
    xp[0,2]=0; xp[0,5]=0
    zav=np.mean(xp[:,2]) 
    z0=z00+zav 
    xp[:,2]=xp[:,2]-zav
    pav=np.mean(xp[:,5]) 
    pz0=pz00+pav; 
    xp[:,5]=xp[:,5]-pav
    Pref=pz0 
    gamref=sqrt((Pref/E_ele_eV)**2+1)
    xxstg=exact_xp_2_xxstg(xp,gamref)
    xxstg0=np.copy(xxstg)
    L0=False
    Lxxs=True
    dS=30;
    f=plt.figure()
    plt.ion();plt.hold(False)
    for i in range(10):
        #drift
        xxstg[:,0]=xxstg[:,0]+xxstg[:,1]*dS
        xxstg[:,2]=xxstg[:,2]+xxstg[:,3]*dS
        xxstg[:,4]=xxstg[:,4]+xxstg[:,5]*dS/gamref**2
        t0=time.time()
        if Lxxs:
            SC_xxstg_update(xxstg,Q,gamref,dS,L0,np.r_[53,53,53])
        else:    
            xp=exact_xxstg_2_xp(xxstg,gamref)
            SC_xp_update(xp,Q,gamref,dS,np.r_[53,53,53])
            xxstg=exact_xp_2_xxstg(xp,gamref)
        t1=time.time()
        print 'step time:', t1-t0,' sec'
        f.add_subplot(211)
        plt.plot(xxstg[:,4],xxstg[:,5],'.',xxstg0[:,4],xxstg0[:,5],'.')
        f.add_subplot(212)
        plt.plot(xxstg[:,4],xxstg[:,0],'.',xxstg0[:,4],xxstg0[:,0],'.')
        plt.draw()
        plt.pause(0.1)
    plt.ioff();plt.show()    
    np.savetxt('D:/pytest.ast',xxstg)
    
    
    
