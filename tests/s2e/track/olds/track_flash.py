'''
tracking with space charge
'''
import time

import matplotlib.pyplot as plt
from PhysConsts import *
from space_charge import *

from ocelot import MagneticLattice
from ocelot.cpbd.optics import *


def get_envelope(p_array):
    tws = Twiss()
    x = p_array.x()
    px = p_array.px()
    tws.xx = np.mean(x*x)
    tws.xxp = np.mean(x*px)
    tws.pxpx = np.mean(px*px)
    y = p_array.y()
    py = p_array.py()
    tws.yy = np.mean(y*y)
    tws.yyp = np.mean(y*py)
    tws.pypy = np.mean(py*py)
    tws.x = np.mean(x)
    tws.y = np.mean(y)
    tws.p = np.mean( p_array.p())
    tws.E = p_array.E
    tws.de = p_array.de
    return tws

BC2=(6.5708,10.818543701164369)

dz = 1.0
z_stop =   BC2[1] #after BC2


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

############# design optics #############################
f=plt.figure();
ax = f.add_subplot(111); ax.set_xlim(0, lat.totalLen)
f.canvas.set_window_title('Betas [m]') 
p1, = plt.plot(map(lambda p: p.s, tws), map(lambda p: p.beta_x, tws), lw=2.0)
p2, = plt.plot(map(lambda p: p.s, tws), map(lambda p: p.beta_y, tws), lw=2.0)
plt.grid(True)
ax2 = ax.twinx()
p3, = plt.plot(map(lambda p: p.s, tws), map(lambda p: p.Dx, tws), 'r--',lw=2.0)
plt.legend([p1,p2,p3], [r'$\beta_x$',r'$\beta_y$', r'$D_x$'])


P0=np.loadtxt('D:/FLASH/FLASH_Simulations/s2e_elegant/InputBunches/pc1000/flash_out_20000.ast')
Q=-P0[:,7]*1e-9 #charge in nC -> in C 
xp=P0[:,:6]
#######################
#xp[:,2]=-xp[:,2]
#######################
np.savetxt('D:/pytest_01.ast',xp)
Pref=xp[0,5]
xp[0,5]=0
gamref=sqrt((Pref/E_ele_eV)**2+1)
xxstg=exact_xp_2_xxstg(xp,gamref)

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
        dz=z_stop-navi.z0
    track(lat=lat, particle_list=p_array, dz=dz, navi=navi)
    Cavity
    t0=time.time()
    #SC_xxstg_update(P,Q,p_array.E / 0.000511,dz,False,np.r_[53,53,63]);
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
plt.ioff();plt.show()  

gamref=p_array.E*1e9/E_ele_eV
print gamref
xp=exact_xxstg_2_xp(P,gamref)
xp[0,5]=xp[0,5]+p_array.E*1e9          
np.savetxt('D:/pytest_2.ast',xp)

