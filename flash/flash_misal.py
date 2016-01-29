__author__ = 'Sergey Tomin'
from desy.flash.lattices.lattice_rf_red import *
from ocelot.gui.accelerator import *
from ocelot import *
from ocelot.gui import *
from ocelot.cpbd.errors import *
from ocelot.cpbd.track import *
from ocelot.cpbd.orbit_correction import *
from copy import copy
import pyqtgraph as pg


beam = Beam()
beam.E = 0.005#148.3148e-3 #in GeV ?!
beam.beta_x = 14.8821
beam.beta_y = 18.8146
beam.alpha_x =  -0.61309
beam.alpha_y = -0.54569
beam.emit_xn = 1.5e-6
beam.emit_yn = 1.5e-6
beam.emit_x = beam.emit_xn / (beam.E / m_e_GeV)
beam.emit_y = beam.emit_yn / (beam.E / m_e_GeV)

tw0 = Twiss(beam)

#lat = MagneticLattice(lattice, start=STARTACC39)

lat = MagneticLattice(lattice)
constr = {STARTACC39:{'beta_x':14.8821, 'beta_y':18.8146, 'alpha_x': -0.61309, 'alpha_y':-0.54569}}
vars = [[tw0, 'beta_x'], [tw0, 'beta_y'], [tw0, 'alpha_x'], [tw0, 'alpha_y']]
match(lat, constr, vars, tw0, xtol=1e-8)

tws=twiss(lat, tw0)
plot_opt_func(lat, tws, top_plot=["E"])
print tws[0].beta_x, tws[0].beta_y, tws[0].alpha_x, tws[0].alpha_y,

X = []
Y = []
s = []
n = 1

for elem in lat.sequence:
    if elem.type in ["bend", "rbend", "sbend"]:
        elem.dx = tgauss(0, sigma=0.0001,trunc=3)
        elem.dy = tgauss(0, sigma=0.0001,trunc=3)
    elif elem.type == "quadrupole":
        elem.dx = tgauss(0, sigma=0.0001,trunc=3)
        elem.dy = tgauss(0, sigma=0.0001,trunc=3)
        elem.dtilt = tgauss(0, sigma=0.0001,trunc=3)
    elif elem.type == "cavity":
        elem.dx = tgauss(0, sigma=0.0001,trunc=3)
        elem.dy = tgauss(0, sigma=0.0001,trunc=3)
    if elem.id in ["V2DBC2","V4DBC2", "V6DBC2", "V10DBC2" ]:
        elem.type = "drift"
lat.update_transfer_maps()

p = Particle(p=0.0, E=beam.E)
plist = lattice_track(lat, p, order=1)
x = np.array([p.x for p in plist])
y = np.array([p.y for p in plist])
s = np.array([p.s for p in plist])
plt.plot(s, x, s, y)
plt.show()
pi = Particle(p=0.0, E=beam.E)
orb = Orbit(lat)
BPM2UBC2.weight = 1
BPM1DBC2.weight = 1
x_bpm, y_bpm = orb.read_virtual_orbit( p_init=Particle(x = 0.001, y = -0.0005, E=beam.E))
sigma_x = sqrt(sum(x_bpm**2/len(x_bpm)))*1000
sigma_y = sqrt(sum(y_bpm**2/len(x_bpm)))*1000
print "sigma_x = ", sqrt(sum(x_bpm**2/len(x_bpm))), "sigma_y = ", sqrt(sum(y_bpm**2/len(x_bpm)))
s_bpm = [p.s for p in orb.bpms]

ax = plot_API(lat)
#plt.figure(1)
ax.plot(s_bpm, x_bpm, "ro")
ax.plot(s, x, "r--", label=r"$\sigma_x=$"+"%.2f" % sigma_x+"mm")

#plt.figure(2)
ax.plot(s_bpm, y_bpm, "bo")
ax.plot(s, y, "b--", label=r"$\sigma_y=$"+"%.2f" % sigma_y+"mm")

#plt.show()

resp_mat = orb.linac_response_matrix(lat, tw_init=tw0)
#resp_mat = orb.measure_response_matrix(lat, p_init=Particle(E=beam.E))
#print resp_mat
#for cor in orb.hcors:
#    print cor.s,  cor.id, cor.phi_x/2./np.pi
#
#for cor in orb.vcors:
#    print cor.s,  cor.id, cor.phi_y/2./np.pi
#print resp_mat
#x_bpm_b = x_bpm
#y_bpm_b = y_bpm

#for i in range(1):
p0 = orb.correction(p_init=Particle(E=beam.E))

p0=Particle(E=beam.E)
x_bpm, y_bpm = orb.read_virtual_orbit(p_init=p0)
#plt.plot(s_bpm, x_bpm, "r")
#p0 = orb.correction(lat, p_init=Particle(E=beam.E))
#p0=Particle(E=beam.E)
#x_bpm, y_bpm = orb.read_virtual_orbit(lat, p_init=p0)
#plt.plot(s_bpm, x_bpm, "b")

#x_bpm = np.array([p.x for p in orb.bpms])
#y_bpm = np.array([p.y for p in orb.bpms])
#x_bpm = (x_bpm_b + x_bpm_i)
#y_bpm = (y_bpm_b + y_bpm_i)
#sigma_x = sqrt(sum(x_bpm**2/len(x_bpm)))*1000.
#sigma_y = sqrt(sum(y_bpm**2/len(y_bpm)))*1000.
#print "sigma_x=", sigma_x, "mm, sigma_y=", sigma_y," mm"
#orb.set_bpm_signal(x_bpm=x_bpm, y_bpm=y_bpm)
print "asdfsdaf"
#p = Particle(p=0.0, E=beam.E)
#x_bpm, y_bpm = orb.read_virtual_orbit(lat, p_init=copy(p0))
sigma_x = sqrt(sum(x_bpm**2/len(x_bpm)))*1000
sigma_y = sqrt(sum(y_bpm**2/len(y_bpm)))*1000
print "sigma_x = ", sqrt(sum(x_bpm**2/len(x_bpm))), "sigma_y = ", sqrt(sum(y_bpm**2/len(x_bpm)))
plist = lattice_track(lat, p0, order=1)
x = np.array([p.x for p in plist])
y = np.array([p.y for p in plist])
s = np.array([p.s for p in plist])

#plt.figure(1)

ax.plot(s, x, "r", label=r"$\sigma_x=$"+"%.2f" % sigma_x+"mm")
ax.plot(s_bpm, x_bpm, "ro")
#plt.figure(2)
ax.plot(s, y, "b", label=r"$\sigma_y=$"+"%.2f" % sigma_y+"mm")
ax.plot(s_bpm, y_bpm, "bo")
ax.set_xlabel("X/Y, m")
plt.xlim([0, lat.totalLen])

ax.legend( loc=1)
plt.show()
#plt.show()

p = Particle(p=0.01, E=beam.E)
plist = lattice_track(lat, p, order=2)
#print plist
xd = np.array([p.x for p in plist])
yd = np.array([p.y for p in plist])
sd = np.array([p.s for p in plist])

#plt.figure(1)

plt.plot(sd, xd - x, "r")
#ax.plot(s_bpm, x_bpm, "ro")
#plt.figure(2)
plt.plot(sd, yd -y, "b")
#ax.plot(s_bpm, y_bpm, "bo")
plt.xlabel("X/Y, m")
#plt.xlim([0, lat.totalLen])

plt.legend(["X", "Y"], loc=1)
plt.show()

exit(0)

if i == 0:
    X = x
    Y = y
else:
    X += x
    Y += y
plt.figure(1)
plt.plot(s, (X/n), "r")
plt.plot(s, (X/n), "r")
#plt.plot([p.s for p in plist], [p.y for p in plist], "b")
#p1 = Particle(E=beam.E)
#plist1 = lattice_track(lat, p1, order=2)
plt.figure(2)
#plt.plot([p.s for p in plist1], [p.x for p in plist1], "r")
plt.plot(s, (Y/n), "b")
plt.show()