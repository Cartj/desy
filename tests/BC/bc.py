# 

# xfel lattice

# component_list_8.3.2.xls . elegant_lattice

#


from numpy import *
from ocelot.cpbd.elements import *
from ocelot.cpbd.beam import *

#q = charge(total=1e-9, id = 'q')
#m0 = watch(filename="%s.m0", id = 'm0')
#m1 = watch(filename="%s.m1", id = 'm1')



csrflag = 0

n_csr_bin = 600

n_csr_kick = 10

fwidth = 20



phi_bc2 = 0.033646252962410

l0 = 0.5

l_bc2 = l0 *phi_bc2 /sin((phi_bc2))

ac_v = 5e+008
#ac_v = 0



# bc2

bb_393_b2 = Bend(l=l_bc2, angle=phi_bc2, e1=0.000000000, e2=phi_bc2, tilt=1.570796330, id = 'bb_393_b2')
bb_402_b2 = Bend(l=l_bc2, angle=-phi_bc2, e1=-phi_bc2, e2=0.000000000, tilt=1.570796330, id = 'bb_402_b2')
bb_404_b2 = Bend(l=l_bc2, angle=-phi_bc2, e1=0.000000000, e2=-phi_bc2, tilt=1.570796330,  id = 'bb_404_b2')
bb_413_b2 = Bend(l=l_bc2, angle=phi_bc2, e1=phi_bc2, e2=0.000000000, tilt=1.570796330,  id = 'bb_413_b2')


d10cm = 	Drift(l=0.1, id = 'd10cm')
cd850cm = 	Drift(l=8.5 / cos(phi_bc2), id = 'cd850cm')
cd150cm = 	Drift(l=1.5, id = 'cd150cm')
cd100cm = 	Drift(l=1, id = 'cd100cm')


bc2  = (d10cm,
     bb_393_b2, cd850cm,
     bb_402_b2, cd150cm,
     bb_404_b2, cd850cm, 
     bb_413_b2, 
     cd100cm)



qd_415_b2 = Quadrupole(l=0.2000000, k1=0.3, tilt=0.000000000, id = 'qd_415_b2')
qd_417_b2 = Quadrupole(l=0.2000000, k1=-0.2, tilt=0.000000000, id = 'qd_417_b2')
qd_418_b2 = Quadrupole(l=0.2000000, k1=-0.5, tilt=0.000000000, id = 'qd_418_b2')


d13cm = 	Drift(l=0.13, id = 'd13cm')
d130cm = Drift(l=1.3, id = 'd130cm')


q_249_l2 = Quadrupole(l=0.3000000, k1=0.25, tilt=0.000000000, id = 'q_249_l2')
q_261_l2 = Quadrupole(l=0.3000000, k1=-0.29711100, tilt=0.000000000, id = 'q_261_l2')


d34cm59 = Drift(l=0.3459, id = 'd34cm59')


c_a3 = Cavity(l=1.0377000, phi=0.0, delta_e = ac_v, freq=1.300e+009, id = 'c_a3')




l3  = (	d13cm,qd_415_b2,d130cm, qd_417_b2, d130cm, qd_418_b2,d130cm,
     	c_a3, d34cm59, c_a3, d34cm59, c_a3, d34cm59, c_a3, d34cm59, 
 	c_a3, d34cm59, c_a3, d34cm59, c_a3, d34cm59, c_a3, d13cm , 
 	q_249_l2, d34cm59, 
 	c_a3, d34cm59, c_a3, d34cm59, c_a3, d34cm59, c_a3, d34cm59, 
 	c_a3, d34cm59, c_a3, d34cm59, c_a3, d34cm59, c_a3, d13cm, 
 	q_261_l2, d130cm)  



bc2_l3  = (bc2,l3)



