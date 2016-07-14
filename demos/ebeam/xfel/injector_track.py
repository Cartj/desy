__author__ = 'Sergey Tomin'
from ocelot import *
from ocelot.gui.accelerator import *
from ocelot.adaptors import *
#tws0 = Twiss()
#tws0.beta_x = 29.171
#tws0.beta_y = 29.171
#tws0.alpha_x = 10.955
#tws0.alpha_y = 10.955


# injector
#from desy.demos.ebeam.xfel.I1 import *
from I1 import *
method = MethodTM()
method.global_method = SecondTM
lat = MagneticLattice(gun_5MeV + i1_150M, method=method)
tws = twiss(lat, tws_5M, nPoints=None)
print("'GUN': length = ", lat.totalLen, "s = ", tws[-1].s)
plot_opt_func(lat, tws, top_plot=["E"], fig_name="i1", legend=False)
plt.show()


p_array, charge_array = astraBeam2particleArray(filename='Exfel.0320.ast')
p_array.s = 0.
#p_array.E = 0.005
#p_array.particles[5::6] = p_array.particles[5::6]*3
#p_array.particles[4::6] = p_array.particles[4::6]*5
#print("energy = ", p_array.E)
bins_start, hist_start = get_current(p_array, charge=charge_array[0], num_bins=200)
tau = np.array([p.tau for p in p_array])
dp = np.array([p.p for p in p_array])
#print(tau[:5])
plt.figure(1)
plt.plot(tau*1000, dp, 'r.')
plt.xlabel("s, mm")
plt.ylabel("dp/p")
plt.grid(True)

plt.figure(2)
plt.title("current: start")
plt.plot(bins_start*1000, hist_start)
plt.xlabel("s, mm")
plt.ylabel("I, A")
plt.grid(True)
plt.show()



method = MethodTM()
method.global_method = SecondTM
#method.global_method = TransferMap
#q_37_i1.k1  = -1.268015360852410
#q_38_i1.k1  =  1.229893780868490
#qi_46_i1.k1 = -0.043222567265718
#qi_47_i1.k1 =  0.081570790435482
#qi_50_i1.k1 = -1.059084673457792
c_a1_1_1_i1.v = 18.455*1e-3; c_a1_1_1_i1.phi = 12
c_a1_1_2_i1.v = 18.455*1e-3; c_a1_1_2_i1.phi = 12
c_a1_1_3_i1.v = 18.455*1e-3; c_a1_1_3_i1.phi = 12
c_a1_1_4_i1.v = 18.455*1e-3; c_a1_1_4_i1.phi = 12
c_a1_1_5_i1.v = 18.455*1e-3; c_a1_1_5_i1.phi = 12
c_a1_1_6_i1.v = 18.455*1e-3; c_a1_1_6_i1.phi = 12
c_a1_1_7_i1.v = 18.455*1e-3; c_a1_1_7_i1.phi = 12
c_a1_1_8_i1.v = 18.455*1e-3; c_a1_1_8_i1.phi = 12

#c3_ah1_1_1_i1.v = 20.2/8*1e-3
#c3_ah1_1_2_i1.v = 20.2/8*1e-3
#c3_ah1_1_3_i1.v = 20.2/8*1e-3
#c3_ah1_1_4_i1.v = 20.2/8*1e-3
#c3_ah1_1_5_i1.v = 20.2/8*1e-3
#c3_ah1_1_6_i1.v = 20.2/8*1e-3
#c3_ah1_1_7_i1.v = 20.2/8*1e-3
#c3_ah1_1_8_i1.v = 20.2/8*1e-3
#lat = MagneticLattice(gun_5MeV + i1_150M, start=start_sim, stop=i1_vcst40t400y, method=method)
lat = MagneticLattice(gun_5MeV, start=start_sim, method=method)
#tws = twiss(lat, tws_5M, nPoints=None)
#print( "'GUN': length = ", lat.totalLen, "s = ", tws[-1].s)
#plot_opt_func(lat, tws, top_plot=["E"], fig_name="i1", legend=False)
#plt.show()

wake1 = Wake()
wake1.wake_file = 'TESLA_MODULE_WAKE_TAYLOR.dat'
wake1.step = 2
wake1.factor = 1./11.0688

wake2 = Wake()
wake2.wake_file = 'THIRD_HARMONIC_SECTION_WAKE_TAYLOR.dat'
wake2.step = 1
wake2.factor = 1./4.864



navi = Navigator(lat)

#navi.add_physics_proc(wake1, w_acc1_start, w_acc1_stop)
#navi.add_physics_proc(wake2, w_acc39_start, w_acc39_stop)
#navi.add_physics_proc(wake2, w2_start, w2_stop)
#navi.add_physics_proc(wake3, w3_start, w3_stop)

navi.unit_step = 0.6

#for elem in lat.sequence:
#    print(elem.l, elem.eid)
#tracking_step(lat=lat, particle_list=p_array, dz=lat.totalLen, navi=navi)

tws_track, p_array = track(lat, p_array, navi)

plot_opt_func(lat, tws_track, top_plot=["E"], fig_name=0, legend=False)
#plt.show()


bins_start, hist_start = get_current(p_array, charge=charge_array[0], num_bins=200)
tau = np.array([p.tau for p in p_array])
dp = np.array([p.p for p in p_array])
x = np.array([p.x for p in p_array])
y = np.array([p.y for p in p_array])

#emit_x = np.array([p.emit_x for p in tws_track])
#emit_y = np.array([p.emit_y for p in tws_track])
#s_tws = np.array([p.s for p in tws_track])

#print(tau[:5])
plt.figure(1)
plt.plot(tau*1000, x*1000, 'r.')
plt.xlabel("s, mm")
plt.ylabel("x, mm")
plt.grid(True)

plt.figure(2)
plt.plot(tau*1000, y*1000, 'r.')
plt.xlabel("s, mm")
plt.ylabel("y, mm")
plt.grid(True)

plt.figure(3)
plt.plot(tau*1000, dp, 'r.')
plt.xlabel("s, mm")
plt.ylabel("dp/p")
plt.grid(True)

#plt.figure(4)
#plt.plot(s_tws, emit_x/emit_x[0], 'r')
#plt.plot(s_tws, emit_y/emit_y[0], 'b')
#plt.xlabel("S, m")
#plt.ylabel("emit.norm.")
#plt.legend(["hor", "ver"])
#plt.grid(True)

plt.figure(6)
plt.title("current: end")
plt.plot(bins_start*1000, hist_start)
plt.xlabel("s, mm")
plt.ylabel("I, A")
plt.grid(True)
plt.show()