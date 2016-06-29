from ocelot import MagneticLattice

__author__ = 'Sergey Tomin'

from ocelot.gui.accelerator import *
from ocelot.mint.xfel_interface import *
#tws0 = Twiss()
#tws0.beta_x = 29.171
#tws0.beta_y = 29.171
#tws0.alpha_x = 10.955
#tws0.alpha_y = 10.955
#
#tws0.E = 0.005 * GeV


# injector
from desy.xfel.linac.I1 import *

lat_i1 = MagneticLattice(gun_5MeV + i1_150M, stop=i1_starti1d)
tws = twiss(lat_i1, tws_5M, nPoints=None)
print( "'GUN': length = ", lat_i1.totalLen, "s = ", tws[-1].s)
plot_opt_func(lat_i1, tws, top_plot=["Dx"], fig_name= "i1", legend=False)
plt.show()

mi = XFELMachineInterface()

for elem in lat_i1.sequence:
    ki = mi.get_value(elem.id)
    k1 = ki/elem.l
    print(elem.id, k1)