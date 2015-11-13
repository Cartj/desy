__author__ = 'Sergey Tomin'

from ocelot.cpbd.elements import *
from ocelot.cpbd.beam import *
from ocelot.cpbd.optics import *
from ocelot.cpbd.track import *
from ocelot.cpbd import sc
from ocelot.gui.accelerator import *

beam = Beam()
beam.E = 148.3148e-3 #in GeV ?!
beam.beta_x = 14.8821
beam.beta_y = 18.8146
beam.alpha_x =  -0.61309
beam.alpha_y = -0.54569
beam.emit_xn = 1.5e-6
beam.emit_yn = 1.5e-6
beam.emit_x = beam.emit_xn / (beam.E / m_e_GeV)
beam.emit_y = beam.emit_yn / (beam.E / m_e_GeV)

tw0 = Twiss(beam)
from lattice_FLASH_S2E import *
#exec(open('lattice_FLASH_S2E.py'))
lat = MagneticLattice(lattice)

tws=twiss(lat, tw0, nPoints=None)
plot_opt_func(lat, tws, top_plot=["Dx"])
plt.show()

P0 = np.loadtxt('elegant_files/flash_out_200000.ast')
Q = -P0[:, 7]*1e-9  #charge in nC -> in C
print "charge = ", sum(Q)
xp = P0[:, :6]
Pref = xp[0, 5]
xp[0,5] = 0
gamref = sqrt((Pref/m_e_eV)**2+1)
xxstg = sc.exact_xp_2_xxstg(xp, gamref)

p_array = ParticleArray(len(Q))
p_array.E = beam.E
p_array.particles[0::6] = xxstg[:,0]
p_array.particles[1::6] = xxstg[:,1]
p_array.particles[2::6] = xxstg[:,2]
p_array.particles[3::6] = xxstg[:,3]
p_array.particles[4::6] = xxstg[:,4]
p_array.particles[5::6] = xxstg[:,5]

p_array.particles[4::6] = sc.smooth_z(p_array.particles[4::6], mslice=10000)

# plot current
bins_start, hist_start = sc.get_current(p_array, charge=Q[0], num_bins=200)

tw0 = get_envelope(p_array)
tws_track = [tw0]

dz = 1.
order = 2
SC = False
debug = False

Z = np.arange(0, lat.totalLen, dz)
if debug:
    f=plt.figure()
    plt.ion()
    plt.hold(False)

navi = Navigator(lattice=lat)
for i, zi in enumerate(Z[1:]):
    print zi
    dz = zi - Z[i]
    step(lat=lat, particle_list=p_array, dz=dz, navi=navi, order=order)
    if SC:
        sc.sc_apply(p_array, q_array=Q, zstep=dz, nmesh_xyz=[63, 63, 63], low_order_kick=True)
    tw = get_envelope(p_array)
    tw.s = navi.z0
    tws_track.append(tw)
    if debug:
        f.add_subplot(211)
        plt.plot(p_array.particles[::6], p_array.particles[2::6], '.')
        f.add_subplot(212)
        plt.plot(p_array.particles[4::6],p_array.particles[5::6],'.')
        plt.draw()
        plt.pause(0.1)
plt.ioff()
"""
L = 0.
for elem in lat.sequence:
    elem.transfer_map.apply(p_array, order=2)
    tw = get_envelope(p_array)
    L += elem.l
    tw.s += L
    print tw.s
    tws_track.append(tw)
"""
# plot current at the beginning of accelerator
plt.figure(1)
plt.title("current: start")
plt.plot(bins_start, hist_start)
plt.xlabel("s, m")
plt.ylabel("I, A")
plt.grid(True)

# plot current at the end of accelerator
bins, hist = sc.get_current(p_array, charge=Q[0], num_bins=200)
plt.figure(2)
plt.title("current: end")
plt.plot(bins, hist)
plt.xlabel("s, m")
plt.ylabel("I, A")
plt.grid(True)


eleg_opt = np.genfromtxt('elegant_files/elegant_beam_optics_2ndOrder.txt')
s_b=eleg_opt[:, 0]
betax_b=eleg_opt[:, 8]
betay_b=eleg_opt[:, 11]


plt.figure(3)
plt.title(r"$\beta - functions$")
plt.plot([p.s for p in tws_track], [p.beta_y for p in tws_track], "ro-", label = "ocelot")
plt.plot(s_b, betay_b, "bo-", label = "elegant")
plt.legend()
plt.grid(True)
plt.show()
#s = [p.s for p in tws_track]
#bx = [p.beta_x for p in tws_track]
#by = [p.beta_y for p in tws_track]
#out = zeros((len(s),3))
#out[:,0] = s
#out[:,1] = bx
#out[:,2] = by
#np.savetxt("beta_sc.txt", out)