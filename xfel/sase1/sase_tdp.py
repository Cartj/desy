'''
SASE
'''
from xframework.gui.accelerator import *
sys.path.append('../utils/')
from xfel_utils import *


launcher = get_genesis_launcher(4)
beta_av = 21.0

from sase1 import *

lat = MagneticLattice(sase1_segment(n=17))

rematch(beta_av, l_fodo, qdh, lat, extra_fodo, beam, qf, qd) # jeez...

stat = False
if len(sys.argv)>4:
	stat = True
	print 'statistical', sys.argv[4]

if len(sys.argv) > 1 : beam.E=float(sys.argv[1])

# print out UR parameter estimates
up = UndulatorParameters(und)
up.E = beam.E
up.printParameters()
if len(sys.argv) > 2:
	und.Kx = up.get_k(float(sys.argv[2]))
	up = UndulatorParameters(und)
	up.E = beam.E
	up.printParameters()

# donno wtf it comes from -- probably section not multiple of xlamd, correcting out for roundoff
qf.k1 *= voodoo
qd.k1 *= voodoo


#taper_func = lambda n : f1(n, n0, a0, a1, a2 )
#lat2 = taper(lat, taper_func)
lat2 = lat


beam.emit_xn, beam.emit_yn = beam.emit[beam.C]
beam.gamma_rel = beam.E / (0.511e-3)
beam.emit_x = beam.emit_xn / beam.gamma_rel
beam.emit_y = beam.emit_yn / beam.gamma_rel

print 'average beam size', np.sqrt(beam.emit_x * beta_av)

inp = generate_input(up, beam, itdp=True)
inp.lattice_str = generate_lattice(lat2, unit = up.lw, energy = beam.E )

#print inp.xlamds

inp.nslice = int(320*1)
inp.ncar = 251
inp.curlen = beam.tpulse * 3.e-7
inp.zsep = int(16 * inp.curlen  / inp.nslice / inp.xlamds )
inp.ntail = - int (inp.nslice/2)
inp.npart = 8192
inp.rmax0 = 0.0
inp.dgrid = 0.5e-3
inp.delz = 1.0
inp.ipseed = 327
inp.zstop = 260.0
inp.nharm = 1

inp.DUMP_PARTICLES = 1


if len(sys.argv) > 3: inp.zstop = sys.argv[3]


s2e = True
if s2e:
	beam = transform_beam_file(beam_file = '../beams/beam_0.1nC.txt',  
         	                         	       transform = [ [beam.beta_x,beam.alpha_x], [beam.beta_y,beam.alpha_y] ], 
         	                         	       energy_scale = beam.E / 17.5, plot=False)
	inp.nslice = 0
	inp.zsep = int(beam.zsep / inp.xlamds)
	inp.beamfile = 'tmp.beam'
	inp.beam_file_str = beam.beam_str


if not stat:
	inp.runid = next_run_id(get_data_dir())
	inp.run_dir = get_data_dir() + 'run_' + str(inp.runid)
	output_file = inp.run_dir + '/run.' + str(inp.runid) + '.gout'
	g = run(inp, launcher)
	#g = readGenesisOutput(output_file)
	show_output(g, show_field = True, output_file = output_file, show_slice=int(inp.nslice / 2))
else:

	#stat_dir = '/data/netapp/xfel/iagapov/xcode_data/sase3/650eV/taper/40fs/14.0GeV/0.5nC.v2/' 
	if len(sys.argv) > 4: stat_dir = sys.argv[4] 
	os.system('mkdir -p ' + stat_dir)
	readme = 'emit:' + str(beam.emit_xn) + ' , ' + str(beam.emit_yn) + ' sig_e:' + str(beam.sigma_E) + 's2e'

	open(stat_dir + 'README.txt','w').write(readme)


	for i in xrange(100):
		inp.runid = next_run_id(stat_dir)
		inp.run_dir = stat_dir + 'run_' + str(inp.runid)
		inp.ipseed = (1+int(inp.runid))*17
		g = run(inp, launcher, read=False)

	print 'done'


