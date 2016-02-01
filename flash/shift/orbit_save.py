__author__ = 'tomins'
import os, sys

from pylab import *
from time import sleep, time
from ocelot.utils.mint.flash1_interface_pydoocs import FLASH1MachineInterface
from desy.flash.lattices.lattice_rf_red import *

sys.path.append('../')


lat = MagneticLattice(lattice)

#bpms = []
#for elem in lat.sequence:
#    if elem.type == "monitor":
#        bpms.append(elem.id)
bpms = ['1GUN', '3GUN', '9ACC1', '2UBC2', '1DBC2', '3DBC2', '5DBC2', '7DBC2', '9DBC2', '11DBC2',
        '9ACC2', '9ACC3', '1UBC3', '2UBC3', '1DBC3', '3DBC3', '9ACC4', '9ACC5', '9ACC6', '11ACC7',
        '15ACC7', '19ACC7', '1TCOL', '6TCOL', '8TCOL', '3ECOL', '5ECOL', '2ORS', '7ORS', '9ORS',
        '12ORS', '1SFUND2', '1SFUND3', '1SFUND4', '1SFELC', '1SMATCH', '6SMATCH', '13SMATCH', '14SMATCH',
        '2UND1', '4UND1', '5UND1', '2UND2', '4UND2', '5UND2', '2UND3', '4UND3', '5UND3', '2UND4', '4UND4',
        '5UND4', '2UND5', '4UND5', '5UND5', '2UND6', '4UND6', '5UND6']

mi = FLASH1MachineInterface()

def print_string(values):
    print str(time())+"\t"+"\t".join([str(v) for v in values])


print "#time" + "\t" + "\t".join([str(v) for v in bpms]) + "\t" + "plane"
while True:
    sleep(1)
    #print time()
    X, Y = mi.get_bpms_xy(bpms)
    values_x = X #[mi.get_value(name) for name in names]
    values_x.append( "X")

    print_string(values_x)
    values_y = Y #[mi.get_value(name) for name in names]
    values_y.append( "Y")
    print_string(values_y)