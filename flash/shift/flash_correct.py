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
plot_opt_func(lat, tws, top_plot=["Dx"])


orb = Orbit(lat)
#orb.set_ref_pos()



resp_mat = orb.linac_response_matrix(tw_init=tw0)

setup.load_orbit("test.txt", lat)

s_bpm = np.array([p.s for p in orb.bpms])
x_bpm = np.array([p.x for p in orb.bpms])
y_bpm = np.array([p.y for p in orb.bpms])

ax = plot_API(lat)
ax.plot(s_bpm, x_bpm*1000.,  "ro-", label="X")
ax.plot(s_bpm, y_bpm*1000.,   "bo-", label="Y")
plt.show()



orb.minus_reference()

s_bpm = np.array([p.s for p in orb.bpms])
x_bpm_b = np.array([p.x for p in orb.bpms])
y_bpm_b = np.array([p.y for p in orb.bpms])

ax = plot_API(lat)
ax.plot(s_bpm, x_bpm_b*1000.,  "ro-", label="X")
ax.plot(s_bpm, y_bpm_b*1000.,   "bo-", label="Y")
plt.show()


orb.correction(lat)
increm = []
cur = []
names = []

for elem in lat.sequence:

    if elem.type == "vcor":
        #print elem.id
        dI = tpk2i(elem.dev_type, elem.E, elem.angle*1000.)
        if abs(dI) > 0.005:
            elem.dI = dI
            #print elem.id, "angle=", elem.angle, " dI = ", elem.dI, " I = ", elem.I
        else:
            elem.dI = 0.
            elem.angle = 0.
    if elem.type == "hcor" :
        dI = tpk2i(elem.dev_type, elem.E, elem.angle*1000.)

        if abs(dI) > 0.005:# and elem.mi_id in ['H3DBC3', 'H10ACC4','H9ACC5', 'H10ACC5', 'H9ACC6', 'H10ACC6', 'H10ACC7']:
            elem.dI = dI
            #print elem.id, "angle = ", elem.angle, " dI = ", elem.dI, " I = ", elem.I
            increm.append(elem.dI)
            cur.append(elem.I)
            names.append(elem.id)
        else:
            elem.dI = 0.
            elem.angle = 0.
        if abs(dI) > 0.5:
            print elem.id, " @@@@@@@@@@@@@@@@ HIGH CURRENT @@@@@@@@@@@@@@@ = ", elem.dI
#print
#print "names = ", names
#print "currents = ", cur
#print "dI = ", increm
lat.update_transfer_maps()

orb.read_virtual_orbit(lat, Particle(E=beam.E))

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
ax.plot(s_bpm, x_bpm*1000.,  "ro-", label="X")
ax.plot(s, x*1000.,  "r-", label="X")
ax.plot(s_bpm, x_bpm_b*1000.,   "bo-", label="Y")
plt.show()

ax = plot_API(lat)
ax.plot(s_bpm, y_bpm*1000.,  "ro-", label="X")
ax.plot(s, y*1000.,  "r-", label="X")
ax.plot(s_bpm, y_bpm_b*1000.,   "bo-", label="Y")
plt.show()

alpha = 0.1

for hcor in orb.hcors:
    print hcor.id, "<-- ", hcor.I + hcor.dI, " was = ", hcor.I, " dI = ", hcor.dI, "x", alpha


inp = raw_input("Do you really want to apply currents for X:? ")
if inp == "yes":
    for hcor in orb.hcors:
        new_I = hcor.I + hcor.dI*alpha
        print hcor.id, "<-- ", new_I, hcor.I
        mi.set_value(hcor.mi_id, new_I)

inp2 = raw_input("Restore orbit for X:? ")

if inp2 == "yes":
    for hcor in orb.hcors:
        new_I = hcor.I + hcor.dI*alpha
        print hcor.id, "<-- ", hcor.I
        mi.set_value(hcor.mi_id, hcor.I)

for vcor in orb.hcors:
    print vcor.id, "<-- ", vcor.I + vcor.dI, " was = ", vcor.I, " dI = ", vcor.dI, "x", alpha

inp = raw_input("Do you really want to apply currents for Y:? ")
if inp == "yes":

    for vcor in orb.vcors:
        new_I = vcor.I + vcor.dI*alpha
        print vcor.id, "<-- ", new_I, vcor.I
        mi.set_value(vcor.mi_id, new_I)

inp2 = raw_input("Restore orbit for Y:? ")
if inp2 == "yes":
    for vcor in orb.vcors:
        new_I = vcor.I + vcor.dI*alpha
        print vcor.id, "<-- ", vcor.I
        mi.set_value(vcor.mi_id, vcor.I)
