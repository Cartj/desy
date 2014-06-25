'''
steady state SASE, including detuning errors
'''
from xframework.gui.accelerator import *
sys.path.append('../')
from xfel_utils import *


launcher = MpiLauncher()
launcher.program = '/home/iagapov/products/xcode/codes/genesis/genesis < tmp.cmd | tee log'
launcher.nproc = 1

beta_av = 15.0

exec( open("sase3.inp" ))
lat = MagneticLattice(sase3_segment(n=11))

rematch(beta_av, l_fodo, qdh, lat, extra_fodo, beam, qf, qd) # jeez...


beam.tpulse = 1.6    # electron bunch length in fs (rms)
beam.C = 0.02        # bunch charge (nC)
beam.I = 1.0e-9 * beam.C / ( np.sqrt(2*pi) * beam.tpulse * 1.e-15 ) 
beam.E = 17.5
beam.sigma_E  = 0.0001


print 'average beam size', np.sqrt(beam.emit_x * beta_av)

# calculate undulator parameters
up = UndulatorParameters(und)
up.E = beam.E
up.printParameters()

qf.k1 *= magic_factor(beam.E)
qd.k1 *= magic_factor(beam.E)

pn = []

for i in xrange(200):

    lat2 = detune_k(lat, 3.e-4)

    inp = generate_input(up, beam, itdp=False)
    inp.lattice_str = generate_lattice(lat2, unit = up.lw*2, energy = beam.E)

    detune_E(inp, beam, 1.e-4)

    inp.runid = next_run_id('/tmp/')
    inp.run_dir = '/tmp/run_' + str(inp.runid)

    g = run(inp, launcher)

    power = np.array(g.sliceValues[g.sliceValues.keys()[0]]['power'])
    z, iz = find_saturation(power, g.z, n=5)
    pn.append(power[iz])


print pn

plt.grid(True)
plt.plot(np.array(pn) / 1.e9,'rs')
plt.ylabel('Power [GW]')
plt.xlabel('Realization')

plt.show()
