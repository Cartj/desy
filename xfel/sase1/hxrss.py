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


from sase1 import *

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

do_plot = True

'''
1 stage SASE
'''

fel_simulator =  FelSimulator()
fel_simulator.engine = 'test_genesis'
fel_simulator.npad = 2
fel_simulator.input = 'test/run_0/run.0.gout'


pulse3d, bunch = fel_simulator.run() 

nproc = 1
iproc = 0
pulse3d.slices = np.reshape(pulse3d.slices, (nproc,-1))
pulse3d_part = Signal3D()
pulse3d_part.nx = int(pulse3d.g('ncar'))
pulse3d_part.ny = int(pulse3d.g('ncar'))
pulse3d_part.tmax = pulse3d.g.nSlices * pulse3d.g('zsep') * pulse3d.g('xlamds') / 2.99792458e8 * 1.e15
#scatter
pulse3d_part.slices = pulse3d.slices[iproc]
pulse3d_part.E_ref = 1./ pulse3d.g('xlamds') * 4.135667516e-15 *2.99792458e8

pulses_1d = pulses_from_field(pulse3d_part) 

print 'created', pulses_1d.n_pulses, ' pulses'

 
if do_plot:
    ''' TODO: determine hat to plot/log'''
    pulse_idx = int(pulse3d_part.nx*pulse3d_part.ny/2.) 
    print 'plotting slice', pulse_idx
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.grid(True)
    ax.plot(pulses_1d.t, np.abs(pulses_1d.f[pulse_idx]), '#000000', alpha=0.5)
    ax.set_title('Stage 1 FEL pulse')



'''
2 stage chicane
'''

''' option 1 -- delay calculated based on pulse'''

'''
TODO: add logic to fine-tune the bragg angle to actual maximum of fel spectrum
'''
E_ev = pulse3d_part.E_ref


r = Ray() 
r.lamb = 2 * pi * hbar * c / E_ev
print 'wavelength', r.lamb


filt = get_crystal_filter(chicane.cryst, r, ref_idx = (4,0,0), k = pulses_1d.freq_k)
chicane.cryst.filter = filt

f_av = np.zeros(len(pulses_1d.t)) 


for i in xrange(pulses_1d.n_pulses):
    print 'processing', i
    sp = np.roll(fft.fft(pulses_1d.f[i,:]), pulses_1d.n/2)
    #sp = fft.fft(pulses_1d.f[i,:])
    sp = sp * chicane.cryst.filter.tr
    pulses_1d.f[i,:] = np.fft.ifft(sp)
    f_av += np.abs(pulses_1d.f[i,:])


#f_wake = get_wake(f_av, d_param=200, smooth_param=20)
f_wake = get_wake(f_av, d_param=12, smooth_param=10)

'''
fig = plt.figure()
ax = fig.add_subplot(111)
ax.grid(True)
ax.set_yscale('log')
plt.plot(f_wake, 'r--')
plt.plot(f_av, 'g--')
plt.show()
'''

x,y = peaks(pulses_1d.t, f_wake, n=4)
x0,y0 = peaks(pulses_1d.t, np.abs(f_av), n=4)

print 'peaks', x, y
print 'peaks original', x0, y0    
    
n_peak = 0

delay = x0[0] - x[n_peak] # based on fel pulse maximum
n_delay = int(np.round(delay / (pulses_1d.t[1] - pulses_1d.t[0])))
n_start = pulses_1d.npad*pulses_1d.nslice - n_delay

print 'delay', x0[0] - x[n_peak], ' fs ', n_delay , ' slices', ' nslice=', pulses_1d.nslice, ' n_start=', n_start 


i1=0
i2=pulses_1d.n_pulses

t = pulses_1d.t[n_start:n_start+pulses_1d.nslice]
pulse3d.slices = np.reshape(pulse3d.slices, (pulses_1d.nslice, pulse3d_part.nx, pulse3d_part.nx))
field_from_pulses( t, pulses_1d.f[i1:i2,n_start:n_start+pulses_1d.nslice], pulse3d.mesh_size,pulse3d.slices)
writeRadiationFile('test.dfl', pulse3d.slices)    

#slices2 = readRadiationFile(fileName='test.dfl', npoints=pulse3d_part.nx)

if do_plot:
    ax.set_yscale('log')
    ax.set_title('Filtered FEL pulse')
    plt.plot(t + delay, np.abs(pulse3d.slices[:,5,5]), 'r--')


plt.show()
sys.exit(0)



''' option 2 -- delay calculated from chicane '''


'''
3 stage FEL
'''

'''
fel_simulator.configure()

pulse, bunch = fel_simulator.run()
'''