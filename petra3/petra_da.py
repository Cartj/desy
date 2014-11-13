__author__ = 'Sergey Tomin'

from ocelot.cpbd.tracking import *
from time import time
from mpi4py import MPI
from ocelot.gui.accelerator import *

mpi_comm = MPI.COMM_WORLD
size = mpi_comm.Get_size()
rank = mpi_comm.Get_rank()


beam = Beam()
beam.E = 6
beam.sigma_E = 0.001
beam.I = 0.1

exec( open("petra_after_ext.inp"))


lat = MagneticLattice(lattice, energy = beam.E)

tw0 = Twiss(beam)
tws=twiss(lat, tw0)

print "Qx = ", tws[-1].mux/2/pi, "  Qy = ", tws[-1].muy/2/pi

#compensate_chromatism(lat, tws[0], ksi_x_comp = 0, ksi_y_comp = 0,  nsuperperiod = 6)

if rank == 0:
    plot_opt_func(lat, tws)
    plt.show()

k_error = 0
err_list = {"quadrupole": {"offset": k_error*0.1e-3, "dtilt": k_error*0.0001},
            "sbend":{"dtilt": k_error*0.0001}, "rbend":{"dtilt": k_error*0.0001}, "bend":{"dtilt": k_error*0.0001}}


nturns = 1096


nx = 130
ny = 70

x_array = linspace(-0.0401, 0.04, nx)
#y_array = linspace(0, 0.050, ny)
y_array = linspace(0.0001, 0.04, ny)


start = time()

pxy_list = create_track_list(x_array, y_array)
pxy_list = tracking_mpi(mpi_comm, lat, nturns, pxy_list, errors = err_list, nsuperperiods = 1)



if rank == 0:
    print "time exec = ", time() - start
    pxy_list = freq_analysis(pxy_list, lat, nturns, harm = True)
    da_contr = contour_da(pxy_list, nturns)
    da_mux = array(map(lambda pxy: pxy.mux, pxy_list))
    da_muy = array(map(lambda pxy: pxy.muy, pxy_list))
    da = array(map(lambda pxy: pxy.turn, pxy_list))

    show_mu(da_contr, da_mux, da_muy, x_array, y_array)
    show_da(da, x_array, y_array)


