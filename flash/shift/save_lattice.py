__author__ = 'Sergey Tomin'

from desy.flash.lattices.lattice_rf_mod import *
from ocelot.cpbd.orbit_correction import *
from ocelot.mint.flash1_converter import *
from ocelot.mint.flash1_interface import *
from ocelot.mint.machine_setup import *

if len(sys.argv)>1:
    filename = sys.argv[1]
else:
    filename = "test.txt"

mi = FLASH1MachineInterface()
dp = FLASH1DeviceProperties()

lat = MagneticLattice(lattice)

setup = MachineSetup(lat, mi, dp)
setup.read_save_lattice(filename)


# read setup file
setup.load_lattice(filename, lat)
print ("gun energy: ", lat.gun_energy, " GeV")
print ("SASE level: ", lat.sase, " uJ")
setup.convert_currents(lat, init_energy=lat.gun_energy)
lat.update_transfer_maps()


beam = Beam()
#beam.E = 148.3148e-3 #in GeV ?!
#7.70182371485 7.77436018811 3.49750217404 3.56720701135
#beam.beta_x = 14.8821
#beam.beta_y = 18.8146
#beam.alpha_x =  -0.61309
#beam.alpha_y = -0.54569

beam.E = lat.gun_energy
beam.beta_x = 8.66
beam.beta_y = 8.79
beam.alpha_x =  3.9
beam.alpha_y = 4.

tw0 = Twiss(beam)
tws=twiss(lat, tw0)
plot_opt_func(lat, tws, top_plot=["E"])



