__author__ = 'Sergey Tomin'
import sys
ind = sys.path[0].find("desy")
sys.path.append(sys.path[0][:ind])
print sys.path[0][:ind]
from ocelot.adaptors.mad8 import lattice_str_from_mad8
from ocelot.cpbd.elements import *
from ocelot.cpbd.io import lat2input
from numpy import *

from ocelot.cpbd.elements import *
from ocelot.cpbd.optics import *
from ocelot.gui.accelerator import *
exec(open("injector.inp"))
emass = 0.511e-3

name = "desy/xfel/mad_input/XFEL.seq"
#lattice_str_from_mad8(sys.path[0][:ind] + name) # convert MAD input file to XCODE input file


name = "desy/xfel/mad_input/XFEL.inp"

exec( open(sys.path[0][:ind] + name))


file_name = "xfelall.inp"
#tw0 = Twiss(Beam())
lat = MagneticLattice(xfelall, energy = 2.5)
print lat.totalLen, len(lat.sequence)
tws0 = Twiss()
tws0.beta_x = 30
tws0.beta_y = 30
tws0.alpha_x = 7
tws0.alpha_y = 7.5

tws0.E = 0.000 * GeV

tws = twiss(lat, tws0, nPoints=None)
plot_opt_func(lat, tws, top_plot=["Dy", "Dx"])
#for elem in lat.sequence:
#    if elem.tilt != 0:
#        print elem.id, elem.type, elem.l, elem.tilt

def collect_drifts(lat):
    drift = 0
    L = 0.
    seq =[]
    for i, elem in enumerate(lat.sequence):
        if elem.type in ["drift", "monitor"]:
            #print elem.id, elem.tilt, elem.l
            drift = 1
            L += elem.l
            if i == len(lat.sequence) -1:
                L =  around(L, decimals = 6)
                seq.append(Drift(l = L, id = "d" + str(int(L*100000 + 10000000))[1:]))
        else:
            if drift > 0 and L>0.:
                L =  around(L, decimals = 6)
                seq.append(Drift(l = L, id = "d" + str(int(L*100000 + 10000000))[1:]))
                drift = 0
            seq.append(elem)
            L = 0.
    return MagneticLattice(seq)



lat = collect_drifts(lat)

print emass

lines = lat2input(lat)

f = open(file_name, 'w')
f.writelines(lines)
f.close()



exec(open(file_name))

lat = MagneticLattice(lattice)

print lat.totalLen
tws0 = Twiss()
tws0.beta_x = 30
tws0.beta_y = 30
tws0.alpha_x = 7
tws0.alpha_y = 7.5

tws0.E = 0.0001 * GeV
L = 0.
for elem in lat.sequence:
    L+=elem.l
    print L, elem.type, elem.id
# first assign energies to elements
tws = twiss(lat, tws0, nPoints=None)
plot_opt_func(lat, tws, top_plot=["Dy", "Dx"])

lat.update_transfer_maps()

#tws = twiss(lat, tws0, nPoints=None)
#plot_opt_func(lat, tws, top_plot=["Dy"])

plt.show()