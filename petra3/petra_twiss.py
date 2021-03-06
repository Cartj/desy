from ocelot.cpbd.e_beam_params import *
from ocelot.cpbd.track import *
from ocelot.gui.accelerator import *

beam = Beam()
beam.E = 6
beam.sigma_E = 0.001
beam.I = 0.1

def RFcavity(l, volt, lag, harmon, id):
    rf = Cavity(l = l, eid= id)
    rf.volt = volt
    rf.lag = lag
    rf.harmon = harmon
    return rf

exec( open("petra_after_ext.inp"))


lat = MagneticLattice(lattice)

tw0 = Twiss(beam)
tws=twiss(lat, tw0)


tw0 = tws[0]
#tw0.beta_x *= 2.1

tws=twiss(lat, tw0)

print "Qx = ", tws[-1].mux/2/pi, "  Qy = ", tws[-1].muy/2/pi

#compensate_chromatism(lat, tws[0], ksi_x_comp = 0, ksi_y_comp = 0,  nsuperperiod = 1)

eb = EbeamParams(lat, beam, nsuperperiod=1)
eb.print_params()
eb.integrals_id()

plot_opt_func(lat, tws)
plt.show()
