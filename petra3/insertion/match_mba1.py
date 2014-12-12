'''
MBA-type var delay achromat -- PetraIII
with geometry preservation
'''

from ocelot.cpbd.tracking import *
from ocelot.cpbd.chromaticity import *
from time import time
from ocelot.gui.accelerator import *
from ocelot.cpbd.match import *
from common import show_optics

beam = Beam()
beam.E = 6
beam.sigma_E = 0.001
beam.I = 0.1

def RFcavity(l, volt, lag, harmon, id):
    rf = Cavity(l = l, id = id)
    rf.volt = volt
    rf.lag = lag
    rf.harmon = harmon
    return rf

exec( open("petra_after_ext.inp"))


lat = MagneticLattice(lattice, energy = beam.E)
#lat2 = MagneticLattice((arc1, mba1, und, mba2, arc2), energy = beam.E)
lat2 = MagneticLattice((arc1), energy = beam.E)
lat3 = MagneticLattice((arc1, mba1, und, mba2), energy = beam.E)
lat_ins = MagneticLattice((mba1, und, mba2), energy = beam.E)
lat_mba1 = MagneticLattice(mba1, energy = beam.E)
lat_mba2 = MagneticLattice(mba2, energy = beam.E)
lat_mba1_new = MagneticLattice(mba1_new, energy = beam.E)

tw0 = Twiss(beam)
tws0=twiss(lat, tw0)


tw0 = tws0[0]
#tw0.beta_x *= 2.1

tws2=twiss(lat2, tw0)
tws3=twiss(lat3, tw0)

tw0 = tws2[-1]
tw_end = tws3[-1]

tws=twiss(lat_ins, tw0)

'''
plot_opt_func(lat_ins, tws)
plot_opt_func(lat3, tws3)
plt.show()
'''
for k in tws[0].__dict__.keys():
    print k, tws[0].__dict__[k] 

for e in lat_mba1.sequence:
    if e.__class__ == Quadrupole:
        print e.id, e.k1

#sys.exit(0)

tw0 = tws[0]
tw0.p = 1.e-2
tws=twiss(lat_mba2, tw0)
plot_opt_func(lat_mba2, tws)
plot_opt_func(lat2, tws2)
plot_opt_func(lat3, tws3)
#show_optics(tws, lat_mba1, beam)

plt.figure()
plt.plot(map(lambda p: p.s, tws3), map(lambda p: p.beta_x, tws3), 'r-', lw=2.0)
plt.plot(map(lambda p: p.s, tws3), map(lambda p: p.beta_y, tws3), 'b-', lw=2.0)
plt.plot(map(lambda p: p.s, tws3), map(lambda p: p.alpha_x, tws3), 'r--', lw=2.0)
plt.plot(map(lambda p: p.s, tws3), map(lambda p: p.alpha_y, tws3), 'g--', lw=2.0)


plt.show()

sys.exit(0)


tws=twiss(lat_mba1_new, tw0)
plot_opt_func(lat_mba1_new, tws)


print 'R56=', tws[-1].tau * 1.e4, ' cm'

'''
constr = {drift_117:{'Dx':0.0, 'Dxp':0.0, 'tau': 24.e-4} }
#constr = {drift_117:{'Dx':0.0, 'Dxp':0.0} }
constr['global'] = {'beta_x':['<',100], 'beta_y':['<',100]}

var = [qd,qf,q3,q2b,q1,q0b,q9n,q7n,q6n]
res = match(lat_mba1, constr, var, tw0, max_iter=5000)

tws=twiss(lat_mba1, tw0)
print 'R56=', tws[-1].tau * 1.e4, ' cm'
show_optics(tws, lat_mba1, beam)
'''
plt.show()
sys.exit(0)

