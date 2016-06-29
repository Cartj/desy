from common import show_optics
from ocelot.cpbd.tracking import *

from ocelot.cpbd.e_beam_params import *
from ocelot.cpbd.match import *
from ocelot.gui.accelerator import *

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
lat_bdc = MagneticLattice((bdc_arc3), energy = beam.E)
lat_arc3 = MagneticLattice((arc3_new), energy = beam.E)
#lat_nw = MagneticLattice((ins_nw), energy = beam.E)
#print lat_nw.totalLen

tw0 = Twiss(beam)
tws0=twiss(lat, tw0)

#eb = EbeamParams(lat, beam, nsuperperiod=1)
#eb.print_params()
#eb.integrals_id()


#plot_opt_func(lat, tws0)

tw0 = deepcopy(tws0[0])
tw_end = tw0


tw_end.Dx = 0.0
tw_end.Dxp = 0.0
tw_end.beta_x = 3.00000000313
tw_end.alpha_x = -0.601367997622
tw_end.beta_y = 7.78559521531 
tw_end.alpha_y = 1.5144714708
tw_end.p = 1.e-2

constr = {}
constr['global'] = {'beta_x':['<',25.], 'beta_y':['<',25.], 'Dx':['<', 1.0], 'Dxp':['<', 0.05]}
constr[drift_398] = {'Dx':0.0, 'Dxp':0.0}

constr[end_arc3] = {'beta_x': 5.7078928123, 'alpha_x':-0.426268101809, 'beta_y':24.0252733016, 'alpha_y':2.08007605731}

variables = [qfa3, qda3, q7na3, q6na3, q9na3, 
            qs_n2a3, qs_n1a3, q0ba3, q2ba3, q3a3, q1a3, 
            [tw_end, 'beta_x'], [tw_end, 'beta_y'], [tw_end, 'alpha_x'], [tw_end, 'alpha_y']]

match(lat_arc3, constr, variables, tw_end,max_iter=5000)

for v in  variables:
    if v.__class__ == Quadrupole: print v.id, v.k1


tws_arc3=twiss(lat_arc3, tw_end)
show_optics(tws_arc3, lat_arc3, beam, scale = 0.0)

plt.show()
