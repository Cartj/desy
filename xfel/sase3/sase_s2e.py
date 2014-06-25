'''
time dependant SASE, with s2e beam
'''
from xframework.gui.accelerator import *
sys.path.append('../utils/')
from xfel_utils import *

launcher = get_genesis_launcher(4)

beta_av = 15.0

exec( open("sase3.inp" ))
lat = MagneticLattice(sase3_segment(n=17))

rematch(beta_av, l_fodo, qdh, lat, extra_fodo, beam, qf, qd) # jeez...


beam.tpulse = 10  # electron bunch length in fs (rms)
beam.I = 5000
beam.sigma_E  = 0.0001

print 'average beam size', np.sqrt(beam.emit_x * beta_av)

# print out UR parameter estimates
up = UndulatorParameters(und)
up.E = beam.E
up.printParameters()


f = '/home/iagapov/workspace/xcode/repository/xfel/beams/beam_1nC.txt'
#f = 'tmp2.beam'
ex, ey, beam_str = transform_beam_file(beam_file = f, out_file = 'tmp.beam', 
                                       transform = [ [beam.beta_x,beam.alpha_x], [beam.beta_y,beam.alpha_y] ], plot=False)
#ex, ey = transform_beam_file(beam_file = f, out_file = 'tmp.beam', transform = None, plot=True)
print ex, ey


# donno wtf it comes from -- probably section not multiple of xlamd, correcting out for roundoff
qf.k1 *= (0.37)
qd.k1 *= (0.37) 

inp = generate_input(up, beam, itdp=True)
inp.lattice_str = generate_lattice(lat, unit = up.lw*2, energy = beam.E )

#inp.zstop = 210
inp.nslice = 128
inp.curlen = beam.tpulse * 3.e-7
inp.zsep = int(4 * inp.curlen  / inp.nslice / inp.xlamds )
inp.ntail = -int ( inp.nslice / 2 )
inp.npart = 2048
inp.rmax0 = 29.0
inp.dgrid = 2.e-4
inp.delz = 1.0
inp.nharm = 3


inp.beamfile = 'tmp.beam'
inp.beam_file_str = beam_str

inp.runid = next_run_id(get_data_dir())
inp.run_dir = get_data_dir() + 'run_' + str(inp.runid)

g = run(inp, launcher)
output_file = inp.run_dir + '/run.' + str(inp.runid) + '.gout'

