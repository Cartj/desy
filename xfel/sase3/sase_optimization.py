'''
steady state SASE
'''
from xframework.gui.accelerator import *
sys.path.append('../')
from xfel_utils import *


launcher = MpiLauncher()
launcher.program = '/home/iagapov/products/xcode/codes/genesis/genesis < tmp.cmd | tee log'
launcher.nproc = 1

#beta_av = 28.0

exec( open("sase3.inp" ))
lat = MagneticLattice(sase3_segment(n=7))

beta_av = 15.0

rematch(beta_av, l_fodo, qdh, lat, extra_fodo, beam, qf, qd) # jeez...
k1 = qf.k1

beam.tpulse = 10  # electron bunch length in fs (rms)
beam.I = 5000
beam.E = 17.5
beam.sigma_E  = 0.0001


# calculate undulator parameters

up = UndulatorParameters(und)

K = []
E = np.linspace(10.5,17.5,20)
I = [2.5,5,10]

P = np.zeros([len(E), len(I)])

def pwr(E, I, up, beam, lat):
    up.E = E
    up.recalculate()
    und.Kx = up.get_k(1500)
    up.K = und.Kx
    up.recalculate()
    
    beam.E = E
    beam.I = I * 1000
    
    qf.k1 = k1 * magic_factor(beam.E)
    qd.k1 = - k1 * magic_factor(beam.E)

    beam.gamma_rel = beam.E / (0.511e-3)
    beam.emit_x = beam.emit_xn / beam.gamma_rel
    beam.emit_y = beam.emit_yn / beam.gamma_rel
    
    inp = generate_input(up, beam, itdp=False)
    inp.lattice_str = generate_lattice(lat, unit = up.lw*2, energy = beam.E )
    
    inp.runid = next_run_id('/tmp/')
    inp.run_dir = '/tmp/run_' + str(inp.runid)
    g = run(inp, launcher)
    p = np.array(g.sliceValues[g.sliceValues.keys()[0]]['power'])
    
    z, iz = find_saturation(p, g.z)
    
    print p[iz]/1.e9, max(p)/1.e9
    return p, p[iz]

    
e, i = meshgrid(E,I)

for i1 in xrange(len(E)):
    for i2 in xrange(len(I)):
        pn, p = pwr(E[i1], I[i2], up, beam, lat)
        #P[i1,i2] = max(pn) / 1.e9
        P[i1,i2] = p / 1.e9


print P
'''
cs = contour(e,i,P, 10, colors='k')
clabel(cs, inline=1, fontsize=20)
title('POWER AT SATURATION')
grid(True)
plt.ylabel('I [kA]')
plt.xlabel('E [GeV]')
'''

#plot(P[0],'o')

title('POWER AT SATURATION')
grid(True)

p = []
labels = []

for i in xrange(len(I)): 
    pi, = plot(E, np.log10(P[:,i]), lw=3)
    p.append(pi)
    labels.append(str(I[i]) + 'kA')    

plt.legend(p, labels, loc=2)    
plt.ylabel('log10(Power) [GW]')
plt.xlabel('E [GeV]')

show()

