from ocelot.cpbd.elements import *
# drifts
D00m25 = Drift(l = 0.25, id = 'D00m25')
D01m = Drift(l = 1, id = 'D01m')
D02m = Drift(l = 2, id = 'D02m')

# quadrupoles
Q1 = Quadrupole(l = 0.5, k1 = 0.215, id = 'Q1')

# lattice
lattice = (D01m,D02m,D02m,D02m,D00m25,Q1,D00m25,D02m,D02m,D02m,D01m)