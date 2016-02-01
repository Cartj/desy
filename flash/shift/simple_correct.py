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

def show_currents( elems, alpha):
    print "******* displaying currents - START ********"
    for elem in elems:
        if elem.dI == 0:
            continue
        n = len(elem.id)
        n2 = len(str(elem.I + elem.dI))
        n3 = len(str(elem.I))
        print elem.id, " "*(10-n) + "<-- ", elem.I + elem.dI,  " "*(18-n2)+ " was = ", elem.I, " "*(18-n3) + " dI = ", elem.dI, "x", alpha
    print "******* displaying currents - END ********"

def set_currents(mi, elems, alpha):
    for elem in elems:
        if elem.dI == 0:
            continue
        n = len(elem.id)
        new_I = elem.I + elem.dI*alpha
        n2 = len(str(new_I))
        print elem.id,  " "*(10-n) + "<-- ", new_I,  " "*(18-n2)+ " was = ", elem.I
        mi.set_value(elem.mi_id, new_I)

def restore_current(mi, elems):
    for elem in elems:
        if elem.dI == 0:
            continue
        n = len(elem.id)
        print elem.id, " "*(10-n) +"<-- ", elem.I
        mi.set_value(elem.mi_id, elem.I)



filename = "lattice_calc.txt"

mi = FLASH1MachineInterface()
dp = FLASH1DeviceProperties()

lat_all = MagneticLattice(lattice)

setup = log.MachineSetup(lat_all, mi, dp)
setup.load_lattice(filename, lat_all)


lat = MagneticLattice(lattice, start=Q1DBC3_U)

orb = Orbit(lat)



resp_mat1 = Response_matrix()
resp_mat1.load("c_rmat_m_A.txt")
orb.export_response_matrix(resp_mat1)
#orb.mode = "ampere"
orb.set_ref_pos()


setup.hli.read_bpms()

orb.show_orbit("absolute orbit")

orb.minus_reference()

orb.show_orbit("relative orbit")


orb.correction()


alpha = 0.1

show_currents(orb.hcors, alpha)

inp = raw_input("Do you really want to apply currents for X:? ")
if inp == "yes":
    set_currents(mi, orb.hcors, alpha)

inp2 = raw_input("Restore orbit for X:? ")

if inp2 == "yes":
    restore_current(mi, orb.hcors)


show_currents(orb.vcors, alpha)

inp = raw_input("Do you really want to apply currents for Y:? ")
if inp == "yes":
    set_currents(mi, orb.vcors, alpha)

inp2 = raw_input("Restore orbit for Y:? ")
if inp2 == "yes":
    restore_current(mi, orb.vcors)