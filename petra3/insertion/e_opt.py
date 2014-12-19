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


tw_end.beta_x = 3.00000000313
tw_end.alpha_x = -0.601367997622
tw_end.beta_y = 7.78559521531 
tw_end.alpha_y = 1.5144714708
tw_end.p = 1.e-2



tws_bdc=twiss(lat_bdc, tw_end)
show_optics(tws_bdc, lat_bdc, beam, scale = 0.0)

constr = {}
constr['global'] = {'beta_x':['<',70.], 'beta_y':['<',160.], 'Dx':['<',3.5]}
constr[drift_319] = {'tau':-47.e-4}
constr[drift_318] = {'beta_x':['<',50.], 'beta_y':['<',100.]}
constr[drift_320] = {'beta_x':['<',50.], 'beta_y':['<',100.]}
constr[drift_321] = {'beta_x':['<',50.], 'beta_y':['<',100.]}
constr[drift_322] = {'beta_x':['<',50.], 'beta_y':['<',100.]}
constr[drift_323] = {'beta_x':['<',50.], 'beta_y':['<',100.]}
constr[drift_324] = {'beta_x':['<',50.], 'beta_y':['<',100.], 'Dx':0.0, 'Dxp':0.0}
constr[drift_314] = {'beta_x':['<',50.], 'beta_y':['<',100.]}
constr[drift_315] = {'beta_x':['<',50.], 'beta_y':['<',100.]}
constr[drift_316] = {'beta_x':['<',50.], 'beta_y':['<',100.]}
constr[drift_317] = {'beta_x':['<',50.], 'beta_y':['<',100.]}



variables = [qms2, qk3nr, q2anr, qk1nr, qfa3_1, qda3_1, qda3_2]
match(lat_bdc, constr, variables, tw_end,max_iter=20)


tws_bdc=twiss(lat_bdc, tw_end)
print 'R56=', tws_bdc[-1].tau*1.e4, 'cm'
print 'Dxp=', tws_bdc[-1].Dxp
show_optics(tws_bdc, lat_bdc, beam, scale = 0.0)




i1 = []
i2 = []
i3 = []
s1 = []

ang = []

for t in tws_bdc:
    #print t.beta_x, t.Dx, t.Dxp, t.gamma_x
    i1.append(t.beta_x * t.Dxp**2)
    i2.append(2* t.alpha_x * t.Dx*t.Dxp)
    i3.append(t.gamma_x * t.Dx**2)
    s1.append(t.s)

for e in lat_bdc.sequence:    
    if e.__class__ in [SBend, Bend, RBend]:
        ang.append(e.angle)
    else:
        ang.append(0)
     
     
print len(s1), len(ang)


plt.figure()
plt.plot(s1, i1, 'r')
plt.plot(s1, i2, 'g')
plt.plot(s1, i3, 'b')
plt.plot(s1, np.array(i1)+ np.array(i2) + np.array(i3), 'b--', lw=3)

plt.plot(s1[0:-1], ang, color='#AAAAAA')

plt.show()
