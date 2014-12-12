'''
MBA-type var delay achromat
6 magnet
'''


import sys
sys.path.append('../utils/')
from xfel_utils import *
from ocelot.gui.accelerator import *
from ocelot.cpbd.match import *

from p3fel import *

ang_total = 0.12 # rad, ~ 6 degree

bc_b1 = RBend (l=6.0*m, angle=ang_total/2.0, id = "b1")
bc_b2 = RBend (l=6.0*m, angle=ang_total/2.0, id = "b2")

bc_q1 = Quadrupole(l=0.1, k1 = 1.0, id="q1")
bc_q2 = Quadrupole(l=0.1, k1 = -1.0, id="q2")
bc_q3 = Quadrupole(l=0.1, k1 = 1.0, id="q3")
bc_q4 = Quadrupole(l=0.1, k1 = -1.0, id="q4")
bc_q5 = Quadrupole(l=0.1, k1 = 1.0, id="q5")
bc_q6 = Quadrupole(l=0.1, k1 = -1.0, id="q6")


bc_d1 = Drift(l=1.0*m)
bc_d2 = Drift(l=2.5*m)
bc_d3 = Drift(l=1.5*m)

m1 = Monitor(id="start")
m2 = Monitor(id="end")
m0 = Monitor(id="m0")

 
bc1 = (m1, (bc_b1, bc_d1, bc_q1, bc_d1, bc_b2, bc_d1, bc_q2, bc_d1), 
       (bc_b1, bc_d1, bc_q3, bc_d1, bc_b2, bc_d1, bc_q4, bc_d1), 
       (bc_b1, bc_d1, bc_q5, bc_d1, bc_b2, bc_d1, m0, bc_q6, bc_d1), m2)

lat = MagneticLattice(bc1, energy=6.0)


tw0 = Twiss(beam)
tw0.beta_x = 0.0
tw0.p = 1.e-2


print 'total deflection: ', bc_b1.angle + bc_b2.angle

tws=twiss(lat, tw0, nPoints = 100)

print 'R56=', tws[-1].tau
print tws[0].beta_x, tws[0].beta_y,tws[0].alpha_x, tws[0].alpha_y  
tw0 = tws[0]
tw0.Dx = 0.0
tw0.Dxp = 0.0
tw0.p = 1.e-2

#constr = {m2:{'Dx':0.0, 'Dxp':0.0, 'beta_x': 15.0, 'beta_y': 30.0, 'tau': 24.e-4}, m1:{'Dx':0.0, 'Dxp':0.0, 'beta_x': 15.0, 'beta_y': 30.0} }
constr = {m2:{'Dx':0.0, 'Dxp':0.0, 'tau': 24.e-4, 'beta_x':['->',m1], 'beta_y':['->',m1]}, 
          m1:{'Dx':0.0, 'Dxp':0.0} }
constr[bc_q4] = {'beta_y':['<',100], 'beta_y':['<',100], 'beta_y':['->', bc_q2], 'beta_x':['->', bc_q2]}
#constr['q4'] = {'beta_x':['<',100]}
#constr['q5'] = {'beta_x':['<',100]}

constr['global'] = {'beta_x':['<',60]}
constr['global'] = {'beta_y':['<',60]}


var = [bc_q1, bc_q2,bc_q3, bc_q4,bc_q5, bc_q6]
res = match(lat, constr, var, tw0, max_iter=5000)

print bc_q1.k1,bc_q2.k1,bc_q3.k1,bc_q4.k1,bc_q5.k1,bc_q6.k1
tws=twiss(lat, tw0, nPoints = 100)
print 'diff:', tws[-1].tau * 1.e4, tws[-1].Dx, tws[-1].Dxp

'''
# knob calculation
quad_tab = {}

for v in var:
    quad_tab[v] = []

taus = np.linspace(-5.e-4, 60.e-4, 50)
errs = []

for tau in taus:
    constr[m2] = {'Dx':0.0, 'Dxp':0.0, 'tau': tau, 'beta_x':['->',m1], 'beta_y':['->',m1]}
    res = match(lat, constr, var, tw0, max_iter=5000)
    tws=twiss(lat, tw0, nPoints = 100)
    err = np.abs(tws[-1].Dx) + np.abs( tws[-1].Dxp)
    errs.append(err)
    for v in var:
        print v.k1
        quad_tab[v].append(v.k1)
                    
fig = plt.figure()
ax  = fig.add_subplot(111)
labs = []
pls = []
for v in var:
    p, = ax.plot(taus * 1.e4, quad_tab[v])
    pls.append(p)
    labs.append(v.id)
plt.legend(pls, labs)
    
ax2 = ax.twinx()
ax2.plot(taus, errs, 'r--', lw=3)
'''


tws=twiss(lat, tw0, nPoints = 100)

from common import show_optics

show_optics(tws, lat, beam)