__author__ = 'Igor Zagorodnov'

from ocelot import *
from ocelot.gui import *
from ocelot.adaptors import *
from ocelot.cpbd.sc import *

beam = Beam()
beam.E = 17.5 #in GeV
beam.beta_x = 22.5995
beam.beta_y = 22.5995
beam.alpha_x =  -1.4285
beam.alpha_y = 1.4285
beam.emit_xn = 1e-6
beam.emit_yn = 1e-6
beam.emit_x = beam.emit_xn / (beam.E / m_e_GeV)
beam.emit_y = beam.emit_yn / (beam.E / m_e_GeV)

tw0 = Twiss(beam)
from lattice0 import *
lat = MagneticLattice(lattice)

tws=twiss(lat, tw0, nPoints=None)
plot_opt_func(lat, tws, top_plot=["E"])

p_array, charge_array, z0 = astraBeam2particleArray(filename='XFEL0.ast')

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
    track(lat=lat, particle_list=p_array, dz=dz, navi=navi, order=order)
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
#np.savetxt('D:/pyoptics.txt',out)
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


plt.figure(3)
plt.title(r"$\beta_y - functions$")
plt.plot([p.s for p in tws_track], [p.beta_y for p in tws_track], "ro-", label = "beta_y ocelot")
plt.hold(True)
plt.plot([p.s for p in tws], [p.beta_y for p in tws], "bo-", label = "design")
plt.legend()
plt.grid(True)
plt.figure(4)
plt.title(r"$\beta_x - functions$")
plt.plot([p.s for p in tws_track], [p.beta_x for p in tws_track], "ro-", label = "beta_x ocelot")
plt.hold(True)
plt.plot([p.s for p in tws], [p.beta_x for p in tws], "bo-", label = "design")
plt.legend()
plt.grid(True)
plt.show()