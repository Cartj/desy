__author__ = 'Sergey Tomin'

from desy.flash.lattices.lattice_rf_red import *
from ocelot import *
from ocelot.cpbd.orbit_correction import *

beam = Beam()
"""
beam.E = 148.3148e-3
beam.beta_x = 14.8821
beam.beta_y = 18.8146
beam.alpha_x =  -0.61309
beam.alpha_y = -0.54569
lat = MagneticLattice(lattice, start=STARTACC39)
"""

beam.E = 0.0053
beam.beta_x = 8.66
beam.beta_y = 8.79
beam.alpha_x =  3.9
beam.alpha_y = 4.
lat = MagneticLattice(lattice)



tw0 = Twiss(beam)

tws=twiss(lat, tw0, nPoints=None)
plot_opt_func(lat, tws, top_plot=["E"])

for elem in lat.sequence:
    if elem.type == "monitor":
        print ("'",elem.id,"'"," ",)