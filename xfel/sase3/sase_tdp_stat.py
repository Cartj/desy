'''
statistical run SASE
'''
from ocelot.gui.accelerator import *
sys.path.append('../utils/')
from xfel_utils import *

launcher = get_genesis_launcher(384)


beta_av = 15.0

from sase3 import *
lat = MagneticLattice(sase3_segment(n=11))

rematch(beta_av, l_fodo, qdh, lat, extra_fodo, beam, qf, qd) # jeez...


beam.tpulse = 20.0    # electron bunch length in fs (rms)
beam.C = 0.25        # bunch charge (nC)
beam.I = 1.0e-9 * beam.C / ( np.sqrt(2*pi) * beam.tpulse * 1.e-15 ) 
beam.E = 17.5
beam.sigma_E  = 0.0001

print 'average beam size', np.sqrt(beam.emit_x * beta_av)

# print out UR parameter estimates
up = UndulatorParameters(und)
up.E = beam.E
up.printParameters()

# donno wtf it comes from -- probably section not multiple of xlamd, correcting out for roundoff
qf.k1 *= (0.37)*2
qd.k1 *= (0.37)*2


inp = generate_input(up, beam, itdp=True)
inp.lattice_str = generate_lattice(lat, unit = up.lw*2, energy = beam.E )

#inp.zstop = 210
inp.nslice = int(384*3)
inp.ncar = 191
inp.curlen = beam.tpulse * 3.e-7
inp.zsep = int(4*inp.curlen  / inp.nslice / inp.xlamds )
inp.ntail = - int ( inp.nslice / 2 )
inp.npart = 8192
inp.rmax0 = 0.0
inp.dgrid = 5.0e-4
inp.delz = 1.0
inp.zstop = 42.5

stat_dir = '/data/netapp/xfel/iagapov/xcode_data/sase3/1500eV/sat/20fs/17.5GeV/0.25nC/'
os.system('mkdir -p ' + stat_dir)

for i in xrange(200):
    inp.runid = next_run_id(stat_dir)
    inp.run_dir = stat_dir + 'run_' + str(inp.runid)
    inp.ipseed = (1+int(inp.runid))*17
    g = run(inp, launcher)

print 'done'
