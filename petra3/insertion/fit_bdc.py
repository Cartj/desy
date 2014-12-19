from ocelot.cpbd.tracking import *
from ocelot.cpbd.chromaticity import *
from time import time
from ocelot.gui.accelerator import *
from ocelot.cpbd.e_beam_params import *
from ocelot.cpbd.match import *
from common import show_optics


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
lat_bdc = MagneticLattice((bc1), energy = beam.E)
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


tw_end.beta_x = 3.00000000313
tw_end.alpha_x = -0.601367997622
tw_end.beta_y = 7.78559521531 
tw_end.alpha_y = 1.5144714708
tw_end.p = 1.e-2



tws_bdc=twiss(lat_bdc, tw_end)
show_optics(tws_bdc, lat_bdc, beam, scale = 0.0)

constr = {m2_bdc:{'tau': -45.e-4, 'Dx':0.0} }
constr['global'] = {'beta_x':['<',40], 'beta_y':['<',40]}



variables = [qf1_bdc, qf2_bdc, qf3_bdc, qf4_bdc, qd1_bdc, qd2_bdc, qd3_bdc, qd4_bdc]
match(lat_bdc, constr, variables, tw_end,max_iter=20000)


tws_bdc=twiss(lat_bdc, tw_end)
print 'R56=', tws_bdc[-1].tau*1.e4, 'cm'
print 'Dxp=', tws_bdc[-1].Dxp
show_optics(tws_bdc, lat_bdc, beam, scale = 0.0)

plt.plot(map(lambda x: x.Dxp, tws_bdc))

plt.show()


tw_end = deepcopy(tws_bdc[-1])

constr = {}
constr['global'] = {'beta_x':['<',80.], 'beta_y':['<',130.], 'Dx':['<', 3.0], 'Dxp':['<', 0.05]}
#constr[sase_end] = {'beta_x':['->', sase_start], 'beta_y':['->', sase_start], 'Dx':0.44, 'Dxp':0.0}
#constr[drift_398] = {'Dx':0.0, 'Dxp':0.0}
#constr[drift_345] = {'Dx':-1.0}
constr[drift_398] = {'Dx':0.0, 'Dxp':0.0}
#constr[qf] = {'beta_x':23.,  'beta_y':6.4}
#constr[qd] = {'beta_x':6.4, 'beta_y':23.}

constr[end_arc3] = {'beta_x': 5.7078928123, 'alpha_x':-0.426268101809, 'beta_y':24.0252733016, 'alpha_y':2.08007605731}

variables = [qfa3_2, qfa3_3, qda3_3, qfa3_4, qda3_4, qfa3, qda3, q7na3, q6na3, q9na3, qs_n2a3, qs_n1a3, q0ba3, q2ba3, q3a3, q1a3]
match(lat_arc3, constr, variables, tw_end,max_iter=5000)

for v in  variables:
    if v.__class__ == Quadrupole: print v.id, v.k1


tws_arc3=twiss(lat_arc3, tw_end)
show_optics(tws_arc3, lat_arc3, beam, scale = 0.0)

lat_full = MagneticLattice((arc1, arc2, sase, bdc_arc3, arc3_new, rest), energy = beam.E)
tws_full=twiss(lat_full, tws0[0])
plot_opt_func(lat_full, tws_full)

eb = EbeamParams(lat_full, beam, nsuperperiod=1)
eb.print_params()
eb.integrals_id()



plt.show()
