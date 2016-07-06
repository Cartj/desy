from ocelot.cpbd.tracking import *

from ocelot.cpbd.e_beam_params import *
from ocelot.cpbd.match import *
from ocelot.gui.accelerator import *

beam = Beam()
beam.E = 6.0
beam.sigma_E = 0.001
beam.I = 0.1

#k, betaMin, betaMax, __ = fodo_parameters(betaXmean=18.0, L=2.2, verbose = True)
#print 'fodo parameters:', k, betaMin, betaMax,
#exit(0)

from petra import *

lat = MagneticLattice(lattice, energy = beam.E)

lat_arc1 = MagneticLattice((arc1), energy = beam.E) # start at end of first straigh section (W)
lat_arc2 = MagneticLattice((arc2), energy = beam.E)
lat_sase = MagneticLattice((sase), energy = beam.E)
lat_bdc = MagneticLattice((bdc_arc3), energy = beam.E)
lat_arc3 = MagneticLattice((arc3_new), energy = beam.E)
lat_rest = MagneticLattice((rest), energy = beam.E)


lat_1 = MagneticLattice((bdc_arc3, arc3_new), energy = beam.E)
lat_2 = MagneticLattice((arc3), energy = beam.E)

def survey(lat, ang = 0.0, x0=0, z0=0):
    x = []
    z = []
    for e in lat.sequence:
        x.append(x0)
        z.append(z0)
        if e.__class__ in [Bend, SBend, RBend]:
            ang += e.angle
        x0 += e.l*cos(ang)  
        z0 += e.l*sin(ang)
    return x, z
            
x1, z1 = survey(lat_1)
x2, z2 = survey(lat_2)
x3, z3 = survey(lat_bdc)

plt.plot(x1,z1)
plt.plot(x2,z2)
plt.plot(x3,z3, lw=3)
plt.show()