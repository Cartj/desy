import sys
from ocelot.cpbd.elements import *
from ocelot.cpbd.optics import *
from ocelot.gui.accelerator import plot_lattice

from bc import *
from pylab import *


#lat = MagneticLattice(sase3_segment(n=7), energy=17.5)
lat = MagneticLattice(bc2_l3, energy=2.4)


beam = Beam()
beam.E = 2.4
beam.beta_x = 41.1209
beam.beta_y = 86.3314
beam.alpha_x = 1.9630
beam.alpha_y = 4.0972



tw0 = Twiss(beam)
print tw0
tws=twiss(lat, tw0, nPoints = 2000)


f=plt.figure()
ax = f.add_subplot(211)
ax.set_xlim(0, lat.totalLen)

f.canvas.set_window_title('Betas [m]') 
p1, = plt.plot(map(lambda p: p.s, tws), map(lambda p: p.beta_x, tws), lw=2.0)
p2, = plt.plot(map(lambda p: p.s, tws), map(lambda p: p.beta_y, tws), lw=2.0)
plt.grid(True)
plt.legend([p1,p2], [r'$\beta_x$',r'$\beta_y$', r'$D_x$'])

ax2 = f.add_subplot(212)
plot_lattice(lat, ax2, alpha=0.5)

# add beam size (arbitrary scale)

s = np.array(map(lambda p: p.s, tws))

scale = 5000

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

plt.show()

