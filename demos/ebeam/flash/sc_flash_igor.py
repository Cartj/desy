__author__ = 'Sergey Tomin & Igor Zagorodnov'

from ocelot import *
from ocelot.gui import *
from ocelot.adaptors import *
from ocelot.cpbd.sc_old import *

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
#exec(open('lattice.inp'))
lat = MagneticLattice(lattice)

tws=twiss(lat, tw0, nPoints=None)
#plot_opt_func(lat, tws, top_plot=["E"])
p_array, charge_array = astraBeam2particleArray(filename='elegant_files/flash_out_200000.ast')

#p_array.particles[4::6] = sc.smooth_z(p_array.particles[4::6], mslice=10000)

# plot current
bins_start, hist_start = get_current(p_array, charge=charge_array[0], num_bins=200)


dz = 1
order = 2
SC = False
debug = True

#Z = np.linspace(0, 10, num=int(10.0/dz))
Z = np.linspace(0, lat.totalLen, num=int(lat.totalLen/dz))

twsi=twiss(lat, tw0, nPoints=len(Z) )
tw0 = get_envelope(p_array, tws_i = twsi[0])
tws_track = [tw0]

if debug:
    f=plt.figure()
    plt.ion()
    plt.hold(False)

navi = Navigator(lattice=lat)
for i, zi in enumerate(Z[1:]):
    print (zi)
    dz = zi - Z[i]
    tracking_step(lat=lat, particle_list=p_array, dz=dz, navi=navi, order=order)
    if SC:
        z_new= smooth_z(p_array.particles[4::6], mslice=10000)
        dz_new=z_new-p_array.particles[4::6]
        p_array.particles[4::6]=z_new
        sc_apply(p_array, q_array=charge_array, zstep=dz, nmesh_xyz=[63, 63, 63], low_order_kick=True)
        p_array.particles[4::6]=p_array.particles[4::6]-dz_new
    tw = get_envelope(p_array,tws_i=twsi[i+1])
    tw.s = navi.z0
    #print tw.s, twsi[i+1].s
    tws_track.append(tw)
    if debug:
        f.add_subplot(211)
        plt.plot(p_array.particles[::6], p_array.particles[2::6], '.')
        f.add_subplot(212)
        plt.plot(p_array.particles[4::6],p_array.particles[5::6],'.')
        plt.draw()
        plt.pause(0.1)
plt.ioff()

#output
s_p=[t.s for t in tws_track]
n_out=len(s_p)
out=np.zeros((n_out,3))
out[:,0]=s_p
out[:,1]=[t.beta_x for t in tws_track]
out[:,2]=[t.beta_y for t in tws_track]
np.savetxt('pyoptics_withoutSC.txt',out)

particleArray2astraBeam(p_array)

# plot current at the beginning of accelerator
plt.figure(1)
plt.title("current: start")
plt.plot(bins_start, hist_start)
plt.xlabel("s, m")
plt.ylabel("I, A")
plt.grid(True)

# plot current at the end of accelerator
bins, hist = get_current(p_array, charge=charge_array[0], num_bins=200)
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
plt.title(r"$\beta_y - functions$")
plt.plot([p.s for p in tws_track], [p.beta_y for p in tws_track], "ro-", label = "ocelot")
plt.plot(s_b, betay_b, "bo-", label = "elegant")
plt.legend()
plt.grid(True)
plt.figure(4)
plt.title(r"$\beta_x - functions$")
plt.plot([p.s for p in tws_track], [p.beta_x for p in tws_track], "ro-", label = "ocelot")
plt.plot(s_b, betax_b, "bo-", label = "elegant")
plt.legend()
plt.grid(True)
plt.show()