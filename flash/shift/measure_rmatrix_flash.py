__author__ = 'Sergey Tomin'

from desy.flash.lattices.lattice_rf_red import *
from ocelot.gui.accelerator import *
from ocelot.gui import *
from ocelot.cpbd.orbit_correction import *
from ocelot.utils.mint.flash1_interface_pydoocs import *
#from flash1_virtual_interface import *
from ocelot.utils.mint.flash1_converter import *
from ocelot.rad.undulator_params import *
from ocelot.utils.mint import machine_setup as log
from ocelot.utils.mint.mint import TestInterface


filename = "orbit1.txt"
rmat_filename = "test_rmatrix.txt"


mi = FLASH1MachineInterface()
dp = FLASH1DeviceProperties()

lat_all = MagneticLattice(lattice)

setup = log.MachineSetup(lat_all, mi, dp)
#setup.read_save_lattice(filename=filename)
# read setup file
setup.load_lattice(filename, lat_all)
setup.convert_currents(lat_all, init_energy=lat_all.gun_energy)
lat_all.update_transfer_maps()

print ("gun energy: ", lat_all.gun_energy, " GeV")
print ("SASE level: ", lat_all.sase, " uJ")




#print "get alarms = ", mi.get_alarms()
beam = Beam()
beam.E = Q1DBC3_U.E
#beam.beta_x = 14.8821
#beam.beta_y = 18.8146
#beam.alpha_x =  -0.61309
#beam.alpha_y = -0.54569
beam.beta_x = 12.8186434746
beam.alpha_x = -1.71640739021
beam.beta_y =  34.1757857554
beam.alpha_y = -1.55018161694

print "starting energy = ", beam.E
tw0 = Twiss(beam)

lat = MagneticLattice(lattice, start=Q1DBC3_U)
#S2ECOL.k2 = 0.
#S6ECOL.k2 = 0.
setup = log.MachineSetup(lat, mi, dp)
setup.load_lattice(filename, lat)


tws=twiss(lat, tw0)
plot_opt_func(lat, tws, top_plot=["Dx"])

orb = Orbit(lat)

rmatrix = orb.response_matrix(TestInterface(), dp)
rmatrix.save(rmat_filename)

rmatrix.show()
