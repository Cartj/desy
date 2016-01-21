__author__ = 'Sergey Tomin'

from lattice_rf_mod import *
from ocelot.gui.accelerator import *
from ocelot import *
from ocelot.gui import *
from ocelot.cpbd.errors import *
from ocelot.cpbd.track import *
from ocelot.cpbd.orbit_correction import *
from copy import copy
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

beam = Beam()
beam.E = 450e-3 #in GeV ?!
#beam.beta_x = 14.8821
#beam.beta_y = 18.8146
#beam.alpha_x =  -0.61309
#beam.alpha_y = -0.54569
beam.beta_x = 12.8186434746
beam.alpha_x = -1.71640739021
beam.beta_y =  34.1757857554
beam.alpha_y = -1.55018161694

tw0 = Twiss(beam)

lat = MagneticLattice(lattice, start=Q1DBC3_U)
tws=twiss(lat, tw0)
plot_opt_func(lat, tws, top_plot=["Dx"])


setup = log.MachineSetup()
#setup.save_lattice(lat, "init.txt")
lat_all = MagneticLattice(lattice)
setup.load_lattice("init.txt", lat_all)

setup.convert_currents(lat_all, init_energy=0.0053)

lat.update_transfer_maps()

lat = MagneticLattice(lat_all.sequence, start=Q1DBC3_U)
tws=twiss(lat, tw0)
plot_opt_func(lat, tws, top_plot=["Dx"])