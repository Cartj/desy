'''
functions common to xfel decks
'''


import scipy.special as sf
import scipy.integrate as integrate
from numpy.polynomial.chebyshev import *
from numpy import *
import numpy as np

from copy import copy, deepcopy

from ocelot.cpbd.elements import Element, Quadrupole, RBend, Drift, Undulator, MagneticLattice, Hcor, Vcor
from ocelot.cpbd.beam import Beam, ParticleArray
from ocelot.cpbd.optics import *

from ocelot.optics.utils import *

from ocelot.common.screen import Screen
#from ocelot.common.xio import XIO

#from ocelot.adaptors import srwutil as srw

import os, socket
from ocelot.utils.launcher import *


from ocelot.rad.sr import *
from ocelot.fel.fel import *
from ocelot.adaptors.genesis import *
from copy import deepcopy, copy

from pylab import *
params = {'backend': 'ps', 'axes.labelsize': 18, 'text.fontsize': 16, 'legend.fontsize': 24, 'xtick.labelsize': 32,  'ytick.labelsize': 32, 'text.usetex': True}
rcParams.update(params)
rc('text', usetex=True) # required to have greek fonts on redhat

def detune_k(lat, sig):
    lat2 = deepcopy(lat)
    n = 0
    for i in xrange(len(lat2.sequence)):
        print lat2.sequence[i].__class__
        if lat2.sequence[i].__class__ == Undulator:
            lat2.sequence[i] = deepcopy(lat.sequence[i]) 
            lat2.sequence[i].Kx = lat2.sequence[i].Kx * (1 + np.random.randn() * sig)
            n += 1

    return lat2

def detune_E(inp, beam, sig):
    # energy modulation
    inp.gamma0 = (beam.E + np.random.randn() * sig) / 0.000510998
    beam.emit_x = beam.emit_xn / inp.gamma0
    beam.emit_y = beam.emit_yn / inp.gamma0
    inp.rxbeam = np.sqrt (beam.emit_x * beam.beta_x )
    inp.rybeam = np.sqrt (beam.emit_y * beam.beta_y )


def taper(lat, k):
    lat2 = deepcopy(lat)
    n = 0
    for i in xrange(len(lat2.sequence)):
        if lat2.sequence[i].__class__ == Undulator:
            #print lat2.sequence[i].id, lat2.sequence[i].Kx
            lat2.sequence[i] = deepcopy(lat.sequence[i]) 
            lat2.sequence[i].Kx = lat2.sequence[i].Kx * k(n+1)
            n += 1

    return lat2



def rematch(beta_mean, l_fodo, qdh, lat, extra_fodo, beam, qf, qd):
    
    '''
    requires l_fodo to be defined in the lattice
    '''
    
    k, betaMin, betaMax, __ = fodo_parameters(betaXmean=beta_mean, L=l_fodo, verbose = True)
    
    k1 = k[0] / qdh.l
    
    tw0 = Twiss(beam)
    
    print 'before rematching k=%f %f   beta=%f %f alpha=%f %f' % (qf.k1, qd.k1, tw0.beta_x, tw0.beta_y, tw0.alpha_x, tw0.alpha_y)

        
    extra = MagneticLattice(extra_fodo, energy=lat.energy)
    tws=twiss(extra, tw0)
    tw2 = tws[-1]
    
    tw2m = Twiss(tw2)
    tw2m.beta_x = betaMin[0]
    tw2m.beta_y = betaMax[0]
    tw2m.alpha_x = 0.0
    tw2m.alpha_y = 0.0
    tw2m.gamma_x = (1 + tw2m.alpha_x * tw2m.alpha_x) / tw2m.beta_x
    tw2m.gamma_y = (1 + tw2m.alpha_y * tw2m.alpha_y) / tw2m.beta_y

    
    #k1 += 0.5
    
    qf.k1 = k1
    qd.k1 = -k1
    qdh.k1 = -k1
    
    lat.update_transfer_maps()
    extra.update_transfer_maps()
    
    m1 = lattice_transfer_map( extra )
    m1.R = np.linalg.inv(m1.R)
    
    tw0m = m1.map_x_twiss(tw2m)
    print 'after rematching k=%f %f   beta=%f %f alpha=%f %f' % (qf.k1, qd.k1, tw0m.beta_x, tw0m.beta_y, tw0m.alpha_x, tw0m.alpha_y)

    beam.beta_x, beam.alpha_x = tw0m.beta_x, tw0m.alpha_x
    beam.beta_y, beam.alpha_y = tw0m.beta_y, tw0m.alpha_y


def run(inp, launcher):

    os.makedirs(inp.run_dir)
    open(inp.run_dir + '/lattice.inp','w').write( inp.lattice_str )
    open(inp.run_dir + '/tmp.cmd','w').write("tmp.gen\n")
    open(inp.run_dir + '/tmp.gen','w').write(inp.input())   
    
    if inp.beamfile != None:
        open(inp.run_dir + '/tmp.beam','w').write(inp.beam_file_str)
    
    launcher.dir = inp.run_dir
    launcher.prepare()
    launcher.launch()
    
    g = readGenesisOutput( inp.run_dir + '/run.' + str(inp.runid) + '.gout')
    return g


def get_genesis_launcher(nproc = 1):
    host = socket.gethostname()
    
    launcher = MpiLauncher()
    
    if host.startswith('kolmogorov'):
        launcher.program = '/home/iagapov/workspace/xcode/codes/genesis/genesis < tmp.cmd | tee log'
    if host.startswith('it-hpc'):
        launcher.program = '/data/netapp/xfel/products/genesis/genesis < tmp.cmd | tee log'
        launcher.mpiParameters ='-x LD_LIBRARY_PATH=/usr/local/lib:/opt/intel/2011/lib/intel64:/usr/lib64/openmpi-intel/lib:/data/netapp/it/tools/gcc47/lib64'
        launcher.mpiParameters = launcher.mpiParameters + ' -hostfile '+ os.path.abspath('.') +'/hosts.txt'
    
    launcher.nproc = nproc
    
    return launcher


def get_data_dir():
    host = socket.gethostname()
        
    if host.startswith('it-hpc'):
        return '/data/netapp/xfel/iagapov/xcode_data/'
    return '/tmp/'


def show_output(g, show_field = False, output_file = None, show_slice=0):
    h = 4.135667516e-15
    c = 299792458.0
    xrms = np.array(g.sliceValues[g.sliceValues.keys()[show_slice]]['xrms'])
    yrms = np.array(g.sliceValues[g.sliceValues.keys()[show_slice]]['yrms'])
    power = 0*np.array(g.sliceValues[g.sliceValues.keys()[show_slice]]['power'])
    
    nslice = len(g.sliceValues.keys())
    power_s = np.zeros(nslice)
    for i in xrange( nslice ):
        power +=  np.array(g.sliceValues[g.sliceValues.keys()[i]]['power']) / nslice
        pend =  g.sliceValues[g.sliceValues.keys()[i]]['power'][-1]
        power_s[i] = pend
        
    f = plt.figure()
    f.add_subplot(131), plt.plot(g.z, xrms, lw=3), plt.plot(g.z, yrms, lw=3), plt.grid(True)
    f.add_subplot(132), plt.plot(g.z, power, lw=3), plt.grid(True)
    I = np.array(g.I)
    t = 1.0e+15 * float(g('zsep')) * float(g('xlamds')) * np.arange(0,len(I)) / c
    f.add_subplot(133), plt.plot(t,power_s, lw=3), plt.plot(t,np.array(I) * np.max(power_s) / np.max(I), lw=3), plt.grid(True)
    
    npoints = g('ncar')
    zstop = g('zstop')
    delz = g('delz')
    xlamd = g('xlamd')
    xlamds = g('xlamds')
    nslice = g('nslice')
    zsep = g('zsep')
    dgrid = g('dgrid')
    
    smax = nslice * zsep * xlamds   
                 
    print 'wavelength ', xlamds
    
    if show_field:
        #from mpi4py import MPI
        
        #comm = MPI.COMM_WORLD
        #slices = readRadiationFile_mpi(comm=comm, fileName=file+'.dfl', npoints=npoints)
        slices = readRadiationFile(fileName=output_file + '.dfl', npoints=npoints)
        print 'slices:', slices.shape
    
        E = np.zeros_like(slices[0,:,:])
        for i in xrange(slices.shape[0]): E += np.multiply(slices[i,:,:], slices[i,:,:].conjugate())
    
        #Z = E*E.conjugate()
    
        fig = plt.figure()
        fig.add_subplot(111)
        m = plt.imshow(abs(E),cmap='YlOrRd')
        z = abs(slices[100,:,:])
    
        fig = plt.figure()
        P = np.zeros_like(slices[:,0,0])
        for i in xrange(len(P)):
            #s = slices[i,int(npoints/2),int(npoints/2)]
            s = sum( np.abs(np.multiply(slices[i,:,:], slices[i,:,:])) )
            P[i] = abs(s*s.conjugate()) * (dgrid**2 / npoints )**2  
    
        plot(P)
    plt.figure()
    plt.plot(np.linspace(-dgrid/2,dgrid/2,npoints),abs(E[:,int(npoints/2)]), lw=3), plt.grid(True)
            
    plt.show()


def show_output_old(g, show_field = False, output_file = None):

    xrms = np.array(g.sliceValues[g.sliceValues.keys()[0]]['xrms'])
    yrms = np.array(g.sliceValues[g.sliceValues.keys()[0]]['yrms'])
    power = np.array(g.sliceValues[g.sliceValues.keys()[0]]['power'])
    
    nslice = len(g.sliceValues.keys())
    power_s = np.zeros(nslice)
    for i in xrange( nslice ):
        power +=  np.array(g.sliceValues[g.sliceValues.keys()[i]]['power']) / nslice
        pend =  g.sliceValues[g.sliceValues.keys()[i]]['power'][-1]
        power_s[i] = pend
        
    f = plt.figure()
    f.add_subplot(131), plt.plot(g.z, xrms, lw=3), plt.plot(g.z, yrms, lw=3), plt.grid(True)
    f.add_subplot(132), plt.plot(g.z, power, lw=3), plt.grid(True)
    f.add_subplot(133), plt.plot(power_s, lw=3), plt.grid(True)
    
    npoints = g('ncar')
    zstop = g('zstop')
    delz = g('delz')
    xlamd = g('xlamd')
    xlamds = g('xlamds')
    nslice = g('nslice')
    zsep = g('zsep')
    dgrid = g('dgrid')
    
    smax = nslice * zsep * xlamds 
                     
    print 'npoints, nslice', npoints, nslice
    
    
    if show_field:
        #from mpi4py import MPI
        
        #comm = MPI.COMM_WORLD
        #slices = readRadiationFile_mpi(comm=comm, fileName=file+'.dfl', npoints=npoints)
        slices = readRadiationFile(fileName=output_file + '.dfl', npoints=npoints)
        print 'slices:', slices.shape
    
        E = np.zeros_like(slices[0,:,:])
        for i in xrange(slices.shape[0]): E += slices[i]
    
        Z = E*E.conjugate()
    
        fig = plt.figure()
        fig.add_subplot(111)
        m = plt.imshow(abs(E),cmap='YlOrRd')
        z = abs(slices[100,:,:])
    
        fig = plt.figure()
        P = np.zeros_like(slices[:,0,0])
        for i in xrange(len(P)):
            s = slices[i,int(npoints/2),int(npoints/2)]
        #s = sum(slices[i,:,:])
            P[i] = abs(s*s.conjugate()) * (dgrid**2 / npoints )**2  
    
        plot(P)
    
    plt.show()



'''
putting arbitrarily many plots on single figure
'''
def show_plots(displays, fig):
    n1 = (len(displays) -1 )/2 + 1
    n2 = (len(displays) -1) / n1 +1
    #print n1, n2
    fmt = str(n1)+ str(n2)
    print fmt
    
    for i in xrange(len(displays)):
        ax = fig.add_subplot(fmt + str(i+1))
        ax.grid(True)
        for f in displays[i].data:
            x,y = f(x = np.linspace(-10, 10, 100))
            ax.plot(x, y, '.')

    show()

class Display:
    def __init__(self, data=lambda x: (x, 0*x) , xlabel='',ylabel=''):
        self.data = (data,)
        self.xlabel = xlabel
        self.ylabel = ylabel



def plot_beam(fig, beam):
    
    ax = fig.add_subplot(321) 
    plt.grid(True)
    ax.set_xlabel(r'$\mu m$')
    p1,= plt.plot(1.e6 * np.array(beam.z),beam.I,'r',lw=3)
    plt.plot(1.e6 * beam.z[beam.idx_max],beam.I[beam.idx_max],'bs')
    
    ax = ax.twinx()
    
    p2,= plt.plot(1.e6 * np.array(beam.z),1.e-3 * np.array(beam.eloss),'g',lw=3)
    
    ax.legend([p1, p2],['I','Wake [KV/m]'])
    
    ax = fig.add_subplot(322) 
    plt.grid(True)
    ax.set_xlabel(r'$\mu m$')
    #p1,= plt.plot(1.e6 * np.array(beam.z),1.e-3 * np.array(beam.eloss),'r',lw=3)
    p1, = plt.plot(1.e6 * np.array(beam.z),beam.g0,'r',lw=3)
    ax = ax.twinx()
    p2, = plt.plot(1.e6 * np.array(beam.z),beam.dg,'g',lw=3)

    ax.legend([p1,p2],[r'$\gamma$',r'$\delta \gamma$'])
    
    ax = fig.add_subplot(323) 
    plt.grid(True)
    ax.set_xlabel(r'$\mu m$')
    p1, = plt.plot(1.e6 * np.array(beam.z),beam.ex, 'r', lw=3)
    p2, = plt.plot(1.e6 * np.array(beam.z),beam.ey, 'g', lw=3)
    plt.plot(1.e6 * beam.z[beam.idx_max],beam.ex[beam.idx_max], 'bs')
    
    ax.legend([p1,p2],[r'$\varepsilon_x$',r'$\varepsilon_y$'])
    #ax3.legend([p3,p4],[r'$\varepsilon_x$',r'$\varepsilon_y$'])
    
    
    ax = fig.add_subplot(324)
    plt.grid(True)
    ax.set_xlabel(r'$\mu m$')
    p1, = plt.plot(1.e6 * np.array(beam.z),beam.betax, 'r', lw=3)
    p2, = plt.plot(1.e6 * np.array(beam.z),beam.betay, 'g', lw=3)
    plt.plot(1.e6 * beam.z[beam.idx_max],beam.betax[beam.idx_max], 'bs')
    
    ax.legend([p1,p2],[r'$\beta_x$',r'$\beta_y$'])


    ax = fig.add_subplot(325)
    plt.grid(True)
    ax.set_xlabel(r'$\mu m$')
    p1, = plt.plot(1.e6 * np.array(beam.z),1.e6 * np.array(beam.x), 'r', lw=3)
    p2, = plt.plot(1.e6 * np.array(beam.z),1.e6 * np.array(beam.y), 'g', lw=3)
    
    ax.legend([p1,p2],[r'$x [\mu m]$',r'$y [\mu m]$'])


    ax = fig.add_subplot(326)
    plt.grid(True)
    ax.set_xlabel(r'$\mu m$')
    p1, = plt.plot(1.e6 * np.array(beam.z),1.e6 * np.array(beam.px), 'r', lw=3)
    p2, = plt.plot(1.e6 * np.array(beam.z),1.e6 * np.array(beam.py), 'g', lw=3)
    
    ax.legend([p1,p2],[r'$p_x [\mu rad]$',r'$p_y [\mu rad]$'])

def plot_beam_2(fig, beam, iplot=0):
    
    ax = fig.add_subplot(111) 
    plt.grid(True)
    
    if iplot == 0:
    
        ax.set_xlabel(r'$\mu m$')
        ax.set_ylabel('A')
        p1,= plt.plot(1.e6 * np.array(beam.z),beam.I,'r',lw=3)
        #plt.plot(1.e6 * beam.z[beam.idx_max],beam.I[beam.idx_max],'bs')
        
        ax = ax.twinx()
        ax.set_ylabel('KV/m')
        
        p2,= plt.plot(1.e6 * np.array(beam.z),1.e-3 * np.array(beam.eloss),'g',lw=3)
        
        ax.legend([p1, p2],['I',r'$E_{wake}$'])

    if iplot == 1:
    
        ax.set_xlabel(r'$\mu m$')
        #p1,= plt.plot(1.e6 * np.array(beam.z),1.e-3 * np.array(beam.eloss),'r',lw=3)
        p1, = plt.plot(1.e6 * np.array(beam.z),beam.g0,'r',lw=3)
        ax = ax.twinx()
        p2, = plt.plot(1.e6 * np.array(beam.z),beam.dg,'g',lw=3)
    
        ax.legend([p1,p2],[r'$\gamma$',r'$\delta \gamma$'])
    
    if iplot == 2:

        ax.set_xlabel(r'$\mu m$')
        ax.set_ylabel(r'$mm \cdot mrad$')
        p1, = plt.plot(1.e6 * np.array(beam.z),1.e6*np.array(beam.ex), 'r', lw=3)
        p2, = plt.plot(1.e6 * np.array(beam.z),1.e6*np.array(beam.ey), 'g', lw=3)
        #plt.plot(1.e6 * beam.z[beam.idx_max],beam.ex[beam.idx_max], 'bs')
        
        ax.legend([p1,p2],[r'$\varepsilon_x$',r'$\varepsilon_y$'])
        #ax3.legend([p3,p4],[r'$\varepsilon_x$',r'$\varepsilon_y$'])
    
    if iplot == 3:
    
        ax.set_xlabel(r'$\mu m$')
        ax.set_ylabel(r'$m$')
        p1, = plt.plot(1.e6 * np.array(beam.z),beam.betax, 'r', lw=3)
        p2, = plt.plot(1.e6 * np.array(beam.z),beam.betay, 'g', lw=3)
        #plt.plot(1.e6 * beam.z[beam.idx_max],beam.betax[beam.idx_max], 'bs')
        
        ax.legend([p1,p2],[r'$\beta_x$',r'$\beta_y$'])

'''
configurable to e.g. semi-empirical models
'''
class FelSimulator(object):
    
    def __init__(self):
        self.engine = 'genesis'
    
    def run(self):
        if self.engine == 'test_1d':
            w1 = read_signal(file_name=self.input, npad = self.npad , E_ref = self.E_ev)
            return w1, None
        if self.engine == 'test_3d':
            ''' produced  sliced field '''
            w1 = read_signal(file_name=self.input, npad = self.npad , E_ref = self.E_ev)
            s3d = Signal3D()
            s3d.fs = [w1, deepcopy(w1), deepcopy(w1), deepcopy(w1)]
            s3d.mesh_size = (2,2)            
            return s3d, None
        if self.engine == 'test_genesis':
            ''' read test sliced field '''
            g = readGenesisOutput(self.input)
            print 'read sliced field ', g('ncar'), g.nSlices
            slices = readRadiationFile(fileName=self.input + '.dfl', npoints=g('ncar'))            
            s3d = Signal3D()
            s3d.slices = slices
            s3d.mesh_size = (int(g('ncar')),int(g('ncar'))) 
            s3d.g = g           
            return s3d, None

