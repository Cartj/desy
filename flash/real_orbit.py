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
from flash1_virtual_interface import *
import pickle
from converter import *
from ocelot.rad.undulator_params import *
import copy
import machine_setup as log
mi = FLASH1MachineInterface()
dp = FLASH1DeviceProperties()

beam = Beam()
beam.E = 148.3148e-3 #in GeV ?!
beam.beta_x = 14.8821
beam.beta_y = 18.8146
beam.alpha_x =  -0.61309
beam.alpha_y = -0.54569
beam.emit_xn = 1.5e-6
beam.emit_yn = 1.5e-6
beam.emit_x = beam.emit_xn / (beam.E / m_e_GeV)
beam.emit_y = beam.emit_yn / (beam.E / m_e_GeV)
gun_energy = 0.0053 #GeV
tw0 = Twiss(beam)

BPM1TCOL.type="drift"
BPM2UND3.type="drift"
#BPM14SMATCH.type="drift"

#lat = MagneticLattice(lattice, start=STARTACC39)
lat = MagneticLattice(lattice)
orb = Orbit(lat)


#lat = MagneticLattice(lattice)
setup = log.MachineSetup()

ampls1, phases1 = mi.get_cavity_info(["M1.ACC1"])
#ampls2, phases2 = mi.get_cavity_info(["M2.ACC1"])

print "energy gun = ", mi.get_gun_energy()

beam.E = mi.get_gun_energy() #+ ampls1[0]*cos(phases1[0]*pi/180.)*0.001
print "ACC1 = ", ampls1[0]*cos(phases1[0]*pi/180.)*0.001
read_cavs(lat, mi)

E = beam.E
print "initial energy = ", E
for elem in lat.sequence:
    E += elem.transfer_map.delta_e
    #print elem.transfer_map.delta_e
    if elem.type == "cavity":
        print elem.id, elem.v, elem.phi, "energy = ", E*1000, " MeV "


read_quads(lat, mi, dp)
read_cors(lat, mi)
read_bpms(lat, mi)

#setup.save_lattice(lat, "init.txt")
#setup.load_lattice("init.txt", lat)
#tws=twiss(lat, tw0)
#plot_opt_func(lat, tws, top_plot=["E"])

print ("Electron energy = ", lambda2Ebeam(Lambda=16.3e-9, lu=0.0272634730539, K=1.2392))

E = beam.E
for elem in lat.sequence:
    E += elem.transfer_map.delta_e
    if elem.type == "quadrupole":

        k1 = tpi2k(elem.dev_type, E, elem.I)
        k1 = abs(k1)*sign(elem.k1)
        if elem.mi_id in ["Q4DBC2","Q9ACC2", 'Q3.5ECOL', 'Q5UND1.3.5', "Q5UND2.4", 'Q6UND1']:
            k1 = abs(k1)*sign(elem.k1)
        #K1 = k1
        print(elem.id,  "ideal: k1 = ", elem.k1, " real k1 = ", k1, "I = ", elem.I, "E = ", E)
        #print(elem.id,  "ideal: k1 = ", elem.k1, " real k1 = ", K1, " dk/k = ", (K1-elem.k1)/elem.k1*100.)
        elem.k1 = k1
    #elif elem.type in ["hcor", "vcor"]:
    #    angle = tpi2k(elem.dev_type, E, elem.I)
    #    if angle == None:
    #        print(elem.id,  elem.I, E, angle, elem.dev_type)
    #    else:
    #        elem.angle = angle*0.001


lat.update_transfer_maps()
#tws=twiss(lat, tw0)
#plot_opt_func(lat, tws, top_plot=["E"])


read_bpms(lat, mi)

#pi = Particle(p=0.0, E=beam.E)

#x_bpm, y_bpm = orb.read_virtual_orbit(lat, p_init=pi)
s_bpm = np.array([p.s for p in orb.bpms])
x_bpm = np.array([p.x for p in orb.bpms])
y_bpm = np.array([p.y for p in orb.bpms])
plt.figure(1)
ax = plot_API(lat)
ax.plot(s_bpm, x_bpm*1000.,  "ro-", label="X")
#ax.plot(s, x, "r--", label=r"$\sigma_x=$"+"%.2f" % sigma_x+"mm")



plt.figure(2)
ax = plot_API(lat)
ax.plot(s_bpm, y_bpm*1000.,   "bo-", label="Y")
#ax.plot(s, y, "b--", label=r"$\sigma_y=$"+"%.2f" % sigma_y+"mm")

plt.show()

resp_mat = orb.linac_response_matrix(lat, tw_init=tw0)