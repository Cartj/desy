'''
tracking with space charge
'''
import time
from math import *

import matplotlib.pyplot as plt
from PhysConsts import *
from space_charge import *

from ocelot import MagneticLattice
from ocelot.cpbd.optics import *


def get_envelope(p_array):
    tws = Twiss()
    x = p_array.x()
    px = p_array.px()
    y = p_array.y()
    py = p_array.py()
    tws.x = np.mean(x)
    tws.y = np.mean(y)
    tws.px = np.mean(px)
    tws.py = np.mean(py)
    tws.xx = np.mean((x-tws.x)*(x-tws.x))
    tws.xpx = np.mean((x-tws.x)*(px-tws.px))
    tws.pxpx = np.mean((px-tws.px)*(px-tws.px))
    tws.yy = np.mean((y-tws.y)*(y-tws.y))
    tws.ypy = np.mean((y-tws.y)*(py-tws.py))
    tws.pypy = np.mean((py-tws.py)*(py-tws.py))
    tws.p = np.mean( p_array.p())
    tws.E = p_array.E
    tws.de = p_array.de
    tws.emittx=sqrt(tws.xx*tws.pxpx-tws.xpx**2)
    tws.emitty=sqrt(tws.yy*tws.pypy-tws.ypy**2)
    tws.betax=tws.xx/tws.emittx
    tws.betay=tws.yy/tws.emitty
    return tws

def dx(r,LB):
    LB2=LB*LB;r2=r*r
    rez=sqrt(1-LB2/r2)*r*(r-sqrt(r2-LB2))/LB
    return rez

def R56(LB,LD,r,m):
    LB2=LB*LB;r2=r*r;
    K=sqrt(1-LB2/r2);
    r56=m*r*asin(LB/r)-m*LB/K-2*LB2*LD/(K**3*r2);
    t566=( r2*LB2*(6*LD+m*LB)-m*LB**5 )/(2*K*(LB2-r2)**2);
    p1=m*LB**7-LB**4*(5*m*LB-6*LD)*r2+4*LB2*(6*LD+m*LB)*r**4;
    p2=6*K*(LB2-r2)**3;
    u5666=p1/p2;
    Sref=m*r*asin(LB/r) + 2*LD/cos(asin(LB/r));
    return r56,t566,u5666,Sref

def R56fromR(LB,LD,r,BCtype):
    r56=0; t566=0; u5666=0;
    if BCtype=='c':
        r56,t566,u5666,Sref=R56(LB,LD,r,4) 
    else:
        if BCtype=='s':
            r56,t566,u5666,Sref=R56(LB,2*LD+dx(r,LB),r,6) 
    return r56,t566,u5666  

def compressor(P,R56,T566,U5666):
    d=P[:,1]
    P[:,0]=P[:,0]+R56*d;
    if T566!=0:
        d2=d*d;
        P[:,0]=P[:,0]+T566*d2
    if U5666!=0:
        if T566==0:
            d2=d*d
        P[:,0]=P[:,0]+U5666*d*d2
    return


BC1=(6.5708,10.818543701164369)
BC2=(53.098343701164396,68.335010600972097)
DL=( 1.381486106009717e+02,1.453505656016716e+02)
Lat_end=1.893185656016718e+02
r1=1.618; r2=6.3727;
r56_1, t566_1, u5666_1=R56fromR(0.5,0.5,r1,'c');
r56_2, t566_2, u5666_2,=R56fromR(0.5,2.38,r2,'s');
r56_3=5.3639e-004; t566_3=0.03; u5666_3=0;

dz = 1.0
z_stop =  Lat_end
SC=True


beam = Beam()
beam.E = 148.3148e-3 #in GeV ?!
beam.beta_x = 14.8821  
beam.beta_y = 18.8146   
beam.alpha_x =  -0.61309   
beam.alpha_y = -0.54569
beam.emit_xn = 1.5e-6
beam.emit_yn = 1.5e-6
beam.emit_x = beam.emit_xn / (beam.E*1e9  / E_ele_eV)
beam.emit_y = beam.emit_yn / (beam.E*1e9  / E_ele_eV)
beam.tlen=2e-3 # in m


tw0 = Twiss(beam)
exec(open('lattice_FLASH_S2E.txt'))
lat = MagneticLattice(lattice, beam.E)
tws=twiss(lat, tw0, nPoints=1000)
lat.update_transfer_maps()
tws=twiss(lat, tw0, nPoints=1000)
lat.update_transfer_maps(track_acceleration = True)

# elegant optics
file_opt='../flash/elegant_old/FLASH_S2E_twi.txt'    
dd = np.genfromtxt(file_opt)
s_dd=dd[:,0]
betax_dd=dd[:,1]
alphax_dd=dd[:,2]
betay_dd=dd[:,7]
alphay_dd=dd[:,8]
energy_dd=dd[:,13]*E_ele_eV*1e-6


############# design optics #############################
f=plt.figure();
ax = f.add_subplot(111); ax.set_xlim(0, lat.totalLen)
f.canvas.set_window_title('Betax [m]') 
p1, = plt.plot(map(lambda p: p.s, tws), map(lambda p: p.beta_x, tws), lw=2.0)
p2, = plt.plot(s_dd, betax_dd, 'g-',lw=2.0)
plt.grid(True)
plt.legend([p1,p2], [r'$\beta_x$',r'elegant'])

P0=np.loadtxt('D:/FLASH/FLASH_Simulations/s2e_elegant/InputBunches/pc1000/flash_out_200000.ast')
Q=-P0[:,7]*1e-9 #charge in nC -> in C 
xp=P0[:,:6]
np.savetxt('D:/pytest_01.ast',xp)
Pref=xp[0,5]
xp[0,5]=0
gamref=sqrt((Pref/E_ele_eV)**2+1)
xxstg=exact_xp_2_xxstg(xp,gamref)
#xxstg[:,5]=0;
#xxstg[:,4]=0;


n = len(Q)
x = [0];s = [0];
p_array = ParticleArray(n)
navi = Navigator(lattice=lat)
p_array.E = beam.E; p_array.de = 0

tws_track = []
p_array.particles[0::6]=xxstg[:,0]
p_array.particles[1::6]=xxstg[:,1]
p_array.particles[2::6]=xxstg[:,2]
p_array.particles[3::6]=xxstg[:,3]
p_array.particles[4::6]=xxstg[:,4]
p_array.particles[5::6]=xxstg[:,5]

P=p_array.particles.view() 
P.shape = len(Q),6

f=plt.figure()
plt.ion();plt.hold(False)
while navi.z0 < z_stop:
    if (z_stop-navi.z0)<dz:
        dz0=z_stop-navi.z0
    else:
        dz0=dz
    if (BC1[0]-navi.z0)<dz0 and navi.z0<BC1[0]:
        dz0=BC1[0]-navi.z0
        track(lat=lat, particle_list=p_array, dz=dz0, navi=navi)
        if SC:
            SC_xxstg_update(P,Q,p_array.E / 0.000511,dz,True,np.r_[53,53,63]);
        dz0=BC1[1]-BC1[0]
        P00=np.copy(P[:,4:]);
        track(lat=lat, particle_list=p_array, dz=dz0, navi=navi)
        compressor(P00,r56_1,t566_1,u5666_1)
        P[:,4]=P00[:,0];
    else:
        if (BC2[0]-navi.z0)<dz0 and navi.z0<BC2[0]:
            dz0=BC2[0]-navi.z0
            track(lat=lat, particle_list=p_array, dz=dz0, navi=navi)
            if SC:
                SC_xxstg_update(P,Q,p_array.E / 0.000511,dz,True,np.r_[53,53,63]);
            dz0=BC2[1]-BC2[0]
            P00=np.copy(P[:,4:]);
            track(lat=lat, particle_list=p_array, dz=dz0, navi=navi)
            compressor(P00,r56_2,t566_2,u5666_2)
            P[:,4]=P00[:,0];
        else:
            if (DL[0]-navi.z0)<dz0 and navi.z0<DL[0]:
                dz0=DL[0]-navi.z0
                track(lat=lat, particle_list=p_array, dz=dz0, navi=navi)
                if SC:
                    SC_xxstg_update(P,Q,p_array.E / 0.000511,dz,False,np.r_[53,53,63]);
                dz0=DL[1]-DL[0]
                P00=np.copy(P[:,4:]);
                track(lat=lat, particle_list=p_array, dz=dz0, navi=navi)
                compressor(P00,r56_3,t566_3,u5666_3)
                P[:,4]=P00[:,0];
            else:
                track(lat=lat, particle_list=p_array, dz=dz0, navi=navi)
                t0=time.time()
                if SC:
                    SC_xxstg_update(P,Q,p_array.E / 0.000511,dz,False,np.r_[53,53,63]);
                t1=time.time();
                print 'SC:, z=', navi.z0, ' time=',t1-t0
    x.append(p_array.particles[0])
    s.append(navi.z0)
    tw = get_envelope(p_array)
    tw.s = navi.z0
    tws_track.append( tw )
    f.add_subplot(211)
    plt.plot(P[:,0],P[:,2],'.')
    f.add_subplot(212)
    plt.plot(P[:,4],P[:,5],'.')
    plt.draw()
    plt.pause(0.1)
plt.ioff();

gamref=p_array.E*1e9/E_ele_eV
print gamref
xp=exact_xxstg_2_xp(P,gamref)
xp[0,5]=xp[0,5]+p_array.E*1e9          
np.savetxt('D:/pytest.ast',xp)

parts = p_array.array2list()



eleg_opt = np.genfromtxt('../flash/elegant_old/beam_optics.txt')
s_b=eleg_opt[:,0]
betax_b=eleg_opt[:,8]
betay_b=eleg_opt[:,11]

plt.hold(True)

plt.figure('beam envelope')
p1, = plt.plot([t.s for t in tws_track], [t.betay for t in tws_track], 'bo', lw=2)
p2,=plt.plot(s_b, betay_b, 'g-', lw=2.0)
plt.legend([p1,p2], [r'$\beta_x$', r'elegant'])
plt.show()
exit()

plt.figure('trajectory')
p1, = plt.plot([t.s for t in tws_track], [t.x for t in tws_track], 'b-', lw=2)
plt.plot([t.s for t in tws], [t.Dx * 1.e-3 for t in tws], 'b--', lw=2)
p2, = plt.plot([t.s for t in tws_track], [t.y for t in tws_track], 'g-', lw=2)
plt.plot([t.s for t in tws], [t.Dy * 1.e-3 for t in tws], 'g--', lw=2)

plt.legend([p1,p2], [r'$x$',r'$y$'])

# current projection project 

I = map(lambda p: p. tau, parts)

n, bins = np.histogram( I, 200, normed=False)
z = 1.e6* (bins[1:] - (bins[1]-bins[0])/2.0)

f=plt.figure()
f.canvas.set_window_title('Current projection') 

ax = f.add_subplot(111)
plt.bar( z , n, width = (bins[1]-bins[0]), alpha=0.2)
p1,=plt.plot( 1.e6 * bins[1:] , n, 'b-')
plt.legend([p1],['current projection (final)'])
plt.grid(True)


plt.show()

