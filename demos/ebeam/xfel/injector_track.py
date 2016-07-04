__author__ = 'Sergey Tomin'
from ocelot import *
from ocelot.gui.accelerator import *
from ocelot.adaptors import *
#tws0 = Twiss()
#tws0.beta_x = 29.171
#tws0.beta_y = 29.171
#tws0.alpha_x = 10.955
#tws0.alpha_y = 10.955
#
#tws0.E = 0.005 * GeV
#Q.37.I1  = -1.268015360852410
#Q.38.I1  =  1.229893780868490
#QI.46.I1 = -0.043222567265718
#QI.47.I1 =  0.081570790435482
#QI.50.I1 = -1.059084673457792

# injector
from desy.demos.ebeam.xfel.I1 import *
method = MethodTM()
method.global_method = SecondTM
lat = MagneticLattice(gun_5MeV + i1_150M, method=method)
tws = twiss(lat, tws_5M, nPoints=None)
print( "'GUN': length = ", lat.totalLen, "s = ", tws[-1].s)
plot_opt_func(lat, tws, top_plot=["E"], fig_name="i1", legend=False)
plt.show()




#lat = MagneticLattice(i1_150M)
#tws = twiss(lat, tws_150M, nPoints=1000)
#print "I1 (from 150MeV) : length = ", lat.totalLen, "s = ", tws[-1].s
#print( "I1 (from 150MeV) : delta on the end:  bx =", tws[-1].beta_x - tws_L1.beta_x , " by =", tws[-1].beta_y - tws_L1.beta_y)
#plot_opt_func(lat, tws, top_plot=["E"], fig_name= "i1 from 150 MeV")
#plt.show()
p_array, charge_array = astraBeam2particleArray(filename='Exfel.0320.ast')
#print(charge_array)
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
#q_37_i1.k1  = -1.268015360852410
#q_38_i1.k1  =  1.229893780868490
#qi_46_i1.k1 = -0.043222567265718
#qi_47_i1.k1 =  0.081570790435482
#qi_50_i1.k1 = -1.059084673457792
lat = MagneticLattice(gun_5MeV + i1_150M, start=start_sim, method=method)
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

tws_track, p_array = track(lat, p_array, navi)

plot_opt_func(lat, tws_track, top_plot=["E"], fig_name= "i1", legend=False)
plt.show()


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
plt.title("current: end")
plt.plot(bins_start*1000, hist_start)
plt.xlabel("s, mm")
plt.ylabel("I, A")
plt.grid(True)
plt.show()