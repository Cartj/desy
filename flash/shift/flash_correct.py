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


def show_currents(elems, alpha):
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


def angles2currents(lat):
    for elem in lat.sequence:

        if elem.type == "vcor":
            #print elem.id
            dI = tpk2i(elem.dev_type, elem.E, elem.angle*1000.)
            if abs(dI) > 0.005:
                elem.dI = dI
                if elem.id in ["V10ACC5", "V10ACC6"]:
                    elem.dI = dI/2.
                #print elem.id, "angle=", elem.angle, " dI = ", elem.dI, " I = ", elem.I
            else:
                elem.dI = 0.
                elem.angle = 0.
            if abs(elem.dI) > 0.5:
                print elem.id, " @@@@@@@@@@@@@@@@ HIGH CURRENT @@@@@@@@@@@@@@@ = ", elem.dI
        if elem.type == "hcor" :
            dI = tpk2i(elem.dev_type, elem.E, elem.angle*1000.)

            if abs(dI) > 0.005:# and elem.mi_id in ['H3DBC3', 'H10ACC4','H9ACC5', 'H10ACC5', 'H9ACC6', 'H10ACC6', 'H10ACC7']:
                elem.dI = dI
                #print elem.id, "angle = ", elem.angle, " dI = ", elem.dI, " I = ", elem.I
                if elem.id in ["H10ACC5", "H10ACC6"]:
                    elem.dI = dI/2.
            else:
                elem.dI = 0.
                elem.angle = 0.
            if abs(elem.dI) > 0.5:
                print elem.id, " @@@@@@@@@@@@@@@@ HIGH CURRENT @@@@@@@@@@@@@@@ = ", elem.dI

mi = FLASH1MachineInterface()
dp = FLASH1DeviceProperties()

lat_all = MagneticLattice(lattice)

setup = log.MachineSetup(lat_all, mi, dp)
#setup.save_lattice(filename="test.txt")


# read setup file
setup.load_lattice("test.txt", lat_all)
print ("gun energy: ", lat_all.gun_energy, " GeV")
print ("SASE level: ", lat_all.sase, " uJ")
setup.convert_currents(lat_all, init_energy=lat_all.gun_energy)
lat_all.update_transfer_maps()



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

setup = log.MachineSetup(lat, mi, dp)
setup.load_lattice("test.txt", lat)


tws=twiss(lat, tw0)
plot_opt_func(lat, tws, top_plot=["E"])


orb = Orbit(lat)
orb.set_ref_pos()



resp_mat = orb.linac_response_matrix(tw_init=tw0)
resp_mat = orb.measure_response_matrix(p_init=Particle(E=beam.E))
#setup.load_orbit("test.txt", lat)

setup.hli.read_bpms()

s_bpm = np.array([p.s for p in orb.bpms])
x_bpm = np.array([p.x for p in orb.bpms])
y_bpm = np.array([p.y for p in orb.bpms])

ax = plot_API(lat)
ax.set_title("absolute orbit")
ax.plot(s_bpm, x_bpm*1000.,  "ro-", label="X")
ax.plot(s_bpm, y_bpm*1000.,   "bo-", label="Y")
ax.legend()
plt.show()



orb.minus_reference()

s_bpm = np.array([p.s for p in orb.bpms])
x_bpm_b = np.array([p.x for p in orb.bpms])
y_bpm_b = np.array([p.y for p in orb.bpms])

ax = plot_API(lat)
ax.set_title("relative orbit")
ax.plot(s_bpm, x_bpm_b*1000.,  "ro-", label="X")
ax.plot(s_bpm, y_bpm_b*1000.,   "bo-", label="Y")
ax.legend()
plt.show()


orb.correction(lat)



#print "names = ", names
#print "currents = ", cur
#print "dI = ", increm
lat.update_transfer_maps()

orb.read_virtual_orbit(Particle(E=beam.E))

s_bpm = np.array([p.s for p in orb.bpms])
x_bpm = np.array([p.x for p in orb.bpms])
y_bpm = np.array([p.y for p in orb.bpms])

p = Particle()
p.E = beam.E
plist = lattice_track(lat, p, order=1)

x = np.array([p.x for p in plist])
y = np.array([p.y for p in plist])
s = np.array([p.s for p in plist])

ax = plot_API(lat)
ax.set_title("corrected orbit")
ax.plot(s_bpm, (x_bpm + x_bpm_b)*1000.,   "ro-", label="X")
ax.plot(s_bpm, (y_bpm + y_bpm_b)*1000.,   "bo-", label="Y")
ax.legend()
plt.show()


angles2currents(lat)

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
