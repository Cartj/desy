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


#plot_opt_func(lat, tws0)

tw0 = tws0[0]


tws_arc1=twiss(lat_arc1, tw0)
#plot_opt_func(lat_arc1, tws_arc1)

tw_end = deepcopy(tws_arc1[-1])
tws_arc2=twiss(lat_arc2, tw_end)
#plot_opt_func(lat_arc2, tws_arc2)

tw_end = tws_arc2[-1]

# match to values

tw_end.beta_x = 3.00000000391
tw_end.alpha_x = 0.601367998599
tw_end.beta_y = 7.78436581638
tw_end.alpha_y = -1.52660480872

tws_sase=twiss(lat_sase, tw_end)
plot_opt_func(lat_sase, tws_sase)
plt.show()

print 'end twiss'
print tws_sase[-1].beta_x, tws_sase[-1].alpha_x  
print tws_sase[-1].beta_y, tws_sase[-1].alpha_y
print tws_sase[-1].Dx, tws_sase[-1].Dxp


'''
solution 5m average
start twiss
3.00000000391 0.601367998599
7.78436581638 -1.52660480872
end twiss
3.00000000391 -0.601367998594
7.78559521144 1.51447147204
qfs 4.08213946419
qds -3.90994199551
'''

constr = {}
constr['global'] = {'beta_x':['<',170.], 'beta_y':['<',170.]}
#constr[sase_end] = {'beta_x':['->', sase_start], 'beta_y':['->', sase_start], 'Dx':0.44, 'Dxp':0.0}
#constr[qds] = {'alpha_x':0.0, 'alpha_y':0.0, 'beta_x':5.0}
constr[qds] = {'beta_x':3.0}
constr[qfs] = {'beta_y':3.0}
constr[m3s] = {'beta_y':['->', m1s], 'beta_x':['->', m1s]}
constr[m4s] = {'beta_y':['->', m2s], 'beta_x':['->', m2s]}
constr[m5s] = {'beta_y':['->', m3s], 'beta_x':['->', m3s]}
constr[m6s] = {'beta_y':['->', m4s], 'beta_x':['->', m4s]}

variables = [qfs, qds, [tw_end, 'beta_x'], [tw_end, 'beta_y'], [tw_end, 'alpha_x'], [tw_end, 'alpha_y']]
match(lat_sase, constr, variables, tw_end,max_iter=10000)

tws_sase=twiss(lat_sase, tw_end)
plot_opt_func(lat_sase, tws_sase)

print 'start twiss'
print tws_sase[0].beta_x, tws_sase[0].alpha_x  
print tws_sase[0].beta_y, tws_sase[0].alpha_y

print 'end twiss'
print tws_sase[-1].beta_x, tws_sase[-1].alpha_x  
print tws_sase[-1].beta_y, tws_sase[-1].alpha_y


for v in  variables:
    if v.__class__ == Quadrupole: print v.id, v.k1


lat_full = MagneticLattice((arc2, sase), energy = beam.E)

tws_full=twiss(lat_full, tws_arc1[-1])
plot_opt_func(lat_full, tws_full)
plt.show()
