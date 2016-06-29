from ocelot import *
tws_T4 = Twiss()
tws_T4.beta_x = 23.355200000
tws_T4.beta_y = 60.234400
tws_T4.alpha_x = -0.753600
tws_T4.alpha_y = 1.980500
tws_T4.E = 17.625300000
tws_T4.s = 2438.521517



d0058 = Drift(l = 0.058, eid= 'd0058')
d03325 = Drift(l = 0.3325, eid= 'd03325')
d0990 = Drift(l = 0.99, eid= 'd0990')
d0210 = Drift(l = 0.21, eid= 'd0210')
d0230 = Drift(l = 0.23, eid= 'd0230')
d5138 = Drift(l = 5.138, eid= 'd5138')
d0100 = Drift(l = 0.1, eid= 'd0100')
d0050 = Drift(l = 0.05, eid= 'd0050')
d0075 = Drift(l = 0.075, eid= 'd0075')
d0080 = Drift(l = 0.08, eid= 'd0080')
d0030 = Drift(l = 0.03, eid= 'd0030')
t4_cex = Drift(l = 0.1, eid= 't4_cex')
d11795 = Drift(l = 11.795, eid= 'd11795')
t4_cey = Drift(l = 0.1, eid= 't4_cey')
d8430 = Drift(l = 8.43, eid= 'd8430')
d10000 = Drift(l = 10.0, eid= 'd10000')
d0450 = Drift(l = 0.45, eid= 'd0450')
d0935 = Drift(l = 0.935, eid= 'd0935')
d0485 = Drift(l = 0.485, eid= 'd0485')
d7930 = Drift(l = 7.93, eid= 'd7930')
d0175 = Drift(l = 0.175, eid= 'd0175')
d0040 = Drift(l = 0.04, eid= 'd0040')
t4_chx = Drift(l = 0.2, eid= 't4_chx')
d1230 = Drift(l = 1.23, eid= 'd1230')
t4_chy = Drift(l = 0.2, eid= 't4_chy')
d8020 = Drift(l = 8.02, eid= 'd8020')
d1000 = Drift(l = 1.0, eid= 'd1000')
d0145 = Drift(l = 0.145, eid= 'd0145')
d0150 = Drift(l = 0.15, eid= 'd0150')
d0250 = Drift(l = 0.25, eid= 'd0250')
d0500 = Drift(l = 0.5, eid= 'd0500')
d0025 = Drift(l = 0.025, eid= 'd0025')
d0000 = Drift(l = 0.0, eid= 'd0000')
d0200 = Drift(l = 0.2, eid= 'd0200')
d1440 = Drift(l = 1.44, eid= 'd1440')
d1500 = Drift(l = 1.5, eid= 'd1500')
d0640 = Drift(l = 0.64, eid= 'd0640')
d2025 = Drift(l = 2.025, eid= 'd2025')
d1290 = Drift(l = 1.29, eid= 'd1290')
d1045 = Drift(l = 1.045, eid= 'd1045')
d1590 = Drift(l = 1.59, eid= 'd1590')
d0275 = Drift(l = 0.275, eid= 'd0275')
d9860 = Drift(l = 9.86, eid= 'd9860')
t4_cfy = Drift(l = 0.1, eid= 't4_cfy')
d5240 = Drift(l = 5.24, eid= 'd5240')
d0400 = Drift(l = 0.4, eid= 'd0400')
d5025 = Drift(l = 5.025, eid= 'd5025')
t4_cfx = Drift(l = 0.1, eid= 't4_cfx')
d2359 = Drift(l = 2.2507, eid= 'd2359')
d4400 = Drift(l = 4.4, eid= 'd4400')
d000675 = Drift(l = 0.00675, eid= 'd000675')
d009975 = Drift(l = 0.09975, eid= 'd009975')
d0125 = Drift(l = 0.125, eid= 'd0125')
d0160 = Drift(l = 0.16, eid= 'd0160')
t4_cny = Drift(l = 0.3, eid= 't4_cny')
d20575 = Drift(l = 2.0575, eid= 'd20575')
d0110 = Drift(l = 0.11, eid= 'd0110')
d17167 = Drift(l = 1.7167, eid= 'd17167')
t4_absp = Drift(l = 0.05, eid= 't4_absp')
d01723 = Drift(l = 0.1723, eid= 'd01723')
d01935 = Drift(l = 0.1935, eid= 'd01935')
d0047 = Drift(l = 0.047, eid= 'd0047')

# quadrupoles 
t4_qe_3 = Quadrupole(l = 0.2, k1 = 0.2670324, eid= 't4_qe_3')
t4_qe_4 = Quadrupole(l = 0.2, k1 = -0.2444023, eid= 't4_qe_4')
t4_qe_5 = Quadrupole(l = 0.2, k1 = 0.2881296, eid= 't4_qe_5')
t4_qe_6 = Quadrupole(l = 0.2, k1 = -0.2757726, eid= 't4_qe_6')
t4_qe_2 = Quadrupole(l = 0.2, k1 = 0.22976, eid= 't4_qe_2')
t4_qe_1 = Quadrupole(l = 0.2, k1 = -0.22976, eid= 't4_qe_1')
t4_qh_4 = Quadrupole(l = 1.0, k1 = 0.20188, eid= 't4_qh_4')
t4_qh_3 = Quadrupole(l = 1.0, k1 = -0.2021, eid= 't4_qh_3')
t4_qh_1 = Quadrupole(l = 1.0, k1 = 0.303952, eid= 't4_qh_1')
t4_qm_2 = Quadrupole(l = 1.0, k1 = -0.303939, eid= 't4_qm_2')
t4_qm_1 = Quadrupole(l = 1.0, k1 = 0.303952, eid= 't4_qm_1')
t4_qh_2 = Quadrupole(l = 1.0, k1 = -0.303939, eid= 't4_qh_2')
t4_qf_7 = Quadrupole(l = 0.5, k1 = -0.1232094, eid= 't4_qf_7')
t4_qf_8 = Quadrupole(l = 0.5, k1 = 0.1550097, eid= 't4_qf_8')
t4_qf_9 = Quadrupole(l = 0.5, k1 = -0.1601755, eid= 't4_qf_9')
t4_qf_10 = Quadrupole(l = 0.5, k1 = 0.1911083, eid= 't4_qf_10')
t4_qa_3 = Quadrupole(l = 0.1, k1 = -1.276015, eid= 't4_qa_3')
t4_qa_4 = Quadrupole(l = 0.1, k1 = 1.392947, eid= 't4_qa_4')

# bending magnets 
t4_be_1 = Bend(l = 2.50001378448, angle = 0.0115035, e1 = 0.00575175, e2 = 0.00575175, tilt = 0.0, eid= 't4_be_1')

# correctors 

# markers 
t4_start = Marker(eid= 't4_start')
t4_vcst10t40 = Marker(eid= 't4_vcst10t40')
t4_tora = Marker(eid= 't4_tora')
t4_vcst40t93x = Marker(eid= 't4_vcst40t93x')
t4_startt9 = Marker(eid= 't4_startt9')
t4_start_arc = Marker(eid= 't4_start_arc')
t4_vcst93xt40 = Marker(eid= 't4_vcst93xt40')
t4_end_arc = Marker(eid= 't4_end_arc')
t4_otrbw = Marker(eid= 't4_otrbw')
t4_vcst40t10 = Marker(eid= 't4_vcst40t10')
t4_end = Marker(eid= 't4_end')

# monitor 
t4_bpma = Monitor(eid= 't4_bpma')
t4_bpme = Monitor(eid= 't4_bpme')

# sextupoles 
t4_saox_1 = Sextupole(l = 0.3, k2 = 25.23, tilt = 0, eid= 't4_saox_1')
t4_saox_2 = Sextupole(l = 0.3, k2 = 8.91, tilt = 0, eid= 't4_saox_2')

# octupole 

# undulator 

# cavity 

# rfcavity 

# Matrices 
t4_u40s = Matrix(l = 0.12, rm11 = 1.0, rm12 = 0.12, rm13 = 0.0, rm21 = 0.0, rm22 = 1.0, rm33 = 0.999999185989, rm34 = 0.11999996744, rm43 = -1.35668453185e-05, rm44 = 0.999999185989, eid= 't4_u40s')

# Solenoids 

# lattice 
T4 = (t4_start, t4_vcst10t40, d0058, d03325, d0990, t4_tora, d0210,
d0230, d5138, d0100, t4_bpma, d0100, d0050, d0075, t4_qe_3, 
d0080, d0050, d0030, t4_cex, d0030, d11795, d0100, t4_bpma, 
d0100, d0050, d0075, t4_qe_4, d0080, d0050, d0030, t4_cey, 
d0030, d11795, d0100, t4_bpma, d0100, d0050, d0075, t4_qe_5, 
d0080, d0050, d0030, t4_cex, d0030, d11795, d0100, t4_bpma, 
d0100, d0050, d0075, t4_qe_6, d0080, d0050, d0030, t4_cey, 
d0030, d8430, d10000, d0450, d0100, t4_bpma, d0100, d0050, 
d0075, t4_qe_2, d0080, d0050, d0030, t4_cex, d0030, d10000, 
d10000, d0935, d0100, t4_bpma, d0100, d0050, d0075, t4_qe_1, 
d0080, d0050, d0030, t4_cey, d0030, d10000, d0485, d7930, 
d0175, d0100, t4_bpma, d0100, d0050, d0075, t4_qh_4, d0080, 
d0050, d0040, t4_chx, d0040, d1230, d0175, d0100, t4_bpma, 
d0100, d0050, d0075, t4_qh_3, d0080, d0050, d0040, t4_chy, 
d0040, d8020, d1000, t4_chx, d0145, d0040, t4_chy, d0040, 
d0050, d0100, t4_bpma, d0100, d0050, d0075, t4_qh_1, d0150, 
t4_vcst40t93x, d0250, t4_startt9, t4_start_arc, t4_be_1, t4_vcst93xt40, d0100, d0500, 
d0025, d0100, d0000, d0100, d0200, d0075, t4_qm_2, d0080, 
d0200, d0040, d0200, d0040, d1440, d1500, d0025, d0100, 
t4_bpma, d0100, d0200, d0075, t4_qm_1, d0080, d0200, d0040, 
t4_chx, d0040, d0640, t4_saox_1, d2025, d0100, t4_bpma, d0100, 
d0200, d0075, t4_qm_2, d0080, d0200, d0040, t4_chy, d0040, 
d1290, t4_saox_2, d1045, d0040, t4_chx, d0040, d0050, d0100, 
t4_bpma, d0100, d0200, d0075, t4_qm_1, d0200, d0200, t4_be_1, 
t4_end_arc, d0100, d0500, d0175, d0100, t4_bpma, d0100, d0050, 
d0075, t4_qh_2, d0080, d0050, d0040, t4_chy, d0040, d1590, 
d7930, d0175, d0100, t4_bpma, d0100, d0050, d0075, t4_qh_4, 
d0080, d0050, d0040, t4_chx, d0040, d1230, d0175, d0100, 
t4_bpma, d0100, d0050, d0075, t4_qh_3, d0080, d0050, d0040, 
t4_chy, d0040, d8020, d10000, d0450, d0100, t4_bpma, d0100, 
d0050, d0075, t4_qe_2, d0080, d0050, d0030, t4_cex, d0030, 
d10000, d10000, d0935, d0100, t4_bpma, d0100, d0050, d0075, 
t4_qe_1, d0080, d0050, d0030, t4_cey, d0030, d10000, d0485, 
d10000, d0450, d0100, t4_bpma, d0100, d0050, d0075, t4_qe_2, 
d0080, d0050, d0030, t4_cex, d0030, d10000, d10000, d0935, 
d0100, t4_bpma, d0100, d0050, d0075, t4_qe_1, d0080, d0050, 
d0030, t4_cey, d0030, d10000, d0485, d0275, t4_otrbw, d10000, 
d0175, d0100, t4_bpma, d0100, d0050, d0075, t4_qe_2, d0080, 
d0050, d0030, t4_cex, d0030, d9860, d10000, d0175, d0100, 
t4_bpma, d0100, d0050, d0075, t4_qf_7, d0080, d0050, d0040, 
t4_cfy, d0040, d5240, d0200, t4_otrbw, d0400, d5025, d0100, 
t4_bpma, d0100, d0050, d0075, t4_qf_8, d0080, d0050, d0040, 
t4_cfx, d0040, d5240, d0200, d0400, d5025, d0100, t4_bpma, 
d0100, d0050, d0075, t4_qf_9, d0080, d0050, d0040, t4_cfy, 
d0040, d5240, d0200, t4_otrbw, d0400, d5025, d0100, t4_bpma, 
d0100, d0050, d0075, t4_qf_10, d0080, d0050, d0040, t4_cfx, 
d0040, d2359, d4400, d0400, t4_tora, d000675, d0500, d0100, 
t4_vcst40t10, d009975, d0100, t4_bpme, d0100, d0125, t4_qa_3, d0160, 
d0025, t4_cny, d0125, t4_cex, d20575, d0110, t4_u40s, d0110, 
d17167, t4_cny, d0150, t4_cex, d0160, d0050, t4_absp, d01723, 
t4_bpme, d01935, t4_qa_4, d0047, t4_end)