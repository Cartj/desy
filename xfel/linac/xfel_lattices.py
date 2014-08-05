__author__ = 'Sergey Tomin'
import sys

from ocelot.cpbd.elements import *
from ocelot.cpbd.optics import *
from ocelot.gui.accelerator import *

tws0 = Twiss()
tws0.beta_x = 30
tws0.beta_y = 30
tws0.alpha_x = 10
tws0.alpha_y = 10

tws0.E = 0.005 * GeV


# injector
exec(open("i1.inp"))
lat_i1 = MagneticLattice(i1)
tws = twiss(lat_i1, tws0, nPoints=None)
lat_i1.update_transfer_maps()
tws = twiss(lat_i1, tws0, nPoints=None)
plot_opt_func(lat_i1, tws, top_plot=["Dx", "Dy"], name = "i1")
tws_end_i1 = tws[-1]

# l1 part of BC
exec(open("l1.inp"))
lat_l1 = MagneticLattice(l1)
tws = twiss(lat_l1, tws[-1], nPoints=None)
plot_opt_func(lat_l1, tws, top_plot=["Dx", "Dy"], name = "l1")

#b1 part of BC
exec(open("b1.inp"))
lat_b1 = MagneticLattice(b1)
tws = twiss(lat_b1, tws[-1], nPoints=None)
plot_opt_func(lat_b1, tws, top_plot=["Dx", "Dy"], name = "b1")


#l2 part of BC
exec(open("l2.inp"))
lat_l2 = MagneticLattice(l2)
tws = twiss(lat_l2, tws[-1], nPoints=None)
plot_opt_func(lat_l2, tws, top_plot=["Dx", "Dy"], name = "l2")


#b2 part of BC
exec(open("b2.inp"))
lat_b2 = MagneticLattice(b2)
tws = twiss(lat_b2, tws[-1], nPoints=None)
plot_opt_func(lat_b2, tws, top_plot=["Dx", "Dy"], name = "b2")


exec(open("l3.inp"))
#lat_l3 = MagneticLattice(l3)
#tws = twiss(lat_l3, tws[-1], nPoints=None)
#plot_opt_func(lat_l3, tws, top_plot=["Dx", "Dy"], name = "l3")


exec(open("cl.inp"))
lat_cl = MagneticLattice(cl)
tws = twiss(lat_cl, tws[-1], nPoints=None)
plot_opt_func(lat_cl, tws, top_plot=["Dx", "Dy"], name = "cl")

tws_cl_end = tws[-1]

exec(open("td2.inp"))
lat_td2 = MagneticLattice(td2)
tws = twiss(lat_td2, tws_cl_end, nPoints=None)
plot_opt_func(lat_td2, tws, top_plot=["Dx", "Dy"], name = "td2")
plt.show()


exec(open("td1.inp"))
lat_td1 = MagneticLattice(td1)
tws = twiss(lat_td1, tws_cl_end, nPoints=None)
plot_opt_func(lat_td1, tws, top_plot=["Dx", "Dy"], name = "td1")
plt.show()

bc = (l1,b1,l2,b2)

lat_bc = MagneticLattice(bc)
tws = twiss(lat_bc, tws_end_i1, nPoints=None)
plot_opt_func(lat_bc, tws, top_plot=["Dx", "Dy"], name = "BC")

plt.show()

xfelall = (i1, bc, l3,cl, td2)
lat_xfelall = MagneticLattice(xfelall)
tws = twiss(lat_xfelall, tws0, nPoints=None)
plot_opt_func(lat_xfelall, tws, top_plot=["Dx", "Dy"], name = "XFEL SASE1 SASE2")

plt.show()

xfelall = (i1, bc, l3,cl, td1)
lat_all_sase3 = MagneticLattice(xfelall)
tws = twiss(lat_all_sase3, tws0, nPoints=None)
plot_opt_func(lat_all_sase3, tws, top_plot=["Dx", "Dy"], name = "XFEL SASE3")

plt.show()