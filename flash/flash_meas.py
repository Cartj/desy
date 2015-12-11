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
import pickle
from converter import *
from ocelot.rad.undulator_params import *
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

tw0 = Twiss(beam)

BPM1TCOL.type="drift"
BPM2UND3.type="drift"
#BPM14SMATCH.type="drift"

lat = MagneticLattice(lattice, start=STARTACC39)

#ampls, phases = mi.get_cavity_info(["ACC1"])
#beam.E = ampls[0]*cos(phases[0]*pi/180.)*0.001

read_cavs(lat, mi)
#read_quads(lat, mi, dp)
#read_cors(lat, mi)

tws=twiss(lat, tw0)
plot_opt_func(lat, tws, top_plot=["E"])

print ("Electron energy = ", lambda2Ebeam(Lambda=16.3e-9, lu=0.0272634730539, K=1.2392))
"""
E = beam.E
for elem in lat.sequence:
    E += elem.transfer_map.delta_e
    if elem.type == "quadrupole":

        k1 = tpi2k(elem.dev_type, E, elem.I)
        K1 = abs(k1)*sign(elem.k1)

        print(elem.id,  "ideal: k1 = ", elem.k1, " real k1 = ", K1, " k1 = ", k1, "pol = ", elem.polarity)
        elem.k1 = K1
    #elif elem.type in ["hcor", "vcor"]:
    #    angle = tpi2k(elem.dev_type, E, elem.I)
    #    if angle == None:
    #        print(elem.id,  elem.I, E, angle, elem.dev_type)
    #    else:
    #        elem.angle = angle*0.001


lat.update_transfer_maps()
#exit(0)
tws=twiss(lat, tw0)
plot_opt_func(lat, tws, top_plot=["E"])
"""

orb = Orbit(lat)
exclude = ["Q9ACC3_U", "Q9ACC3_D", "Q10ACC3_U", "Q10ACC3_D"]
exclude = []
q_resp = elem_response_matrix(orb, lat, Particle(E=beam.E), elem_types=["quadrupole"], remove_elem=exclude)
pickle.dump(q_resp, open("quad_resp_mat.text", "wb"))
q_resp = pickle.load(open("quad_resp_mat.text", "rb"))
#print q_resp
#exit(0)

read_bpms(orb, mi)


p = orb.elem_correction(lat, q_resp, elem_types=["quadrupole"], remove_elems=exclude)
print ("particle ", p.x, p.px, p.y, p.py)
p.E = beam.E
plist = lattice_track(lat, p, order=1)
x = np.array([p.x for p in plist])
y = np.array([p.y for p in plist])
s = np.array([p.s for p in plist])
s_bpm = np.array([bpm.s for bpm in orb.bpms])
x_bpm = np.array([bpm.x for bpm in orb.bpms])
y_bpm = np.array([bpm.y for bpm in orb.bpms])

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
    if elem.type == "quadrupole":
        S.append(L - elem.l/2.)
        X.append(elem.dx)
        Y.append(elem.dy)
        w.append(elem.l)
        #if abs(elem.dx) > max(abs(np.array(X))) or abs(elem.dy) > max(abs(np.array(Y))):
        print(elem.id, elem.dx, elem.dy)
S = arange(len(X))
w = 0.3
plt.figure(1)
plt.bar(S+w, X, w, color="r" )
#plt.figure(2)
plt.bar(S, Y, w, color="b" )
plt.show()



plt.plot([bpm.s for bpm in orb.bpms], [bpm.x for bpm in orb.bpms], "ro-")
plt.plot([bpm.s for bpm in orb.bpms], [bpm.y for bpm in orb.bpms], "bo-")
plt.show()

