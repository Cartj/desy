__author__ = 'Sergey Tomin'
import sys
print sys.path
from desy.flash.lattices.lattice_rf_red import *
#from ocelot.gui.accelerator import *
from ocelot.gui import *
from ocelot.cpbd.orbit_correction import *
from ocelot.utils.mint.flash1_interface_pydoocs import *
#from flash1_virtual_interface import *
from ocelot.utils.mint.flash1_converter import *
from ocelot.rad.undulator_params import *
from ocelot.utils.mint import machine_setup as log
from ocelot.utils.mint.mint import TestInterface


#filename = "test.txt"
rmat_filename = "rmatrix_new2.txt"


mi = FLASH1MachineInterface()
dp = FLASH1DeviceProperties()



lat_all = MagneticLattice(lattice)

setup = log.MachineSetup(lat_all, mi, dp)
setup.read_save_lattice(filename="lattice_test.txt")



lat = MagneticLattice(lattice, start=Q1DBC3_U)



horizantal = ['H3DBC3',
              'H10ACC4', 'H10ACC5', 'H10ACC6', 'H10ACC7', 'H18ACC7',
              'H1TCOL', 'H4TCOL',
              'H8TCOL',
              'H2ECOL', 'H4ECOL', 'H6ECOL',                     # in dogleg
              'H5ORS', 'H10ORS', 'H3SFELC', 'H4SFELC',
              'H10SMATCH', 'H12SMATCH'
              ]

hcor_und = ["H3UND1", "H3UND2", "H3UND3", "H3UND4", "H3UND5", "H3UND6"]

vertical = ['V3DBC3',
            'V10ACC4' 'V10ACC5', 'V10ACC6', 'V10ACC7',
            'V1TCOL', 'V2TCOL', 'V4TCOL',
            'V8TCOL',
            'V4ECOL',                                                  #in dogleg
            'V10ORS', 
#'V6.4ORS', 'V7ORS', 
'V9ORS', 'V11ORS', 'V12ORS',
            'V2SFELC', 'V4SFELC', 'V6SFELC',
            'V7SMATCH', 'V14SMATCH'
            ]

bpms = [#'1DBC3', '3DBC3', '9ACC4', '9ACC5', '9ACC6', '11ACC7', '15ACC7', '19ACC7',
        # '1TCOL', '6TCOL', '8TCOL',
         '3ECOL', '5ECOL',                              # dogleg
        '2ORS', '7ORS', '9ORS', '12ORS',
        '1SFUND2', '1SFUND3', '1SFUND4', '1SFELC', '1SMATCH', '6SMATCH',
        '13SMATCH', '14SMATCH', '5UND1', '5UND2', '5UND3', '5UND4', '5UND5', '5UND6'  #undulator section
        ]
bpm_extr = ['2UND1', '4UND1', '2UND2', '4UND2', '2UND3', '4UND3', '2UND4', '4UND4', '2UND5', '4UND5', '2UND6', '4UND6']


#V7SMATCH.dI = 0.1
H3DBC3.dI = 0.01
H3DBC3.dI = 0.01
H10ACC4.dI = 0.2
V10ACC4.dI = 0.2
H10ACC5.dI = 0.2
V10ACC5.dI = 0.2

H10ACC6.dI = 0.2
V10ACC6.dI = 0.2
H10ACC7.dI = 0.2
V10ACC7.dI = 0.2

H18ACC7.dI = 0.2

H1TCOL.dI = 0.02
H4TCOL.dI = 0.02

V1TCOL.dI = 0.02
V2TCOL.dI = 0.02
V4TCOL.dI = 0.02

H2ECOL.dI = 0.02
H8TCOL.dI = 0.01
H4ECOL.dI = 0.01
V8TCOL.dI = 0.01
V4ECOL.dI = 0.01

H3UND1.dI = 0.5
H3UND2.dI = 0.5
H3UND3.dI = 0.5
H3UND4.dI = 0.5
H3UND5.dI = 0.5
H3UND6.dI = 0.5


orb = Orbit(lat)

orb.create_COR(cor_list=np.append(horizantal+hcor_und, vertical))

orb.create_BPM(bpm_list=bpms)

#rmatrix = orb.response_matrix(TestInterface(), dp, timeout=0.5, delta_i=0.05)
rmatrix = orb.response_matrix(mi, dp, timeout=5, delta_i=0.05)
rmatrix.save(rmat_filename)

rmatrix.show()
print
print rmatrix.matrix



