from ocelot import MagneticLattice

__author__ = 'Sergey Tomin'

from ocelot.gui.accelerator import *


exec( open("i1_old.inp"))

tws0 = Twiss()
tws0.beta_x = 13.172200000
tws0.beta_y = 13.172200
tws0.alpha_x = -1.635400
tws0.alpha_y = -1.635400

tws0.E = 0.1503

lat = MagneticLattice(lat_150MeV)
tws = twiss(lat, tws0, nPoints=None)
plot_opt_func(lat, tws, top_plot=["Dy", "Dx"])
plt.show()
print tws[-1].beta_x, tws[-1].beta_y, tws[-1].alpha_x, tws[-1].alpha_y, tws[-1].E
# Problem! the first section works wrong.
# Probably the difference is because R matrices in MAD8 and Ocelot for cavities on low energy is different

tws0 = Twiss()
tws0.beta_x = 29.171000000
tws0.beta_y = 29.171000000
tws0.alpha_x = 10.955000
tws0.alpha_y = 10.955000


tws0.E = 0.005

lat_gun = MagneticLattice(gun_5MeV)
tws = twiss(lat_gun, tws0, nPoints=None)
fig_name="twiss function is wrong in low energy section"
plot_opt_func(lat_gun, tws, top_plot=["Dy", "Dx"],fig_name="twiss function is wrong in low energy section")
plt.show()