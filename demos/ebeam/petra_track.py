__author__ = 'Sergey Tomin'
import sys
ind = sys.path[0].find("repository")

sys.path.append(sys.path[0][:ind] + "repository")
print sys.path[-1]
from ocelot.cpbd.beam import *
from ocelot.cpbd import track
from time import time
from ocelot.gui.accelerator import *
from copy import deepcopy
from ocelot.cpbd.elements import *
beam = Beam()
beam.E = 6.
beam.sigma_E = 0.001
beam.I = 0.1


tw0 = Twiss(beam)

exec( open("petra3.inp" ))
lat = MagneticLattice(lattice)
tw0 = Twiss(beam)
tws = twiss(lat, tw0, nPoints=500)

plot_opt_func(lat, tws)
plt.show()

# trajectory with energy offset

p1 = Particle(x=0.03, y=0.01, p=0.0)
p2 = Particle(x=0.03, y=0.01, p=0.0)
P1 = [copy(p1)]
P2 = [copy(p2)]
navi1 = Navigator()
navi2 = Navigator()
dz = 1.

for i in range(int(lat.totalLen/dz)):
    track.step(lat, [p1], dz=dz, navi=navi1, order=2)  # R only
    track.step(lat, [p2], dz=dz, navi=navi2, order=3)  # R + T
    P1.append(copy(p1))
    P2.append(copy(p2))

s = [p.s for p in P1]
x1 = [p.x for p in P1]
x2 = [p.x for p in P2]
y1 = [p.y for p in P1]
y2 = [p.y for p in P2]
plt.title("Trajectories with $\Delta p/p = 0.02$")
plt.xlabel("S, m")
plt.ylabel("X, m")
plt.plot(s, x1,'r', s, x2, 'b')
plt.plot(s, y1,'g', s, y2, 'k')
plt.legend(["R", "R+T","y:R", "y:R+T" ], loc=2)
plt.show()

# phase trajectory

t = linspace(0, 2*pi, num = 100)
x, y = 0.005*cos(t), 0.005*sin(t)
plist = []
for xi, yi in zip(x,y):
    plist.append(Particle(x = xi, y= yi))

plist_1 = deepcopy(plist)
navi = Navigator()
# lat.totalLen
track.step(lat, plist_1, dz=lat.totalLen, navi=copy(navi), order=3)
track.step(lat, plist, dz=lat.totalLen, navi=copy(navi), order=1)
#for i, p in enumerate(plist_1):
#    print p.x, x[i], p.y, y[i]
x2 = [f.x for f in plist]
y2 = [f.y for f in plist]

x1 = [f.x for f in plist_1]
y1 = [f.y for f in plist_1]

plt.suptitle("Tracking")
plt.subplot(121)
plt.title("S = 0 m")
plt.plot(x, y, "r.-", label = "X")
plt.xlabel("X, m")
plt.ylabel("Xp, rad")
plt.grid(True)

plt.subplot(122)
plt.title("end of section")
plt.plot(x2, y2, "r.-",label="R + T")
plt.plot(x1, y1, 'b.-', label="R")
plt.legend(loc=2)
plt.xlabel("X, m")
plt.ylabel("Xp, rad")
plt.grid(True)
plt.show()