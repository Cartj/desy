__author__ = 'tomins'
import os, sys

from pylab import *
from time import sleep, time
from ocelot.utils.mint.flash1_interface_pydoocs import FLASH1MachineInterface
from desy.flash.lattices.lattice_rf_red import *

sys.path.append('../')


lat = MagneticLattice(lattice)

bpms = []
for elem in lat.sequence:
    if elem.type == "monitor":
        bpms.append(elem.id)


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