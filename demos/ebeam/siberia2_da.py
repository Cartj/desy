__author__ = 'Sergey Tomin'
import sys
ind = sys.path[0].find("scripts")
sys.path.append(sys.path[0][:ind])

from ocelot.cpbd.optics import *
from ocelot.cpbd.elements import *
from ocelot.cpbd.e_beam_params import *
from ocelot.cpbd.track import *
from ocelot.cpbd.chromaticity import *
from ocelot.gui.accelerator import *
#from codes.genera.src.python.trajectory import undulator
import pylab as plt
from time import time
from copy import deepcopy


#resonans_diag(Qx = 0, Qy = 0, order=3)

def phase_space(x_stable, y_stable):
    pxy_blue = []
    pxy_blue_p = []
    pxy_red = []
    pxy_red_p = []

    for i, x in enumerate(x_stable):
        if i % 2 == 0:
            pxy = nearest_particle(pxy_stable, xi = x_stable[i], yi = y_stable[i])
            #print "1 = ", pxy, pxy.x, pxy.y
            #print pxy.p_list
            pxy_blue.extend(pxy.get_x())
            pxy_blue_p.extend(pxy.get_xp())
        elif i%2 == 1:
            pxy = nearest_particle(pxy_stable, xi = x_stable[i], yi = y_stable[i])
            #print "2 = ", pxy, pxy.x, pxy.y
            pxy_red.extend(pxy.get_x())
            pxy_red_p.extend(pxy.get_xp())
    return pxy_blue, pxy_blue_p, pxy_red, pxy_red_p



#exec( open("../../repository/siberia2/siberia2.inp" ))
exec( open("siberia2.inp" ))
#exec( open(sys.path[0][:ind] + "repository/siberia2/siberia2.inp" ))
tw0 = Twiss(beam)
tw0.x = 0.1
lat = MagneticLattice(superperiod)


nturns = 1000


nx = 30
ny = 20

x_array = linspace(-0.06, 0.06, nx)

y_array = linspace(0.0001, 0.06, ny)


start = time()

start = time()

pxy_list = create_track_list(x_array, y_array, p_array=[0.])
pxy_list_2 = tracking(lat, nturns, deepcopy(pxy_list), order=2, nsuperperiods = 6)
pxy_list_1 = tracking(lat, nturns, deepcopy(pxy_list), order=1, nsuperperiods = 6)
rank = 0


if rank == 0:
    print "time exec = ", time() - start
    da2 = array(map(lambda pxy: pxy.turn, pxy_list_2))
    da1 = array(map(lambda pxy: pxy.turn, pxy_list_1))
    show_da(da2, x_array, y_array)
    show_da(da1, x_array, y_array)

if rank == 0:

    pxy_stable = stable_particles(pxy_list_1, nturns)
    x_stable = np.unique(np.sort(map(lambda pxy: pxy.x, pxy_stable)))
    x_stable = x_stable[x_stable>=0]
    pxy_blue_x, pxy_blue_xp, pxy_red_x, pxy_red_xp = phase_space(x_stable, np.zeros(len(x_stable)))

    y_stable = np.unique(np.sort(map(lambda pxy: pxy.y, pxy_stable)))
    y_stable = y_stable[y_stable>=0]
    pxy_blue_y, pxy_blue_yp, pxy_red_y, pxy_red_yp = phase_space(np.zeros(len(y_stable)), y_stable)
    plt.figure(1)
    plt.plot(pxy_blue_x, pxy_blue_xp, "r.", pxy_red_x,pxy_red_xp, "b.")
    plt.xlabel("X, m")
    plt.ylabel("X', rad")
    plt.figure(2)
    plt.plot(pxy_blue_y, pxy_blue_yp, "r.", pxy_red_y,pxy_red_yp, "b.")
    plt.xlabel("Y, m")
    plt.ylabel("Y', rad")
    plt.show()
