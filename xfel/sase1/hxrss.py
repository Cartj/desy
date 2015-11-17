'''
hard x-ray self-seeding
this is a template file
please copy this file into your working directory and use it there
'''

rep_dir = '/data/netapp/xfel/products/desy/xfel/'

from ocelot import *
from ocelot.utils.xfel_utils import *
from ocelot.utils.hxrss_common import *
from ocelot.utils.sim_info import *
from ocelot.gui.accelerator import *

from copy import copy
import numpy.fft as fft
import time

launcher = get_genesis_launcher(384)

sys.path.append(rep_dir + 'sase1/')
from sase1 import *

exp_dir = '/data/fhgfs/iagapov/exp207/'
#exp_dir = './exp1/'
run_ids = xrange(0,1)
beta_av = 25.0
xt_couple = True
start_stage = 1
stop_stage = 3
debug = True

create_exp_dir(exp_dir, run_ids)

lat = MagneticLattice(sase1_segment(n=20))
rematch(beta_av, l_fodo, qdh, lat, extra_fodo, beam, qf, qd) # jeez...

tw0 = Twiss(beam)
tws=twiss(lat, tw0, nPoints = 100) # to make sure the average beta exists, show twiss if needed 

beam.E = float(sys.argv[1]) # 14.0
E_ev = float(sys.argv[2])   # 8000.0

# calculate UR parameters (required later for input generation)
up = UndulatorParameters(und)
up.E = beam.E
up.printParameters()
und.Kx = up.get_k(E_ev)
up = UndulatorParameters(und)
up.E = beam.E
up.printParameters()

#tapering functions around 9 kev, 17.5 gev

#taper_func_1 = lambda n : f1(n, [0, 20], 0.999, [0,0], [0,0])
taper_func_1 = lambda n : f1(n, [0, 20], 0.9995, [0,0], [0,0])

#taper_func_2 = lambda n : f1(n, [0, 20], 0.998, [0,0], [0,0])
taper_func_2 = lambda n : f1(n, [0, 20], 0.999, [0,0], [0,0])

n0 = [0,18,29,36]
a0 = 0.999
a1 = [0.0, -0.0006,  -0.0006 ]
a2 = [0.0, -0.00013, -0.0001 ]
taper_func_3 = lambda n : f1(n, n0, a0, a1, a2 )

lat1 = taper(lat, taper_func_1)
lat2 = taper(lat, taper_func_2)
lat3 = taper(lat, taper_func_3)

beam.emit_xn, beam.emit_yn = beam.emit[beam.C]
beam.gamma_rel = beam.E / (0.511e-3)
beam.emit_x = beam.emit_xn / beam.gamma_rel
beam.emit_y = beam.emit_yn / beam.gamma_rel

inp = generate_input(up, beam, itdp=True)
inp.lattice_str = generate_lattice(lat1, unit = up.lw, energy = beam.E )

inp.ncar = 101
inp.curlen = beam.tpulse * 3.e-7
inp.zsep = int(8 * inp.curlen  / inp.nslice / inp.xlamds )
inp.ntail = - int (inp.nslice/2)
inp.npart = 8192 
inp.rmax0 = 0.0
inp.dgrid = 1.6e-4
inp.delz = 1.0
inp.ipseed = 147
inp.zstop = 30.0
inp.nharm = 1
inp.DUMP_PARTICLES = 0

beamf = rep_dir + '/beams/beam_0.25nC_wake_sase1.txt'
#beamf = rep_dir + '/beams/b30pC_ACC.txt'
# nb: beam is now the 'beam file' object!
beam_new = transform_beam_file(beam_file = beamf,transform = [ [beam.beta_x,beam.alpha_x], [beam.beta_y,beam.alpha_y] ], energy_scale = beam.E / 17.5, emit_scale = 1.40, n_interp=1000)

beam_new.x *= 0.0
beam_new.px *= 0.0
beam_new.y *= 0.0
beam_new.py *= 0.0
#beam_new.eloss *= 0.0
#beam_new.I *= 1.e-5

inp.nslice = 0
inp.zsep = int(beam_new.zsep / inp.xlamds)
inp.beamfile = 'tmp.beam'
inp.beam_file_str = beam_new.f_str= beam_file_str(beam_new)

# plotting beam not required
if debug: plot_beam(plt.figure(), beam_new)
idx_max = beam_new.idx_max
if debug: print 'idx_max', idx_max
if debug: plt.show()


sim_info = SimInfo()
sim_info.log_dir = exp_dir

save_output = True
new_beams = {}


# stage 1
shift_ev = 0.0
if start_stage <= 1 and stop_stage >= 1:
    spec_av = None
    skip_s1 = False
    debug = True
    for run_id in run_ids:
        inp.runid = run_id
        inp.run_dir = exp_dir + 'run_' + str(inp.runid)
        inp.ipseed = 61*(run_id + 1 )
        inp.zstop = 42.0

        if skip_s1: g = readGenesisOutput( inp.run_dir + '/run.' + str(inp.runid) + '.s1.gout')
        else: g = run(inp, launcher)

        if spec_av == None: spec_av = np.abs(g.spec)**2
        else: spec_av += np.abs(g.spec)**2        
        idx = np.argmax(spec_av)
        print 'freq shift:', spec_av[idx], g.freq_ev[idx]

        if debug: show_output(g, show_field = True, show_slice=475)
        if debug: plt.show()

        log_info(sim_info, g, run_id, 1)

        beam_stage1 = deepcopy(beam_new)
        update_beam(beam_stage1, g, beam)
        new_beams[run_id] = beam_stage1
        open(inp.run_dir + '/beam.s1.txt','w').write( beam_file_str(new_beams[run_id]) )

        checkout_run(inp.run_dir, run_id, '', '.s1', True)

        if debug: plt.plot(beam_stage1.dg)
        if debug: plt.show()

    shift_ev = g.freq_ev[idx]
    print 'frequency shift [ev]:', shift_ev 
    shift_ev = - shift_ev # TODO: fix this, this is due to a feature in the filter calculation
                          # which seems to introduce artificial wavevector reversal
                          # to conform to genesis time direction

# stage 2 (filter -- get average delay -- filter individually)
if start_stage <= 2 and stop_stage >= 2:
    delays = []
    wakes = []
    npad = 0
    nslice = 0
    debug = True

    for run_id in run_ids:
        run_dir = exp_dir + 'run_' + str(run_id)
        input_file = run_dir + '/run.' + str(run_id) + '.s1.gout'
        # set debug to True to see plot of the seed pulse
        t1 = time.time()
        g = sseed(input_file, E_ev + shift_ev, chicane1, run_dir, debug=debug, xt_couple = xt_couple,
                  threaded = False)
        print 'seeding function run time', time.time()- t1, ' sec'
        delays.append(g.delay)
        wakes.append(g.wake)

    if debug: plt.figure()
    wake_av = np.zeros(len(wakes[0]))
    for w in wakes:
        if debug: plt.plot(w,'b--')
        wake_av += np.array(w) /len(wakes)
    if debug: plt.plot(wake_av, 'r-')
    if debug: plt.show()

    for run_id in run_ids:
        run_dir = exp_dir + 'run_' + str(run_id)
        input_file = run_dir + '/run.' + str(run_id) + '.s1.gout'

        t1 = time.time()
        g = sseed(input_file, E_ev + shift_ev, chicane1, run_dir, 
                  debug=debug, output_file=run_dir +'/tmp2', wake = wake_av, xt_couple = xt_couple)
        print 'seeding function run time', time.time()- t1, ' sec'
        log_info_seed(sim_info, g, run_id, 2)

# stage 3
if start_stage <= 3 and stop_stage >= 3:
    inp.lattice_str = generate_lattice(lat2, unit = up.lw, energy = beam.E )
    skip_s3 = True
    spec_av = None
    debug = True

    for run_id in run_ids:        
        inp.runid = run_id
        inp.run_dir = exp_dir + 'run_' + str(inp.runid)
        inp.fieldfile='tmp2.dfl'
        inp.ipseed = 17*(run_id + 1 )
        try: # if previous stage has calculated/read in reasults
            inp.beam_file_str = beam_new.f_str = beam_file_str(new_beams[run_id])
        except KeyError: # if start from stage 3 and 
            try:
                inp.beam_file_str = beam_new.f_str = open(inp.run_dir + '/beam.s1.txt').read()
            except:
                print 'ERROR: beam file from stage 1 not present, cannot calculate '

        inp.zstop = 42.0

        if skip_s3: g = readGenesisOutput( inp.run_dir + '/run.' + str(inp.runid) + '.s3.gout')
        else: g = run(inp, launcher)

        if spec_av == None: spec_av = np.abs(g.spec)**2
        else: spec_av += np.abs(g.spec)**2        
        idx = np.argmax(spec_av)
        print 'freq shift:', spec_av[idx], g.freq_ev[idx]

        if debug: show_output(g, show_field = True, show_slice=475)
        if debug: plt.show()

        log_info(sim_info, g, run_id, 3)

        beam_stage3 = deepcopy(beam_new)
        update_beam(beam_stage3, g, beam)
        new_beams[run_id] = beam_stage3
        open(inp.run_dir + '/beam.s3.txt','w').write( beam_file_str(new_beams[run_id]) )

        checkout_run(inp.run_dir, run_id, '', '.s3', True)

    shift_ev = g.freq_ev[idx]
    print 'frequency shift [ev]:', shift_ev 
    shift_ev = - shift_ev

# stage 4.0 (filter -- get average delay)
if start_stage <= 4 and stop_stage >= 4:
    delays = []
    wakes = []
    npad = 0
    nslice = 0
    debug = True

    for run_id in run_ids:
        run_dir = exp_dir + 'run_' + str(run_id)
        input_file = run_dir + '/run.' + str(run_id) + '.s3.gout'

        g = sseed(input_file, E_ev + shift_ev + 1.1, chicane1, run_dir, debug=debug, xt_couple = xt_couple)
        delays.append(g.delay)
        wakes.append(g.wake)

    if debug: plt.figure()
    wake_av = np.zeros(len(wakes[0]))
    for w in wakes:
        if debug: plt.plot(w,'b--')
        wake_av += np.array(w) /len(wakes)
    if debug: plt.plot(wake_av, 'r-')
    if debug: plt.show()

    for run_id in run_ids:
        run_dir = exp_dir + 'run_' + str(run_id)
        input_file = run_dir + '/run.' + str(run_id) + '.s4.gout'
        checkout_run(run_dir, run_id, '.s3', '.s4', True)
        #g = sseed(input_file, run_dir + 'tmp', E_ev, chicane1, run_dir, delay=69, debug=True)
        g = sseed(input_file, E_ev + shift_ev + 1.1, chicane1, run_dir, 
                  debug=debug, output_file=run_dir + '/tmp4', wake = wake_av, xt_couple = xt_couple)

        log_info_seed(sim_info, g, run_id, 4)

# stage 5
if start_stage <= 5 and stop_stage >= 5:
    inp.lattice_str = generate_lattice(lat3, unit = up.lw, energy = beam.E )
    for run_id in run_ids:
        inp.runid = run_id
        inp.run_dir = exp_dir + 'run_' + str(inp.runid)
        inp.ipseed = 71*(run_id + 1 )
        inp.fieldfile='tmp4.dfl'

        try: # if previous stage has calculated/read in reasults
            inp.beam_file_str = beam_new.f_str = beam_file_str(new_beams[run_id])
        except KeyError: # if start from stage 5 and prev. beam file present
            try:
                inp.beam_file_str = beam_new.f_str = open(inp.run_dir + '/beam.s3.txt').read()
            except:
                print 'ERROR: beam file from stage 3 not present, cannot calculate '
                sys.exit(0)

        inp.zstop = 84.0
        g = run(inp, launcher)
        if debug: show_output(g, show_field = True, show_slice=475)
        if debug: plt.show()
        log_info(sim_info, g, run_id, 5)

