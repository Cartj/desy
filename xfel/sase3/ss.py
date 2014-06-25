import sys
sys.path.append('../utils/')
from xfel_utils import *
from xframework.gui.accelerator import plot_lattice

exec( open("sase3.py" )) 

#lat = MagneticLattice(sase3_segment(n=7), energy=17.5)
lat = MagneticLattice(sase3_ss, energy=17.5)
lat1 = MagneticLattice(sase3_ss_1, energy=17.5)
lat2 = MagneticLattice(sase3_ss_2m, energy=17.5)
lat3 = MagneticLattice(sase3_ss_3, energy=17.5)

rematch(15.0, l_fodo, qdh, lat, extra_fodo, beam, qf, qd) # jeez...

tw0 = Twiss(beam)

tw1=twiss(lat1, tw0)

tw2=twiss(lat2, tw1[-1])

tw3=twiss(lat3, tw2[-1])


m2 = lattice_transfer_map(lat2)
print m2.R[4,5]

tws = tw1+tw2+tw3 # to plot

f=plt.figure()
f.canvas.set_window_title('Betas [m]')
ax = f.add_subplot(211)
ax.set_xlim(0, lat.totalLen)
 
p1, = plt.plot(map(lambda p: p.s, tws), map(lambda p: p.beta_x, tws), lw=2.0)
p2, = plt.plot(map(lambda p: p.s, tws), map(lambda p: p.beta_y, tws), lw=2.0)
plt.grid(True)
plt.legend([p1,p2], [r'$\beta_x$',r'$\beta_y$', r'$D_x$'])

ax1 = ax.twinx()
p1, = plt.plot(map(lambda p: p.s, tws), map(lambda p: p.Dx, tws), 'r--', lw=2.0)
p2, = plt.plot(map(lambda p: p.s, tws), map(lambda p: p.Dy, tws), lw=2.0)
plt.legend([p1], [r'$D_x$'],loc=2)
ax1.set_xlim(0, lat.totalLen)

ax2 = f.add_subplot(212)
plot_lattice(lat, ax2, alpha=0.5)

# add beam size (arbitrary scale)

s = np.array(map(lambda p: p.s/lat.totalLen, tws))

scale = 5000

sig_x = scale * np.array(map(lambda p: np.sqrt(p.beta_x*beam.emit_x), tws)) # 0.03 is for plotting same scale
sig_y = scale * np.array(map(lambda p: np.sqrt(p.beta_y*beam.emit_y), tws))

x = scale * np.array(map(lambda p: p.x, tws))
y = scale * np.array(map(lambda p: p.y, tws))


plt.plot(s, x + sig_x, color='#0000AA', lw=2.0)
plt.plot(s, x-sig_x, color='#0000AA', lw=2.0)

plt.plot(s, sig_y, color='#00AA00', lw=2.0)
plt.plot(s, -sig_y, color='#00AA00', lw=2.0)

#f=plt.figure()
plt.plot(s, x, 'r--', lw=2.0)
#plt.plot(s, y, 'r--', lw=2.0)

#
# sase first part
#

launcher = get_genesis_launcher(1)

beam.tpulse = 1.6    # electron bunch length in fs (rms)
beam.C = 0.02        # bunch charge (nC)
beam.I = 1.0e-9 * beam.C / ( np.sqrt(2*pi) * beam.tpulse * 1.e-15 ) 
beam.E = 17.5
beam.sigma_E  = 0.002


# calculate undulator parameters
up = UndulatorParameters(und)
up.E = beam.E
up.printParameters()

#qf.k1 *= magic_factor(beam.E)
#qd.k1 *= magic_factor(beam.E)

inp = generate_input(up, beam, itdp=False)
inp.lattice_str = generate_lattice(lat1, unit = up.lw*2, energy = beam.E)

inp.runid = next_run_id(get_data_dir())
inp.run_dir = get_data_dir() + 'run_' + str(inp.runid)

g = run(inp, launcher)

xrms = np.array(g.sliceValues[g.sliceValues.keys()[0]]['xrms'])
yrms = np.array(g.sliceValues[g.sliceValues.keys()[0]]['yrms'])
power = np.array(g.sliceValues[g.sliceValues.keys()[0]]['power'])


f = plt.figure()
f.add_subplot(121), plt.plot(g.z, xrms, lw=3), plt.plot(g.z, yrms, lw=3), plt.grid(True)
f.add_subplot(122), plt.plot(g.z, power / 1.e9, lw=3), plt.grid(True)

# field filtering
# slices = readField()
# transform_slices()
# write_slices()

# tracking through chicane

if False:

    n = 8000 * 1
    
    print 'seeding distribution', n
    
    p_array = ParticleArray(n)
    
    for i in xrange(0,n):
        x,xp = gaussFromTwiss(beam.emit_x, tw1[-1].beta_x, tw1[-1].alpha_x)
        y,yp = gaussFromTwiss(beam.emit_x, tw1[-1].beta_x, tw1[-1].alpha_x)
        E = np.random.randn() * beam.sigma_E/ beam.E
        s = tw1[-1].s
        tau = 0
        p = Particle(x=x,y=y,px=xp,py=yp,s=s, tau=tau, p=E)
        p_array[i] = p


    parts0 = p_array.array2list()
    
    print 'tracking for', lat2.totalLen
    
    navi = Navigator(lattice=lat)
    track(lat=lat, particle_list=p_array, dz=lat2.totalLen, navi=navi)
    
    parts = p_array.array2list()
    
    f=plt.figure()
    f.canvas.set_window_title('Phase space [m]')
    ax2 = f.add_subplot(211) 
    p1, = plt.plot(map(lambda p: p.x, parts0), map(lambda p: p.px, parts0), 'g.', lw=8.0)
    p2, = plt.plot(map(lambda p: p.x, parts), map(lambda p: p.px, parts), 'r.', lw=8.0)
    plt.grid(True)
    plt.legend([p1], [r'$x / xp$'])
    
    #track(lat=lat, particle_list=parts, dz=2.0, navi=navi)
    
    ax2 = f.add_subplot(212) 
    p1, = plt.plot(map(lambda p: p.y, parts0), map(lambda p: p.py, parts0), 'g.', lw=8.0)
    p2, = plt.plot(map(lambda p: p.y, parts), map(lambda p: p.py, parts), 'r.', lw=8.0)
    plt.grid(True)
    plt.legend([p1], [r'$y / yp$'])


#
# FEL second part
#

inp = generate_input(up, beam, itdp=False)
inp.lattice_str = generate_lattice(lat3, unit = up.lw*2, energy = beam.E)

inp.runid = next_run_id(get_data_dir())
inp.run_dir = get_data_dir() + 'run_' + str(inp.runid)

g = run(inp, launcher)

xrms = np.array(g.sliceValues[g.sliceValues.keys()[0]]['xrms'])
yrms = np.array(g.sliceValues[g.sliceValues.keys()[0]]['yrms'])
power = np.array(g.sliceValues[g.sliceValues.keys()[0]]['power'])


f = plt.figure()
f.add_subplot(121), plt.plot(g.z, xrms, lw=3), plt.plot(g.z, yrms, lw=3), plt.grid(True)
f.add_subplot(122), plt.plot(g.z, power / 1.e9, lw=3), plt.grid(True)


plt.show()

