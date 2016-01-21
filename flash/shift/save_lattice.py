__author__ = 'Sergey Tomin'

from lattice_rf_mod import *
from ocelot.gui.accelerator import *
from ocelot import *
#from ocelot.gui import *
#from ocelot.cpbd.errors import *
#from ocelot.cpbd.track import *
from ocelot.cpbd.orbit_correction import *
#from copy import copy
from high_level_mint_flash import *
#import pyqtgraph as pg
from ocelot.utils.mint.flash1_interface_pydoocs import *
#from flash1_virtual_interface import *
import pickle
from converter import *
from ocelot.rad.undulator_params import *
import copy
import machine_setup as log

mi = FLASH1MachineInterface()
dp = FLASH1DeviceProperties()

lat = MagneticLattice(lattice)
read_cavs(lat, mi)
read_quads(lat, mi, dp)
read_bends(lat, mi, dp)
read_sexts(lat, mi)
read_cors(lat, mi)
read_bpms(lat, mi)


setup = log.MachineSetup()
setup.save_lattice(lat, "init.txt")

setup.load_lattice("init.txt",lat)

setup.convert_currents(lat, init_energy=0.0053)

lat.update_transfer_maps()


beam = Beam()
beam.E = 148.3148e-3 #in GeV ?!
beam.beta_x = 14.8821
beam.beta_y = 18.8146
beam.alpha_x =  -0.61309
beam.alpha_y = -0.54569

beam.E = 0.0053

tw0 = Twiss(beam)
tws=twiss(lat, tw0)
plot_opt_func(lat, tws, top_plot=["Dx"])



