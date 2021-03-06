from ocelot import *
tws_L2 = Twiss()
tws_L2.beta_x = 9.736100000
tws_L2.beta_y = 36.061400
tws_L2.alpha_x = -1.041100
tws_L2.alpha_y = 1.843100
tws_L2.E = 0.7003
tws_L2.s = 212.122976


l2_cfb = Drift(l = 3.35, eid= 'l2_cfb')
d0080 = Drift(l = 0.08, eid= 'd0080')
d01416 = Drift(l = 0.1416, eid= 'd01416')
d02043 = Drift(l = 0.2043, eid= 'd02043')
ltwakecav = Drift(l = 0.0, eid= 'ltwakecav')
l2_cx = Drift(l = 0, eid= 'l2_cx')
d0085 = Drift(l = 0.085, eid= 'd0085')
d00729 = Drift(l = 0.0729, eid= 'd00729')
d0300 = Drift(l = 0.3, eid= 'd0300')
l2_cy = Drift(l = 0, eid= 'l2_cy')
l2_ctb = Drift(l = 3.25, eid= 'l2_ctb')

# quadrupoles 
l2_q_a3_1 = Quadrupole(l = 0.3, k1 = 0.2604636, eid= 'l2_q_a3_1')
l2_q_a3_2 = Quadrupole(l = 0.3, k1 = -0.2391746, eid= 'l2_q_a3_2')
l2_q_a3_3 = Quadrupole(l = 0.3, k1 = 0.15, eid= 'l2_q_a3_3')
l2_q_a3_4 = Quadrupole(l = 0.3, k1 = -0.15, eid= 'l2_q_a3_4')
l2_q_a4_1 = Quadrupole(l = 0.3, k1 = 0.15, eid= 'l2_q_a4_1')
l2_q_a4_2 = Quadrupole(l = 0.3, k1 = -0.15, eid= 'l2_q_a4_2')
l2_q_a4_3 = Quadrupole(l = 0.3, k1 = 0.15, eid= 'l2_q_a4_3')
l2_q_a4_4 = Quadrupole(l = 0.3, k1 = -0.15, eid= 'l2_q_a4_4')
l2_q_a5_1 = Quadrupole(l = 0.3, k1 = 0.1368622, eid= 'l2_q_a5_1')
l2_q_a5_2 = Quadrupole(l = 0.3, k1 = -0.3658154, eid= 'l2_q_a5_2')
l2_q_a5_3 = Quadrupole(l = 0.3, k1 = 0.2606671, eid= 'l2_q_a5_3')
l2_q_a5_4 = Quadrupole(l = 0.3, k1 = -0.3647037, eid= 'l2_q_a5_4')

# bending magnets 

# correctors 

# markers 
l2_start_l2 = Marker(eid= 'l2_start_l2')
l2_vcst40t78 = Marker(eid= 'l2_vcst40t78')
l2_stac_a3_1 = Marker(eid= 'l2_stac_a3_1')
miac = Marker(eid= 'miac')
l2_enac_a3_1 = Marker(eid= 'l2_enac_a3_1')
l2_stac_a3_2 = Marker(eid= 'l2_stac_a3_2')
l2_enac_a3_2 = Marker(eid= 'l2_enac_a3_2')
l2_stac_a3_3 = Marker(eid= 'l2_stac_a3_3')
l2_enac_a3_3 = Marker(eid= 'l2_enac_a3_3')
l2_stac_a3_4 = Marker(eid= 'l2_stac_a3_4')
l2_enac_a3_4 = Marker(eid= 'l2_enac_a3_4')
l2_stac_a4_1 = Marker(eid= 'l2_stac_a4_1')
l2_enac_a4_1 = Marker(eid= 'l2_enac_a4_1')
l2_stac_a4_2 = Marker(eid= 'l2_stac_a4_2')
l2_enac_a4_2 = Marker(eid= 'l2_enac_a4_2')
l2_mid_l2 = Marker(eid= 'l2_mid_l2')
l2_stac_a4_3 = Marker(eid= 'l2_stac_a4_3')
l2_enac_a4_3 = Marker(eid= 'l2_enac_a4_3')
l2_stac_a4_4 = Marker(eid= 'l2_stac_a4_4')
l2_enac_a4_4 = Marker(eid= 'l2_enac_a4_4')
l2_stac_a5_1 = Marker(eid= 'l2_stac_a5_1')
l2_enac_a5_1 = Marker(eid= 'l2_enac_a5_1')
l2_stac_a5_2 = Marker(eid= 'l2_stac_a5_2')
l2_enac_a5_2 = Marker(eid= 'l2_enac_a5_2')
l2_stac_a5_3 = Marker(eid= 'l2_stac_a5_3')
l2_enac_a5_3 = Marker(eid= 'l2_enac_a5_3')
l2_stac_a5_4 = Marker(eid= 'l2_stac_a5_4')
l2_enac_a5_4 = Marker(eid= 'l2_enac_a5_4')
l2_vcst78t40 = Marker(eid= 'l2_vcst78t40')
l2_end_l2 = Marker(eid= 'l2_end_l2')

# monitor 
l2_bpmr = Monitor(eid= 'l2_bpmr')
l2_bpmc = Monitor(eid= 'l2_bpmc')

# sextupoles 

# octupole 

# undulator 

# cavity 
l2_c_a3 = Cavity(l = 1.0377, v = 0.0177083333333, delta_e = 0.0177083333333, freq = 1300.0, phi = 0.0, volterr = 0.0, eid= 'l2_c_a3')
l2_c_a4 = Cavity(l = 1.0377, v = 0.0177083333333, delta_e = 0.0177083333333, freq = 1300.0, phi = 0.0, volterr = 0.0, eid= 'l2_c_a4')
l2_c_a5 = Cavity(l = 1.0377, v = 0.0177083333333, delta_e = 0.0177083333333, freq = 1300.0, phi = 0.0, volterr = 0.0, eid= 'l2_c_a5')

# rfcavity 

# Matrices 

# Solenoids 

# lattice 
L2 = (l2_start_l2, l2_vcst40t78, l2_cfb, l2_stac_a3_1, d0080, d01416, l2_c_a3,
d02043, ltwakecav, d01416, l2_c_a3, d02043, ltwakecav, d01416, l2_c_a3, 
d02043, ltwakecav, d01416, l2_c_a3, d02043, ltwakecav, miac, d01416, 
l2_c_a3, d02043, ltwakecav, d01416, l2_c_a3, d02043, ltwakecav, d01416, 
l2_c_a3, d02043, ltwakecav, d01416, l2_c_a3, d02043, ltwakecav, l2_q_a3_1, 
l2_cx, d0085, l2_bpmr, d0085, d00729, d0300, l2_enac_a3_1, l2_stac_a3_2, 
d0080, d01416, l2_c_a3, d02043, ltwakecav, d01416, l2_c_a3, d02043, 
ltwakecav, d01416, l2_c_a3, d02043, ltwakecav, d01416, l2_c_a3, d02043, 
ltwakecav, miac, d01416, l2_c_a3, d02043, ltwakecav, d01416, l2_c_a3, 
d02043, ltwakecav, d01416, l2_c_a3, d02043, ltwakecav, d01416, l2_c_a3, 
d02043, ltwakecav, l2_q_a3_2, l2_cy, d0085, l2_bpmr, d0085, d00729, 
d0300, l2_enac_a3_2, l2_stac_a3_3, d0080, d01416, l2_c_a3, d02043, ltwakecav, 
d01416, l2_c_a3, d02043, ltwakecav, d01416, l2_c_a3, d02043, ltwakecav, 
d01416, l2_c_a3, d02043, ltwakecav, miac, d01416, l2_c_a3, d02043, 
ltwakecav, d01416, l2_c_a3, d02043, ltwakecav, d01416, l2_c_a3, d02043, 
ltwakecav, d01416, l2_c_a3, d02043, ltwakecav, l2_q_a3_3, l2_cx, d0085, 
l2_bpmc, d0085, d00729, d0300, l2_enac_a3_3, l2_stac_a3_4, d0080, d01416, 
l2_c_a3, d02043, ltwakecav, d01416, l2_c_a3, d02043, ltwakecav, d01416, 
l2_c_a3, d02043, ltwakecav, d01416, l2_c_a3, d02043, ltwakecav, miac, 
d01416, l2_c_a3, d02043, ltwakecav, d01416, l2_c_a3, d02043, ltwakecav, 
d01416, l2_c_a3, d02043, ltwakecav, d01416, l2_c_a3, d02043, ltwakecav, 
l2_q_a3_4, l2_cy, d0085, l2_bpmc, d0085, d00729, d0300, l2_enac_a3_4, 
l2_stac_a4_1, d0080, d01416, l2_c_a4, d02043, ltwakecav, d01416, l2_c_a4, 
d02043, ltwakecav, d01416, l2_c_a4, d02043, ltwakecav, d01416, l2_c_a4, 
d02043, ltwakecav, miac, d01416, l2_c_a4, d02043, ltwakecav, d01416, 
l2_c_a4, d02043, ltwakecav, d01416, l2_c_a4, d02043, ltwakecav, d01416, 
l2_c_a4, d02043, ltwakecav, l2_q_a4_1, l2_cx, d0085, l2_bpmc, d0085, 
d00729, d0300, l2_enac_a4_1, l2_stac_a4_2, d0080, d01416, l2_c_a4, d02043, 
ltwakecav, d01416, l2_c_a4, d02043, ltwakecav, d01416, l2_c_a4, d02043, 
ltwakecav, d01416, l2_c_a4, d02043, ltwakecav, miac, d01416, l2_c_a4, 
d02043, ltwakecav, d01416, l2_c_a4, d02043, ltwakecav, d01416, l2_c_a4, 
d02043, ltwakecav, d01416, l2_c_a4, d02043, ltwakecav, l2_q_a4_2, l2_cy, 
d0085, l2_bpmc, d0085, d00729, d0300, l2_enac_a4_2, l2_mid_l2, l2_stac_a4_3, 
d0080, d01416, l2_c_a4, d02043, ltwakecav, d01416, l2_c_a4, d02043, 
ltwakecav, d01416, l2_c_a4, d02043, ltwakecav, d01416, l2_c_a4, d02043, 
ltwakecav, miac, d01416, l2_c_a4, d02043, ltwakecav, d01416, l2_c_a4, 
d02043, ltwakecav, d01416, l2_c_a4, d02043, ltwakecav, d01416, l2_c_a4, 
d02043, ltwakecav, l2_q_a4_3, l2_cx, d0085, l2_bpmc, d0085, d00729, 
d0300, l2_enac_a4_3, l2_stac_a4_4, d0080, d01416, l2_c_a4, d02043, ltwakecav, 
d01416, l2_c_a4, d02043, ltwakecav, d01416, l2_c_a4, d02043, ltwakecav, 
d01416, l2_c_a4, d02043, ltwakecav, miac, d01416, l2_c_a4, d02043, 
ltwakecav, d01416, l2_c_a4, d02043, ltwakecav, d01416, l2_c_a4, d02043, 
ltwakecav, d01416, l2_c_a4, d02043, ltwakecav, l2_q_a4_4, l2_cy, d0085, 
l2_bpmc, d0085, d00729, d0300, l2_enac_a4_4, l2_stac_a5_1, d0080, d01416, 
l2_c_a5, d02043, ltwakecav, d01416, l2_c_a5, d02043, ltwakecav, d01416, 
l2_c_a5, d02043, ltwakecav, d01416, l2_c_a5, d02043, ltwakecav, miac, 
d01416, l2_c_a5, d02043, ltwakecav, d01416, l2_c_a5, d02043, ltwakecav, 
d01416, l2_c_a5, d02043, ltwakecav, d01416, l2_c_a5, d02043, ltwakecav, 
l2_q_a5_1, l2_cx, d0085, l2_bpmc, d0085, d00729, d0300, l2_enac_a5_1, 
l2_stac_a5_2, d0080, d01416, l2_c_a5, d02043, ltwakecav, d01416, l2_c_a5, 
d02043, ltwakecav, d01416, l2_c_a5, d02043, ltwakecav, d01416, l2_c_a5, 
d02043, ltwakecav, miac, d01416, l2_c_a5, d02043, ltwakecav, d01416, 
l2_c_a5, d02043, ltwakecav, d01416, l2_c_a5, d02043, ltwakecav, d01416, 
l2_c_a5, d02043, ltwakecav, l2_q_a5_2, l2_cy, d0085, l2_bpmc, d0085, 
d00729, d0300, l2_enac_a5_2, l2_stac_a5_3, d0080, d01416, l2_c_a5, d02043, 
ltwakecav, d01416, l2_c_a5, d02043, ltwakecav, d01416, l2_c_a5, d02043, 
ltwakecav, d01416, l2_c_a5, d02043, ltwakecav, miac, d01416, l2_c_a5, 
d02043, ltwakecav, d01416, l2_c_a5, d02043, ltwakecav, d01416, l2_c_a5, 
d02043, ltwakecav, d01416, l2_c_a5, d02043, ltwakecav, l2_q_a5_3, l2_cx, 
d0085, l2_bpmr, d0085, d00729, d0300, l2_enac_a5_3, l2_stac_a5_4, d0080, 
d01416, l2_c_a5, d02043, ltwakecav, d01416, l2_c_a5, d02043, ltwakecav, 
d01416, l2_c_a5, d02043, ltwakecav, d01416, l2_c_a5, d02043, ltwakecav, 
miac, d01416, l2_c_a5, d02043, ltwakecav, d01416, l2_c_a5, d02043, 
ltwakecav, d01416, l2_c_a5, d02043, ltwakecav, d01416, l2_c_a5, d02043, 
ltwakecav, l2_q_a5_4, l2_cy, d0085, l2_bpmr, d0085, d00729, d0300, 
l2_enac_a5_4, l2_ctb, l2_vcst78t40, l2_end_l2)