'''
steady state SASE
'''
from xframework.gui.accelerator import *
sys.path.append('../')
from xfel_utils import *


launcher = MpiLauncher()
launcher.program = '/home/iagapov/products/xcode/codes/genesis/genesis < tmp.cmd | tee log'
launcher.nproc = 1


exec( open("sase1.inp" ))
lat = MagneticLattice(sase1_segment(n=17))

beam.tpulse = 10  # electron bunch length in fs (rms)
beam.I = 4500
beam.sigma_E  = 0.001

# print out UR parameter estimates
up = UndulatorParameters(und)
up.E = beam.E
up.printParameters()

f = plt.figure(str(up.lamd_ev) + ' eV')
f.add_subplot(111)
plt.grid(True)
 
p = []
labels = []

scan_beta = True
scan_emittance = False
scan_current = False

if scan_beta:
    for beta_av in linspace(17,45, 8):
        rematch(beta_av, l_fodo, qdh, lat, extra_fodo, beam, qf, qd) # jeez...
    
        # donno wtf it comes from -- probably section not multiple of xlamd, correcting out for roundoff
        qf.k1 *= (0.63 * 1.0)
        qd.k1 *= (0.63 * 1.0) 
    
        inp = generate_input(up, beam, itdp=False)
        inp.lattice_str = generate_lattice(lat, unit = up.lw, energy = beam.E )
    
        inp.runid = next_run_id('/tmp/')
        inp.run_dir = '/tmp/run_' + str(inp.runid)
    
        g = run(inp, launcher)
    
        power = np.array(g.sliceValues[g.sliceValues.keys()[0]]['power'])
    
        pi, = plt.plot(g.z, power, '-', lw=2)
        p.append(pi)
        labels.append(str(beta_av) + 'm')



if scan_emittance:
    beta_av = 20.0
    rematch(beta_av, l_fodo, qdh, lat, extra_fodo, beam, qf, qd) # jeez...
    # donno wtf it comes from -- probably section not multiple of xlamd, correcting out for roundoff
    qf.k1 *= (0.63 * 1.0)
    qd.k1 *= (0.63 * 1.0) 

    for emit in linspace(5e-7,2.e-6, 10):
        beam.emit_xn = emit
        beam.emit_yn = emit
        beam.gamma_rel = beam.E / (0.511e-3)
        beam.emit_x = beam.emit_xn / beam.gamma_rel
        beam.emit_y = beam.emit_yn / beam.gamma_rel

        inp = generate_input(up, beam, itdp=False)
        inp.lattice_str = generate_lattice(lat, unit = up.lw, energy = beam.E )
    
        inp.runid = next_run_id('/tmp/')
        inp.run_dir = '/tmp/run_' + str(inp.runid)
    
        g = run(inp, launcher)
    
        power = np.array(g.sliceValues[g.sliceValues.keys()[0]]['power'])
    
        pi, = plt.plot(g.z, power, '-', lw=2)
        p.append(pi)
        labels.append(str(emit))

if scan_current:
    beta_av = 20.0
    rematch(beta_av, l_fodo, qdh, lat, extra_fodo, beam, qf, qd) # jeez...
    # donno wtf it comes from -- probably section not multiple of xlamd, correcting out for roundoff
    qf.k1 *= (0.63 * 1.0)
    qd.k1 *= (0.63 * 1.0) 

    for I in linspace(2000,6000, 10):

        beam.I = I

        inp = generate_input(up, beam, itdp=False)
        inp.lattice_str = generate_lattice(lat, unit = up.lw, energy = beam.E )
    
        inp.runid = next_run_id('/tmp/')
        inp.run_dir = '/tmp/run_' + str(inp.runid)
    
        g = run(inp, launcher)
    
        power = np.array(g.sliceValues[g.sliceValues.keys()[0]]['power'])
    
        pi, = plt.plot(g.z, power, '-', lw=2)
        p.append(pi)
        labels.append(str(I))


plt.legend(p, labels)
plt.show()
