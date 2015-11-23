import ocelot.adaptors.astra2ocelot

__author__ = 'Sergey Tomin'


from ocelot import *
from ocelot.gui import *
from ocelot.adaptors import *

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
plot_opt_func(lat, tws, top_plot=["E"])

for elem in lat.sequence:
    if elem.id == "C1_ACC39":
        elem.v = elem.v*10

lat.update_transfer_maps()

tws=twiss(lat, tw0, nPoints=1000)
plot_opt_func(lat, tws, top_plot="E")

p_array, charge_array = astraBeam2particleArray(filename='elegant_files/flash_out_200000.ast')

#p_array.particles[4::6] = sc.smooth_z(p_array.particles[4::6], mslice=10000)

# plot current
bins_start, hist_start = get_current(p_array, charge=charge_array[0], num_bins=200)


dz = 1.
order = 2
SC = False
debug = False

Z = np.linspace(0, lat.totalLen, num=int(lat.totalLen/dz))

twsi=twiss(lat, tw0, nPoints=len(Z) )
tw0 = get_envelope(p_array, tws_i = twsi[0])
tws_track = [tw0]
"""
if debug:
    f=plt.figure()
    plt.ion()
    plt.hold(False)

navi = Navigator(lattice=lat)
for i, zi in enumerate(Z[1:]):
    print zi
    dz = zi - Z[i]
    track(lat=lat, particle_list=p_array, dz=dz, navi=navi, order=order)
    #p_array.particles[4::6] = sc.smooth_z(p_array.particles[4::6], mslice=10000)
    if SC:
        sc_apply(p_array, q_array=charge_array, zstep=dz, nmesh_xyz=[63, 63, 63], low_order_kick=True)
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
"""
L = 0.
for elem in lat.sequence:
    #print elem.id, elem.id == "W1"

    if elem.id == "W1":
        p_array_t, charge_array_t = astraBeam2particleArray(filename='elegant_files/PD/FLASH_S2E_001_w1.ast')
        bins_t, hist_2 = get_current(p_array_t, charge=charge_array_t[0], num_bins=200)
        bins, hist = get_current(p_array, charge=charge_array[0], num_bins=200)
        print "W1: ", L
        plt.figure(20)
        plt.title("W1")
        #plt.plot(p_array.tau(), p_array.p(), "r.", label="ocelot")
        #plt.plot(p_array_t.tau(), p_array_t.p(), "b.", label="elegant")
        plt.plot(bins, hist, label="ocelot")
        plt.plot(bins_t, hist_2, label="elegant")
        plt.legend()
        plt.xlabel("s, m")
        plt.ylabel("I, A")
        #plt.xlabel(r"$dl, m$")
        #plt.ylabel(r"$dp/p$")
        plt.grid(True)
    if elem.id == 'WATCHBC2':
        p_array_t, charge_array_t = astraBeam2particleArray(filename='elegant_files/PD/FLASH_S2E_001_bc2.ast')
        bins_t, hist_2 = get_current(p_array_t, charge=charge_array_t[0], num_bins=200)
        bins, hist = get_current(p_array, charge=charge_array[0], num_bins=200)
        print "WATCHBC2: ", L
        plt.figure(21)
        plt.title("WATCHBC2")
        #plt.plot(p_array.tau(), p_array.p(), "r.", label="ocelot")
        #plt.plot(p_array_t.tau(), p_array_t.p(), "b.", label="elegant")
        plt.plot(bins, hist, label="ocelot")
        plt.plot(bins_t, hist_2, label="elegant")
        plt.xlabel("s, m")
        plt.ylabel("I, A")
        #plt.xlabel(r"$dl, m$")
        #plt.ylabel(r"$dp/p$")
        plt.legend()
        plt.grid(True)
        #plt.show()
    if elem.id == 'WATCHBC2_2':
        p_array_t, charge_array_t = astraBeam2particleArray(filename='elegant_files/PD/FLASH_S2E_002_bc2.ast')
        bins_t, hist_2 = get_current(p_array_t, charge=charge_array_t[0], num_bins=200)
        bins, hist = get_current(p_array, charge=charge_array[0], num_bins=200)
        print "WATCHBC2_2: ", L
        plt.figure(23)
        plt.title("WATCHBC2_2")
        #plt.plot(p_array.tau(), p_array.p(), "r.", label="ocelot")
        #plt.plot(p_array_t.tau(), p_array_t.p(), "b.", label="elegant")
        plt.plot(bins, hist, label="ocelot")
        plt.plot(bins_t, hist_2, label="elegant")
        plt.xlabel("s, m")
        plt.ylabel("I, A")
        #plt.xlabel(r"$dl, m$")
        #plt.ylabel(r"$dp/p$")
        plt.legend()
        plt.grid(True)
        #plt.show()
    if elem.id == 'WATCHBC3':
        p_array_t, charge_array_t = astraBeam2particleArray(filename='elegant_files/PD/FLASH_S2E_001_bc3.ast')
        bins_t, hist_2 = get_current(p_array_t, charge=charge_array_t[0], num_bins=200)
        bins, hist = get_current(p_array, charge=charge_array[0], num_bins=200)
        print "WATCHBC3: ", L
        plt.figure(31)
        plt.title("WATCHBC3")
        #plt.plot(p_array.tau(), p_array.p(), "r.", label="ocelot")
        #plt.plot(p_array_t.tau(), p_array_t.p(), "b.", label="elegant")
        plt.plot(bins, hist, label="ocelot")
        plt.plot(bins_t, hist_2, label="elegant")
        plt.xlabel("s, m")
        plt.ylabel("I, A")
        #plt.xlabel(r"$dl, m$")
        #plt.ylabel(r"$dp/p$")
        plt.legend()
        plt.grid(True)
        #plt.show()
    if elem.id == 'WATCHBC3_2':
        p_array_t, charge_array_t = astraBeam2particleArray(filename='elegant_files/PD/FLASH_S2E_002_bc3.ast')
        bins_t, hist_2 = get_current(p_array_t, charge=charge_array_t[0], num_bins=200)
        bins, hist = get_current(p_array, charge=charge_array[0], num_bins=200)
        print "WATCHBC3_2: ", L
        plt.figure(32)
        plt.title("WATCHBC3_2")
        #plt.plot(p_array.tau(), p_array.p(), "r.", label="ocelot")
        #plt.plot(p_array_t.tau(), p_array_t.p(), "b.", label="elegant")
        plt.plot(bins, hist, label="ocelot")
        plt.plot(bins_t, hist_2, label="elegant")
        plt.xlabel("s, m")
        plt.ylabel("I, A")
        #plt.xlabel(r"$dl, m$")
        #plt.ylabel(r"$dp/p$")
        plt.legend()
        plt.grid(True)
    if elem.id == 'W1_end':
        p_array_t, charge_array_t = astraBeam2particleArray(filename='elegant_files/PD/FLASH_S2E_002_w1.ast')
        bins_t, hist_2 = get_current(p_array_t, charge=charge_array_t[0], num_bins=200)
        bins, hist = get_current(p_array, charge=charge_array[0], num_bins=200)
        print "W1_end: ", L
        plt.figure(42)
        plt.title("W1_end")
        #plt.plot(p_array.tau(), p_array.p(), "r.", label="ocelot")
        #plt.plot(p_array_t.tau(), p_array_t.p(), "b.", label="elegant")
        plt.plot(bins, hist, label="ocelot")
        plt.plot(bins_t, hist_2, label="elegant")
        plt.xlabel("s, m")
        plt.ylabel("I, A")
        #plt.xlabel(r"$dl, m$")
        #plt.ylabel(r"$dp/p$")
        plt.legend()
        plt.grid(True)
        # plt.show()
    tw0 = elem.transfer_map*tw0
    elem.transfer_map.apply(p_array, order=2)
    tw = get_envelope(p_array, tws_i=tw0)
    L += elem.l
    tw.s += L
    print tw.s
    tws_track.append(tw)

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
#s = [p.s for p in tws_track]
#bx = [p.beta_x for p in tws_track]
#by = [p.beta_y for p in tws_track]
#out = zeros((len(s),3))
#out[:,0] = s
#out[:,1] = bx
#out[:,2] = by
#np.savetxt("beta_sc.txt", out)