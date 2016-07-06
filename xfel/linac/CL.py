from ocelot import *
tws_CL = Twiss()
tws_CL.beta_x = 49.638700000
tws_CL.beta_y = 76.439300
tws_CL.alpha_x = -2.249400
tws_CL.alpha_y = 3.884600
tws_CL.E = 17.625300000
tws_CL.s = 1629.706502


d70887 = Drift(l = 6.3887, eid= 'd70887')
d0100 = Drift(l = 0.1, eid= 'd0100')
d0600 = Drift(l = 0.6, eid= 'd0600')
d0050 = Drift(l = 0.05, eid= 'd0050')
d0075 = Drift(l = 0.075, eid= 'd0075')
d0080 = Drift(l = 0.08, eid= 'd0080')
d0040 = Drift(l = 0.04, eid= 'd0040')
cl_cfx = Drift(l = 0.1, eid= 'cl_cfx')
d6170 = Drift(l = 6.17, eid= 'd6170')
cl_chy = Drift(l = 0.2, eid= 'cl_chy')
d0170 = Drift(l = 0.17, eid= 'd0170')
d0250 = Drift(l = 0.25, eid= 'd0250')
d0200 = Drift(l = 0.2, eid= 'd0200')
d0025 = Drift(l = 0.025, eid= 'd0025')
d0175 = Drift(l = 0.175, eid= 'd0175')
cl_chx = Drift(l = 0.2, eid= 'cl_chx')
d0490 = Drift(l = 0.49, eid= 'd0490')
cl_cfy = Drift(l = 0.1, eid= 'cl_cfy')
d0180 = Drift(l = 0.18, eid= 'd0180')
d02265 = Drift(l = 0.2265, eid= 'd02265')
d0096 = Drift(l = 0.096, eid= 'd0096')
d01275 = Drift(l = 0.1275, eid= 'd01275')
d00315 = Drift(l = 0.0315, eid= 'd00315')
d00225 = Drift(l = 0.0225, eid= 'd00225')
d0350 = Drift(l = 0.35, eid= 'd0350')
d1550 = Drift(l = 1.55, eid= 'd1550')
d1925 = Drift(l = 1.925, eid= 'd1925')
d0500 = Drift(l = 0.5, eid= 'd0500')
d0125 = Drift(l = 0.125, eid= 'd0125')
d0450 = Drift(l = 0.45, eid= 'd0450')
d1050 = Drift(l = 1.05, eid= 'd1050')
cl_cols = Drift(l = 1.0, eid= 'cl_cols')
d2150 = Drift(l = 2.15, eid= 'd2150')
d0750 = Drift(l = 0.75, eid= 'd0750')
cl_colm = Drift(l = 0.5, eid= 'cl_colm')
d4650 = Drift(l = 4.65, eid= 'd4650')
d0930 = Drift(l = 0.93, eid= 'd0930')
d2500 = Drift(l = 2.5, eid= 'd2500')
d2050 = Drift(l = 2.05, eid= 'd2050')
d0380 = Drift(l = 0.38, eid= 'd0380')
d0675 = Drift(l = 0.675, eid= 'd0675')
d0275 = Drift(l = 0.275, eid= 'd0275')
d0510 = Drift(l = 0.51, eid= 'd0510')
d0700 = Drift(l = 0.7, eid= 'd0700')
d2475 = Drift(l = 2.475, eid= 'd2475')
d1975 = Drift(l = 1.975, eid= 'd1975')
d04342 = Drift(l = 0.4343, eid= 'd04342')
d1975c = Drift(l = 1.5407, eid= 'd1975c')
d0685 = Drift(l = 0.685, eid= 'd0685')
d1700 = Drift(l = 1.7, eid= 'd1700')
d4200 = Drift(l = 4.2, eid= 'd4200')

# quadrupoles 
cl_qf_3 = Quadrupole(l = 0.5, k1 = 0.2259544, eid= 'cl_qf_3')
cl_qh_1 = Quadrupole(l = 1.0, k1 = -0.1687852, eid= 'cl_qh_1')
cl_qh_2 = Quadrupole(l = 1.0, k1 = 0.3287715, eid= 'cl_qh_2')
cl_qfh_4_1 = Quadrupole(l = 0.25, k1 = -0.3202590143, eid= 'cl_qfh_4_1')
cl_qf_4_2 = Quadrupole(l = 0.5, k1 = 0.3202497705, eid= 'cl_qf_4_2')
cl_qf_4_1 = Quadrupole(l = 0.5, k1 = -0.3202590143, eid= 'cl_qf_4_1')
cl_qh_3 = Quadrupole(l = 1.0, k1 = 0.328104, eid= 'cl_qh_3')
cl_qh_4 = Quadrupole(l = 1.0, k1 = -0.2520441, eid= 'cl_qh_4')
cl_qf_5 = Quadrupole(l = 0.5, k1 = 0.3614608, eid= 'cl_qf_5')
cl_qf_6 = Quadrupole(l = 0.5, k1 = -0.0247003, eid= 'cl_qf_6')
cl_qfh_7 = Quadrupole(l = 0.25, k1 = -0.08973852, eid= 'cl_qfh_7')

# bending magnets 
cl_be_1 = Bend(l = 2.50000404725, angle = 0.00623326508226, e1 = 0.00311663254113, e2 = 0.00311663254113, tilt = 1.5707963268, eid= 'cl_be_1')
cl_bl_1 = Bend(l = 0.200000004527, angle = -0.000737026298601, e1 = -0.000368513149301, e2 = -0.000368513149301, tilt = 1.5707963268, eid= 'cl_bl_1')
cl_be_2 = Bend(l = 2.50000391393, angle = -0.00612973992124, e1 = -0.00306486996062, e2 = -0.00306486996062, tilt = 1.5707963268, eid= 'cl_be_2')
cl_bl_2 = Bend(l = 0.200000004378, angle = 0.000724781857982, e1 = 0.000362390928991, e2 = 0.000362390928991, tilt = 1.5707963268, eid= 'cl_bl_2')

# correctors 

# markers 
cl_start = Marker(eid= 'cl_start')
cl_tora = Marker(eid= 'cl_tora')
cl_dcm = Marker(eid= 'cl_dcm')
cl_start_arc = Marker(eid= 'cl_start_arc')
cl_mpbpmi_e = Marker(eid= 'cl_mpbpmi_e')
cl_otrb = Marker(eid= 'cl_otrb')
cl_end = Marker(eid= 'cl_end')

# monitor 
cl_bpma = Monitor(eid= 'cl_bpma')
cl_bpmi_e = Monitor(eid= 'cl_bpmi_e')

# sextupoles 
cl_sa_1 = Sextupole(l = 0.3, k2 = 18.590202663, tilt = 1.5707963268, eid= 'cl_sa_1')
cl_sa_2 = Sextupole(l = 0.3, k2 = -15.6304560049, tilt = 1.5707963268, eid= 'cl_sa_2')
cl_sa_3 = Sextupole(l = 0.3, k2 = 3.01313108964, tilt = 1.5707963268, eid= 'cl_sa_3')
cl_sa_4 = Sextupole(l = 0.3, k2 = -18.590202663, tilt = 1.5707963268, eid= 'cl_sa_4')
cl_sa_5 = Sextupole(l = 0.3, k2 = 15.6304560049, tilt = 1.5707963268, eid= 'cl_sa_5')
cl_sa_6 = Sextupole(l = 0.3, k2 = -3.01313108964, tilt = 1.5707963268, eid= 'cl_sa_6')

# octupole 

# undulator 

# cavity 

# rfcavity 

# Matrices 

# Solenoids 

# lattice 
CL = (cl_start, d70887, cl_tora, d0100, cl_dcm, d0600, d0100,
cl_bpma, d0100, d0050, d0075, cl_qf_3, d0080, d0050, d0040, 
cl_cfx, d0040, d6170, cl_chy, d0170, cl_qh_1, d0250, cl_qh_1, 
d0200, d0025, cl_bpma, d0175, d0200, cl_qh_2, d0250, cl_qh_2, 
d0170, cl_chx, d0490, d0100, d0170, cl_qfh_4_1, cl_start_arc, cl_qfh_4_1, 
d0170, cl_cfy, d0180, cl_sa_1, d02265, d0096, d01275, cl_bpmi_e, 
d0096, cl_mpbpmi_e, d00315, d00225, d0350, d1550, cl_be_1, d1925, 
d0100, d0500, d0100, d0125, cl_qf_4_2, d0170, cl_cfx, d0180, 
cl_sa_2, d0450, cl_bpma, d1050, cl_cols, d2150, cl_bl_1, d0450, 
cl_otrb, d0750, cl_colm, d0450, cl_sa_3, d0125, d0100, d0100, 
d0125, cl_qf_4_1, d0170, cl_cfy, d0180, cl_sa_3, d02265, d0096, 
d01275, cl_bpmi_e, d0096, cl_mpbpmi_e, d00315, d00225, d1550, cl_bl_1, 
d4650, cl_sa_2, d0125, d0100, d0100, d0125, cl_qf_4_2, d0170, 
cl_cfx, d0930, cl_bpma, d1550, cl_be_1, d2500, cl_sa_1, d0125, 
d0100, d0100, d0125, cl_qfh_4_1, cl_qfh_4_1, d0170, cl_cfy, d0180, 
cl_sa_1, d0450, cl_bpma, d2050, cl_be_1, d1925, d0100, d0500, 
d0100, d0125, cl_qf_4_2, d0170, cl_cfx, d0180, cl_sa_2, d0450, 
cl_bpma, d1050, cl_cols, d2150, cl_bl_1, d0450, cl_otrb, d0750, 
cl_colm, d0450, cl_sa_3, d0125, d0100, d0100, d0125, cl_qf_4_1, 
d0170, cl_cfy, d0180, cl_sa_3, d02265, d0096, d01275, cl_bpmi_e, 
d0096, cl_mpbpmi_e, d00315, d00225, d1550, cl_bl_1, d4650, cl_sa_2, 
d0125, d0100, d0100, d0125, cl_qf_4_2, d0170, cl_cfx, d0930, 
cl_bpma, d1550, cl_be_1, d2500, cl_sa_1, d0125, d0100, d0100, 
d0125, cl_qfh_4_1, cl_qfh_4_1, d0170, cl_cfy, d0380, cl_bpma, d0675, 
cl_chx, d0170, cl_qh_3, d0250, cl_qh_3, d0125, d0100, cl_bpma, 
d0100, d0275, cl_qh_4, d0250, cl_qh_4, d0170, cl_chy, d0510, 
d0700, d0125, cl_qf_5, d0170, cl_cfx, d0930, cl_bpma, d2475, 
d0700, d0125, cl_qf_6, d0170, cl_cfy, d0930, cl_bpma, d1975, 
d0200, d0125, cl_qfh_7, cl_qfh_7, d0170, cl_cfx, d0930, cl_bpma, 
d04342, cl_tora, d1975c, d0200, d0125, cl_qf_6, d0170, cl_cfy, 
d0930, cl_bpma, d2475, d0700, d0125, cl_qf_5, d0170, cl_cfx, 
d0380, cl_bpma, d0685, cl_chy, d0170, cl_qh_4, d0250, cl_qh_4, 
d0125, d0100, cl_bpma, d0100, d0275, cl_qh_3, d0250, cl_qh_3, 
d0170, cl_chx, d0500, d0100, d0500, d0100, d0125, cl_qfh_4_1, 
cl_qfh_4_1, d0170, cl_cfy, d0180, cl_sa_4, d0450, cl_bpma, d2050, 
cl_be_2, d1925, d0100, d0500, d0100, d0125, cl_qf_4_2, d0170, 
cl_cfx, d0180, cl_sa_5, d0450, cl_bpma, d1050, cl_cols, d2150, 
cl_bl_2, d0450, cl_otrb, d0750, cl_colm, d0450, cl_sa_6, d0125, 
d0100, d0100, d0125, cl_qf_4_1, d0170, cl_cfy, d0180, cl_sa_6, 
d0450, cl_bpma, d1700, cl_bl_2, d4650, cl_sa_5, d0125, d0100, 
d0100, d0125, cl_qf_4_2, d0170, cl_cfx, d0930, cl_bpma, d1550, 
cl_be_2, d2500, cl_sa_4, d0125, d0100, d0100, d0125, cl_qfh_4_1, 
cl_qfh_4_1, d0170, cl_cfy, d0180, cl_sa_4, d0450, cl_bpma, d2050, 
cl_be_2, d1925, d0100, d0500, d0100, d0125, cl_qf_4_2, d0170, 
cl_cfx, d0180, cl_sa_5, d0450, cl_bpma, d4200, cl_bl_2, d0450, 
cl_otrb, d0750, cl_colm, d0450, cl_sa_6, d0125, d0100, d0100, 
d0125, cl_qf_4_1, d0170, cl_cfy, d0180, cl_sa_6, d02265, d0096, 
d01275, cl_bpmi_e, d0096, cl_mpbpmi_e, d00315, d00225, d1550, cl_bl_2, 
d4650, cl_sa_5, d0125, d0100, d0100, d0125, cl_qf_4_2, d0170, 
cl_cfx, d0930, cl_bpma, d1550, cl_be_2, d2500, cl_sa_4, d0125, 
d0100, cl_bpma, d0100, d0125, cl_qfh_4_1, cl_qfh_4_1, cl_end)