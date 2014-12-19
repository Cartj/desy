from ocelot.cpbd.tracking import *
from ocelot.cpbd.chromaticity import *
from time import time
from ocelot.gui.accelerator import *
from ocelot.cpbd.e_beam_params import *
from ocelot.cpbd.match import *


beam = Beam()
beam.E = 6.0
beam.sigma_E = 0.001
beam.I = 0.1

#k, betaMin, betaMax, __ = fodo_parameters(betaXmean=18.0, L=2.2, verbose = True)
#print 'fodo parameters:', k, betaMin, betaMax,
#exit(0)

from petra import *

lat = MagneticLattice(lattice, energy = beam.E)

lat_arc1 = MagneticLattice((arc1), energy = beam.E) # start at end of first straigh section (W)
lat_arc2 = MagneticLattice((arc2), energy = beam.E)
lat_sase = MagneticLattice((sase), energy = beam.E)
#lat_sase_old = MagneticLattice((sase_old), energy = beam.E)
lat_arc3 = MagneticLattice((arc3), energy = beam.E)
#lat_nw = MagneticLattice((ins_nw), energy = beam.E)
#print lat_nw.totalLen

tw0 = Twiss(beam)
tws0=twiss(lat, tw0)

eb = EbeamParams(lat, beam, nsuperperiod=1)
eb.print_params()
eb.integrals_id()


plot_opt_func(lat, tws0)
plt.show()
sys.exit(0)

tw0 = tws0[0]


tws_arc1=twiss(lat_arc1, tw0)
#plot_opt_func(lat_arc1, tws_arc1)

tw_end = tws_arc1[-1]
tws_arc2=twiss(lat_arc2, tw_end)
plot_opt_func(lat_arc2, tws_arc2)

tw_end = tws_arc2[-1]
tws_sase=twiss(lat_sase, tw_end)
tws_sase_old=twiss(lat_sase_old, tw_end)
plot_opt_func(lat_sase, tws_sase)
plot_opt_func(lat_sase_old, tws_sase_old)

tw_end = tws_sase[-1]
tws_arc3=twiss(lat_arc3, tw_end)
plot_opt_func(lat_arc3, tws_arc3)

tw_end = tws_arc2[-1]
#constr = {sase_end:{'Dx':0.0}}
constr = {}
constr['global'] = {'beta_x':['<',40.], 'beta_y':['<',40.]}
#constr[sase_end] = {'beta_x':['->', sase_start], 'beta_y':['->', sase_start], 'Dx':0.44, 'Dxp':0.0}
constr[sase_end] = {'beta_x':tws_sase_old[-1].beta_x, 'beta_y':tws_sase_old[-1].beta_y, 
                    'alpha_x':tws_sase_old[-1].alpha_x, 'alpha_y':tws_sase_old[-1].alpha_y}

variables = [qms1, qms2, qfs, qds]
match(lat_sase, constr, variables, tw_end)

tws_sase=twiss(lat_sase, tw_end)
plot_opt_func(lat_sase, tws_sase)

tw_end = tws_sase_old[-1]
tws_arc3=twiss(lat_arc3, tw_end)
plot_opt_func(lat_arc3, tws_arc3)


plt.show()
