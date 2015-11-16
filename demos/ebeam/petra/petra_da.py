__author__ = 'Sergey Tomin'

import sys
ind = sys.path[0].find("petraIII")
#sys.path.append(sys.path[0][:ind])
ind4mpi = sys.path[0].find("siberia2")
sys.path.append(sys.path[0][:ind4mpi])
#print sys.path[0][:ind4mpi]
#print sys.path

from ocelot.cpbd.track import *
from ocelot.cpbd.beam import *

#from ocelot.adaptors.madx import lattice_str_from_madx, madx_seq2ocelot_seq
#from ocelot.cpbd.io import *

from time import time
from mpi4py import MPI


mpi_comm = MPI.COMM_WORLD
size = mpi_comm.Get_size()
rank = mpi_comm.Get_rank()


beam = Beam()
beam.E = 6.
beam.sigma_E = 0.001
beam.I = 0.1


tw0 = Twiss(beam)

exec( open("petra3.inp" ))
lat = MagneticLattice(lattice)

#for elem in lat.sequence:
#    if elem.type == "drift":
#        print elem.type, elem.id, elem.l, elem.k2
#        print elem.transfer_map.R
#        print elem.transfer_map.T
tws=twiss(lat, tw0)

print "Qx = ", tws[-1].mux/2/pi, "  Qy = ", tws[-1].muy/2/pi

#compensate_chromatism(lat, tws[0], ksi_x_comp = 0, ksi_y_comp = 0,  nsuperperiod = 6)

from ocelot.gui.accelerator import *
plot_opt_func(lat, tws)


k_error = 0
err_list = {"quadrupole": {"offset": k_error*0.1e-3, "dtilt": k_error*0.0001},
            "sbend":{"dtilt": k_error*0.0001}, "rbend":{"dtilt": k_error*0.0001}, "bend":{"dtilt": k_error*0.0001}}

#print "error = ", errors[1][3]


nturns = 200


nx = 80
ny = 50

x_array = linspace(-0.0401, 0.04, nx)
#y_array = linspace(0, 0.050, ny)
y_array = linspace(0.0001, 0.04, ny)


start = time()

pxy_list = create_track_list(x_array, y_array, p_array=[0])
pxy_list = tracking_mpi(mpi_comm, lat, nturns, pxy_list, errors=err_list, nsuperperiods=1, order=2)



if rank == 0:
    print "time exec = ", time() - start
    pxy_list = freq_analysis(pxy_list, lat, nturns, harm = True)
    da_contr = contour_da(pxy_list, nturns)
    da_mux = array(map(lambda pxy: pxy.mux, pxy_list))
    da_muy = array(map(lambda pxy: pxy.muy, pxy_list))
    da = array(map(lambda pxy: pxy.turn, pxy_list))


def phase_space_x(pxy_list, nturns):
    pxy_blue_x = []
    pxy_blue_xp = []
    pxy_red_x = []
    pxy_red_xp = []
    pxy_stable = stable_particles(pxy_list, nturns)
    x_stable = np.unique(np.sort(map(lambda pxy: pxy.x, pxy_stable)))
    x_stable = x_stable[x_stable>=0]
    for i, x in enumerate(x_stable):
        if i % 2 == 0:
            pxy = nearest_particle(pxy_stable, xi = x, yi = 0)
            pxy_blue_x.extend(pxy.get_x())
            pxy_blue_xp.extend(pxy.get_xp())
        elif i%2 == 1:
            pxy = nearest_particle(pxy_stable, xi = x, yi = 0)
            pxy_red_x.extend(pxy.get_x())
            pxy_red_xp.extend(pxy.get_xp())
    return pxy_blue_x, pxy_blue_xp, pxy_red_x,pxy_red_xp

def phase_space_y(pxy_list, nturns):
    pxy_blue = []
    pxy_blue_p = []
    pxy_red = []
    pxy_red_p = []
    pxy_stable = stable_particles(pxy_list, nturns)
    y_stable = np.unique(np.sort(map(lambda pxy: pxy.y, pxy_stable)))
    y_stable = y_stable[y_stable>=0]
    #print x_stable
    for i, y in enumerate(y_stable):
        #print x
        if i % 2 == 0:
            pxy = nearest_particle(pxy_stable, xi = 0, yi = y)
            #print "1 = ", pxy, pxy.x, pxy.y
            #print pxy.p_list
            pxy_blue.extend(pxy.get_y())
            pxy_blue_p.extend(pxy.get_yp())
        elif i%2 == 1:
            pxy = nearest_particle(pxy_stable, xi = 0, yi = y)
            #print "2 = ", pxy, pxy.x, pxy.y
            pxy_red.extend(pxy.get_y())
            pxy_red_p.extend(pxy.get_yp())
    return pxy_blue, pxy_blue_p, pxy_red,pxy_red_p

if rank == 0:

    pxy_blue_y, pxy_blue_py, pxy_red_y,pxy_red_py = phase_space_y(pxy_list, nturns)
    pxy_blue_x, pxy_blue_px, pxy_red_x,pxy_red_px = phase_space_x(pxy_list, nturns)
    plt.figure("horizontal phase trajectories")
    plt.plot(pxy_blue_x, pxy_blue_px, "r.", pxy_red_x, pxy_red_px, "r.")
    plt.grid(True)
    plt.figure("vertical phase trajectories")
    plt.plot(pxy_blue_y, pxy_blue_py, "b.", pxy_red_y, pxy_red_py, "b.")
    plt.grid(True)
    plt.show()
    pxy1 = nearest_particle(pxy_list, xi = 0.002, yi = 0.001)
    print pxy1.x, pxy1.y
    pxy2 = nearest_particle(pxy_list, xi = 0.015, yi = 0.015)
    print pxy2.x, pxy2.y

    fqx, ftx = spectrum(pxy1.get_x())
    fqy, fty = spectrum(pxy1.get_y())
    fqx2, ftx2 = spectrum(pxy2.get_x())
    fqy2, fty2 = spectrum(pxy2.get_y())
    plt.figure(1)
    plt.title("point 1")
    plt.plot(fqx, ftx, "r")
    plt.legend("X")
    plt.grid(True)

    plt.figure(2)
    plt.title("point 1")
    plt.plot(fqy, fty, "b")
    plt.legend("Y")
    plt.grid(True)

    plt.figure(21)
    plt.title("point 2")
    plt.plot(fqx2, ftx2, "r")
    plt.legend("X")
    plt.grid(True)

    plt.figure(22)
    plt.title("point 2")
    plt.plot(fqy2, fty2, "b")
    plt.legend("Y")
    plt.grid(True)

    plt.figure(3)
    plt.title("point 1")
    plt.plot(pxy1.get_x()*1000., pxy1.get_xp()*1000., "r.")
    #plt.legend("X")
    plt.xlabel("x, mm")
    plt.ylabel("px, mrad")
    plt.grid(True)

    plt.figure(32)
    plt.title("point 1")
    plt.plot(pxy1.get_y()*1000., pxy1.get_yp()*1000., "b.")
    #plt.legend("Y")
    plt.xlabel("y, mm")
    plt.ylabel("py, mrad")
    plt.grid(True)

    plt.figure(6)
    plt.title("point 2")
    plt.plot(pxy2.get_x()*1000., pxy2.get_xp()*1000., "r.")
    #plt.legend("X")
    plt.xlabel("x, mm")
    plt.ylabel("px, mrad")
    plt.grid(True)

    plt.figure(4)
    plt.title("point 2")
    plt.plot(pxy2.get_y()*1000., pxy2.get_yp()*1000., "b.")
    plt.xlabel("y, mm")
    plt.ylabel("py, mrad")
    #plt.legend("Y")
    plt.grid(True)

if rank == 0:
    pxy_list_stl = stable_particles(pxy_list, nturns)
    R1 = []
    R2 = []
    R3 = []
    R4 = []
    R5 = []
    R6 = []
    R7 = []
    for pxy in pxy_list_stl:
        r = sqrt(pxy.x*pxy.x + pxy.y*pxy.y)
        if r<0.005:
            R1.append(pxy)
        if 0.005 <= r <0.01:
            R2.append(pxy)
        if 0.01 <= r <0.015:
            R3.append(pxy)
        if 0.015 <= r <0.02:
            R4.append(pxy)
        if 0.02 <= r <0.025:
            R5.append(pxy)
        if 0.028 <= r <0.033:
            R6.append(pxy)
        if r >=0.035:
            R7.append(pxy)
    #print len(R1), len(R2), len(R3),len(R4), len(R5), len(R6)
    plt.figure(5)

    plt.plot(map(lambda p:p.mux, R1), map(lambda p:p.muy, R1), "ro")
    plt.plot(map(lambda p:p.mux, R2), map(lambda p:p.muy, R2), "bo")
    plt.plot(map(lambda p:p.mux, R3), map(lambda p:p.muy, R3), "go")
    plt.plot(map(lambda p:p.mux, R4), map(lambda p:p.muy, R4), "co")
    #plt.plot(map(lambda p:p.mux, R5), map(lambda p:p.muy, R5), "m.")
    #plt.plot(map(lambda p:p.mux, R6), map(lambda p:p.muy, R6), "y.")
    #plt.plot(map(lambda p:p.mux, R7), map(lambda p:p.muy, R7), "k.")
    plt.legend(["r = 5 mm", "r = 10 mm", "r = 15 mm", "r = 20 mm"])
    resonans_diag(Qx = 0, Qy = 0, order=5)
    plt.xlabel("Qx")
    plt.ylabel("Qy")
    #plt.legend("Y")
    plt.grid(True)
    plt.show()

if rank == 0:

    show_mu(da_contr, da_mux, da_muy, x_array, y_array)
    show_da(da, x_array, y_array)






"""
import multiprocessing
start = time.time()
jobs = []

for i in range(4):
    nturns = 100
    x_array = linspace(-0.1, 0.1,20)
    y_array = linspace(0, 0.1, 10)
    out_da = zeros((len(x_array),len(y_array)))
    p = multiprocessing.Process(target=track_da, args=(lat, nturns, x_array, y_array, out_da))
    jobs.append(p)
    p.start()
#da = track_da(lat,100)
print "time execution = ", time.time() - start, "  sec"
"""

"""
f=plt.figure()
f.canvas.set_window_title('Betas [m]')
p1, = plt.plot(map(lambda p: p.s, tws), map(lambda p: p.beta_x, tws), lw=2.0)
p2, = plt.plot(map(lambda p: p.s, tws), map(lambda p: p.beta_y, tws), lw=2.0)
#p3, = plt.plot(map(lambda p: p.s, tws), map(lambda p: p.H, tws), lw=2.0)
#p4, = plt.plot(map(lambda p: p.s, tws), map(lambda p: p.K, tws), lw=2.0)
plt.grid(True)
plt.legend([p1,p2], [r'$\beta_x$',r'$\beta_y$', r'$D_x$'])

f=plt.figure()
f.canvas.set_window_title('Dispersion [m]')
p1, = plt.plot(map(lambda p: p.s, tws), map(lambda p: p.dx, tws), lw=2.0)
p2, = plt.plot(map(lambda p: p.s, tws), map(lambda p: p.dy, tws), lw=2.0)
plt.grid(True)
plt.legend([p1,p2], [r'$D_x$', r'$D_y$'])
#print map(lambda p: p.x, tws)

f=plt.figure()
f.canvas.set_window_title('Orbit [m]')
p1, = plt.plot(map(lambda p: p.s, particle_list), map(lambda p: p.x, particle_list), lw=2.0)
p2, = plt.plot(map(lambda p: p.s, particle_list), map(lambda p: p.y, particle_list), lw=2.0)

#p3, = plt.plot(map(lambda p: p[0].s, mon_dict), map(lambda p: p[0].x, mon_dict), lw=2.0)
#p4, = plt.plot(map(lambda p: p[0].s, mon_dict), map(lambda p: p[0].y, mon_dict), lw=2.0)
#plt.grid(True)
#plt.legend([p1,p2, p3,p4], [r'$x$', r'$y$', r'$x_m$',r'$y_m$'])


plt.show()
"""