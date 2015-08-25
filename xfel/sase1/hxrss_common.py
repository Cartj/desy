'''
FEL self-seeding
'''

from ocelot.optics.elements import *

from ocelot.optics.wave import *
from ocelot.optics.bragg import *
from ocelot.optics.ray import Ray, trace as trace_ray

from ocelot.gui.optics import *
from ocelot.common.math_op import peaks
from ocelot.adaptors.genesis import *


from copy import deepcopy


from ocelot.optics.utils import *
import mpi4py


import numpy.fft as fft



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



def pulses_from_field(pulse3d, range=None, npad = 2):
    import gc
    gc.collect()
    nx, ny = pulse3d.nx, pulse3d.ny
    n_slices = len(pulse3d.slices) / (nx*ny)
    n_pulses = nx*ny
    
    n = (2*npad+1)*n_slices
    
    tmax = pulse3d.tmax
    E_ref = pulse3d.E_ref
    k0 = E_ref / (hbar * c)
    print 'creating ', n_pulses, ' pulses ', nx, 'x', ny, ' tmax=', tmax

    
    pulses = Signal()
             
    ''' spectrum with finer resolution '''
    pulses.nslice = n_slices
    pulses.npad = npad
    pulses.n = n
    pulses.n_pulses = n_pulses
    pulses.t = (npad+1)*np.linspace(0, tmax, n)
    
    dt = (pulses.t[1] - pulses.t[0]) * 1.e-15
    pulses.freq_k = 2*pi*(fftfreq(n, d=dt) / c )            
    pulses.freq_k = -np.roll(pulses.freq_k, n/2) + k0            
    pulses.freq_ev = pulses.freq_k * hbar * c

    pulses.f = np.zeros([n_pulses,n], dtype=complex)
    #pulses.sp = np.zeros([n_pulses,n], dtype=complex)
             
     
    for i in xrange(n_pulses): 
        print i
        pulses.f[i,npad*n_slices:(npad+1)*n_slices] = pulse3d.slices[i::nx*ny]        
        #pulses.sp[i,:] = np.roll(fft.fft(pulses.f[i]), n/2)

    #del(pulse3d.slices)
    return pulses


def field_from_pulses_test(t, fs):
    s3d = Signal3D()
    s3d.t = t
    s3d.fs = fs
    return s3d

def field_from_pulses(t, fs, mesh_size, slices=None, write_file = None):
    
    nslice = fs.shape[1]
    print fs.shape
    print 'creating field', nslice , 'x', mesh_size[0], 'x', mesh_size[1]
    if slices == None: 
        slices = np.zeros([nslice, mesh_size[0], mesh_size[1]], dtype=complex)
        
    for i in xrange(nslice):
        for j in xrange(mesh_size[0]):
            for k in xrange(mesh_size[1]):
                #print i, j, k, j*mesh_size[0] + k, fs[j*mesh_size[0] + k][i]
                slices[i,j,k] = fs[j*mesh_size[0] + k,i]
                
    s3d = Signal3D()
    s3d.t = t
    s3d.slices = slices
    
    return s3d

'''
modulus of wake signal (fel pulse minus core), for seed delay finding
f -- modulus of the original signal (time domain)
'''
def get_wake(f, d_param=200, smooth_param=120):
    f2 = copy(f)
    fact = 1.0
    d = np.abs(np.diff(f2))
    for i in xrange(1,len(f2)):
        if d[i-1] > d_param:
            fact = 0.0
        f2[i] *= fact
    f2 = np.convolve(f2, np.ones(smooth_param) / float(smooth_param), mode='same')
    return f2

