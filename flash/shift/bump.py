__author__ = 'Sergey Tomin'

from lattice_rf_mod import *
from ocelot.gui.accelerator import *
from ocelot import *
from ocelot.gui import *
from ocelot.cpbd.errors import *
from ocelot.cpbd.track import *
from ocelot.cpbd.orbit_correction import *
from copy import copy
from high_level_mint_flash import *
#import pyqtgraph as pg
from ocelot.utils.mint.flash1_interface_pydoocs import *
#from flash1_virtual_interface import *
import pickle
from converter import *
from ocelot.rad.undulator_params import *
import copy
import machine_setup as log
mi = FLASH1MachineInterface()
dp = FLASH1DeviceProperties()

print "SASE=", mi.get_sase()
print "get alarms = ", mi.get_alarms()
beam = Beam()
beam.E = 450e-3 #in GeV ?!
#beam.beta_x = 14.8821
#beam.beta_y = 18.8146
#beam.alpha_x =  -0.61309
#beam.alpha_y = -0.54569
beam.beta_x = 12.8186434746
beam.alpha_x = -1.71640739021
beam.beta_y =  34.1757857554
beam.alpha_y = -1.55018161694

tw0 = Twiss(beam)

lat = MagneticLattice(lattice, start=Q1DBC3_U)

KICKER4SFELC.type = "drift"
KICKER2SFELC.type = "drift"
KICKER6SMATCH.type = "drift"
H1ECOL.type = "drift"
H7ECOL.type = "drift"
D12SMATCH.type = "drift"

tws=twiss(lat, tw0)
plot_opt_func(lat, tws, top_plot=["Dx"])


setup = log.MachineSetup()
#setup.save_lattice(lat, "init.txt")
lat_all = MagneticLattice(lattice)
setup.load_lattice("init.txt", lat_all)

setup.convert_currents(lat_all, init_energy=0.0053)

lat.update_transfer_maps()

lat = MagneticLattice(lat_all.sequence, start=Q1DBC3_U)
tws=twiss(lat, tw0)
plot_opt_func(lat, tws, top_plot=["Dx"])

orb = Orbit(lat)
orb.set_ref_pos()
resp_mat = orb.linac_response_matrix(lat, tw_init=tw0)
read_bpms(lat, mi)

s_bpm = np.array([p.s for p in orb.bpms])
x_bpm = np.array([p.x for p in orb.bpms])
y_bpm = np.array([p.y for p in orb.bpms])

ax = plot_API(lat)
ax.plot(s_bpm, x_bpm*1000.,  "ro-", label="X")
ax.plot(s_bpm, y_bpm*1000.,   "bo-", label="Y")
plt.show()



orb.minus_reference()

s_bpm = np.array([p.s for p in orb.bpms])
x_bpm = np.array([p.x for p in orb.bpms])
y_bpm = np.array([p.y for p in orb.bpms])

ax = plot_API(lat)
ax.plot(s_bpm, x_bpm*1000.,  "ro-", label="X")
ax.plot(s_bpm, y_bpm*1000.,   "bo-", label="Y")
plt.show()
x = 0.001
BPM3DBC3.x = 0.000
BPM9ACC4.x = x
BPM9ACC5.x = x
BPM9ACC6.x = x
BPM11ACC7.x = 0.0000
BPM3DBC3.weight = 10
BPM9ACC5.weight = 10
BPM9ACC4.weight = 10.
BPM9ACC6.weight = 10

orb.correction(lat)
for elem in lat.sequence:
    if elem.type == "vcor":
        elem.dI = 0.
        elem.angle = 0.
    if elem.type == "hcor":
        dI = tpk2i(elem.dev_type, elem.E, elem.angle*1000.)
        if abs(dI) > 0.01:
            elem.dI = dI
            print elem.id, "angle=", elem.angle, " dI = ", elem.dI, " I = ", elem.I
        else:
            elem.dI = 0.
            elem.angle = 0.
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
ax.plot(s_bpm, y_bpm*1000.,   "bo-", label="Y")
ax.plot(s, y*1000.,  "b-", label="Y")
plt.show()


