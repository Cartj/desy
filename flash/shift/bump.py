__author__ = 'Sergey Tomin'

from desy.flash.lattices.lattice_rf_red import *
from ocelot.gui.accelerator import *
from ocelot.gui import *
from ocelot.cpbd.orbit_correction import *
#from high_level_mint_flash import *
#import pyqtgraph as pg
from ocelot.utils.mint.flash1_interface_pydoocs import *
#from flash1_virtual_interface import *
from ocelot.utils.mint.flash1_converter import *
from ocelot.rad.undulator_params import *
from ocelot.utils.mint import machine_setup as log


def currents2angles(orb):
    for elem in np.append(orb.hcors, orb.vcors):

        angle = tpi2k(elem.dev_type, elem.E, elem.dI)*0.001

        #print elem.id, elem.dI, angle, elem.E
        elem.angle = angle
        #dI = tpk2i(elem.dev_type, elem.E, elem.angle*1000.)
        if abs(angle) > 1e-10:
            elem.angle = angle
            if elem.id in ['H10ACC5', 'H10ACC6', 'V10ACC5', 'V10ACC6', 'V2SFELC']:
                elem.angle = angle*2.
            #print elem.id, "angle=", elem.angle, " dI = ", elem.dI, " I = ", elem.I
        else:
            elem.dI = 0.
            elem.angle = 0.
        if abs(elem.angle) > 0.005:
            print elem.id, " @@@@@@@@@@@@@@@@ HIGH CURRENT @@@@@@@@@@@@@@@ = ", elem.angle


mi = FLASH1MachineInterface()
dp = FLASH1DeviceProperties()

#print "SASE=", mi.get_sase()
#print "get alarms = ", mi.get_alarms()

lat_ref = MagneticLattice(lattice)
setup = log.MachineSetup(lat_ref, mi, dp)

setup.load_lattice("lattice_calc.txt", lat_ref)
setup.convert_currents(lat_ref, init_energy=lat_ref.gun_energy)
#setup.set_elem_energy(lat_ref, init_energy=0.0053)


print "energy Q1DBC3_U = ", Q1DBC3_U.E
beam = Beam()
beam.E = Q1DBC3_U.E #in GeV ?!
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
setup = log.MachineSetup(lat, mi, dp)
setup.load_lattice("lattice_calc.txt", lat)


tws=twiss(lat, tw0)
plot_opt_func(lat, tws, top_plot=["Dx"])




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
            'V10ACC4', 'V10ACC5', 'V10ACC6', 'V10ACC7',
            'V1TCOL', 'V2TCOL', 'V4TCOL',
            'V8TCOL',
            'V4ECOL',                                                  #in dogleg
            'V5ORS', 'V6.4ORS', 'V7ORS', 'V9ORS',
            'V11ORS', 'V12ORS',
            'V2SFELC', 'V4SFELC', 'V6SFELC',
            'V7SMATCH', 'V14SMATCH'
            ]

bpms = ['1DBC3', '3DBC3', '9ACC4', '9ACC5', '9ACC6', '11ACC7', '15ACC7', '19ACC7',
        '1TCOL', '6TCOL', '8TCOL',
        '3ECOL', '5ECOL',                              # dogleg
        '2ORS', '7ORS', '9ORS', '12ORS',
        '1SFUND2', '1SFUND3', '1SFUND4', '1SFELC', '1SMATCH', '6SMATCH',
        '13SMATCH', '14SMATCH', '5UND1', '5UND2', '5UND3', '5UND4', '5UND5', '5UND6'  #undulator section
        ]
bpm_extr = ['2UND1', '4UND1', '2UND2', '4UND2', '2UND3', '4UND3', '2UND4', '4UND4', '2UND5', '4UND5', '2UND6', '4UND6']

orb = Orbit(lat)

orb.create_COR(horizantal+vertical)
orb.create_BPM(bpms)


#orb.set_ref_pos()

resp_mat = Response_matrix()
resp_mat.load("c_rmat_m_rad.txt")
rmatrix = resp_mat.extract(cor_list=vertical, bpm_list=bpms)

orb.export_response_matrix(rmatrix)


orb.set_ref_pos()
#resp_mat = orb.linac_response_matrix(tw_init=tw0)



setup.load_orbit("lattice_calc2.txt", lat)

setup.hli.read_bpms()




orb.minus_reference()
s_bpm_b = np.array([p.s for p in orb.bpms])
x_bpm_b = np.array([p.x for p in orb.bpms])
y_bpm_b = np.array([p.y for p in orb.bpms])



x = 0.001
#BPM3DBC3.x = 0.000
#BPM9ACC4.x = x
#BPM9ACC5.x = x
#BPM9ACC6.x = x
#BPM11ACC7.x = 0.0000
#BPM5UND1.x = x
#BPM5UND2.x = x
#BPM13SMATCH.y = x
#BPM14SMATCH.y = x
#BPM5UND1.y = x
"""
BPM1SFUND2.x = x
BPM1SFUND3.x = x
BPM1SFUND4.x = x
"""
"""
BPM3ECOL.x = x
BPM5ECOL.x = x
"""

BPM3ECOL.y = x
BPM5ECOL.y = x

#BPM3DBC3.weight = 1
#BPM9ACC5.weight = 1
#BPM9ACC4.weight = 1.
#BPM9ACC6.weight = 1

orb.show_orbit(title="relative orbit")

plt.show()

orb.correction(lat)


lat.update_transfer_maps()

orb.read_virtual_orbit(Particle(E=Q1DBC3_U.E))

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
ax.plot(s_bpm, (x_bpm + x_bpm_b)*1000.,  "ro-", label="X")
#ax.plot(s, x*1000.,  "r-", label="X")
ax.plot(s_bpm, (y_bpm + y_bpm_b)*1000.,   "bo-", label="Y")
#ax.plot(s, y*1000.,  "b-", label="Y")
plt.show()

log.angles2currents(orb)


alpha = 0.1

show_currents(orb.hcors, alpha)

inp = raw_input("Do you really want to apply currents for X:? ")
if inp == "yes":
    log.set_currents(mi, orb.hcors, alpha)

inp2 = raw_input("Restore orbit for X:? ")

if inp2 == "yes":
    log.restore_current(mi, orb.hcors)


show_currents(orb.vcors, alpha)

inp = raw_input("Do you really want to apply currents for Y:? ")
if inp == "yes":
    log.set_currents(mi, orb.vcors, alpha)

inp2 = raw_input("Restore orbit for Y:? ")
if inp2 == "yes":
    log.restore_current(mi, orb.vcors)
