'''
steady state SASE
'''
from xframework.gui.accelerator import *
sys.path.append('../utils/')
from xfel_utils import *

launcher = get_genesis_launcher(1)


exec( open("sase3.inp" ))
lat = MagneticLattice(sase3_segment(n=9))

beam.tpulse = 1.6    # electron bunch length in fs (rms)
beam.C = 0.015        # bunch charge (nC)
beam.I = 1.0e-9 * beam.C / ( np.sqrt(2*pi) * beam.tpulse * 1.e-15 ) 
beam.E = 17.5
beam.sigma_E  = 0.002

# print out UR parameter estimates
up = UndulatorParameters(und)
#up.E = beam.E
#up.printParameters()

f = plt.figure()
f.add_subplot(111)
plt.grid(True)
 
p = []
x = []
labels = []

scan_beta = True
scan_emittance = False
scan_current = False
scan_sigmae = False

if scan_beta:
    for beta_av in linspace(14.0,20.0, 6):
        rematch(beta_av, l_fodo, qdh, lat, extra_fodo, beam, qf, qd) # jeez...
    
        # donno wtf it comes from -- probably section not multiple of xlamd, correcting out for roundoff
        qf.k1 *= voodoo #(0.37 * 1.0)
        qd.k1 *= voodoo #(0.37 * 1.0) 
    
        inp = generate_input(up, beam, itdp=False)
        inp.lattice_str = generate_lattice(lat, unit = up.lw, energy = beam.E )
        inp.delz = 2.0
    
        inp.runid = next_run_id('/tmp/')
        inp.run_dir = '/tmp/run_' + str(inp.runid)
    
        g = run(inp, launcher)
    
        power = np.array(g.sliceValues[g.sliceValues.keys()[0]]['power'])
        xrms = np.array(g.sliceValues[g.sliceValues.keys()[0]]['xrms'])
    
        pi, = plt.plot(g.z, power / 1.e9, '-', lw=2)
        p.append(pi)
        x.append(xrms)
        labels.append(str(beta_av) + 'm')



if scan_emittance:
    beta_av = 15.0
    rematch(beta_av, l_fodo, qdh, lat, extra_fodo, beam, qf, qd) # jeez...
    # donno wtf it comes from -- probably section not multiple of xlamd, correcting out for roundoff
    qf.k1 *= (0.37 * 1.0)
    qd.k1 *= (0.37 * 1.0) 

    for emit in linspace(1e-7,1.e-6, 5):
        beam.emit_xn = emit
        beam.emit_yn = emit

        inp = generate_input(up, beam, itdp=False)
        inp.lattice_str = generate_lattice(lat, unit = up.lw*2, energy = beam.E )
    
        inp.runid = next_run_id('/tmp/')
        inp.run_dir = '/tmp/run_' + str(inp.runid)
    
        g = run(inp, launcher)
    
        power = np.array(g.sliceValues[g.sliceValues.keys()[0]]['power'])
    
        pi, = plt.plot(g.z, power / 1.e9, '-', lw=2)
        p.append(pi)
        labels.append(str(emit))

if scan_current:
    beta_av = 18.0
    rematch(beta_av, l_fodo, qdh, lat, extra_fodo, beam, qf, qd) # jeez...
    # donno wtf it comes from -- probably section not multiple of xlamd, correcting out for roundoff
    qf.k1 *= magic_factor(beam.E)
    qd.k1 *= magic_factor(beam.E)

    for i in linspace(2000,6000, 10):

        beam.I = i

        inp = generate_input(up, beam, itdp=False)
        inp.lattice_str = generate_lattice(lat, unit = up.lw, energy = beam.E )
    
        inp.runid = next_run_id('/tmp/')
        inp.run_dir = '/tmp/run_' + str(inp.runid)
    
        g = run(inp, launcher)
    
        power = np.array(g.sliceValues[g.sliceValues.keys()[0]]['power'])
    
        pi, = plt.plot(g.z, power, '-', lw=2)
        p.append(pi)
        labels.append(str(i))

if scan_sigmae:
    beta_av = 18.0
    rematch(beta_av, l_fodo, qdh, lat, extra_fodo, beam, qf, qd) # jeez...
    # donno wtf it comes from -- probably section not multiple of xlamd, correcting out for roundoff
    qf.k1 *= 0.37 #magic_factor(beam.E)
    qd.k1 *= 0.37 #magic_factor(beam.E)


    for de in linspace(1.e-3,1.0e-2, 5):

        beam.sigma_E = de

        inp = generate_input(up, beam, itdp=False)
        inp.lattice_str = generate_lattice(lat, unit = up.lw*2, energy = beam.E )

        inp.runid = next_run_id(get_data_dir())
        inp.run_dir = get_data_dir() + 'run_' + str(inp.runid)
    
        inp.runid = next_run_id('/tmp/')
        inp.run_dir = '/tmp/run_' + str(inp.runid)
    
        g = run(inp, launcher)
    
        power = np.array(g.sliceValues[g.sliceValues.keys()[0]]['power'])
    
        pi, = plt.plot(g.z, power/ 1.e9, '-', lw=2)
        p.append(pi)
        labels.append(str(de*1.e3) + ' MeV')


plt.ylabel('Power [GW]')
plt.xlabel('z [m]')
plt.legend(p, labels)

plt.figure()

for xx in x:
    plt.plot(xx)

plt.show()
