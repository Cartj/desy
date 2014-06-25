'''
steady state SASE
'''
from xframework.gui.accelerator import *
sys.path.append('../utils/')
from xfel_utils import *


launcher = get_genesis_launcher(1)

beta_av = 21.0

from sase1 import *

#lat = MagneticLattice(sase3_segment(n=11))
lat = MagneticLattice(sase1_segment(n=17))

rematch(beta_av, l_fodo, qdh, lat, extra_fodo, beam, qf, qd) # jeez...


beam.tpulse = 1.6    # electron bunch length in fs (rms)
beam.C = 0.01        # bunch charge (nC)
beam.I = 1.0e-9 * beam.C / ( np.sqrt(2*pi) * beam.tpulse * 1.e-15 ) 
beam.E = 14.0
beam.sigma_E  = 0.002

print 'average beam size', np.sqrt(beam.emit_x * beta_av)

# calculate undulator parameters
up = UndulatorParameters(und)
up.E = beam.E
up.printParameters()

#uncomment to recalculate the wavelength

und.Kx = up.get_k(12000)
print 'recalculating for K=', und.Kx

up = UndulatorParameters(und)
up.E = beam.E
up.printParameters()

#sys.exit(0)

print qf.k1
qf.k1 *= voodoo
qd.k1 *= voodoo
#sys.exit(0)

lat2 = detune_k(lat, 0.0)

inp = generate_input(up, beam, itdp=False)
inp.lattice_str = generate_lattice(lat2, unit = up.lw, energy = beam.E)

detune_E(inp, beam, 0.0)


inp.runid = next_run_id(get_data_dir())
inp.run_dir = get_data_dir() + 'run_' + str(inp.runid)

inp.delz = 2.0

g = run(inp, launcher)

xrms = np.array(g.sliceValues[g.sliceValues.keys()[0]]['xrms'])
yrms = np.array(g.sliceValues[g.sliceValues.keys()[0]]['yrms'])
power = np.array(g.sliceValues[g.sliceValues.keys()[0]]['power'])


f = plt.figure()
f.add_subplot(121), plt.plot(g.z, xrms, lw=3), plt.plot(g.z, yrms, lw=3), plt.grid(True)
f.add_subplot(122), plt.plot(g.z, power / 1.e9, lw=3), plt.grid(True)


z, iz = find_saturation(power, g.z, n_smooth=5)
print 'saturation len:', z, iz
plt.plot(g.z[iz], power[iz]/ 1.e9,'rs')

plt.show()
