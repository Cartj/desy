from pylab import *
import time
sys.path.append('/data/netapp/xfel/products/xdb/xfel/utils/')
sys.path.append('/data/netapp/xfel/products/xdb/xfel/sase1/')

from sase1 import *
from hxrss_common import *


def sseed_test(input_file, output_file,E_ev, chicane, run_dir, delay = None, debug=True, write_file = False, wake=None):

    h = 4.135667516e-15
    c = 299792458.0
    

    g = readGenesisOutput(input_file)
    print 'read sliced field ', g('ncar'), g.nSlices
    ncar = int(g('ncar'))
    dgrid = int(g('dgrid'))

    idx_max, Imax = peaks(xrange(len(g.I)), g.I, n=1)

    #print len(g.z)
    #print len(g.I)

    #plt.plot(g.z, g.I)
    #plt.show()


    #print zmax

    g.idx_max = idx_max #g.z.index(zmax)
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
        print 'processing', i, len(pulses_1d.f[i,:])
        sp = np.fft.fft(pulses_1d.f[i,:])
        #sp = np.roll(np.fft.fft(pulses_1d.f[i,:]), pulses_1d.n/2)
        #sp = sp * chicane.cryst.filter.tr
        #sp = np.roll( sp, pulses_1d.n/2)
        #pulses_1d.f[i,:] = np.fft.ifft(sp)
        #f_av += np.abs(pulses_1d.f[i,:])

    if wake != None:
        f_av = wake

    n_marg = 20 / (pulses_1d.t[1] - pulses_1d.t[0]) # number of margin slices prior to FEL pulse
    f_wake = get_wake(f_av, n_fel_start - n_marg, smooth_param=2)

    x,y = peaks(pulses_1d.t, f_wake, n=4)
    print 'peaks', x, y
    
    n_peak = 1

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


    return g




E_ev = 8000

t1 = time.time()

input_file = '/data/fhgfs/iagapov/exp2/run_0/run.0.s1.gout'
g = sseed_test(input_file, '/dev/null', E_ev, chicane1, '/dev/null', delay = None, debug=False)

print time.time() - t1, 'sec'

sys.exit(0)

n1 = 101 * 101
n2 = 13000

f = np.zeros([n1,n2], dtype=complex)

print 'init'

for i1 in xrange(n1):
	f[i1,:] = np.random.random_sample(n2) + 1j * np.random.random_sample(n2)
	
for i in xrange(n1):
    print 'averaging', i
    sp = np.roll(np.fft.fft(f[i,:]), n2/2)
    #sp = sp * tr
    sp = np.roll( sp, n2/2)
    f[i,:] = np.fft.ifft(sp)

print time.time() - t1, 'sec'
