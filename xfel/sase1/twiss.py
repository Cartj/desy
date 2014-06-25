from xframework.gui.accelerator import *
sys.path.append('../')
from xfel_utils import *


exec( open("sase1.inp" )) 

lat = MagneticLattice(sase1_segment(n=10))

rematch(18.0, l_fodo, qdh, lat, extra_fodo, beam, qf, qd) # jeez...

tw0 = Twiss(beam)
print tw0
tws=twiss(lat, tw0, nPoints = 1000)


f=plt.figure()
ax = f.add_subplot(211)
ax.set_xlim(0, lat.totalLen)

f.canvas.set_window_title('Betas [m]') 
p1, = plt.plot(map(lambda p: p.s, tws), map(lambda p: p.beta_x, tws), lw=2.0)
p2, = plt.plot(map(lambda p: p.s, tws), map(lambda p: p.beta_y, tws), lw=2.0)
plt.grid(True)
plt.legend([p1,p2], [r'$\beta_x$',r'$\beta_y$', r'$D_x$'])

ax2 = f.add_subplot(212)
plot_lattice(lat, ax2, alpha=0.1)

# add beam size (arbitrary scale)

s = np.array(map(lambda p: p.s/lat.totalLen, tws))
sig_x = 0.03* np.array(map(lambda p: np.sqrt(p.beta_x), tws))
sig_y = 0.03* np.array(map(lambda p: np.sqrt(p.beta_y), tws))

plt.plot(s, sig_x, color='#0000AA', lw=2.0)
plt.plot(s, -sig_x, color='#0000AA', lw=2.0)

plt.plot(s, sig_y, color='#00AA00', lw=2.0)
plt.plot(s, -sig_y, color='#00AA00', lw=2.0)


plt.show()

