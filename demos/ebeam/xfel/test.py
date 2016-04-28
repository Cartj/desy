# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 15:46:05 2016

@author: tomins
"""

import numpy as np
from ocelot import *
from ocelot.cpbd.high_order import *
from ocelot.gui import *
from ocelot.adaptors import *
from ocelot.cpbd.track import*

D1 = Drift(l=1., id="D1")
D2 = Drift(l=2.5, id="D2")

B1 = RBend(l = 0.3, angle=200e-6, id="B1")
B2 = RBend(l = 0.3, angle=-200e-6, id="B2")

Q1 = Quadrupole(l=0.3, k1=2.5*0, id="Q1")

lattice = [D1, B1, D2, Q1, D2, B2, D1]

beam = Beam()
beam.E = 17.5 #in GeV ?!

beam.beta_x = 14.8821
beam.beta_y = 18.8146
beam.alpha_x =  -0.61309
beam.alpha_y = -0.54569
beam.emit_xn = 1.5e-6
beam.emit_yn = 1.5e-6
beam.emit_x = beam.emit_xn / (beam.E / m_e_GeV)
beam.emit_y = beam.emit_yn / (beam.E / m_e_GeV)


tw0 = Twiss(beam)

lat = MagneticLattice(lattice)
tws=twiss(lat, tw0, nPoints=None)

plot_opt_func(lat, tws, top_plot=["Dx"])

#for i in range(10):
#    Q1.k1 = -5+i
#    lat.update_transfer_maps
#    print("Q1.k1 = ", Q1.k1, "  R56 = ", lattice_transfer_map(lat, energy=beam.E)[4,5])

print("Q1.k1 = ", Q1.k1, "  R56 = ", lattice_transfer_map(lat, energy=beam.E)[4,5])

p_list1 = lattice_track(lat, Particle(p=0.001), order=2)
p_list2 = lattice_track(lat, Particle(p=-0.001), order=2)
f3, ax3 = plt.subplots(1, 1, sharey=False)
ax3.plot([p.s for p in p_list1], [p.x for p in p_list1])
ax3.plot([p.s for p in p_list2], [p.x for p in p_list2])


#Q1.k1 = 0.
#lat.update_transfer_maps

p_array, charge_array = astraBeam2particleArray(filename='../flash/elegant_files/flash_out_200000.ast')


f, (ax1, ax2) = plt.subplots(1, 2, sharey=False)
ax1.plot(p_array.particles[4::6], p_array.particles[5::6], 'r.')

ax2.plot(p_array.particles[0::6], p_array.particles[1::6], 'r.')

navi = Navigator()
for elem in lat.sequence:
    track(lat=lat, particle_list=p_array, dz=elem.l, navi=navi, order=1)


ax1.plot(p_array.particles[4::6], p_array.particles[5::6], 'b.')

ax2.plot(p_array.particles[0::6], p_array.particles[1::6], 'b.')
plt.show()
    
    
    