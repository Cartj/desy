from ocelot.cpbd.elements import *
# drifts
D00m25 = Drift(l = 0.25, eid= 'D00m25')
D01m = Drift(l = 1, eid= 'D01m')
D02m = Drift(l = 2, eid= 'D02m')

# quadrupoles
Q1 = Quadrupole(l = 0.5, k1 = 0.215, eid= 'Q1')

# lattice
lattice = (D01m,D02m,D02m,D02m,D00m25,Q1,D00m25,D02m,D02m,D02m,D01m)