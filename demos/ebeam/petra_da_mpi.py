__author__ = 'Sergey Tomin'
import sys
ind = sys.path[0].find("repository")

sys.path.append(sys.path[0][:ind] + "repository")
print sys.path[-1]
from ocelot.cpbd.beam import *
from ocelot.cpbd.track import *
from time import time
from mpi4py import MPI
import pickle
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
lat = merge_drifts(lat)

nturns = 10


nx = 80
ny = 50

x_array = linspace(-0.0401, 0.04, nx)
#y_array = linspace(0, 0.050, ny)
y_array = linspace(0.0001, 0.04, ny)

start = time()
pxy_list = create_track_list(x_array, y_array, p_array=[0.])
pxy_list = tracking_mpi( mpi_comm, lat, nturns, pxy_list,  nsuperperiods=1, order=3, save_track=True)
if rank == 0:
    print( time() - start)
    da = array(map(lambda pxy: pxy.turn, pxy_list))
    data = {"x_array": x_array, "y_array": y_array, "da": da}
    with open("da.txt",'w') as f:
        pickle.dump(data, f)
    #pickle.dump(y_array, "da_test.txt")
    #pickle.dump(da, "da_test.txt")
    #f = open("da_test.txt", "w")
    #f.write("# x: " + str(x_array[0]) + ", " + str(x_array[-1]) + ", " + str(nx) + "\n")
    #f.write("# y: " + str(y_array[0]) + ", " + str(y_array[-1]) + ", " + str(ny) + "\n")
    #for d in da:
    #    f.write(d)
    #f.close()
    #np.savetxt("da.txt", da)
    #b = []
    #for x, y in zip(x_array, y_array):
    #    a = [x, y]
    #    b.append(array([x,y]))
    #np.savetxt("da_axis.txt", array(b))