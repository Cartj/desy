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


filename = "test.txt"
rmat_filename = "test_rmatrix.txt"


mi = FLASH1MachineInterface()
dp = FLASH1DeviceProperties()



lat_all = MagneticLattice(lattice)

setup = log.MachineSetup(lat_all, mi, dp)
setup.read_save_lattice(filename=filename)
"""
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
"""


lat = MagneticLattice(lattice, start=Q1DBC3_U)
#S2ECOL.k2 = 0.
#S6ECOL.k2 = 0.
#setup = log.MachineSetup(lat, mi, dp)
#setup.load_lattice(filename, lat)


#tws=twiss(lat, tw0)
#plot_opt_func(lat, tws, top_plot=["Dx"])


horizantal = [#'H3DBC3',
              #'H10ACC4', 'H10ACC5', 'H10ACC6', 'H10ACC7', 'H18ACC7',
              #'H1TCOL', 'H4TCOL',
              #'H8TCOL',
              #'H2ECOL', 'H4ECOL', 'H6ECOL',                     # in dogleg
              #'H5ORS', 'H10ORS', 'H3SFELC', 'H4SFELC',
              'H10SMATCH', 'H12SMATCH'
              ]
hcor_und = ["H3UND1", "H3UND2", "H3UND3", "H3UND4", "H3UND5", "H3UND6"]

vertical = [#'V3DBC3',
            #'V10ACC4' 'V10ACC5', 'V10ACC6', 'V10ACC7',
            #'V1TCOL', 'V2TCOL', 'V4TCOL',
            #'V8TCOL',
            #'V4ECOL',                                                  #in dogleg
            #'V5ORS', 'V6.4ORS', 'V7ORS', 'V9ORS', 'V11ORS', 'V12ORS',
            #'V2SFELC', 'V4SFELC', 'V6SFELC',
            'V7SMATCH', 'V14SMATCH'
            ]

bpms = [#'1DBC3', '3DBC3', '9ACC4', '9ACC5', '9ACC6', '11ACC7', '15ACC7', '19ACC7',
        # '1TCOL', '6TCOL', '8TCOL',
         #'3ECOL', '5ECOL',                              # dogleg
        #'2ORS', '7ORS', '9ORS', '12ORS',
        #'1SFUND2', '1SFUND3', '1SFUND4', '1SFELC', '1SMATCH', '6SMATCH',
        '13SMATCH', '14SMATCH', '5UND1', '5UND2', '5UND3', '5UND4', '5UND5', '5UND6'  #undulator section
        ]

V7SMATCH.dI = 0.1
#rm = Response_matrix()
#rm.load(rmat_filename)
#print rm.matrix
orb = Orbit(lat)

#rmatrix = orb.measure_response_matrix(p_init=Particle(E=beam.E))
#rmatrix.save("test_r.txt")

#rmatrix.extract(cor_list=horizantal, bpm_list=bpms)

orb.create_COR(cor_list=np.append(horizantal, vertical))

orb.create_BPM(bpm_list=bpms)
#orb.export_response_matrix(rmatrix)
#rmatrix = orb.response_matrix(TestInterface(), dp, timeout=0.5, delta_i=0.05)
rmatrix = orb.response_matrix(mi, dp, timeout=0.5, delta_i=0.05)
rmatrix.save(rmat_filename)

rmatrix.show()
print
print rmatrix.matrix

#H10SMATCH.angle = 0.001

#orb.read_virtual_orbit(Particle(E=beam.E))
#plt.plot([b.s for b in orb.bpms], [b.x for b in orb.bpms], "ro-")
#orb.correction(Particle(E=beam.E))
#orb.read_virtual_orbit(Particle(E=beam.E))
#plt.plot([b.s for b in orb.bpms], [b.x for b in orb.bpms], "bo-")
#plt.show()

