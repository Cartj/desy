__author__ = 'Sergey Tomin'

from ocelot.cpbd.beam import *
from ocelot.common.globals import *
from ocelot.cpbd.elements import *
from ocelot.cpbd.optics import *
from ocelot.gui.accelerator import *
exec( open("lattice_FLASH_S2E.py" ))

beam = Beam()
beam.E = 148.3148e-3 #in GeV ?!
beam.beta_x = 14.8821
beam.beta_y = 18.8146
beam.alpha_x =  -0.61309
beam.alpha_y = -0.54569
beam.emit_xn = 1.5e-6
beam.emit_yn = 1.5e-6
beam.emit_x = beam.emit_xn / (beam.E / m_e_GeV)
beam.emit_y = beam.emit_yn / (beam.E / m_e_GeV)
beam.tlen=2e-3 # in m


tw0 = Twiss(beam)

lat = MagneticLattice(lattice)
tws=twiss(lat, tw0, nPoints=None)

plot_opt_func(lat, tws, top_plot = ["E"])
plt.show()