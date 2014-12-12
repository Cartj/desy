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
lat_arc3 = MagneticLattice((arc3), energy = beam.E)
#lat_nw = MagneticLattice((ins_nw), energy = beam.E)
#print lat_nw.totalLen

tw0 = Twiss(beam)
tws0=twiss(lat, tw0)

#eb = EbeamParams(lat, beam, nsuperperiod=1)
#eb.print_params()
#eb.integrals_id()


plot_opt_func(lat, tws0)

tw0 = deepcopy(tws0[0])
tw_end = tw0

tw_end.beta_x = 6.41765286468
tw_end.alpha_x = -0.741360424519
tw_end.beta_y = 11.0128045182 
tw_end.alpha_y = 1.19914414542



tws_arc3=twiss(lat_arc3, tw_end)
plot_opt_func(lat_arc3, tws_arc3)

plt.show()

constr = {}
constr['global'] = {'beta_x':['<',370.], 'beta_y':['<',370.]}
#constr[sase_end] = {'beta_x':['->', sase_start], 'beta_y':['->', sase_start], 'Dx':0.44, 'Dxp':0.0}
constr[drift_398] = {'Dx':0.0, 'Dxp':0.0}
constr[qf] = {'beta_x':23.,  'beta_y':6.4}
constr[qd] = {'beta_x':6.4, 'beta_y':23.}

variables = [qk1nr, q2anr, qk3nr, qms2, qfa3, qda3]
match(lat_arc3, constr, variables, tw_end,max_iter=10000)

tws_sase=twiss(lat_arc3, tw_end)
plot_opt_func(lat_arc3, tws_arc3)


lat_full = MagneticLattice((arc1, arc2, sase, arc3), energy = beam.E)
tws_full=twiss(lat_full, tws0[0])
plot_opt_func(lat_full, tws_full)



lat_full = MagneticLattice((arc1, arc2, sase, arc3, rest), energy = beam.E)
tws_full=twiss(lat_full, tws0[0])
plot_opt_func(lat_full, tws_full)

eb = EbeamParams(lat_full, beam, nsuperperiod=1)
eb.print_params()
eb.integrals_id()


plt.show()
