__author__ = 'Sergey Tomin'
import sys

from ocelot.cpbd.elements import *
from ocelot.cpbd.optics import *
from ocelot.gui.accelerator import *

#tws0 = Twiss()
#tws0.beta_x = 29.171
#tws0.beta_y = 29.171
#tws0.alpha_x = 10.955
#tws0.alpha_y = 10.955
#
#tws0.E = 0.005 * GeV


# injector
exec(open("I1.inp"))
exec(open("L1.inp"))
exec(open("B1.inp"))
exec(open("L2.inp"))
exec(open("B2.inp"))
exec(open("L3.inp"))
exec(open("CL.inp"))
exec(open("CL2SA1.inp"))
exec(open("SA1.inp"))
exec(open("T4.inp"))
exec(open("SA3.inp"))
exec(open("CL2SA2.inp"))
exec(open("SA2.inp"))

lat_i1 = MagneticLattice(gun_5MeV)
tws = twiss(lat_i1, tws_5M, nPoints=1000)
print "'GUN': length = ", lat_i1.totalLen, "s = ", tws[-1].s
#plot_opt_func(lat_i1, tws, top_plot=["E"], fig_name= "i1")
#plt.show()

lat = MagneticLattice(i1_150M)
tws = twiss(lat, tws_150M, nPoints=1000)
#print "I1 (from 150MeV) : length = ", lat.totalLen, "s = ", tws[-1].s
print "I1 (from 150MeV) : delta on the end:  bx =", tws[-1].beta_x - tws_L1.beta_x , " by =", tws[-1].beta_y - tws_L1.beta_y
#plot_opt_func(lat, tws, top_plot=["E"], fig_name= "i1 from 150 MeV")
#plt.show()

#exec(open("L1.inp"))

lat = MagneticLattice(L1)
tws = twiss(lat, tws_L1, nPoints=1000)
#print "L1               : length = ", lat.totalLen, "s = ", tws[-1].s
print "L1               : delta on the end:  bx =", tws[-1].beta_x - tws_B1.beta_x , " by =", tws[-1].beta_y - tws_B1.beta_y
#L= tws_L1.s
#for elem in lat.sequence:
#    L+= elem.l
#    print L - elem.l/2., elem.type, elem.id, elem.l
#plot_opt_func(lat, tws, top_plot=["E"], fig_name= "L1")
#plt.show()


lat = MagneticLattice(B1)
tws = twiss(lat, tws_B1, nPoints=1000)
#print "B1               : length = ", lat.totalLen, "s = ", tws[-1].s
print "B1               : delta on the end:  bx =", tws[-1].beta_x - tws_L2.beta_x , " by =", tws[-1].beta_y - tws_L2.beta_y
#plot_opt_func(lat, tws, top_plot=["Dx", "Dy"], fig_name= "B1")
#plt.show()


lat = MagneticLattice(L2)
tws = twiss(lat, tws_L2, nPoints=1000)
#print "L2               : length = ", lat.totalLen, "s = ", tws[-1].s
print "L2               : delta on the end:  bx =", tws[-1].beta_x - tws_B2.beta_x , " by =", tws[-1].beta_y - tws_B2.beta_y
#plot_opt_func(lat, tws, top_plot=["E"], fig_name= "L2")
#plt.show()


lat = MagneticLattice(B2)
tws = twiss(lat, tws_B2, nPoints=1000)
#print "B2               : length = ", lat.totalLen, "s = ", tws[-1].s
print "B2               : delta on the end:  bx =", tws[-1].beta_x - tws_L3.beta_x , " by =", tws[-1].beta_y - tws_L3.beta_y
#plot_opt_func(lat, tws, top_plot=["Dx", "Dy"], fig_name="B2")
#plt.show()



lat = MagneticLattice(L3)
tws = twiss(lat, tws_L3, nPoints=1000)
#print "L3               : length = ", lat.totalLen, "s = ", tws[-1].s
print "L3               : delta on the end:  bx =", tws[-1].beta_x - tws_CL.beta_x , " by =", tws[-1].beta_y - tws_CL.beta_y
#plot_opt_func(lat, tws, top_plot=["E"], fig_name="L3")
#plt.show()




lat = MagneticLattice(CL)
tws = twiss(lat, tws_CL, nPoints=1000)
#print "CL               : length = ", lat.totalLen, "s = ", tws[-1].s
print "CL               : delta on the end:  bx =", tws[-1].beta_x - tws_CL2SA1.beta_x , " by =", tws[-1].beta_y - tws_CL2SA1.beta_y
#plot_opt_func(lat, tws, top_plot=["Dx", "Dy"], fig_name="CL")
#plt.show()



lat = MagneticLattice(CL2SA1)
tws = twiss(lat, tws_CL2SA1, nPoints=1000)
#print "CL to SA1        : length = ", lat.totalLen, "s = ", tws[-1].s
print "CL to SA1        : delta on the end:  bx =", tws[-1].beta_x - tws_SA1.beta_x , " by =", tws[-1].beta_y - tws_SA1.beta_y
#plot_opt_func(lat, tws, top_plot=["Dx", "Dy"], fig_name="CL2SA1")
#plt.show()




lat = MagneticLattice(SA1)
tws = twiss(lat, tws_SA1, nPoints=1000)
#print "SA1              : length = ", lat.totalLen, "s = ", tws[-1].s
print "SA1              : delta on the end:  bx =", tws[-1].beta_x - tws_T4.beta_x , " by =", tws[-1].beta_y - tws_T4.beta_y
#plot_opt_func(lat, tws, top_plot=["Dx", "Dy"], fig_name="SA1")
#plt.show()



lat = MagneticLattice(T4)
tws = twiss(lat, tws_T4, nPoints=1000)
#print "T4 (SA1 to SA3)  : length = ", lat.totalLen, "s = ", tws[-1].s
print "T4 (SA1 to SA3)  : delta on the end:  bx =", tws[-1].beta_x - tws_SA3.beta_x , " by =", tws[-1].beta_y - tws_SA3.beta_y
#plot_opt_func(lat, tws, top_plot=["Dx", "Dy"], fig_name="T4")
#plt.show()




lat = MagneticLattice(SA3)
tws = twiss(lat, tws_SA3, nPoints=1000)
print "SA3              : length = ", lat.totalLen, "s = ", tws[-1].s
#plot_opt_func(lat, tws, top_plot=["Dx", "Dy"], fig_name="SA3")
#plt.show()


lat = MagneticLattice((i1_150M,L1, B1, L2, B2, L3, CL,CL2SA1,SA1, T4,  SA3))
tws = twiss(lat, tws_150M, nPoints=1000)
print "i1 to SA3        : length = ", lat.totalLen, "s = ", tws[-1].s
plot_opt_func(lat, tws, top_plot=["Dx", "Dy"], fig_name="S2E SASE1 and SASE3")
#plt.show()

#print len(lat.sequence)
lat = MagneticLattice((i1_150M,L1, B1, L2, B2, L3, CL, CL2SA2, SA2))
tws = twiss(lat, tws_150M, nPoints=1000)
print "i1 to SA2        : length = ", lat.totalLen, "s = ", tws[-1].s
plot_opt_func(lat, tws, top_plot=["Dx", "Dy"], fig_name="S2E SASE2")
plt.show()

