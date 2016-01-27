__author__ = 'Sergey Tomin'

from lattice_rf_red import *
from ocelot.gui.accelerator import *
from ocelot.cpbd.orbit_correction import *
from ocelot.utils.mint.machine_setup import *
from ocelot.utils.mint.flash1_interface_pydoocs import *
from ocelot.utils.mint.flash1_converter import *



filename = "test.txt"


mi = FLASH1MachineInterface()
dp = FLASH1DeviceProperties()

lat = MagneticLattice(lattice)

setup = MachineSetup(lat, mi, dp)
setup.save_lattice(filename)


# read setup file
setup.load_lattice(filename, lat)
print ("gun energy: ", lat.gun_energy, " GeV")
print ("SASE level: ", lat.sase, " uJ")
setup.convert_currents(lat, init_energy=lat.gun_energy)
lat.update_transfer_maps()


beam = Beam()
beam.E = 148.3148e-3 #in GeV ?!
beam.beta_x = 14.8821
beam.beta_y = 18.8146
beam.alpha_x =  -0.61309
beam.alpha_y = -0.54569

beam.E = lat.gun_energy

tw0 = Twiss(beam)
tws=twiss(lat, tw0)
plot_opt_func(lat, tws, top_plot=["Dx"])



