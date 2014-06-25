'''
SASE
'''
from xframework.gui.accelerator import *
sys.path.append('../utils/')
from xfel_utils import *


launcher = get_genesis_launcher(320)
beta_av = 14.0

from sase3 import *

lat = MagneticLattice(sase3_segment(n=7))

rematch(beta_av, l_fodo, qdh, lat, extra_fodo, beam, qf, qd) # jeez...

stat = False
if len(sys.argv)>4:
	stat = True
	print 'statistical', sys.argv[4]

beam.E=float(sys.argv[1])

# print out UR parameter estimates
up = UndulatorParameters(und)
up.E = beam.E
up.printParameters()
und.Kx = up.get_k(float(sys.argv[2]))
up = UndulatorParameters(und)
up.E = beam.E
up.printParameters()
#sys.exit(0)
beam.sigma_E = 0.005

# donno wtf it comes from -- probably section not multiple of xlamd, correcting out for roundoff
qf.k1 *= voodoo
qd.k1 *= voodoo

n0, a0, a1, a2 = get_taper_coeff(14, float(sys.argv[2]))


# fix 
#n0 = [0,7, 25,35]
#a0 = 0.999
#a1 = [-0.0005, -0.0015,  -0.00 ]
#a2 = [0., -0.00015, -0.000 ]

taper_func = lambda n : f1(n, n0, a0, a1, a2 )


n0 = 7
a0 = 0.999
a1 = -0.0007
a2 = 1.5
taper_func = lambda n : f2(n, n0, a0, a1, a2)


lat2 = taper(lat, taper_func)
#lat2 = lat


beam.emit_xn, beam.emit_yn = beam.emit[beam.C]
beam.gamma_rel = beam.E / (0.511e-3)
beam.emit_x = beam.emit_xn / beam.gamma_rel
beam.emit_y = beam.emit_yn / beam.gamma_rel

print 'average beam size', np.sqrt(beam.emit_x * beta_av)

inp = generate_input(up, beam, itdp=True)
inp.lattice_str = generate_lattice(lat2, unit = up.lw, energy = beam.E )

#print inp.xlamds

inp.nslice = int(320*3)
inp.ncar = 101
inp.curlen = beam.tpulse * 3.e-7
inp.zsep = int(16 * inp.curlen  / inp.nslice / inp.xlamds )
inp.ntail = - int (inp.nslice/2)
#inp.npart = 8192
inp.npart = 8192
inp.rmax0 = 0.0
inp.dgrid = 0.6e-3
inp.delz = 1.0
inp.ipseed = 147
inp.zstop = 145.0
inp.nharm = 5

inp.DUMP_PARTICLES = 0

if len(sys.argv)>3: inp.zstop = float(sys.argv[3])

s2e = True
if s2e:
	beamf = '../beams/beam_0.1nC_sase1_12kev_fresh.txt'
	#beamf = '../beams/beam_0.02nC.txt'
	beam_new = transform_beam_file(beam_file = beamf,  
						transform = [ [beam.beta_x,beam.alpha_x], [beam.beta_y,beam.alpha_y] ], 
						energy_scale = beam.E / 14.0)
	
	inp.nslice = 0
	inp.zsep = int(beam_new.zsep / inp.xlamds)
	inp.beamfile = 'tmp.beam'
	inp.beam_file_str = beam_new.f_str
	
	#plot_beam(plt.figure(), beam_new)
	#plt.show()
		

if not stat:
	inp.runid = next_run_id(get_data_dir())
	inp.run_dir = get_data_dir() + 'run_' + str(inp.runid)
	output_file = inp.run_dir + '/run.' + str(inp.runid) + '.gout'
	g = run(inp, launcher)
	if True: show_output(g, show_field = True, output_file = output_file, show_slice=396)
else:

	#stat_dir = '/data/netapp/xfel/iagapov/xcode_data/sase3/650eV/taper/40fs/14.0GeV/0.5nC.v2/'
	stat_dir = sys.argv[4] 
	os.system('mkdir -p ' + stat_dir)
	readme = 'emit:' + str(beam.emit_xn) + ' , ' + str(beam.emit_yn) + ' sig_e:' + str(beam.sigma_E) + 's2e'

	open(stat_dir + 'README.txt','w').write(readme)


	for i in xrange(100):
		inp.runid = next_run_id(stat_dir)
		inp.run_dir = stat_dir + '/run_' + str(inp.runid)
		inp.ipseed = (1+int(inp.runid))*17
		g = run(inp, launcher)

	print 'done'


