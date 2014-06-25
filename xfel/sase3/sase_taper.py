'''
steady state SASE
'''
from xframework.gui.accelerator import *
sys.path.append('../utils/')
from xfel_utils import *

import copy

launcher = MpiLauncher()
launcher.program = '/home/iagapov/products/xcode/codes/genesis/genesis < tmp.cmd | tee log'
launcher.nproc = 1

beta_av = 28.0

exec( open("sase3.inp" ))
lat = MagneticLattice(sase3_segment(n=11))

rematch(beta_av, l_fodo, qdh, lat, extra_fodo, beam, qf, qd) # jeez...


beam.tpulse = 10  # electron bunch length in fs (rms)
beam.I = 3000
beam.E = 17.5
beam.sigma_E  = 0.0001

print 'average beam size', np.sqrt(beam.emit_x * beta_av)

# calculate undulator parameters
up = UndulatorParameters(und)
up.E = beam.E
up.printParameters()
und.Kx = up.get_k(775)
print 'recalculating for K=', und.Kx

up = UndulatorParameters(und)
up.E = beam.E
up.printParameters()

#sys.exit(0)

# donno wtf it comes from -- probably section not multiple of xlamd, correcting out for roundoff
qf.k1 *= (0.37)*1
qd.k1 *= (0.37)*1

def taper(lat, k, a):
    lat2 = copy.deepcopy(lat)
    n = 0
    for i in xrange(len(lat2.sequence)):
    
        if lat2.sequence[i].__class__ == Undulator:
            lat2.sequence[i] = copy.copy(lat.sequence[i]) 
            lat2.sequence[i].Kx = lat2.sequence[i].Kx * k(n+1, a)
            n += 1

    return lat2


def k(n,a):
    n0 = 7
    
    a0 = a[0] #0.997
    a1 = a[1]
    a2 = a[2]
    
    if n < n0:
        return a0 #0.9985 # 0.9985
    else:
        return a0 - (n-n0)*a1 - (n-n0)**2 * a2

f = plt.figure()
f.add_subplot(111)
plt.grid(True)

a1 = np.linspace(-5.e-3, 2.e-3, 20)
a2 = np.linspace(-2.e-1, 2.e-1, 20)

P = np.zeros([20,20])

for i in xrange(len(a1)):
    for j in xrange(len(a2)):

        lat2 = taper(lat, k, [0.99999, a1[i], a2[j]])
    
        inp = generate_input(up, beam, itdp=False)
        inp.lattice_str = generate_lattice(lat2, unit = up.lw*2, energy = beam.E )
    
        inp.runid = next_run_id('/tmp/')
        inp.run_dir = '/tmp/run_' + str(inp.runid)
    
        g = run(inp, launcher)
    
        power = np.array(g.sliceValues[g.sliceValues.keys()[0]]['power'])
    
        P[i,j] = np.max(np.log10(power))
    
        #plt.plot(g.z, np.log10(power), 'b--', lw=1)

'''
def find_sat(power):
    p = np.diff(np.log10(power))

    u = np.convolve(p, np.ones(5) / 5.0, mode='same')
    um = np.max(u)

    for i in xrange(len(u)):
        if u[i] < 0.0 * um and g.z[i] > 10: 
            ii = i
            break
    
    #plt.plot(g.z[1:], u, lw=3)
    #plt.plot(g.z[ii+1], p[ii], 'rd')

    #plt.plot(g.z, power, lw=3)
    plt.plot(g.z[ii+1], np.log10(power[ii]), 'rd')
'''
'''
p = np.diff(np.log10(power))

u = np.convolve(p, np.ones(5) / 5.0, mode='same')
um = np.max(u)

for i in xrange(len(u)):
    if u[i] < 0.0 * um and g.z[i] > 10: 
        ii = i
        break
    
#plt.plot(g.z[1:], u, lw=3)
#plt.plot(g.z[ii+1], p[ii], 'rd')

#plt.plot(g.z, power, lw=3)
plt.plot(g.z[ii+1], np.log10(power[ii]), 'rd')
'''

#plt.imshow(P)
e1, e2 = np.meshgrid(a1,a2)
cs = contour(e1,e2,P, 10, colors='k')
clabel(cs, inline=1, fontsize=20)
title('Tapering coefficients')

plt.show()
