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

#lat_mi = MagneticLattice(copy.deepcopy(lattice))
#mi = FLASH1VirtualInterface(lat_mi, gun_energy=0.005)
#dp = FLASH1VirtualProperties()

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

lat = MagneticLattice(lattice, start=STARTACC39)
#lat = MagneticLattice(lattice)
setup = log.MachineSetup()

ampls1, phases1 = mi.get_cavity_info(["M1.ACC1"])
#ampls2, phases2 = mi.get_cavity_info(["M2.ACC1"])

print "energy gun = ", mi.get_gun_energy()

beam.E = mi.get_gun_energy() + ampls1[0]*cos(phases1[0]*pi/180.)*0.001
print "ACC1 = ", ampls1[0]*cos(phases1[0]*pi/180.)*0.001
read_cavs(lat, mi)
E = beam.E
for elem in lat.sequence:
    E += elem.transfer_map.delta_e
    if elem.type == "cavity":
        print elem.id, elem.v, elem.phi, "energy = ", E*1000, " MeV "

#E = gun_energy
#for elem in lat_mi.sequence:
#    E += elem.transfer_map.delta_e
#    elem.E = E
#    #print E
read_quads(lat, mi, dp)
read_cors(lat, mi)

setup.save_lattice(lat, "init.txt")
setup.load_lattice("init.txt", lat)
#exit(0)
#log.save_currents(lat, filename="curr.txt")

#log.load_currents("curr.txt", lat)
#pickle.dump(lat.sequence, open("lat_with_currents.txt", "wb"))

tws=twiss(lat, tw0)
#for tw in tws:
#    print tw.s, tw.beta_x, tw.beta_y
plot_opt_func(lat, tws, top_plot=["E"])

print ("Electron energy = ", lambda2Ebeam(Lambda=16.3e-9, lu=0.0272634730539, K=1.2392))

E = beam.E
for elem in lat.sequence:
    E += elem.transfer_map.delta_e
    if elem.type == "quadrupole":

        k1 = tpi2k(elem.dev_type, E, elem.I)
        if elem.mi_id in ["Q4DBC2","Q9ACC2", 'Q3.5ECOL', 'Q5UND1.3.5', "Q5UND2.4", 'Q6UND1']:
            k1 = abs(k1)*sign(elem.k1)
        #K1 = k1
        print(elem.id,  "ideal: k1 = ", elem.k1, " real k1 = ", k1, "pol = ", elem.polarity)
        #print(elem.id,  "ideal: k1 = ", elem.k1, " real k1 = ", K1, " dk/k = ", (K1-elem.k1)/elem.k1*100.)
        elem.k1 = k1
    #elif elem.type in ["hcor", "vcor"]:
    #    angle = tpi2k(elem.dev_type, E, elem.I)
    #    if angle == None:
    #        print(elem.id,  elem.I, E, angle, elem.dev_type)
    #    else:
    #        elem.angle = angle*0.001


lat.update_transfer_maps()
"""
constr = {Q6TCOL:{'beta_x':38.25, 'beta_y':18.44}, Q8SMATCH:{'beta_x':14.657, 'beta_y':4.07}}
vars = [[tw0, 'beta_x'], [tw0, 'beta_y'], [tw0, 'alpha_x'], [tw0, 'alpha_y']]
match(lat, constr, vars, tw0, xtol=1e-5)

L = 0.
constr_pos = []
for elem in lat.sequence:
    L += elem.l
    if elem in constr.keys():
        constr_pos.append(L)
print constr_pos
"""
tws=twiss(lat, tw0)
#for tw in tws:
#    if tw.s in constr_pos:
#        print tw.s, tw.beta_x, tw.beta_y
plot_opt_func(lat, tws, top_plot=["E"])


orb = Orbit(lat)
#exclude = ["Q9ACC3_U", "Q9ACC3_D", "Q10ACC3_U", "Q10ACC3_D"]
exclude = []
elem_types_meas = ["quadrupole", "bend"]
#q_resp = elem_response_matrix(orb, lat, Particle(E=beam.E), elem_types=elem_types_meas, remove_elem=exclude)
#pickle.dump(q_resp, open("quad_resp_mat.text", "wb"))
q_resp = pickle.load(open("quad_resp_mat.text", "rb"))

#print q_resp
#exit(0)
#Q12DBC2.dx = 0.0001
#Q12DBC2.dy = -0.0001
#Q3DBC3.dx = 0.0001
#Q3DBC3.dy = -0.0001
#lat.update_transfer_maps()
read_bpms(orb, mi)

setup.save_orbit(orb, "orbit.txt")
setup.load_orbit("orbit.txt", orb)


#orb.read_virtual_orbit(lat, p_init=Particle(y = 0.001, x = 0.001, E=beam.E))
#Q12DBC2.dx = 0
#Q12DBC2.dy = 0
#Q3DBC3.dx  = 0
#Q3DBC3.dy  = 0
lat.update_transfer_maps()
p = orb.elem_correction(lat, q_resp, elem_types=elem_types_meas, remove_elems=exclude)
print ("particle ", p.x, p.px, p.y, p.py)
p.E = beam.E
plist = lattice_track(lat, p, order=1)
x = np.array([p.x for p in plist])
y = np.array([p.y for p in plist])
s = np.array([p.s for p in plist])
s_bpm = np.array([bpm.s for bpm in orb.bpms])
x_bpm = np.array([bpm.x for bpm in orb.bpms])
y_bpm = np.array([bpm.y for bpm in orb.bpms])
#plt.plot(s, [p.E for p in plist])
#plt.plot(s_bpm, [p.E for p in orb.bpms])
#plt.show()
ax = plot_API(lat)

ax.plot(s_bpm, x_bpm, "ro--", label="X: bpm, line")
ax.plot(s, x, "r", label="X sim. tr.")
ax.legend()
#plt.show()
ax2 = plot_API(lat)
ax2.plot(s_bpm, y_bpm, "bo--", label="Y: bpm, line")
ax2.plot(s, y, "b", label="Y sim. tr.")
ax2.legend()
plt.show()


L = 0
S = []
X = []
Y = []
w = []
for elem in lat.sequence:
    L += elem.l
    if elem.type in elem_types_meas:
        S.append(L - elem.l/2.)
        if "_D" in elem.id:
            X.append(elem.dx/2.)
            Y.append(elem.dy/2.)
        else:
            X.append(elem.dx)
            Y.append(elem.dy)
        w.append(elem.l)
        #if abs(elem.dx) > max(abs(np.array(X))) or abs(elem.dy) > max(abs(np.array(Y))):
        #print(elem.id, elem.dx, elem.dy)
S = array(S)
w = 0.3
#plt.figure(1)
#plt.bar(S-w/4., X, w/2, color="r" )
##plt.figure(2)
#plt.bar(S-w/4., Y, w/2, color="b" )
#plt.show()

ax3 = plot_API(lat)
ax3.bar(S-w/2., X, w/2., color="r" , label="dx")
ax3.bar(S, Y, w/2., color="b", label="dy" )
ax3.legend()
plt.show()


#plt.plot([bpm.s for bpm in orb.bpms], [bpm.x for bpm in orb.bpms], "ro-")
#plt.plot([bpm.s for bpm in orb.bpms], [bpm.y for bpm in orb.bpms], "bo-")
#plt.show()
