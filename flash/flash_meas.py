__author__ = 'Sergey Tomin'
from lattice_rf_mod import *
from ocelot.gui.accelerator import *
from ocelot import *
from ocelot.gui import *
from ocelot.cpbd.errors import *
from ocelot.cpbd.track import *
from ocelot.cpbd.orbit_correction import *
from copy import copy
#import pyqtgraph as pg
from ocelot.utils.mint.flash1_interface_pytine import *

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

tw0 = Twiss(beam)

lat = MagneticLattice(lattice, start=STARTACC39)
tws=twiss(lat, tw0)
plot_opt_func(lat, tws, top_plot=["Dx"])

orb = Orbit(lat)



mi = FLASH1MachineInterface()

for bpm in orb.bpms:
    name = bpm.id.replace("BPM", "")
    print(name)
    try:
        print(bpm.id, name, mi.get_bpms_XY([name]))
    except:
        print(name, "  CAN MOT FIND")

for elem in lat.sequence:
    if elem.type == "quadrupole":
        name = elem.id
        print(name)
        try:
            print(elem.id, name, mi.get_quads_current([name]))
        except:
            print(name, "  CAN MOT FIND")