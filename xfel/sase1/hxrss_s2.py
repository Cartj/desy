'''
SASE
'''
from ocelot.gui.accelerator import *
sys.path.append('../utils/')
from xfel_utils import *

from copy import copy

launcher = get_genesis_launcher(320)
beta_av = 15.0

from sase1 import *

experiment_dir = 'exp0'
runs = xrange(0,2)


lat = MagneticLattice(sase1_segment(n=3))
rematch(beta_av, l_fodo, qdh, lat, extra_fodo, beam, qf, qd) # jeez...

lat3 = MagneticLattice(sase1_segment(n=8))
lat4 = MagneticLattice(sase1_segment(n=10))

tw0 = Twiss(beam)
tws=twiss(lat, tw0, nPoints = 100)

beam.E = float(sys.argv[1]) # 14.0
E_ev = float(sys.argv[2])   # 8000.0

# print out UR parameter estimates
up = UndulatorParameters(und)
up.E = beam.E
up.printParameters()
und.Kx = up.get_k(E_ev)
up = UndulatorParameters(und)
up.E = beam.E
up.printParameters()

# donno wtf it comes from -- probably section not multiple of xlamd, correcting out for roundoff
#qf.k1 *= voodoo
#qd.k1 *= voodoo

#qf.k1 *= 20.0
#qd.k1 *= 20.0

# 5-9 kev, 14 gev
'''
n0 = [0,8, 21,36]
a0 = 0.999
a1 = [0.0, -0.001,  -0.0001 ]
a2 = [0.0, -0.00015, -0.00015 ]
'''

n0 = [0,8, 21,36]
a0 = 0.9993
a1 = [0.0, -0.001,  -0.0001 ]
a2 = [0.0, -0.00015, -0.00015 ]

taper_func = lambda n : f1(n, n0, a0, a1, a2 )

#taper_func = lambda n : f1(n, n0, a0, a1, a2 )

#lat2 = taper(lat, taper_func)
lat2 = lat
lat3 = lat3
lat4 = taper(lat4, taper_func)

beam.emit_xn, beam.emit_yn = beam.emit[beam.C]
beam.gamma_rel = beam.E / (0.511e-3)
beam.emit_x = beam.emit_xn / beam.gamma_rel
beam.emit_y = beam.emit_yn / beam.gamma_rel

print 'average beam size', np.sqrt(beam.emit_x * beta_av)

print 'preparing runs...'


inp = generate_input(up, beam, itdp=True)
inp.lattice_str = generate_lattice(lat2, unit = up.lw, energy = beam.E )

#print inp.xlamds

inp.nslice = int(320*1)
inp.ncar = 51
inp.curlen = beam.tpulse * 3.e-7
inp.zsep = int(8 * inp.curlen  / inp.nslice / inp.xlamds )
inp.ntail = - int (inp.nslice/2)
inp.npart = 8192 
inp.rmax0 = 0.0
inp.dgrid = 0.3e-4
inp.delz = 1.0
inp.ipseed = 147
inp.zstop = 35.0
inp.nharm = 1
inp.DUMP_PARTICLES = 0

inp2_lattice_str = generate_lattice(lat3, unit = up.lw, energy = beam.E )
inp3_lattice_str = generate_lattice(lat4, unit = up.lw, energy = beam.E )

beamf = '../beams/b30pC_ACC.txt'
#beamf = '../beams/beam_0.5nC.txt'

# nb: beam is now the 'beam file' object!
beam_new = transform_beam_file(beam_file = beamf,transform = [ [beam.beta_x,beam.alpha_x], [beam.beta_y,beam.alpha_y] ], energy_scale = beam.E / 14.0, n_interp=1600)

beam_new.x *= 0.0
beam_new.px *= 0.0
beam_new.y *= 0.0
beam_new.py *= 0.0
#beam_new.eloss *= 0.0
#beam_new.I *= 1.e-5

print beam_new.betax[beam_new.idx_max], beam_new.alphax[beam_new.idx_max]
#sys.exit(0)

inp.nslice = 0
inp.zsep = int(beam_new.zsep / inp.xlamds)
inp.beamfile = 'tmp.beam'
inp.beam_file_str = beam_new.f_str= beam_file_str(beam_new)
#plot_beam(plt.figure(), beam_new)
#plt.show()

inp.runid = next_run_id(get_data_dir())
inp.run_dir = get_data_dir() + 'run_' + str(inp.runid)
output_file = inp.run_dir + '/run.' + str(inp.runid) + '.gout'

g = run(inp, launcher)
#g = readGenesisOutput( output_file)

'''
plt.figure()
for show_slice in xrange(450,500):

    xrms = np.array(g.sliceValues[g.sliceValues.keys()[show_slice]]['xrms'])
    yrms = np.array(g.sliceValues[g.sliceValues.keys()[show_slice]]['yrms'])
    plt.plot(g.z, xrms, lw=1)
    #plt.plot(g.z, yrms, lw=1)
    #f.add_subplot(132), plt.plot(g.z, power, lw=3), plt.grid(True)
'''
#show_output(g, show_field = True, output_file = output_file, show_slice=beam_new.idx_max)

#plt.show()
#sys.exit(0)

from hxrss_common import *

def seed(output_file, E_ev, chicane, do_plot=True):

    g = readGenesisOutput(output_file)
    print 'read sliced field ', g('ncar'), g.nSlices
    slices = readRadiationFile(fileName=output_file + '.dfl', npoints=g('ncar'))  
    os.system('rm ' + output_file + '.dfl')   
    s3d = Signal3D()
    s3d.slices = slices
    s3d.mesh_size = (int(g('ncar')),int(g('ncar'))) 
    s3d.g = g           
    pulse3d, bunch = s3d, None


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

    pulses_1d = pulses_from_field(pulse3d_part, npad=6) 

    print '*** created', pulses_1d.n_pulses, ' pulses *** '


    if do_plot:
    #TODO: determine hat to plot/log
        pulse_idx = int(pulse3d_part.nx*pulse3d_part.ny/2.) 
        print 'plotting slice', pulse_idx
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.grid(True)
        ax.plot(pulses_1d.t, np.abs(pulses_1d.f[pulse_idx]), '#000000', alpha=0.5)
        ax.set_title('Stage 1 FEL pulse')


    r = Ray() 
    r.lamb = 2 * pi * hbar * c / E_ev
    print 'wavelength', r.lamb


    filt = get_crystal_filter(chicane.cryst, r, ref_idx = chicane.cryst.ref_idx, k = pulses_1d.freq_k)
    chicane.cryst.filter = filt

    f_av = np.zeros(len(pulses_1d.t)) 


    for i in xrange(pulses_1d.n_pulses):
        print 'processing', i
        sp = np.roll(fft.fft(pulses_1d.f[i,:]), pulses_1d.n/2)
        sp = sp * chicane.cryst.filter.tr
        sp = np.roll( sp, pulses_1d.n/2)
        pulses_1d.f[i,:] = np.fft.ifft(sp)
        f_av += np.abs(pulses_1d.f[i,:])

    #f_wake = get_wake(f_av, d_param=35, smooth_param=20)
    f_wake = get_wake(f_av, d_param=50, smooth_param=20)

    fig = plt.figure()
    ax2 = fig.add_subplot(111)
    ax2.grid(True)
    ax2.set_yscale('log')
    ax2.plot(f_wake, 'r--')
    ax2.plot(f_av, 'g--')
    #plt.show()

    x,y = peaks(pulses_1d.t, f_wake, n=4)
    x0,y0 = peaks(pulses_1d.t, np.abs(f_av), n=4)

    print 'peaks', x, y
    print 'peaks original', x0, y0    
    
    n_peak = 1

    delay = x0[0] - x[n_peak] # based on fel pulse maximum
    n_delay = int(np.round(delay / (pulses_1d.t[1] - pulses_1d.t[0])))
    n_start = pulses_1d.npad*pulses_1d.nslice - n_delay

    print 'delay', x0[0] - x[n_peak], ' fs ', n_delay , ' slices', ' nslice=', pulses_1d.nslice, ' n_start=', n_start 


    i1=0
    i2=pulses_1d.n_pulses

    t = pulses_1d.t[n_start:n_start+pulses_1d.nslice]
    pulse3d.slices = np.reshape(pulse3d.slices, (pulses_1d.nslice, pulse3d_part.nx, pulse3d_part.nx))
    field_from_pulses( t, pulses_1d.f[i1:i2,n_start:n_start+pulses_1d.nslice], pulse3d.mesh_size,pulse3d.slices)
    os.system('rm ' + inp.run_dir + '/tmp.dfl' )
    writeRadiationFile(inp.run_dir + '/tmp.dfl', pulse3d.slices)    

    print 'written radiation file, slices', len(pulse3d.slices[:,25,25])
    #slices2 = readRadiationFile(fileName='test.dfl', npoints=pulse3d_part.nx)

    if do_plot:
        ax.set_yscale('log')
        ax.set_title('Filtered FEL pulse')
        ax.plot(t + delay, np.abs(pulse3d.slices[:,inp.ncar/2,inp.ncar/2]), 'r--')
        ax.plot(t + delay, np.abs(pulse3d.slices[:,inp.ncar/2,inp.ncar/2 + 1]), 'r-', alpha=0.4)
        ax.plot(t + delay, np.abs(pulse3d.slices[:,inp.ncar/2,inp.ncar/2 + 2]), 'r-', alpha=0.4)
        ax.plot(t + delay, np.abs(pulse3d.slices[:,inp.ncar/2,inp.ncar/2 + 3]), 'r-', alpha=0.4)
        ax.plot(t + delay, np.abs(pulse3d.slices[:,inp.ncar/2,inp.ncar/2 + 4]), 'r-', alpha=0.4)
        ax.plot(t + delay, np.abs(pulse3d.slices[:,inp.ncar/2,inp.ncar/2 + 5]), 'r-', alpha=0.4)
        ax.plot(t + delay, np.abs(pulse3d.slices[:,inp.ncar/2,inp.ncar/2 + 6]), 'r-', alpha=0.4)

        plt.figure()
        plt.title('Seed signal axis')
        plt.plot(t + delay, np.abs(pulse3d.slices[:,inp.ncar/2,inp.ncar/2]), 'r-', lw=2)
        plt.plot(t + delay, np.real(pulse3d.slices[:,inp.ncar/2,inp.ncar/2]), 'g-', lw=1)
        plt.plot(t + delay, np.imag(pulse3d.slices[:,inp.ncar/2,inp.ncar/2]), 'b-', lw=1)

        plt.figure()
        plt.plot(np.abs(np.fft.fft(pulse3d.slices[:,inp.ncar/2,inp.ncar/2])))
        plt.title('Spectrum (middle pulse after seed)')



seed(output_file, E_ev, chicane1, do_plot=True)

plt.show()

inp.lattice_str =  inp2_lattice_str
inp.fieldfile='tmp.dfl'
inp.zstop = 30.0
g = run(inp, launcher)
show_output(g, show_field = True, output_file = output_file, show_slice=beam_new.idx_max)
plt.show()

seed(output_file, E_ev, chicane2, do_plot=True)

inp.lattice_str =  inp3_lattice_str
inp.fieldfile='tmp.dfl'
inp.zstop = 70.1
g = run(inp, launcher)
show_output(g, show_field = True, output_file = output_file, show_slice=beam_new.idx_max)
plt.show()
