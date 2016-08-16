from ocelot.cpbd.elements import *
# drifts
D00m25 = Drift(l = 0.25, eid= 'D00m25')
D01m = Drift(l = 1, eid= 'D01m')
D02m = Drift(l = 2, eid= 'D02m')
w1_start = Marker(eid="w1_start")
w1_stop = Marker(eid="w1_stop")

w2_start = Marker(eid="w2_start")
w2_stop = Marker(eid="w2_stop")

w3_start = Marker(eid="w3_start")
w3_stop = Marker(eid="w3_stop")

w4_start = Marker(eid="w4_start")
w4_stop = Marker(eid="w4_stop")

w5_start = Marker(eid="w5_start")
w5_stop = Marker(eid="w5_stop")

w6_start = Marker(eid="w6_start")
w6_stop = Marker(eid="w6_stop")
# quadrupoles
Q1 = Quadrupole(l = 0.5, k1 = 0.215, eid= 'Q1')

# lattice
lattice = (D01m, w1_start, D02m, w1_stop, w2_start, D02m, w2_stop, w3_start, D02m, w3_stop, D00m25, Q1,
           D00m25, w4_start, D02m, w4_stop, w5_start, D02m, w5_stop, w6_start, D02m, w6_stop, D01m)