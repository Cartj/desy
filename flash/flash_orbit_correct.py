__author__ = 'Sergey Tomin'
from desy.flash.lattices.lattice_rf_mod import *
from ocelot.gui.accelerator import *
from ocelot.gui import *
from ocelot.cpbd.orbit_correction import *
from ocelot.utils.mint.machine_setup import *
from ocelot.utils.mint.flash1_converter import *
from ocelot.utils.mint.flash1_interface_pydoocs import *

mi = FLASH1MachineInterface()
dp = FLASH1DeviceProperties()

lat_ref = MagneticLattice(lattice)
setup = MachineSetup(lat_ref, mi, dp)

setup.load_lattice("exp_files_22/start_7_00.txt", lat_ref)
setup.set_elem_energy(lat_ref, init_energy=0.0053)

print STARTACC39.E
lat = MagneticLattice(lattice, start=STARTACC39)
setup.load_lattice("exp_files_22/start_7_00.txt", lat)
setup.convert_currents(lat, init_energy =STARTACC39.E)

#S2ECOL.k2 = 0.
#S6ECOL.k2 = 0.


beam = Beam()
beam.E = STARTACC39.E #in GeV ?!
beam.beta_x = 14.8821
beam.beta_y = 18.8146
beam.alpha_x =  -0.61309
beam.alpha_y = -0.54569
beam.emit_xn = 1.5e-6
beam.emit_yn = 1.5e-6
beam.emit_x = beam.emit_xn / (beam.E / m_e_GeV)
beam.emit_y = beam.emit_yn / (beam.E / m_e_GeV)

tw0 = Twiss(beam)


tws=twiss(lat, tw0)
plot_opt_func(lat, tws, top_plot=["Dx","Dy"])

orb = Orbit(lat)
s_bpm_b = np.array([p.s for p in orb.bpms])
x_bpm_b = np.array([p.x for p in orb.bpms])
y_bpm_b = np.array([p.y for p in orb.bpms])


ax = plot_API(lat)
ax.plot(s_bpm_b, x_bpm_b*1000., "ro-")
ax.plot(s_bpm_b, y_bpm_b*1000., "bo-")
plt.show()


resp_mat1 = orb.linac_response_matrix(lat, tw_init=tw0)
#resp_mat2 = orb.measure_response_matrix(lat, p_init = Particle(E=beam.E))

"""

s = np.shape(resp_mat1)
for i in range(s[0]):
    bpm_id = orb.bpms[i%54].id
    plane = "X"
    if i>54:
        plane = "Y"
    for j in range(s[1]):
        x1 = resp_mat1[i,j]
        x2 = resp_mat2[i,j]
        if x1 == 0 and x2 == 0:
            continue
        if abs(x1 - x2)/max(np.abs([x1, x2])) < 0.10:
            continue
        if j <=48:
            name = orb.hcors[j].id
        elif j>48:
            print j, j-49, len(orb.vcors)
            name = orb.vcors[j-49].id
        print "resp: ", plane, bpm_id, name, "V=", resp_mat1[i,j], resp_mat2[i,j]
"""
setup.set_orbit(lat)

p0 = orb.correction(lat, p_init=Particle(E=beam.E))

p0=Particle(E=beam.E)
x_bpm, y_bpm = orb.read_virtual_orbit(lat, p_init=p0)


ax = plot_API(lat)
ax.plot(s_bpm_b, (x_bpm + x_bpm_b)*1000., "ro-")
ax.plot(s_bpm_b, (y_bpm + y_bpm_b)*1000., "bo-")
plt.show()


plist = lattice_track(lat, p0, order=1)

xd = np.array([p.x for p in plist])
yd = np.array([p.y for p in plist])
sd = np.array([p.s for p in plist])

ax = plot_API(lat)
ax.plot(sd, xd*1000., "r-")
ax.plot(sd, yd*1000., "b-")
plt.show()








setup.load_lattice("exp_files_22/4correct.txt", lat)


for elem in lat.sequence:
    if elem.type in ["hcor", "vcor"]:
        elem.angle = 0.
lat.update_transfer_maps()


s_bpm_c = np.array([p.s for p in orb.bpms])
x_bpm_c = np.array([p.x for p in orb.bpms])
y_bpm_c = np.array([p.y for p in orb.bpms])

ax = plot_API(lat)
ax.plot(s_bpm_c, (x_bpm_c - x_bpm_b)*1000., "ro-")
ax.plot(s_bpm_c, (y_bpm_c - y_bpm_b)*1000., "bo-")
plt.show()



orb2 = Orbit(lat)
correctors = ['H10SMATCH', 'H12SMATCH', 'V7SMATCH', 'V14SMATCH' ]
bpms = ['BPM13SMATCH', 'BPM14SMATCH', 'BPM5UND1', 'BPM5UND2', 'BPM5UND3', 'BPM5UND4', 'BPM5UND5', 'BPM5UND6']
orb2.create_BPM(lat, bpm_list=bpms)
orb2.create_COR(lat, cor_list=correctors)

resp_mat3 = orb2.linac_response_matrix(lat, tw_init=tw0)
#print "beam.E = ", beam.E
resp_mat2 = orb2.measure_response_matrix(lat, p_init = Particle(E=beam.E), match_ic=False)
#orb2.save_r_matrix()
#print resp_mat3
#print resp_mat2

for i, bpm in enumerate(orb.bpms):
    bpm.x = x_bpm_c[i] - x_bpm_b[i]
    bpm.y = y_bpm_c[i] - y_bpm_b[i]


ax = plot_API(lat)
ax.plot(np.array([p.s for p in orb2.bpms]), (np.array([p.y for p in orb2.bpms]) )*1000., "ro-")
ax.plot(s_bpm_c, (y_bpm_c )*1000., "bo-")
plt.show()


bpm_x_before = np.array([b.x for b in orb2.bpms])
bpm_y_before = np.array([b.y for b in orb2.bpms])
bpm_s_before = np.array([b.s for b in orb2.bpms])

p0 = orb2.correction(lat, p_init=Particle(E=beam.E))

p0=Particle(E=beam.E)
x_bpm, y_bpm = orb2.read_virtual_orbit(lat, p_init=p0)


ax = plot_API(lat)
ax.plot(s_bpm_b, (x_bpm_c - x_bpm_b)*1000., "ro-", label="X:before")
ax.plot(bpm_s_before, (x_bpm + bpm_x_before)*1000., "bo-", label="X:after")

ax.plot(s_bpm_b, (y_bpm_c - y_bpm_b)*1000., "go-", label="Y:before")
ax.plot(bpm_s_before, (y_bpm + bpm_y_before)*1000., "ko-", label="Y:after")
ax.legend()
plt.show()

for cor in orb2.hcors:
    angle_0 = tpi2k(cor.dev_type, cor.E, cor.I)*0.001
    angle = angle_0 + cor.angle
    I1 = tpk2i(cor.dev_type, cor.E, angle*1000.)
    print cor.id, "angle = ", cor.angle, "Io = ", cor.I, "I = ", I1 - cor.I
for cor in orb2.vcors:
    angle_0 = tpi2k(cor.dev_type, cor.E, cor.I)*0.001
    angle = angle_0 + cor.angle
    I1 = tpk2i(cor.dev_type, cor.E, angle*1000.)
    print cor.id, "angle = ", cor.angle, "Io = ", cor.I, "I = ", I1 - cor.I

setup.load_lattice("exp_files_22/4correct_after.txt", lat)

print "H10SMATCH = ", H10SMATCH.I
print "H12SMATCH = ", H12SMATCH.I
print "V7SMATCH = ",  V7SMATCH.I
print "V14SMATCH = ", V14SMATCH.I