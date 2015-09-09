__author__ = 'Sergey Tomin'
import sys
ind = sys.path[0].find("repository")
sys.path.append(sys.path[0][:ind]+ "repository\ocelot")

from ocelot.cpbd.beam import *
from ocelot.cpbd.track import *
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


nturns = 1000


nx = 80
ny = 50

x_array = linspace(-0.0401, 0.04, nx)
#y_array = linspace(0, 0.050, ny)
y_array = linspace(0.0001, 0.04, ny)

start = time()
pxy_list = create_track_list(x_array, y_array, p_array=[0.])
pxy_list = tracking_mpi( mpi_comm, lat, nturns, pxy_list,  nsuperperiods=1, order=1, save_track=False)
if rank == 0:
    print( time() - start)
    da = array(map(lambda pxy: pxy.turn, pxy_list))
    np.savetxt("da.txt", (da))
    b = []
    for x, y in zip(x_array, y_array):
        a = [x, y]
        b.append(array([x,y]))
    np.savetxt("da_axis.txt", array(b))