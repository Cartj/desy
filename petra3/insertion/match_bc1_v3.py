'''
MBA-type var delay achromat
'''


import sys
from ocelot.cpbd.match import *
from ocelot.gui.accelerator import *
from common import show_optics

from p3fel import *

b1 = RBend (l=1.0*m, angle=0.03)
b2 = RBend (l=1.0*m, angle=0.03)
b3 = RBend (l=1.0*m, angle=0.03)
b4 = RBend (l=1.0*m, angle=0.03)
b5 = RBend (l=1.0*m, angle=0.03)
b6 = RBend (l=1.0*m, angle=-0.03) # change sign
b7 = RBend (l=1.0*m, angle=-0.03) # change sign
b8 = RBend (l=1.0*m, angle=0.03)
b9 = RBend (l=1.0*m, angle=0.03)
b10 = RBend (l=1.0*m, angle=0.03)
b11 = RBend (l=1.0*m, angle=0.03)
b12 = RBend (l=1.0*m, angle=0.03)

q1 = Quadrupole(l=0.1, k1 = -1.0)
q2 = Quadrupole(l=0.1, k1 = 1.0)
q3 = Quadrupole(l=0.1, k1 = -1.0)
q4 = Quadrupole(l=0.1, k1 = 1.0)
q5 = Quadrupole(l=0.1, k1 = -1.0)
q6 = Quadrupole(l=0.1, k1 = 1.0)
q7 = Quadrupole(l=0.1, k1 = -1.0)
q8 = Quadrupole(l=0.1, k1 = 1.0)
q9 = Quadrupole(l=0.1, k1 = -1.0)
q10 = Quadrupole(l=0.1, k1 = 1.0)
q11 = Quadrupole(l=0.1, k1 = -1.0)
q12 = Quadrupole(l=0.1, k1 = 1.0)


d1 = Drift(l=2.95*m)
d2 = Drift(l=2.5*m)
d3 = Drift(l=1.5*m)

m1 = Monitor()
m2 = Monitor()
m0 = Monitor()

 
bc1 = (m1, (b1, d1, q1, d1, b2, d1, q2, d1), 
       (b3, d1, q3, d1, b4, d1, q4, d1), 
       (b5, d1, q5, d1, b6, d1, m0, q6, d1),
       (b7, d1, q7, d1, b8, d1, q8, d1),
       (b9, d1, q9, d1, b10, d1, q10, d1),
       (b11, d1, q11, d1, b12, d1, q12, d1),
        m2)

lat = MagneticLattice(bc1, energy=6.0)


tw0 = Twiss(beam)
tw0.beta_x = 0.0
tw0.p = 1.e-2

tot_angle = 0.0
for e in lat.sequence:
    if e.__class__ == Quadrupole:
        print 'quadrupole', e.id, e.k1
    if e.__class__ in (Bend, SBend, RBend):
        print 'bend', e.id, e.angle
        tot_angle += e.angle


print 'total deflection: ', tot_angle

'''
tws=twiss(lat, tw0, nPoints = 100) # periodic solution for initial guess
tw0 = tws[0]
tw0.Dx = 0.0
tw0.Dxp = 0.0
tw0.p = 1.e-2
'''

tw0.beta_x = 22.0
tw0.alpha_x = -0.8
tw0.beta_y = 7.0
tw0.alpha_y = 1.8

tw0.Dx = 0.0
tw0.Dxp = 0.0
tw0.p = 1.e-2



tws=twiss(lat, tw0, nPoints = 100)
print 'R56=', tws[-1].tau

show_optics(tws, lat, beam, scale = 0.0)
plt.show()


#constr = {m2:{'Dx':0.0, 'Dxp':0.0, 'beta_x': 15.0, 'beta_y': 30.0, 'tau': 24.e-4}, m1:{'Dx':0.0, 'Dxp':0.0, 'beta_x': 15.0, 'beta_y': 30.0} }
constr = {m2:{'Dx':0.0, 'Dxp':0.0, 'tau': -10.e-4} }
#constr[q4] = {'beta_y':['<',100], 'beta_y':['<',100], 'beta_y':['->', q2], 'beta_x':['->', q2]}

constr['global'] = {'beta_x':['<',120], 'beta_y':['<',120]}


var = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11]
res = match(lat, constr, var, tw0, max_iter=5000)

tws=twiss(lat, tw0, nPoints = 100)
print 'diff:', tws[-1].tau * 1.e4, tws[-1].Dx, tws[-1].Dxp

show_optics(tws, lat, beam, scale = 0.0)
plt.show()


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

