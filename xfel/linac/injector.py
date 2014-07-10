__author__ = 'Sergey Tomin'
import sys

from ocelot.cpbd.elements import *
from ocelot.cpbd.optics import *
from ocelot.gui.accelerator import *
exec(open("injector.inp"))

lat = MagneticLattice(lattice)

'''
for elem in lat.sequence:
    if elem.type == "cavity":
        print elem.type, elem.f, elem.v, elem.delta_e
'''

tws0 = Twiss()
tws0.beta_x = 30
tws0.beta_y = 30
tws0.alpha_x = 7
tws0.alpha_y = 7.5

tws0.E = 0.001 * GeV
L = 0.
for elem in lat.sequence:
    L+=elem.l
    print L, elem.type, elem.id
# first assign energies to elements
tws = twiss(lat, tws0, nPoints=None)
plot_opt_func(lat, tws, top_plot="Dx")

lat.update_transfer_maps()

tws = twiss(lat, tws0, nPoints=None)
plot_opt_func(lat, tws, top_plot="Dy")

plt.show()


