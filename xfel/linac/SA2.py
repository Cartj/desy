from ocelot import *
tws_SA2 = Twiss()
tws_SA2.beta_x = 43.572000000
tws_SA2.beta_y = 21.748300
tws_SA2.alpha_x = 1.398300
tws_SA2.alpha_y = -0.562600
tws_SA2.Dx = 0.014300
tws_SA2.Dxp = -0.000400
tws_SA2.Dy = -0.060100
tws_SA2.E = 17.625300000
tws_SA2.s = 2174.812899




d0058 = Drift(l = 0.058, eid= 'd0058')
d0230 = Drift(l = 0.23, eid= 'd0230')
d000472 = Drift(l = 0.00472, eid= 'd000472')
d0025 = Drift(l = 0.025, eid= 'd0025')
d004778 = Drift(l = 0.04778, eid= 'd004778')
sa2_u00 = Drift(l = 5.0, eid= 'sa2_u00')
d00467 = Drift(l = 0.0467, eid= 'd00467')
d0050 = Drift(l = 0.05, eid= 'd0050')
sa2_absp = Drift(l = 0.05, eid= 'sa2_absp')
d01723 = Drift(l = 0.1723, eid= 'd01723')
d01935 = Drift(l = 0.1935, eid= 'd01935')
d0047 = Drift(l = 0.047, eid= 'd0047')
sa2_bps = Drift(l = 0.23, eid= 'sa2_bps')
sa2_cxa = Drift(l = 0.025, eid= 'sa2_cxa')
sa2_cya = Drift(l = 0.025, eid= 'sa2_cya')
ud0020 = Drift(l = 0.02, eid= 'ud0020')

# quadrupoles 
sa2_qa_1 = Quadrupole(l = 0.1, k1 = -0.6339604, eid= 'sa2_qa_1')
sa2_qa_2 = Quadrupole(l = 0.1, k1 = 0.6354469, eid= 'sa2_qa_2')

# bending magnets 

# correctors 

# markers 
sa2_start = Marker(eid= 'sa2_start')
sa2_end = Marker(eid= 'sa2_end')

# monitor 
sa2_bpme = Monitor(eid= 'sa2_bpme')

# sextupoles 

# octupole 

# undulator 

# cavity 

# rfcavity 

# Matrices 
sa2_u40 = Matrix(l = 4.96, rm11 = 1.0, rm12 = 4.96, rm13 = 0.0, rm21 = 0.0, rm22 = 1.0, rm33 = 0.999626080602, rm34 = 4.95938177118, rm43 = -0.000150764553993, rm44 = 0.999626080602, eid= 'sa2_u40')

# Solenoids 

# lattice 
SA2 = (sa2_start, d0058, d0230, d000472, d0025, d0025, d004778,
sa2_u00, d00467, d0025, d0025, d0050, sa2_absp, d01723, sa2_bpme, 
d01935, sa2_qa_1, d0047, d0058, sa2_bps, d000472, d0025, d0025, 
d004778, sa2_u00, d00467, d0025, d0025, d0050, sa2_absp, d01723, 
sa2_bpme, d01935, sa2_qa_2, d0047, d0058, sa2_bps, d000472, sa2_cxa, 
sa2_cya, d004778, ud0020, sa2_u40, ud0020, d00467, sa2_cxa, sa2_cya, 
d0050, sa2_absp, d01723, sa2_bpme, d01935, sa2_qa_1, d0047, d0058, 
sa2_bps, d000472, sa2_cxa, sa2_cya, d004778, ud0020, sa2_u40, ud0020, 
d00467, sa2_cxa, sa2_cya, d0050, sa2_absp, d01723, sa2_bpme, d01935, 
sa2_qa_2, d0047, d0058, sa2_bps, d000472, sa2_cxa, sa2_cya, d004778, 
ud0020, sa2_u40, ud0020, d00467, sa2_cxa, sa2_cya, d0050, sa2_absp, 
d01723, sa2_bpme, d01935, sa2_qa_1, d0047, d0058, sa2_bps, d000472, 
sa2_cxa, sa2_cya, d004778, ud0020, sa2_u40, ud0020, d00467, sa2_cxa, 
sa2_cya, d0050, sa2_absp, d01723, sa2_bpme, d01935, sa2_qa_2, d0047, 
d0058, sa2_bps, d000472, sa2_cxa, sa2_cya, d004778, ud0020, sa2_u40, 
ud0020, d00467, sa2_cxa, sa2_cya, d0050, sa2_absp, d01723, sa2_bpme, 
d01935, sa2_qa_1, d0047, d0058, sa2_bps, d000472, sa2_cxa, sa2_cya, 
d004778, ud0020, sa2_u40, ud0020, d00467, sa2_cxa, sa2_cya, d0050, 
sa2_absp, d01723, sa2_bpme, d01935, sa2_qa_2, d0047, d0058, sa2_bps, 
d000472, sa2_cxa, sa2_cya, d004778, ud0020, sa2_u40, ud0020, d00467, 
sa2_cxa, sa2_cya, d0050, sa2_absp, d01723, sa2_bpme, d01935, sa2_qa_1, 
d0047, d0058, sa2_bps, d000472, sa2_cxa, sa2_cya, d004778, ud0020, 
sa2_u40, ud0020, d00467, sa2_cxa, sa2_cya, d0050, sa2_absp, d01723, 
sa2_bpme, d01935, sa2_qa_2, d0047, d0058, sa2_bps, d000472, sa2_cxa, 
sa2_cya, d004778, ud0020, sa2_u40, ud0020, d00467, sa2_cxa, sa2_cya, 
d0050, sa2_absp, d01723, sa2_bpme, d01935, sa2_qa_1, d0047, d0058, 
sa2_bps, d000472, sa2_cxa, sa2_cya, d004778, ud0020, sa2_u40, ud0020, 
d00467, sa2_cxa, sa2_cya, d0050, sa2_absp, d01723, sa2_bpme, d01935, 
sa2_qa_2, d0047, d0058, sa2_bps, d000472, sa2_cxa, sa2_cya, d004778, 
ud0020, sa2_u40, ud0020, d00467, sa2_cxa, sa2_cya, d0050, sa2_absp, 
d01723, sa2_bpme, d01935, sa2_qa_1, d0047, d0058, sa2_bps, d000472, 
sa2_cxa, sa2_cya, d004778, ud0020, sa2_u40, ud0020, d00467, sa2_cxa, 
sa2_cya, d0050, sa2_absp, d01723, sa2_bpme, d01935, sa2_qa_2, d0047, 
d0058, sa2_bps, d000472, sa2_cxa, sa2_cya, d004778, ud0020, sa2_u40, 
ud0020, d00467, sa2_cxa, sa2_cya, d0050, sa2_absp, d01723, sa2_bpme, 
d01935, sa2_qa_1, d0047, d0058, sa2_bps, d000472, sa2_cxa, sa2_cya, 
d004778, ud0020, sa2_u40, ud0020, d00467, sa2_cxa, sa2_cya, d0050, 
sa2_absp, d01723, sa2_bpme, d01935, sa2_qa_2, d0047, d0058, sa2_bps, 
d000472, sa2_cxa, sa2_cya, d004778, ud0020, sa2_u40, ud0020, d00467, 
sa2_cxa, sa2_cya, d0050, sa2_absp, d01723, sa2_bpme, d01935, sa2_qa_1, 
d0047, d0058, sa2_bps, d000472, sa2_cxa, sa2_cya, d004778, ud0020, 
sa2_u40, ud0020, d00467, sa2_cxa, sa2_cya, d0050, sa2_absp, d01723, 
sa2_bpme, d01935, sa2_qa_2, d0047, d0058, sa2_bps, d000472, sa2_cxa, 
sa2_cya, d004778, ud0020, sa2_u40, ud0020, d00467, sa2_cxa, sa2_cya, 
d0050, sa2_absp, d01723, sa2_bpme, d01935, sa2_qa_1, d0047, d0058, 
sa2_bps, d000472, sa2_cxa, sa2_cya, d004778, ud0020, sa2_u40, ud0020, 
d00467, sa2_cxa, sa2_cya, d0050, sa2_absp, d01723, sa2_bpme, d01935, 
sa2_qa_2, d0047, d0058, sa2_bps, d000472, sa2_cxa, sa2_cya, d004778, 
ud0020, sa2_u40, ud0020, d00467, sa2_cxa, sa2_cya, d0050, sa2_absp, 
d01723, sa2_bpme, d01935, sa2_qa_1, d0047, d0058, sa2_bps, d000472, 
sa2_cxa, sa2_cya, d004778, ud0020, sa2_u40, ud0020, d00467, sa2_cxa, 
sa2_cya, d0050, sa2_absp, d01723, sa2_bpme, d01935, sa2_qa_2, d0047, 
d0058, sa2_bps, d000472, sa2_cxa, sa2_cya, d004778, ud0020, sa2_u40, 
ud0020, d00467, sa2_cxa, sa2_cya, d0050, sa2_absp, d01723, sa2_bpme, 
d01935, sa2_qa_1, d0047, d0058, sa2_bps, d000472, sa2_cxa, sa2_cya, 
d004778, ud0020, sa2_u40, ud0020, d00467, sa2_cxa, sa2_cya, d0050, 
sa2_absp, d01723, sa2_bpme, d01935, sa2_qa_2, d0047, d0058, sa2_bps, 
d000472, sa2_cxa, sa2_cya, d004778, ud0020, sa2_u40, ud0020, d00467, 
sa2_cxa, sa2_cya, d0050, sa2_absp, d01723, sa2_bpme, d01935, sa2_qa_1, 
d0047, d0058, sa2_bps, d000472, sa2_cxa, sa2_cya, d004778, ud0020, 
sa2_u40, ud0020, d00467, sa2_cxa, sa2_cya, d0050, sa2_absp, d01723, 
sa2_bpme, d01935, sa2_qa_2, d0047, d0058, sa2_bps, d000472, sa2_cxa, 
sa2_cya, d004778, ud0020, sa2_u40, ud0020, d00467, sa2_cxa, sa2_cya, 
d0050, sa2_absp, d01723, sa2_bpme, d01935, sa2_qa_1, d0047, d0058, 
sa2_bps, d000472, sa2_cxa, sa2_cya, d004778, ud0020, sa2_u40, ud0020, 
d00467, sa2_cxa, sa2_cya, d0050, sa2_absp, d01723, sa2_bpme, d01935, 
sa2_qa_2, d0047, d0058, sa2_bps, d000472, sa2_cxa, sa2_cya, d004778, 
ud0020, sa2_u40, ud0020, d00467, sa2_cxa, sa2_cya, d0050, sa2_absp, 
d01723, sa2_bpme, d01935, sa2_qa_1, d0047, d0058, sa2_bps, d000472, 
sa2_cxa, sa2_cya, d004778, ud0020, sa2_u40, ud0020, d00467, sa2_cxa, 
sa2_cya, d0050, sa2_absp, d01723, sa2_bpme, d01935, sa2_qa_2, d0047, 
d0058, sa2_bps, d000472, sa2_cxa, sa2_cya, d004778, ud0020, sa2_u40, 
ud0020, d00467, sa2_cxa, sa2_cya, d0050, sa2_absp, d01723, sa2_bpme, 
d01935, sa2_qa_1, d0047, d0058, sa2_bps, d000472, sa2_cxa, sa2_cya, 
d004778, ud0020, sa2_u40, ud0020, d00467, sa2_cxa, sa2_cya, d0050, 
sa2_absp, d01723, sa2_bpme, d01935, sa2_qa_2, d0047, d0058, sa2_bps, 
d000472, sa2_cxa, sa2_cya, d004778, ud0020, sa2_u40, ud0020, d00467, 
sa2_cxa, sa2_cya, d0050, sa2_absp, d01723, sa2_bpme, d01935, sa2_qa_1, 
d0047, d0058, sa2_bps, d000472, sa2_cxa, sa2_cya, d004778, ud0020, 
sa2_u40, ud0020, d00467, sa2_cxa, sa2_cya, d0050, sa2_absp, d01723, 
sa2_bpme, d01935, sa2_qa_2, d0047, d0058, sa2_bps, d000472, sa2_cxa, 
sa2_cya, d004778, ud0020, sa2_u40, ud0020, d00467, sa2_cxa, sa2_cya, 
d0050, sa2_absp, d01723, sa2_bpme, d01935, sa2_qa_1, d0047, d0058, 
sa2_bps, d000472, sa2_cxa, sa2_cya, d004778, ud0020, sa2_u40, ud0020, 
d00467, sa2_cxa, sa2_cya, d0050, sa2_absp, d01723, sa2_bpme, d01935, 
sa2_qa_2, d0047, d0058, sa2_bps, d000472, sa2_cxa, sa2_cya, d004778, 
ud0020, sa2_u40, ud0020, d00467, sa2_cxa, sa2_cya, d0050, sa2_absp, 
d01723, sa2_bpme, d01935, sa2_qa_1, d0047, sa2_end)