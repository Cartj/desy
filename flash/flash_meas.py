__author__ = 'Sergey Tomin'

from lattice_rf_mod import *
from ocelot.gui.accelerator import *
from ocelot import *
from ocelot.gui import *
from ocelot.cpbd.errors import *
from ocelot.cpbd.track import *
from ocelot.cpbd.orbit_correction import *
from copy import copy
#import pyqtgraph as pg
from ocelot.utils.mint.flash1_interface_pytine import *
import pickle

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

lat = MagneticLattice(lattice, start=STARTACC39)

tws=twiss(lat, tw0)
plot_opt_func(lat, tws, top_plot=["Dx"])

for elem in lat.sequence:
    if elem.type in ["hcor", "vcor"]:
        elem.mi_id = elem.id
        try:
            print(elem.mi_id, )
            vals = mi.init_corrector_vals([elem.mi_id])
            print(vals)
        except:
            print("UNKNOW")

exit(0)

orb = Orbit(lat)

q_resp = sim_quad_response_matrix(orb, lat, Particle(E=beam.E))
pickle.dump(q_resp, open("quad_resp_mat.text", "wb"))
q_resp = pickle.load(open("quad_resp_mat.text", "rb"))
#print q_resp
#exit(0)


for bpm in orb.bpms:
    name = bpm.id.replace("BPM", "")
    print(name)
    bpm.mi_id = name
    try:
        X, Y = mi.get_bpms_xy([bpm.mi_id])
        bpm.x = X[0]
        bpm.y = Y[0]
        print (bpm.s, bpm.x, bpm.y)
    except:
        print(name, "  CAN MOT FIND")


lat = orb.quad_correction(lat, q_resp)
p = Particle(p=0.0, E=beam.E)
plist = lattice_track(lat, p, order=1)
x = np.array([p.x for p in plist])
y = np.array([p.y for p in plist])
s = np.array([p.s for p in plist])
s_bpm = np.array([bpm.s for bpm in orb.bpms])
x_bpm = np.array([bpm.x for bpm in orb.bpms])
y_bpm = np.array([bpm.y for bpm in orb.bpms])
plt.plot(s_bpm, x_bpm, "ro")
plt.plot(s, x, "r--", label=r"$\sigma_x=$")
plt.plot(s_bpm, y_bpm, "bo")
plt.plot(s, y, "b--", label=r"$\sigma_y=$")
plt.show()
for elem in lat.sequence:
    if elem.type == "quadrupole":
        name = elem.id
        if "_U" in name:
            continue
        name = name.replace("_U", "")
        name = name.replace("_D", "")
        name = name.replace("_", ".")
        #print(name)
        try:
            elem.mi_id
        except:
            elem.mi_id = name
        print(elem.mi_id)
        try:
            elem.I = mi.get_quads_current([elem.mi_id])
            elem.polarity = dp.get_polarity([elem.mi_id])
            #type_magnet = dp.get_type_magnet([elem.mi_id])
            #print(type_magnet, elem.dev_type)
            #print(elem.id, name, mi.get_quads_current([elem.mi_id]))
        except:
            print(name, "  CAN MOT FIND")

plt.plot([bpm.s for bpm in orb.bpms], [bpm.x for bpm in orb.bpms], "ro-")
plt.plot([bpm.s for bpm in orb.bpms], [bpm.y for bpm in orb.bpms], "bo-")
plt.show()

