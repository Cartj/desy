'''
steady state SASE
'''
from ocelot.gui.accelerator import *
sys.path.append('../utils/')
from xfel_utils import *


launcher = get_genesis_launcher(1)

beta_av = 15.0

from sase3 import *

#lat = MagneticLattice(sase3_segment(n=11))
lat = MagneticLattice(sase3_segment(n=13))

rematch(beta_av, l_fodo, qdh, lat, extra_fodo, beam, qf, qd) # jeez...


beam.tpulse = 20     # electron bunch length in fs (rms)
beam.C = 0.25        # bunch charge (nC)
beam.I = 1.0e-9 * beam.C / ( np.sqrt(2*pi) * beam.tpulse * 1.e-15 ) 
beam.E = 14.0
beam.sigma_E  = 0.002

print 'average beam size', np.sqrt(beam.emit_x * beta_av)

# calculate undulator parameters
up = UndulatorParameters(und)
up.E = beam.E
up.printParameters()
und.Kx = up.get_k(3000)
up = UndulatorParameters(und)
up.E = beam.E
up.printParameters()


print qf.k1
qf.k1 *= voodoo
qd.k1 *= voodoo
#sys.exit(0)

n0, a0, a1, a2 = get_taper_coeff(14, 3000)

'''
n0 = [0,8, 25,35]
a0 = 0.999
a1 = [-0., -0.002,  -0.00 ]
a2 = [0., -0.00015, -0.000 ]
taper_func = lambda n : f1(n, n0, a0, a1, a2 )

'''
n0 = 7
a0 = 0.999
a1 = -0.0009
a2 = 1.5
taper_func = lambda n : f2(n, n0, a0, a1, a2)


#lat2 = taper(lat, taper_func)
lat2 = lat

x = np.linspace(1,20.99,200)
x = np.linspace(1,21,21)
y = 0*x
for i in xrange(len(x)): y[i] = taper_func( int(x[i]) )

f = figure()
ax = f.add_subplot(111)
#plot(x,y, lw=3)
bar(x,y, lw=1, alpha=0.5)
grid(True)
ax.set_ylabel(r'$K/K_0$')
ax.set_xlabel(r'$N_{segment}$')

#lat2 = detune_k(lat2, 0.0)

inp = generate_input(up, beam, itdp=False)
inp.lattice_str = generate_lattice(lat2, unit = up.lw, energy = beam.E)

#detune_E(inp, beam, 0.0)


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
