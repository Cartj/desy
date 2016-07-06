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
lat_arc3 = MagneticLattice((arc3), energy = beam.E)
#lat_nw = MagneticLattice((ins_nw), energy = beam.E)
#print lat_nw.totalLen

tw0 = Twiss(beam)
tws0=twiss(lat, tw0)

#eb = EbeamParams(lat, beam, nsuperperiod=1)
#eb.print_params()
#eb.integrals_id()


#plot_opt_func(lat, tws0)

tw0 = tws0[0]


tws_arc1=twiss(lat_arc1, tw0)
#plot_opt_func(lat_arc1, tws_arc1)

tw_end = tws_arc1[-1]
tws_arc2=twiss(lat_arc2, tw_end)
plot_opt_func(lat_arc2, tws_arc2)



betx = 3.00000000391 
alfx = 0.601367998599
bety = 7.78436581638
alfy = -1.52660480872



constr = {}
constr['global'] = {'beta_x':['<',150.], 'beta_y':['<',150.]}

#constr[arc2_end] = {'beta_x':5.0, 'beta_y':9.75284, 'alpha_x':-0.63097627533, 'alpha_y':1.20340638868, 'Dx':0.0, 'Dxp':0.0}
constr[arc2_end] = {'beta_x':betx, 'beta_y':bety, 'alpha_x':alfx, 'alpha_y':alfy, 'Dx':0.0, 'Dxp':0.0}

variables = [qfa2, qda2, q1a2, q2a2, q3a2, q4a2, q5a2, q6a2]
match(lat_arc2, constr, variables, tw_end,max_iter=50)

tw_end.p = 1.e-2
tws_arc2=twiss(lat_arc2, tw_end)
plot_opt_func(lat_arc2, tws_arc2)

print 'R56=', tws_arc2[-1].tau*1.e4, 'cm'
print tws_arc2[-1].beta_x, tws_arc2[-1].alpha_x  
print tws_arc2[-1].beta_y, tws_arc2[-1].alpha_y
print tws_arc2[-1].Dx, tws_arc2[-1].Dxp

for v in  variables:
    print v.id, v.k1


plt.show()
