'''
tuning fel bandwidth for flash
'''
from xframework.adaptors.genesis import *
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import *

#from xframework.adaptors.srwutil import *
from xframework.adaptors.genesis import *

from xframework.optics.elements import *
from xframework.optics.wavefront import *
from xframework.common.math import *

from scipy.interpolate import interp1d


def read_wf(file):

    #g = readGenesisOutput(file)
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    
    if rank == 0:
        g = readGenesisOutput(file)
    else:
        g = None

    g = comm.bcast(g, root=0)
    
    
    npoints = int(g('ncar'))
    zstop = g('zstop')
    delz = g('delz')
    xlamd = g('xlamd')
    xlamds = g('xlamds')
    nslice = int(g.nSlices)
    zsep = g('zsep')
    dgrid = g('dgrid')
    
    #print npoints, nslice, xlamds
    
    #slices = readRadiationFile(file+'.dfl', npoints=int(npoints))
    slices = readRadiationFile_mpi(comm=comm, fileName=file+'.dfl', npoints=npoints)
    
    if rank != 0: return
    
    ofs = []
    
    for i in xrange(len(slices)):
        slice = slices[i]
                
        of = ParaxialFieldSlice(lam=xlamds, nx=npoints, ny=npoints, size_x=dgrid/2, size_y =dgrid/2)
        of.mesh = Mesh(nx=of.nx, ny=of.ny, dtype = np.complex)
        of.mesh.x = -of.size_x
        of.mesh.y = -of.size_y
        
        of.mesh.dx = 2*(-of.mesh.x) / ( of.mesh.nx -1)
        of.mesh.dy = 2*(-of.mesh.y) / ( of.mesh.ny -1)
        
        x=0; y=0
        
        for i1 in xrange(of.mesh.nx):
            for i2 in xrange(of.mesh.ny):
                x = of.mesh.x + of.mesh.dx * i1
                y = of.mesh.y + of.mesh.dy * i2
                of.mesh[i1,i2] = slice[i1,i2]
                
                of.x[i1] = x
                of.y[i2] = y
            
        ofs.append(of)
            
    del slices
    return ofs

def plot_one(ofs, ax1, ax2, plot_slices=False):
    of = ofs[0]
    
    nx, ny = of.mesh.points.shape
    
    x = np.linspace(-of.size_x, of.size_x, of.mesh.nx) / 1.e-6
    x_full = np.linspace(-of.size_x, of.size_x, of.mesh.nx*10) / 1.e-6
    
    
    specs = np.real(np.zeros_like(of[:,ny/2]))
    sizes = np.real(np.zeros_like(of[:,ny/2]))
    
    
    for of in ofs:
        if plot_slices: ax1.plot(x, np.abs(of[:,ny/2])**2, 'b--')
        sizes += np.abs(of[:,ny/2])**2 / len(ofs)
    
    f = interp1d(x, sizes, kind='cubic')
    ax1.plot(x, sizes, 'bs')
    ax1.plot(x_full, f(x_full), 'b-', lw=2)
            
    for of in ofs:
        spec = fft.fft(of[:,ny/2])
    
        kx = np.fft.fftfreq(of.nx, d=of.size_x/of.nx)
        ky = np.fft.fftfreq(of.ny, d=of.size_y/of.ny)
    
        kx = np.roll(kx, len(kx)/2) / 1.e-6 / (2*pi)
        ky = np.roll(ky, len(ky)/2) / 1.e-6 / (2*pi)
        
        spec = np.roll(spec, len(ky)/2)
        
        specs += np.abs(spec[:]) / len(ofs)
        
        if plot_slices: ax2.plot(kx * of.lam, np.abs(spec), 'b--', lw=1)
    
    ax2.plot(kx* of.lam, specs, 'rs', lw=3)
    
    sig_xp = fwhm(kx* of.lam, specs)
    sig_x = fwhm(x, sizes)
    sig_x_2 = fwhm(x_full, f(x_full))
    print 'size:', sig_x, sig_x_2
    print 'divergence:', sig_xp
    return sig_x_2, sig_xp

if len(sys.argv) >= 2:
    n_files = len(sys.argv) - 1
    file = sys.argv[1]
else:
    n_files = 1
    file = '/home/iagapov/tmp/run_13/run.13.gout'

from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()


if rank ==0 :
    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    ax1.grid(True)
    ax1.set_xlabel(r'[$mu m$]')
    ax2 = fig.add_subplot(212)
    ax2.grid(True)
    ax2.set_xlabel(r'[$mu rad$]')


if n_files ==1:
    ofs = read_wf(file=file)
    if rank ==0 : plot_one(ofs, ax1, ax2, plot_slices=True)
else:
    sig_x = []
    sig_xp = []
    for i in xrange(n_files):
        ofs = read_wf(file=sys.argv[i+1])
        if rank ==0: 
		s,sx = plot_one(ofs, ax1, ax2, plot_slices=False)
		sig_x.append(s)
		sig_xp.append(sx)
		
    if rank == 0:
    	print sig_x
	print sig_xp



#propagate_fourier(of, dz=7)
#z,sig = get_waist(of, dz=1.0, n=20)

'''
wfr = SRWLWfr()
nx = 51
wfr.allocate(1, nx, nx)


Ex = np.ones([nx,nx])
Ey = np.ones([nx,nx])

wfr.arEx = of.mesh.points.reshape(-1)
wfr.arEy = 0*Ey.reshape(-1)


wfr.mesh.zStart =  0.0 #Longitudinal Position [m] at which Electric

mesh_x = 1.e-3 # m
wfr.mesh.eStart =  100.0 #Initial Photon Energy [eV]
wfr.mesh.eFin   =  100.0 #Final Photon Energy [eV]
wfr.mesh.xStart = -mesh_x #Initial Horizontal Position [m]
wfr.mesh.xFin   =  mesh_x #Final Horizontal Position [m]
wfr.mesh.yStart = -mesh_x #Initial Vertical Position [m]
wfr.mesh.yFin   =  mesh_x #Final Vertical Position [m]
'''

plt.show()

