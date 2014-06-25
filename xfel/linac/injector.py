__author__ = 'Sergey Tomin'
import sys
ind = sys.path[0].find("desy")
sys.path.append(sys.path[0][:ind])

from ocelot.cpbd.elements import *
from ocelot.cpbd.optics import *
from ocelot.gui.accelerator import *
exec(open("injector.inp"))

lat = MagneticLattice(lattice)

for elem in lat.sequence:
    if elem.type == "cavity":
        print elem.type, elem.f, elem.v, elem.delta_e


tws0 = Twiss()
tws0.beta_x = 1
tws0.beta_y = 1
tws0.alpha_x = 0
tws0.alpha_y = 0
tws = twiss(lat, tws0)
plot_opt_func(lat, tws)