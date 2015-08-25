'''
csr
'''

import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

from numpy import cos, sin, log, abs, exp

from ocelot.cpbd.elements import *
from ocelot.cpbd.beam import *
from ocelot.cpbd.optics import *
from ocelot.cpbd import *
from ocelot.gui.accelerator import plot_lattice




def apply_sc(parts):
    I = map(lambda p: p. tau, parts)
    n, bins = np.histogram( I, nhist, normed=False)

    z = 1.e6 * (bins[1:] - (bins[1]-bins[0])/2.0)
    
    n_smooth = 15
    kernel_n = np.linspace(1,n_smooth,n_smooth) 
    kernel = np.exp(-(kernel_n-1)**2 / 24**2) / n_smooth

    I_smooth = np.convolve(n, kernel, mode='same')

    
'''
lattice and beam definition
'''
    
rfc1 = Drift(l = 5.0) #Cavity(l=5.0, f=1.3 * GHz, v=25.5 * MV, id='rfc1')
d0 = Drift(l = 2.0)
e1 = RBend(angle = 0.1, l = 2.0)
d1 = Drift(l = 1.0)
e2 = RBend(angle = -0.1, l = 2.0)
d2 = Drift(l = 1.0)

beam = Beam()
beam.E = 1.0 # GeV
beam.sigma_E = 1.0e-3 # GeV
beam.beta_x = 10
beam.beta_y = 20
beam.emit_x = 1.e-6
beam.emit_y = 1.e-6

lat = MagneticLattice((rfc1, d0, e1, d1, e2, (d2,)*5, e2, d2, e1,d1))


'''
twiss calculation
'''

tw0 = Twiss(beam)
tws=twiss(lat, tw0, nPoints = 1000)

f=plt.figure()
ax = f.add_subplot(111)
ax.set_xlim(0, lat.totalLen)

f.canvas.set_window_title('Betas [m]') 
p1, = plt.plot(map(lambda p: p.s, tws), map(lambda p: p.beta_x, tws), lw=2.0)
p2, = plt.plot(map(lambda p: p.s, tws), map(lambda p: p.beta_y, tws), lw=2.0)
plt.grid(True)

ax2 = ax.twinx()
p3, = plt.plot(map(lambda p: p.s, tws), map(lambda p: p.Dx, tws), 'r--',lw=2.0)
plot_lattice(lat, ax2, alpha=0.5)

plt.legend([p1,p2,p3], [r'$\beta_x$',r'$\beta_y$', r'$D_x$'])


'''
tracking
'''

n = 5000

parts = []

for i in np.arange(0,n):
    x,xp = gaussFromTwiss(beam.emit_x, beam.beta_x, beam.alpha_x)
    y,yp = gaussFromTwiss(beam.emit_y, beam.beta_y, beam.alpha_y)
    E = np.random.randn() * beam.sigma_E/ beam.E
    s = 0
    tau = np.random.randn() * 1.e-6
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
p_array.list2array(parts)
navi = Navigator(lattice=lat)


dz_csr = 0.1
nhist = 200

while navi.z0 < lat.totalLen:
    track(lat=lat, particle_list=p_array, dz=dz_csr, navi=navi)
    x.append(p_array.particles[0])
    s.append(navi.z0)
    
    # apply space charge
    apply_sc(parts)
    
out_file = open('dump.txt', 'w')    
for i in xrange(p_array.size()):
    out_file.write(str(p_array[i].x) + '\t' + str(p_array[i].y) +'\n')
    
out_file.close()        
    
parts = p_array.array2list()

#plt.plot(s, x, 'r--', lw=2.0)


#navi = Navigator(lattice=lat)

if True:
    f=plt.figure()
    f.canvas.set_window_title('Phase space [m]') 
    ax = f.add_subplot(221)
    p1, = plt.plot(map(lambda p: p.x, parts0), map(lambda p: p.px, parts0), 'g.', lw=8.0)
    p2, = plt.plot(map(lambda p: p.x, parts), map(lambda p: p.px, parts), 'r.', lw=8.0)
    plt.grid(True)
    plt.legend([p1], [r'$x / xp$'])
    
    #track(lat=lat, particle_list=parts, dz=20.0, navi=navi)
    
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
p1,=plt.plot( 1.e6 * bins0[1:] , n0, '.-')
plt.legend([p1],['current projection (initial)'])
plt.grid(True)

ax = f.add_subplot(212)
plt.bar( z , n, width = (bins[1]-bins[0]), alpha=0.2)
p1,=plt.plot( 1.e6 * bins[1:] , n, 'b.-')
plt.legend([p1],['current projection (final)'])
plt.grid(True)

n_smooth = 15
kernel_n = np.linspace(1,n_smooth,n_smooth) 
kernel = np.exp(-(kernel_n-1)**2 / 24**2) / n_smooth

I_smooth = np.convolve(n, kernel, mode='same')

p2,=plt.plot(z ,I_smooth,'g-', lw=3)
plt.grid(True)




plt.show()
    
    