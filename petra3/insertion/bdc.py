'''
MBA-type var delay achromat
'''

from common import show_optics

from ocelot.cpbd.e_beam_params import *
from ocelot.cpbd.match import *
from ocelot.gui.accelerator import *

beam = Beam()
beam.E = 6.0
beam.sigma_E = 0.001
beam.I = 0.1


m = 1.0

b1_bdc = RBend (l=1.0, angle=0.1)
b2_bdc = RBend (l=2.0, angle=-0.27)
b3_bdc = RBend (l=2.0, angle=0.29)

#print 'max field [T]', beam.E * b3_bdc.angle / (b3_bdc.l * 0.2998)


qf1_bdc = Quadrupole(l=0.1, k1 = 0.9)
qd1_bdc = Quadrupole(l=0.1, k1 = -1.3)
qd3_bdc = Quadrupole(l=0.1, k1 = -1.3)
qd4_bdc = Quadrupole(l=0.1, k1 = -1.3)
qd2_bdc = Quadrupole(l=0.1, k1 = -1.3)
qf2_bdc = Quadrupole(l=0.1, k1 = 1.4)
qf3_bdc = Quadrupole(l=0.1, k1 = 2.0)
qf4_bdc = Quadrupole(l=0.1, k1 = 1.4)

d1_bdc = Drift(l=3*m)
d1h_bdc =Drift(l=1.45*m)
d2_bdc = Drift(l=2.5*m)
d3_bdc = Drift(l=2.0*m)

m1_bdc = Monitor()
m2_bdc = Monitor()

 
bc1 = (m1_bdc, b1_bdc, d1h_bdc, qd1_bdc, d1h_bdc, b2_bdc, qf1_bdc, d1h_bdc, qd2_bdc, d1h_bdc, b3_bdc, qf2_bdc, Drift(l=2.45), qd3_bdc, Drift(l=2.45),
       qf3_bdc, b2_bdc,  d1h_bdc, qd4_bdc, d1h_bdc, b3_bdc, qf4_bdc, Drift(l=1.0), m2_bdc)

lat = MagneticLattice(bc1, energy=6.0)


tw0 = Twiss(beam)
tw0.beta_x = 3.00000000313
tw0.alpha_x = -0.601367997622
tw0.beta_y = 7.78559521531 
tw0.alpha_y = 1.5144714708
tw0.p = 1.e-2


tot_angle = 0.0
for e in lat.sequence:
    if e.__class__ == Quadrupole:
        print 'quadrupole', e.id, e.k1
    if e.__class__ in (Bend, SBend, RBend):
        print 'bend', e.id, e.angle
        tot_angle += e.angle


print 'total deflection: ', tot_angle


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

constr = {m2_bdc:{'tau': -45.e-4, 'Dx':0.0} }
constr['global'] = {'beta_x':['<',40], 'beta_y':['<',40]}


var = [qf1_bdc, qf2_bdc, qf3_bdc, qf4_bdc, qd1_bdc, qd2_bdc, qd3_bdc, qd4_bdc]
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

