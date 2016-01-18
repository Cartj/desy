__author__ = 'Sergey Tomin'
from lattice_rf_mod import *
from ocelot.gui.accelerator import *
from ocelot import *
from ocelot.gui import *
from ocelot.cpbd.errors import *
from ocelot.cpbd.track import *
from ocelot.cpbd.orbit_correction import *
from copy import copy
import pyqtgraph as pg
lat = MagneticLattice(lattice)
for elem in lat.sequence:
    if elem.type == "quadrupole":
        name = elem.id.replace("_D", "")
        name = elem.id.replace("_U", "")
        print "k1"+name, " = ", elem.k1



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

lat = MagneticLattice(lattice, start=STARTACC39)
tws=twiss(lat, tw0)
plot_opt_func(lat, tws, top_plot=["Dx"])

#for elem in lat.sequence:
#    if elem.type == "vcor" and elem.id not in ["V1DBC3", "V3DBC3", "V9ACC5", "V10ACC5", "V10ACC4", "V10ACC7"]:
#        elem.type = "drift"


pi = Particle(p=0.0, E=beam.E)
orb = Orbit(lat)

x_bpm, y_bpm = orb.read_virtual_orbit(lat, p_init=pi)
resp_mat = orb.linac_response_matrix(lat, tw_init=tw0)
ax = plot_API(lat)
for x in linspace(-0.001, 0.001, num=11):
    for cor in orb.hcors:
        #print cor.angle
        cor.angle = 0.
    #print x
    BPM3DBC3.x = 0.000
    BPM9ACC4.x = x
    BPM9ACC5.x = x
    BPM9ACC6.x = x
    BPM11ACC7.x = 0.0000
    BPM3DBC3.weight = 0
    BPM9ACC5.weight = 1
    BPM9ACC4.weight = 1.
    BPM9ACC6.weight = 1
    orb.correction(lat)
    p = Particle(p=0.0, E=beam.E)
    x_bpm, y_bpm = orb.read_virtual_orbit(lat, p_init=copy(p))
    #print y_bpm
    #sigma_x = sqrt(sum(x_bpm**2/len(x_bpm)))*1000
    #sigma_y = sqrt(sum(y_bpm**2/len(x_bpm)))*1000
    #print "sigma_x = ", sqrt(sum(x_bpm**2/len(x_bpm))), "sigma_y = ", sqrt(sum(y_bpm**2/len(x_bpm)))
    plist = lattice_track(lat, p, order=1)
    x = np.array([p.x for p in plist])
    y = np.array([p.y for p in plist])
    s = np.array([p.s for p in plist])

    #plt.figure(1)

    ax.plot(s, x, "r")
    #ax.plot(s_bpm, x_bpm, "ro")
    #plt.figure(2)
    #ax.plot(s, y, "b")
    #ax.plot(s_bpm, y_bpm, "bo")
    ax.set_xlabel("X/Y, m")
    plt.xlim([0, lat.totalLen])

    #ax.legend( loc=1)
plt.show()