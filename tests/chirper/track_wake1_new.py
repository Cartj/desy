__author__ = 'Igor Zagorodnov'

from ocelot.cpbd.wake3D_old import *
from ocelot.gui import *
from ocelot import *
from ocelot.cpbd.wake3D import *
#drive = 'd:/'
Ns = 500  # wake sampling
NF = 20  # smoothing filter order

beam = Beam()
beam.E = 17.5  # in GeV
beam.beta_x = 22.5995
beam.beta_y = 22.5995
beam.alpha_x = -1.4285
beam.alpha_y = 1.4285
beam.emit_xn = 1e-6
beam.emit_yn = 1e-6
beam.emit_x = beam.emit_xn / (beam.E / m_e_GeV)
beam.emit_y = beam.emit_yn / (beam.E / m_e_GeV)

tw0 = Twiss(beam)
from lattice0 import *
method = MethodTM()
method.global_method = SecondTM
lat = MagneticLattice(lattice, method=method)

tws = twiss(lat, tw0, nPoints=None)
plot_opt_func(lat, tws, top_plot=["E"])
plt.show()

#drive = 'd:/'
#filename = drive + 'TEST_DECHIRPER/ASTRA/XFEL01_ideal/LCLS.ast'
#p_array, charge_array, z0, gamref = astraBeam2particleArray(filename)
#p_array, charge_array = astraBeam2particleArray(filename='/home/sergey/Dropbox/DESY/repository/desy/demos/ebeam/flash/elegant_files/flash_out_200000.ast')
p_array, charge_array = astraBeam2particleArray(filename='LCLS.ast')

# plot current
bins_start, hist_start = get_current(p_array, charge=charge_array[0], num_bins=200)



wake1 = Wake()
wake1.wake_file = 'wake_vert_1m.txt'
wake1.step = 1

wake2 = Wake()
wake2.wake_file = 'wake_hor_1m.txt'
wake2.step = 1

wake3 = Wake()
wake3.wake_file = 'wake_vert_1m.txt'
wake3.step = 1


navi = Navigator(lat)

navi.add_physics_proc(wake1, w1_start, w1_stop)
navi.add_physics_proc(wake2, w2_start, w2_stop)
navi.add_physics_proc(wake3, w3_start, w3_stop)

navi.unit_step = 0.2

tws_track, p_array = track(lat, p_array, navi)




plt.figure(1)
plt.plot(p_array.particles[4::6], p_array.particles[5::6] + p_array.E, '.')

# output
s_p = [t.s for t in tws_track]
n_out = len(s_p)
out = np.zeros((n_out, 3))
out[:, 0] = s_p
out[:, 1] = [t.beta_x for t in tws_track]
out[:, 2] = [t.beta_y for t in tws_track]
# np.savetxt('D:/pyoptics.txt',out)
np.savetxt('pyoptics_withoutSC1.txt', out)

particleArray2astraBeam(p_array, charge_array, 'ocelot.ast')

# plot current at the beginning of accelerator
# plt.figure(1)
# plt.title("current: start")
# plt.plot(bins_start, hist_start)
# plt.xlabel("s, m")
# plt.ylabel("I, A")
# plt.grid(True)

# plot current at the end of accelerator
# bins, hist = get_current(p_array, charge=charge_array[0], num_bins=200)
# plt.figure(2)
# plt.title("current: end")
# plt.plot(bins, hist)
# plt.xlabel("s, m")
# plt.ylabel("I, A")
# plt.grid(True)


st = [p.s for p in tws_track]
s = [p.s for p in tws]
plt.figure(3)
plt.title(r"$\beta - functions$")
plt.plot(st, [p.beta_x for p in tws_track], "ro-")
plt.hold(True)
plt.plot(s, [p.beta_x for p in tws], "r-")
plt.plot(st, [p.beta_y for p in tws_track], "bo-")
plt.plot(s, [p.beta_y for p in tws], "b-")
plt.legend()
plt.grid(True)

em_x = [p.emit_x for p in tws_track]
em_y = [p.emit_y for p in tws_track]
em_x = em_x / em_x[0]
em_y = em_y / em_y[0]
plt.figure(4)
# plt.title(r"$\emittances$")
plt.plot(st, em_x, "ro-")
plt.hold(True)
plt.plot(st, em_y, "bo-")
# plt.ylim(0.95,1.05)
plt.legend()
plt.grid(True)
plt.show()

