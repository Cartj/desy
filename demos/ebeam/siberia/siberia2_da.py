__author__ = 'Sergey Tomin'
import sys
ind = sys.path[0].find("scripts")
sys.path.append(sys.path[0][:ind])

from desy.demos.ebeam.siberia.siberia2_lattice import*
from ocelot import *
from ocelot.gui import *
#from codes.genera.src.python.trajectory import undulator
from pylab import *
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



#exec( open("../../repository/siberia2/siberia2_lattice.py" ))
#print(open("siberia2_lattice.py" ))
#exec( open("siberia2_lattice.py" ))
#exec( open(sys.path[0][:ind] + "repository/siberia2/siberia2_lattice.py" ))
tw0 = Twiss(beam)
tw0.x = 0.1
lat = MagneticLattice(superperiod)
R = lattice_transfer_map(lat, energy=2.5)
print(R)
#tws0 = Twiss()
#tws = twiss(lat, tws0)
#plot_opt_func(lat, tws)
compensate_chromaticity(lat, ksi_x_comp=0, ksi_y_comp=0,  nsuperperiod=6)
L = 0
#for elem in lat.sequence:
#    L += elem.l
#    if elem.type != "drift":
#        print elem.id, ":", elem.id, ", at = ", L - elem.l/2.
#for elem in lat.sequence:
#    if elem.id == "SD":
#        print elem.transfer_map.T
#from ocelot.cpbd.chromaticity import *
#DZ(lat, energy=0)
#exit(0)

nturns = 400


nx = 40
ny = 20

x_array = linspace(-0.06, 0.06, nx)

y_array = linspace(0.0001, 0.06, ny)


start = time()



pxy_list = create_track_list(x_array, y_array, p_array=[0.])
pxy_list_2 = track_nturns(lat, nturns, deepcopy(pxy_list), order=1, nsuperperiods = 6)
pxy_list_1 = track_nturns(lat, nturns, deepcopy(pxy_list), order=2, nsuperperiods = 6)
rank = 0


if rank == 0:
    print ("time exec = ", time() - start)
    da2 = array([pxy.turn for pxy in pxy_list_2])
    #print(da2)
    da1 = array([pxy.turn for pxy in pxy_list_1])

    show_da(da2, x_array, y_array)
    show_da(da1, x_array, y_array)

if rank == 0:

    pxy_stable = stable_particles(pxy_list_1, nturns)
    x_stable = np.unique(np.sort([pxy.x for pxy in pxy_stable]))
    x_stable = x_stable[x_stable>=0]
    pxy_blue_x, pxy_blue_xp, pxy_red_x, pxy_red_xp = phase_space(x_stable, np.zeros(len(x_stable)))

    y_stable = np.unique(np.sort([pxy.y for pxy in pxy_stable]))
    y_stable = y_stable[y_stable>=0]
    pxy_blue_y, pxy_blue_yp, pxy_red_y, pxy_red_yp = phase_space(np.zeros(len(y_stable)), y_stable)
    plt.figure(1)
    plt.plot(pxy_blue_x, pxy_blue_xp, "r.", pxy_red_x,pxy_red_xp, "b.")
    plt.xlabel("X, m")
    plt.title("Brown")
    plt.ylabel("X', rad")
    plt.figure(2)
    plt.title("Brown")
    plt.plot(pxy_blue_y, pxy_blue_yp, "r.", pxy_red_y,pxy_red_yp, "b.")
    plt.xlabel("Y, m")
    plt.ylabel("Y', rad")

    # second order symplectic maps

    pxy_stable = stable_particles(pxy_list_2, nturns)
    x_stable = np.unique(np.sort([pxy.x for pxy in pxy_stable]))
    x_stable = x_stable[x_stable>=0]
    pxy_blue_x, pxy_blue_xp, pxy_red_x, pxy_red_xp = phase_space(x_stable, np.zeros(len(x_stable)))

    y_stable = np.unique(np.sort([pxy.y for pxy in pxy_stable]))
    y_stable = y_stable[y_stable>=0]
    pxy_blue_y, pxy_blue_yp, pxy_red_y, pxy_red_yp = phase_space(np.zeros(len(y_stable)), y_stable)
    plt.figure(3)
    plt.title("Symplectic")
    plt.plot(pxy_blue_x, pxy_blue_xp, "r.", pxy_red_x,pxy_red_xp, "b.")
    plt.xlabel("X, m")
    plt.ylabel("X', rad")
    plt.figure(4)
    plt.title("Symplectic")
    plt.plot(pxy_blue_y, pxy_blue_yp, "r.", pxy_red_y,pxy_red_yp, "b.")
    plt.xlabel("Y, m")
    plt.ylabel("Y', rad")



    plt.show()
