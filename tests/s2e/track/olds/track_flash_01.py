'''
tracking with space charge
'''

import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import time

from numpy import cos, sin, log, abs, exp

from ocelot.cpbd.elements import *
from ocelot.cpbd.beam import *
from ocelot.cpbd.optics import *

from ocelot.cpbd import *
from ocelot.gui.accelerator import plot_lattice


from space_charge import SC_xxstg_update

import sys


q0=1.60217733e-19
me=9.10938188e-31
c=299792458
mue0=4*pi*1e-7   
eps0=1/(c*c*mue0)
E_ele_eV=me*c*c/q0

E00=5.109986258350895e+05

beam = Beam()
beam.sigma_E = 0.0
beam.I = 2.5e-10


beam.E = 148.3148e-3 #in GeV
beam.beta_x = 14.8821  
beam.beta_y = 18.8146   
beam.alpha_x =  -0.61309   
beam.alpha_y = -0.54569



s_start=0
s_stop=190



beam.emit_xn = 1.5e-6
beam.emit_yn = 1.5e-6

beam.emit_x = beam.emit_xn / (beam.E  / 0.000511)
beam.emit_y = beam.emit_yn / (beam.E  / 0.000511)


tw0 = Twiss(beam)


exec( open('lattice_FLASH_S2E.txt'))
lat = MagneticLattice(lattice, beam.E)

tws=twiss(lat, tw0, nPoints=1000)
lat.update_transfer_maps()
tws=twiss(lat, tw0, nPoints=1000)

lat.update_transfer_maps(track_acceleration = True)

f=plt.figure()
ax = f.add_subplot(111)
ax.set_xlim(0, lat.totalLen)

f.canvas.set_window_title('Betas [m]') 
p1, = plt.plot(map(lambda p: p.s, tws), map(lambda p: p.beta_x, tws), lw=2.0)
p2, = plt.plot(map(lambda p: p.s, tws), map(lambda p: p.beta_y, tws), lw=2.0)
plt.grid(True)

ax2 = ax.twinx()
p3, = plt.plot(map(lambda p: p.s, tws), map(lambda p: p.Dx, tws), 'r--',lw=2.0)

plt.legend([p1,p2,p3], [r'$\beta_x$',r'$\beta_y$', r'$D_x$'])

z = np.linspace(-2,22,1000)
x = 0*np.linspace(-1,1,10)
y = 0*np.linspace(-1,1,10)

    
p = Particle()
p.x = 0.
p.y = 0.
p.z = 0.0

p.xp = 0.0
p.yp = 0.
p.zp = sqrt(1.0 - p.xp**2)

p.gam = beam.E  / 0.000511



# tracking particle ensemble

n = 200000

parts = []

for i in np.arange(0,n):
    x,xp = gaussFromTwiss(beam.emit_x, beam.beta_x, beam.alpha_x)
    y,yp = gaussFromTwiss(beam.emit_y, beam.beta_y, beam.alpha_y)
    E = np.random.randn() * beam.sigma_E / beam.E
    s = 0 
    tau = np.random.randn() * 2.e-3
    p = Particle(x=x,y=y,px=xp,py=yp,s=s, tau=tau, p=E)
    parts.append(p)


parts0 = np.copy(parts)

import copy
p0 = copy.deepcopy(parts[0])

x = []
s = []
x.append(parts[0].x)
s.append(parts[0].s)


p_array = ParticleArray(len(parts))

Q0 = 1e-9 
Q = np.ones(len(parts)) * Q0 / len(parts)


#plt.figure()
#plt.plot(Q)
#plt.show()
  

p_array.list2array(parts)
navi = Navigator(lattice=lat)
p_array.E = beam.E

dz = 1.0



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

tws_track = []


z_stop =  150.0 #lat.totalLen

while navi.z0 < z_stop:
    track(lat=lat, particle_list=p_array, dz=dz, navi=navi)
    t0=time.time()
    SC_xxstg_update(p_array.particles.reshape(len(Q),6),Q,p_array.E / 0.000511,dz,False,np.r_[53,53,63]);
    t1=time.time(); print t1-t0
    print 'SC:, z=', navi.z0
    
    x.append(p_array.particles[0])
    s.append(navi.z0)
    tw = get_envelope(p_array)
    tw.s = navi.z0
    tws_track.append( tw )
        
    
parts = p_array.array2list()

plt.figure('energy')
plt.plot([t.s for t in tws_track], [t.E for t in tws_track], 'b-', lw=2)

plt.figure('beam envelope')
p1, = plt.plot([t.s for t in tws_track], [t.xx / (beam.emit_xn / (t.E/ 0.000511 ) ) for t in tws_track], 'bd-', lw=2)
plt.plot([t.s for t in tws], [t.beta_x for t in tws], 'bd--', lw=2.0)
p2, = plt.plot([t.s for t in tws_track], [t.yy / (beam.emit_yn / (t.E/ 0.000511 ) ) for t in tws_track], 'gd-', lw=2)
plt.plot([t.s for t in tws], [t.beta_y for t in tws], 'gd--', lw=2.0)
plt.legend([p1,p2], [r'$\beta_x$',r'$\beta_y$'])

plt.figure('trajectory')
p1, = plt.plot([t.s for t in tws_track], [t.x for t in tws_track], 'b-', lw=2)
plt.plot([t.s for t in tws], [t.Dx * 1.e-3 for t in tws], 'b--', lw=2)
p2, = plt.plot([t.s for t in tws_track], [t.y for t in tws_track], 'g-', lw=2)
plt.plot([t.s for t in tws], [t.Dy * 1.e-3 for t in tws], 'g--', lw=2)

plt.legend([p1,p2], [r'$x$',r'$y$'])

#plt.plot([t.s for t in tws], [t.beta_x for t in tws], 'b--', lw=2.0)


f=plt.figure()
f.canvas.set_window_title('Phase space [m]') 
ax = f.add_subplot(221)
p1, = plt.plot(map(lambda p: p.x, parts0), map(lambda p: p.px, parts0), 'g.', lw=8.0)
p2, = plt.plot(map(lambda p: p.x, parts), map(lambda p: p.px, parts), 'r.', lw=8.0)
plt.grid(True)
plt.legend([p1], [r'$x / xp$'])

#track(lat=lat, particle_list=parts, dz=2.0, navi=navi)

ax = f.add_subplot(222)
p1, = plt.plot(map(lambda p: p.y, parts0), map(lambda p: p.py, parts0), 'g.', lw=8.0)
p2, = plt.plot(map(lambda p: p.y, parts), map(lambda p: p.py, parts), 'r.', lw=8.0)
plt.grid(True)
plt.legend([p1], [r'$y / yp$'])

ax = f.add_subplot(223)
p1, = plt.plot(map(lambda p: p.tau, parts0), map(lambda p: p.p, parts0), 'g.', lw=8.0)
p2, = plt.plot(map(lambda p: p.tau, parts), map(lambda p: p.p, parts), 'r.', lw=8.0)
plt.grid(True)
plt.legend([p1], [r'$p / tau$'])




# current projection project 

I0 = map(lambda p: p. tau, parts0)
I = map(lambda p: p. tau, parts)

n0, bins0 = np.histogram( I0, 200, normed=False)
z0 = 1.e6 * (bins0[1:] - (bins0[1]-bins0[0])/2.0)

n, bins = np.histogram( I, 200, normed=False)
z = 1.e6* (bins[1:] - (bins[1]-bins[0])/2.0)


f=plt.figure()
f.canvas.set_window_title('Current projection') 
ax = f.add_subplot(211)
plt.bar( z0 , n0, width = (bins0[1]-bins0[0]), alpha=0.2)
p1,=plt.plot( 1.e6 * bins0[1:] , n0, '-')
plt.legend([p1],['current projection (initial)'])
plt.grid(True)

ax = f.add_subplot(212)
plt.bar( z , n, width = (bins[1]-bins[0]), alpha=0.2)
p1,=plt.plot( 1.e6 * bins[1:] , n, 'b-')
plt.legend([p1],['current projection (final)'])
plt.grid(True)


plt.show()
    
    