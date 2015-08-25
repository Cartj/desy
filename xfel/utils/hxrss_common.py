'''
FEL self-seeding
'''

from ocelot.optics.elements import *
from ocelot.optics.wave import *
from ocelot.optics.bragg import *
from ocelot.optics.ray import Ray, trace as trace_ray
from ocelot.gui.optics import *
from ocelot.common.math import peaks
from ocelot.adaptors.genesis import *
from sim_info import *

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
def get_wake(f, n_fel_start, smooth_param=120):
    f2 = copy(f)
    fact = 1.0
    #d = np.abs(np.diff(f2))
    for i in xrange(1,len(f2)):
        if i >= n_fel_start:
            fact = 0.0
        f2[i] *= fact
    f2 = np.convolve(f2, np.ones(smooth_param) / float(smooth_param), mode='same')
    return f2


def update_beam(beam_new, g, beam):
    g0 = np.array(map(lambda x : g.sliceValues[x]['energy'][-1], xrange(1,g.nSlices+1)) )
    dg = np.array(map(lambda x : g.sliceValues[x]['e-spread'][-1], xrange(1,g.nSlices+1)) )
    I = np.array(g.I)

    i_diff = len(g0) - len(beam_new.z)
    if i_diff <= 0: i_diff = -len(g0)

    print 'i_diff', i_diff

    g0 = g0[:-i_diff]
    dg = dg[:-i_diff]
    I = I[:-i_diff]
    beam_new.z = beam_new.z[:-i_diff]

    '''
    plt.figure()
    plt.plot(beam_new.g0)
    plt.plot(g0 + beam.gamma_rel)
    plt.figure()
    plt.plot(beam_new.dg)
    plt.plot(dg)
    plt.figure()
    plt.plot(I)
    plt.plot(beam_new.I)
    plt.show()
    '''

    beam_new.g0 = g0 + beam.gamma_rel
    beam_new.dg = dg


def log_info(sim_info, g, run_id, stage):
    
    r = RunInfo(run_id)
    r.max_power = g.max_power
    r.power = g.power
    r.power_z = g.power_z
    r.stage = stage
    r.z = g.z
    r.t = g.t
    r.spec = g.spec
    r.freq_ev = g.freq_ev

    sim_info.runs[r.id] = r


    print 'saving run ', id
    f_obj = open(sim_info.log_dir + 'dump.dat', 'wb')
    pickle.dump(sim_info, f_obj)
    f_obj.close()

def log_info_seed(sim_info, g, run_id, stage):
    r = RunInfo(run_id)
    r.max_power = g.max_power
    r.power_z = []
    r.power = g.power
    r.spec = g.spec
    r.freq_ev = g.freq_ev 
    r.power_ref = g.power_ref
    r.stage = stage
    sim_info.runs[r.id] = r
    f_obj = open(sim_info.log_dir + 'dump.dat', 'wb')
    pickle.dump(sim_info, f_obj)
    f_obj.close()

def sseed(input_file, E_ev, chicane, run_dir, delay = None, debug=True, output_file = None, wake=None, xt_couple=False, n_peak = 1):

    h = 4.135667516e-15
    c = 299792458.0
    
    g = readGenesisOutput(input_file)
    print 'read sliced field ', g('ncar'), g.nSlices
    ncar = int(g('ncar'))
    dgrid = float(g('dgrid'))

    #idx_max, Imax = peaks(xrange(len(g.I)), g.I, n=3)
    idx_max = np.argmax(g.I)
    #plt.figure()
    #plt.plot(g.I,'.')
    #plt.show()
    #print 'idx_max ', idx_max 

    g.idx_max = idx_max
    print 'ss idx_max:', g.idx_max

    slices = readRadiationFile(fileName=input_file + '.dfl', npoints=g('ncar'))  

    s3d = Signal3D()
    s3d.slices = slices
    s3d.mesh_size = (int(g('ncar')),int(g('ncar'))) 
    s3d.g = g           
    pulse3d, bunch = s3d, None


    nproc = 1
    iproc = 0
    pulse3d.slices = np.reshape(pulse3d.slices, (nproc,-1)) # 1d array
    pulse3d_part = Signal3D()
    pulse3d_part.nx = int(pulse3d.g('ncar'))
    pulse3d_part.ny = int(pulse3d.g('ncar'))
    pulse3d_part.tmax = pulse3d.g.nSlices * pulse3d.g('zsep') * pulse3d.g('xlamds') / 2.99792458e8 * 1.e15
    #scatter
    pulse3d_part.slices = pulse3d.slices[iproc]
    pulse3d_part.E_ref = 1./ pulse3d.g('xlamds') * 4.135667516e-15 *2.99792458e8

    npad = 6
    g.npad = npad
    pulses_1d = pulses_from_field(pulse3d_part, npad=npad) 
    g.nslice = pulses_1d.nslice
    print '*** created', pulses_1d.n_pulses, ' pulses *** '


    if debug:
        pulse_idx = int(pulse3d_part.nx*pulse3d_part.ny/2.) 
        print 'plotting slice', pulse_idx
        fig = plt.figure()
        ax = fig.add_subplot(221)
        ax.grid(True)
        ax.plot(pulses_1d.t, np.abs(pulses_1d.f[pulse_idx])+1, '#000000', alpha=0.5)
        ax.set_title('Stage 1 FEL pulse')

    pulse_idx = int(pulse3d_part.nx*pulse3d_part.ny/2.) 
    
    n_fel_start = 0
    for i in range(len(pulses_1d.f[pulse_idx])):
        if np.abs(pulses_1d.f[pulse_idx][i]) > 1.0:
            n_fel_start = i
            break

    n_points = len(pulses_1d.f[pulse_idx]) / (2*npad + 1)
    g.power_ref = np.abs(pulses_1d.f[pulse_idx])[n_points*npad:n_points*(npad+1)]

    r = Ray() 
    r.lamb = 2 * pi * hbar * c / E_ev
    print 'wavelength', r.lamb


    filt = get_crystal_filter(chicane.cryst, r, ref_idx = chicane.cryst.ref_idx, k = pulses_1d.freq_k)
    chicane.cryst.filter = filt


    f_av = np.zeros(len(pulses_1d.t)) 
    for i in xrange(pulses_1d.n_pulses):
        n_p = len(pulses_1d.f[i,:])
        if n_p % 100 != 0:
            n_p1 = n_p - n_p % 100 
            pulses_1d.f[i,n_p1: n_p] = 0.0
        print 'filtering:', i,len(pulses_1d.f[i,:]), n_p1
        sp = np.roll(np.fft.fft(pulses_1d.f[i,0:n_p1]), pulses_1d.n/2)
        sp = sp * chicane.cryst.filter.tr[0:n_p1]
        sp = np.roll( sp, pulses_1d.n/2)
        pulses_1d.f[i,0:n_p1] = np.fft.ifft(sp)
        f_av += np.abs(pulses_1d.f[i,:])

    if wake != None:
        f_av = wake

    n_marg = 20 / (pulses_1d.t[1] - pulses_1d.t[0]) # number of margin slices prior to FEL pulse
    f_wake = get_wake(f_av, n_fel_start - n_marg, smooth_param=2)

    if debug:
        ax2 = fig.add_subplot(222)
        ax2.set_title('Wake')
        ax2.grid(True)
        ax2.set_yscale('log')
        ax2.plot(f_wake, 'r--')
        ax2.plot(f_av, 'g--')

    x,y = peaks(pulses_1d.t, f_wake, n=4)
    print 'peaks', x, y

    if delay == None:
        delay = pulses_1d.t[pulses_1d.nslice*npad + g.idx_max] - x[n_peak] # based on current maximum

    n_delay = int(delay / (pulses_1d.t[1] - pulses_1d.t[0]))
    n_start = pulses_1d.npad*pulses_1d.nslice - n_delay

    print 'delay', delay, ' fs ', delay * 1.e-15 * 3.e8 / 1.e-6 , 'mu m ', n_delay , ' slices', ' nslice=', pulses_1d.nslice, ' n_start=', n_start 
    print 'max current slice: ', pulses_1d.nslice*npad + g.idx_max

    i1=0
    i2=pulses_1d.n_pulses

    t = pulses_1d.t[n_start:n_start+pulses_1d.nslice]
    pulse3d.slices = np.reshape(pulse3d.slices, (pulses_1d.nslice, pulse3d_part.nx, pulse3d_part.nx))
    field_from_pulses( t, pulses_1d.f[i1:i2,n_start:n_start+pulses_1d.nslice], pulse3d.mesh_size,pulse3d.slices)

    g.spec = np.fft.fft(pulse3d.slices[:,ncar/2,ncar/2])
    g.max_power = np.max(np.abs(pulse3d.slices[:,ncar/2,ncar/2]))
    g.power =  np.abs(pulse3d.slices[:,ncar/2,ncar/2])
    g.freq_ev = h * fftfreq(len(g.spec), d=(t[1]-t[0])*1.e-15) 

    g.delay = delay

    g.seed_axis = np.abs(pulse3d.slices[:,ncar/2,ncar/2])
    g.wake = f_av
    nslice = len(pulse3d.slices[:,0,0])

    if xt_couple: # spatial-temporal coupling
        dct = (pulses_1d.t[1] - pulses_1d.t[0]) * 1.e-15 * c    

        for i_slice in xrange(len(pulse3d.slices[:,0,0])):
            print 'shifting slice', i_slice
            shift_x = (nslice - i_slice)*dct * cos(chicane.cryst.thetaB) / sin(chicane.cryst.thetaB)
            print 'shift_x' , shift_x
            print dgrid, ncar
            n_shift = int( shift_x / (dgrid / ncar) )
            print 'n_shift', n_shift
            pulse3d.slices[i_slice,:,:] = np.roll(pulse3d.slices[i_slice,:,:], n_shift, 0)
    

    if debug:
        ax.set_yscale('log')
        ax.plot(t + 0, np.abs(pulse3d.slices[:,ncar/2,ncar/2]), 'r--')
        ax.plot(t + 0, np.abs(pulse3d.slices[:,ncar/2,ncar/2+5]), 'r--')
        ax.plot(t + delay, np.abs(pulse3d.slices[:,ncar/2,ncar/2]), 'g-')
        ax.plot(pulses_1d.t[pulses_1d.nslice*npad + g.idx_max], f_wake[pulses_1d.nslice*npad + g.idx_max], 'bs')
        print 'seed t', pulses_1d.t[pulses_1d.nslice*npad + g.idx_max], f_wake[pulses_1d.nslice*npad + g.idx_max]

        ax3 = fig.add_subplot(223)
        #ax3.plot(t + delay, np.imag(pulse3d.slices[:,ncar/2,ncar/2]), 'b-', lw=1)
        print 'debug: max slice', g.idx_max,
        ax3.plot(np.abs(pulse3d.slices[100,:,ncar/2]), 'r--')
        ax3.plot(np.abs(pulse3d.slices[200,:,ncar/2]), 'g--')
        ax3.plot(np.abs(pulse3d.slices[300,:,ncar/2]), 'b--')
        ax3.plot(np.abs(pulse3d.slices[g.idx_max,:,ncar/2]), 'b-')

        ax4 = fig.add_subplot(224)
        ax4.plot(g.freq_ev, np.abs(g.spec))
        #plt.title('Spectrum (middle pulse after seed)')

        fig = plt.figure()
        ax5 = fig.add_subplot(111)
        ax5.set_yscale('log')
        ax5.plot(np.abs(pulse3d.slices[:,ncar/2,ncar/2]), 'r-')
        ax5.plot(g.wake[n_start:n_start+pulses_1d.nslice], 'b-')
        ax5.plot(g.I, 'g-')

        plt.show()
    
    if output_file != None:
        writeRadiationFile(output_file+'.dfl', pulse3d.slices)    
        print 'written radiation file, slices', len(pulse3d.slices[:,ncar/2,ncar/2])

    return g

