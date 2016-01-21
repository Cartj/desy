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

BPM1TCOL.weight = 0
#BPM2UND3.type="drift"
#BPM14SMATCH.type="drift"

lat = MagneticLattice(lattice, start=STARTACC39)
#lat = MagneticLattice(lattice)

V1ORS.type = "drift"
H7ECOL.type = "drift"
H1ECOL.type = "drift"


#lat = MagneticLattice(lattice)
setup = log.MachineSetup()

ampls1, phases1 = mi.get_cavity_info(["M1.ACC1"])
#ampls2, phases2 = mi.get_cavity_info(["M2.ACC1"])

print "energy gun = ", mi.get_gun_energy()

beam.E = mi.get_gun_energy() + ampls1[0]*cos(phases1[0]*pi/180.)*0.001
print "ACC1 = ", ampls1[0]*cos(phases1[0]*pi/180.)*0.001
read_cavs(lat, mi)

E = beam.E
tw0.E = beam.E
print "initial energy = ", E
for elem in lat.sequence:
    E += elem.transfer_map.delta_e
    #print elem.transfer_map.delta_e
    if elem.type == "cavity":
        print elem.id, elem.v, elem.phi, "energy = ", E*1000, " MeV "


read_quads(lat, mi, dp)
read_bends(lat, mi, dp)
read_sexts(lat, mi)
read_cors(lat, mi)
read_bpms(lat, mi)

orb = Orbit(lat)
orb.set_ref_pos()

setup.save_lattice(lat, "init.txt")
#setup.load_lattice("init.txt", lat)
#tws=twiss(lat, tw0)
#plot_opt_func(lat, tws, top_plot=["E"])

print ("Electron energy = ", lambda2Ebeam(Lambda=25.8e-9, lu=0.0272634730539, K=1.2392))

E = beam.E
for elem in lat.sequence:
    E += elem.transfer_map.delta_e
    elem.E = E
    if elem.type == "quadrupole":

        k1 = tpi2k(elem.dev_type, elem.E, elem.I)
        k1 = abs(k1)*sign(elem.k1)
        #if elem.mi_id in ["Q4DBC2","Q9ACC2", 'Q3.5ECOL', 'Q5UND1.3.5', "Q5UND2.4", 'Q6UND1']:
        #    k1 = abs(k1)*sign(elem.k1)
        #K1 = k1
        #print elem.id,  "i.k1=", elem.k1, " r.k1=", k1, "I=", elem.I, "E=", E
        #print(elem.id,  "ideal: k1 = ", elem.k1, " real k1 = ", K1, " dk/k = ", (K1-elem.k1)/elem.k1*100.)
        elem.k1 = k1
    elif elem.type == "sextupole":
        #pass

        k2 = tpi2k(elem.dev_type, elem.E, elem.I)
        print elem.id,  "i.k1=", elem.k2, " r.k1=", k2, "I=", elem.I, "E=", E
        elem.k2 = k2
        #print elem.id, elem.k2
    elif elem.type in ["bend", "sbend", "rbend"]:
        try:
            elem.dev_type
        except:
            continue
        angle = tpi2k(elem.dev_type, elem.E, elem.I)
        angle = abs(angle)*sign(elem.angle)*np.pi/180.
        print elem.id,  "i.a=", elem.angle, " r.a=", angle, "I=", elem.I, "E=", E
        elem.angle = angle


    #elif elem.type in ["hcor", "vcor"]:
    #    angle = tpi2k(elem.dev_type, E, elem.I)
    #    if angle == None:
    #        print(elem.id,  elem.I, E, angle, elem.dev_type)
    #    else:
    #        elem.angle = angle*0.001


lat.update_transfer_maps()
tws=twiss(lat, tw0)
plot_opt_func(lat, tws, top_plot=["Dx"])

"""
constr = {Q5UND1:{'beta_x':12, 'beta_y':3}, Q5UND3:{'beta_x':27., 'beta_y':4}}
vars = [[tw0, 'beta_x'], [tw0, 'beta_y'], [tw0, 'alpha_x'], [tw0, 'alpha_y']]
match(lat, constr, vars, tw0, xtol=1e-5)

L = 0.
constr_pos = []
for elem in lat.sequence:
    L += elem.l
    if elem in constr.keys():
        constr_pos.append(L)
print constr_pos


tws=twiss(lat, tw0)
#for tw in tws:
#    if tw.s in constr_pos:
#        print tw.s, tw.beta_x, tw.beta_y
plot_opt_func(lat, tws, top_plot=["E"])
"""

read_bpms(lat, mi)

#pi = Particle(p=0.0, E=beam.E)

#x_bpm, y_bpm = orb.read_virtual_orbit(lat, p_init=pi)
s_bpm = np.array([p.s for p in orb.bpms])
x_bpm = np.array([p.x for p in orb.bpms])
y_bpm = np.array([p.y for p in orb.bpms])

ax = plot_API(lat)
ax.plot(s_bpm, x_bpm*1000.,  "ro-", label="X")
#ax.plot(s, x, "r--", label=r"$\sigma_x=$"+"%.2f" % sigma_x+"mm")
ax.plot(s_bpm, y_bpm*1000.,   "bo-", label="Y")
#ax.plot(s, y, "b--", label=r"$\sigma_y=$"+"%.2f" % sigma_y+"mm")
plt.show()

resp_mat = orb.measure_response_matrix(lat, p_init=Particle(E=beam.E))
#resp_mat = orb.linac_response_matrix(lat, tw_init=tw0)
#pickle.dump(resp_mat, open("resp_mat.txt", "wb"))
resp_mat1 = pickle.load(open("resp_mat.txt", "rb"))


#print resp_mat
#print resp_mat1
orb.resp = resp_mat

read_bpms(lat, mi)

orb.minus_reference()

s_bpm_b = np.array([p.s for p in orb.bpms])
x_bpm_b = np.array([p.x for p in orb.bpms])
y_bpm_b = np.array([p.y for p in orb.bpms])

for i in range(20):
    orb.correction(lat)
    orb.read_virtual_orbit(lat, p_init=Particle(E=beam.E))
    x_bpm_i = np.array([p.x for p in orb.bpms])
    y_bpm_i = np.array([p.y for p in orb.bpms])
    x_bpm = -(x_bpm_b + x_bpm_i)
    y_bpm = -(y_bpm_b + y_bpm_i)
    orb.set_bpm_signal(x_bpm=x_bpm, y_bpm=y_bpm)
    sigma_x = sqrt(sum(x_bpm**2/len(x_bpm)))*1000.
    sigma_y = sqrt(sum(y_bpm**2/len(y_bpm)))*1000.
    print "sigma_x=", sigma_x, "mm, sigma_y=", sigma_y," mm"
    #plt.plot(s_bpm_b, x_bpm_b, "ro-")
    #plt.plot(s_bpm_b, x_bpm, "bo-")
    #plt.show()

"""
for elem in lat.sequence:
    if elem.type == "hcor":
        #print elem.dev_type, elem.E, elem.angle*1000.
        try:
            elem.dI = tpk2i(elem.dev_type, elem.E, elem.angle*1000.)
        except:
            print "could not find current:"
            print elem.id, elem.E, elem.angle*1000.
            elem.dI = None
        if abs(elem.dI) > 1.:
            #print elem.dev_type, elem.E, elem.angle*1000.
            print "X:", elem.id, "angle=", elem.angle, "dI=", elem.dI, "E=", elem.E
    elif elem.type == "vcor":
        try:
            elem.dI = tpk2i(elem.dev_type, elem.E, elem.angle*1000.)
        except:
            print "could not find current:"
            print elem.id, elem.E, elem.angle*1000.
            elem.dI = None
        if abs(elem.dI) > 1.:
            #print elem.dev_type, elem.E, elem.angle*1000.
            print "Y:", elem.id, "angle=", elem.angle, "dI=", elem.dI, "E=", elem.E
"""
orb.read_virtual_orbit(lat, p_init=Particle(E=beam.E))

p = Particle()
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
ax.plot(s_bpm_b, x_bpm_b, "bo--", label="X: bpm, line")
ax.plot(s, x, "r", label="X sim. tr.")
ax.legend()
#plt.show()
ax2 = plot_API(lat)
ax2.plot(s_bpm, y_bpm, "ro--", label="Y: bpm, line")
ax2.plot(s_bpm_b, y_bpm_b, "bo--", label="Y: bpm, line")
ax2.plot(s, y, "r", label="Y sim. tr.")
ax2.legend()
plt.show()