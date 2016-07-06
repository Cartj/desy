from ocelot import *
tws_L1 = Twiss()
tws_L1.beta_x = 4.346400000
tws_L1.beta_y = 13.623800
tws_L1.alpha_x = -0.438400
tws_L1.alpha_y = 0.344600
tws_L1.E = 0.1303
tws_L1.s = 96.604101



l1_cfb = Drift(l = 3.35, eid= 'l1_cfb')
d0080 = Drift(l = 0.08, eid= 'd0080')
d01416 = Drift(l = 0.1416, eid= 'd01416')
d02043 = Drift(l = 0.2043, eid= 'd02043')
ltwakecav = Drift(l = 0.0, eid= 'ltwakecav')
l1_cx = Drift(l = 0, eid= 'l1_cx')
l1_cy = Drift(l = 0, eid= 'l1_cy')
d0085 = Drift(l = 0.085, eid= 'd0085')
d00729 = Drift(l = 0.0729, eid= 'd00729')
d0300 = Drift(l = 0.3, eid= 'd0300')
l1_ctb = Drift(l = 3.25, eid= 'l1_ctb')

# quadrupoles 
l1_q_a2_1 = Quadrupole(l = 0.3, k1 = 0.219222826375, eid= 'l1_q_a2_1')
l1_q_a2_2 = Quadrupole(l = 0.3, k1 = -0.211095518521, eid= 'l1_q_a2_2')
l1_q_a2_3 = Quadrupole(l = 0.3, k1 = 0.141481449266, eid= 'l1_q_a2_3')
l1_q_a2_4 = Quadrupole(l = 0.3, k1 = -0.144615140151, eid= 'l1_q_a2_4')

# bending magnets 

# correctors 

# markers 
l1_start_l1 = Marker(eid= 'l1_start_l1')
l1_vcst40t78 = Marker(eid= 'l1_vcst40t78')
l1_stac_a2_1 = Marker(eid= 'l1_stac_a2_1')
miac = Marker(eid= 'miac')
l1_enac_a2_1 = Marker(eid= 'l1_enac_a2_1')
l1_stac_a2_2 = Marker(eid= 'l1_stac_a2_2')
l1_enac_a2_2 = Marker(eid= 'l1_enac_a2_2')
l1_stac_a2_3 = Marker(eid= 'l1_stac_a2_3')
l1_enac_a2_3 = Marker(eid= 'l1_enac_a2_3')
l1_stac_a2_4 = Marker(eid= 'l1_stac_a2_4')
l1_enac_a2_4 = Marker(eid= 'l1_enac_a2_4')
l1_vcst78t40 = Marker(eid= 'l1_vcst78t40')
l1_end_l1 = Marker(eid= 'l1_end_l1')

# monitor 
l1_bpmc = Monitor(eid= 'l1_bpmc')
l1_bpmr = Monitor(eid= 'l1_bpmr')

# sextupoles 

# octupole 

# undulator 

# cavity 
l1_c_a2 = Cavity(l = 1.0377, v = 0.0178125, delta_e = 0.0178125, freq = 1300.0, phi = 0.0, volterr = 0.0, eid= 'l1_c_a2')

# rfcavity 

# Matrices 

# Solenoids 

# lattice 
L1 = (l1_start_l1, l1_vcst40t78, l1_cfb, l1_stac_a2_1, d0080, d01416, l1_c_a2,
d02043, ltwakecav, d01416, l1_c_a2, d02043, ltwakecav, d01416, l1_c_a2, 
d02043, ltwakecav, d01416, l1_c_a2, d02043, ltwakecav, miac, d01416, 
l1_c_a2, d02043, ltwakecav, d01416, l1_c_a2, d02043, ltwakecav, d01416, 
l1_c_a2, d02043, ltwakecav, d01416, l1_c_a2, d02043, ltwakecav, l1_q_a2_1, 
l1_cx, l1_cy, d0085, l1_bpmc, d0085, d00729, d0300, l1_enac_a2_1, 
l1_stac_a2_2, d0080, d01416, l1_c_a2, d02043, ltwakecav, d01416, l1_c_a2, 
d02043, ltwakecav, d01416, l1_c_a2, d02043, ltwakecav, d01416, l1_c_a2, 
d02043, ltwakecav, miac, d01416, l1_c_a2, d02043, ltwakecav, d01416, 
l1_c_a2, d02043, ltwakecav, d01416, l1_c_a2, d02043, ltwakecav, d01416, 
l1_c_a2, d02043, ltwakecav, l1_q_a2_2, l1_cx, l1_cy, d0085, l1_bpmr, 
d0085, d00729, d0300, l1_enac_a2_2, l1_stac_a2_3, d0080, d01416, l1_c_a2, 
d02043, ltwakecav, d01416, l1_c_a2, d02043, ltwakecav, d01416, l1_c_a2, 
d02043, ltwakecav, d01416, l1_c_a2, d02043, ltwakecav, miac, d01416, 
l1_c_a2, d02043, ltwakecav, d01416, l1_c_a2, d02043, ltwakecav, d01416, 
l1_c_a2, d02043, ltwakecav, d01416, l1_c_a2, d02043, ltwakecav, l1_q_a2_3, 
l1_cx, l1_cy, d0085, l1_bpmc, d0085, d00729, d0300, l1_enac_a2_3, 
l1_stac_a2_4, d0080, d01416, l1_c_a2, d02043, ltwakecav, d01416, l1_c_a2, 
d02043, ltwakecav, d01416, l1_c_a2, d02043, ltwakecav, d01416, l1_c_a2, 
d02043, ltwakecav, miac, d01416, l1_c_a2, d02043, ltwakecav, d01416, 
l1_c_a2, d02043, ltwakecav, d01416, l1_c_a2, d02043, ltwakecav, d01416, 
l1_c_a2, d02043, ltwakecav, l1_q_a2_4, l1_cx, l1_cy, d0085, l1_bpmr, 
d0085, d00729, d0300, l1_enac_a2_4, l1_ctb, l1_vcst78t40, l1_end_l1)