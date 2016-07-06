'''
chicane-type var delay achromat
'''

import sys

sys.path.append('../utils/')
from xfel_utils import *
from ocelot.gui.accelerator import *
from ocelot.cpbd.match import *

from p3fel import *

ang_total = 0.24 # rad, ~ 6 degree

comp_ang = -0.021# middle magnet bend angle in opposite direction

bc_b1 = RBend (l=6.0*m, angle=ang_total/2. - comp_ang / 2.0, eid= "b1")
bc_b2_1 = RBend (l=3.0*m, angle=comp_ang/2.0, eid= "b2")
bc_b2_2 = RBend (l=3.0*m, angle=comp_ang/2.0, eid= "b2")
bc_b3 = RBend (l=6.0*m, angle=ang_total/2. - comp_ang / 2.0, eid= "b2")

bc_q1 = Quadrupole(l=0.1, k1 = -2.0)
bc_q2 = Quadrupole(l=0.1, k1 = 2.0)


bc_d1 = Drift(l=2.0*m)
bc_d2 = Drift(l=0.5*m)
bc_d3 = Drift(l=1.5*m)
m1 = Monitor(eid="start")
m2 = Monitor(eid="end")


bc1 = (m1, bc_d1, bc_b1, bc_d1, bc_q1, bc_d1, bc_b2_1, bc_d2, bc_q2, bc_d2, bc_b2_2, bc_d1, bc_q1, bc_d1, bc_b3, bc_d1, m2)

lat = MagneticLattice(bc1, energy=6.0)

tw0 = Twiss(beam)
tw0.p = 1.e-2


print 'total deflection: ', bc_b1.angle + bc_b2.angle + bc_b3.angle 

'''
r56 = []
cas = np.linspace(-0.24, -0.02, 20)

for comp_ang in cas:
    bc_b1.angle = ang_total/2. - comp_ang / 2.0
    bc_b2_1.angle = comp_ang/2.0
    bc_b2_2.angle = comp_ang/2.0
    bc_b3.angle = ang_total/2. - comp_ang / 2.0
    lat.update_transfer_maps()


    constr = {'end':{'Dx':0.0, 'Dxp':0.0}, 'start':{'Dx':0.0, 'Dxp':0.0}}
    vars = [bc_q1, bc_q2]
    #bc_q1.k1 = 0.0; vars = [bc_q2]
    match(lat, constr, vars, tw0)
    
    tws=twiss(lat, tw0, nPoints = 100)
    print tws[-1].tau * 1.e4, ' cm'
    r56.append(tws[-1].tau * 1.e4)
    
plt.plot(cas, r56)
plt.grid(True)
#plt.show()
'''

constr = {m2:{'Dx':0.0, 'Dxp':0.0, 'beta_x':['->',m1], 'beta_y':['->',m1]}, m1:{'Dx':0.0, 'Dxp':0.0}}
vars = [bc_q1, bc_q2]
#bc_q1.k1 = 0.0; vars = [bc_q2]
match(lat, constr, vars, tw0)


tws=twiss(lat, tw0, nPoints = 100)

f=plt.figure()
ax = f.add_subplot(211)
ax.set_xlim(0, lat.totalLen)

f.canvas.set_window_title('Betas [m]') 
p1, = ax.plot(map(lambda p: p.s, tws), map(lambda p: p.beta_x, tws), lw=2.0)
p2, = ax.plot(map(lambda p: p.s, tws), map(lambda p: p.beta_y, tws), lw=2.0)
ax2 = ax.twinx()
p3, = ax2.plot(map(lambda p: p.s, tws), map(lambda p: p.Dx, tws), 'r-', lw=2.0)
plt.grid(True)
plt.legend([p1,p2,p3], [r'$\beta_x$',r'$\beta_y$', r'$D_x$'], fancybox=True, framealpha=0.5)

ax2 = f.add_subplot(212)
plot_lattice(lat, ax2, alpha=0.5)

# add beam size (arbitrary scale)

s = np.array(map(lambda p: p.s, tws))

scale = 10

sig_x = scale * np.array(map(lambda p: np.sqrt(p.beta_x*beam.emit_x), tws)) # 0.03 is for plotting same scale
sig_y = scale * np.array(map(lambda p: np.sqrt(p.beta_y*beam.emit_y), tws))

x = scale * np.array(map(lambda p: p.x, tws))
y = scale * np.array(map(lambda p: p.y, tws))


plt.plot(s, x + sig_x, color='#0000AA', lw=2.0)
plt.plot(s, x-sig_x, color='#0000AA', lw=2.0)

plt.plot(s, sig_y, color='#00AA00', lw=2.0)
plt.plot(s, -sig_y, color='#00AA00', lw=2.0)

#f=plt.figure()
plt.plot(s, x, 'r--', lw=2.0)
#plt.plot(s, y, 'r--', lw=2.0)
fig = plt.figure()
ax = fig.add_subplot(111)
p1, = plt.plot(s, np.array(map(lambda p: p.tau, tws)) * 1.e4)
ax.set_xlabel('[m]')
ax.set_ylabel('[cm]')

fig = plt.figure()
ax = fig.add_subplot(111)
p1, = plt.plot(s, np.array(map(lambda p: p.mux, tws)))
p2, = plt.plot(s, np.array(map(lambda p: p.muy, tws)))
#ax.set_xlabel('[m]')
#ax.set_ylabel('[cm]')
plt.show()
