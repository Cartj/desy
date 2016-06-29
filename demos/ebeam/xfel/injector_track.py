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

lat_i1 = MagneticLattice(gun_5MeV + i1_150M, stop=i1_starti1d)
tws = twiss(lat_i1, tws_5M, nPoints=None)
print( "'GUN': length = ", lat_i1.totalLen, "s = ", tws[-1].s)
plot_opt_func(lat_i1, tws, top_plot=["E"], fig_name= "i1", legend=False)
plt.show()




lat = MagneticLattice(i1_150M)
tws = twiss(lat, tws_150M, nPoints=1000)
#print "I1 (from 150MeV) : length = ", lat.totalLen, "s = ", tws[-1].s
#print( "I1 (from 150MeV) : delta on the end:  bx =", tws[-1].beta_x - tws_L1.beta_x , " by =", tws[-1].beta_y - tws_L1.beta_y)
plot_opt_func(lat, tws, top_plot=["E"], fig_name= "i1 from 150 MeV")
plt.show()
p_array, charge_array = astraBeam2particleArray(filename='Exfel.0320.ast')
print(charge_array)
bins_start, hist_start = get_current(p_array, charge=charge_array[0], num_bins=200)
tau = [p.tau for p in p_array]
dp = [p.p for p in p_array]
print(tau[:5])
plt.plot(tau, dp, 'r.')
plt.show()


plt.figure(1)
plt.title("current: start")
plt.plot(bins_start, hist_start)
plt.xlabel("s, m")
plt.ylabel("I, A")
plt.grid(True)
plt.show()