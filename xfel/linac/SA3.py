from ocelot import *
tws_SA3 = Twiss()
tws_SA3.beta_x = 20.021300000
tws_SA3.beta_y = 15.594600
tws_SA3.alpha_x = 1.387000
tws_SA3.alpha_y = -0.983500
tws_SA3.E = 17.625300000
tws_SA3.s = 2777.819245



d0058 = Drift(l = 0.058, eid= 'd0058')
d0230 = Drift(l = 0.23, eid= 'd0230')
d000472 = Drift(l = 0.00472, eid= 'd000472')
d0025 = Drift(l = 0.025, eid= 'd0025')
d004778 = Drift(l = 0.04778, eid= 'd004778')
sa3_u00 = Drift(l = 5.0, eid= 'sa3_u00')
d00467 = Drift(l = 0.0467, eid= 'd00467')
d0050 = Drift(l = 0.05, eid= 'd0050')
sa3_absp = Drift(l = 0.05, eid= 'sa3_absp')
d01723 = Drift(l = 0.1723, eid= 'd01723')
d01935 = Drift(l = 0.1935, eid= 'd01935')
d0047 = Drift(l = 0.047, eid= 'd0047')
sa3_bps = Drift(l = 0.23, eid= 'sa3_bps')
sa3_cxa = Drift(l = 0.025, eid= 'sa3_cxa')
sa3_cya = Drift(l = 0.025, eid= 'sa3_cya')
d0052 = Drift(l = 0.052, eid= 'd0052')

# quadrupoles 
sa3_qa_1 = Quadrupole(l = 0.1, k1 = -1.355866, eid= 'sa3_qa_1')
sa3_qa_2 = Quadrupole(l = 0.1, k1 = 1.358532, eid= 'sa3_qa_2')

# bending magnets 

# correctors 

# markers 
sa3_start = Marker(eid= 'sa3_start')
sa3_end = Marker(eid= 'sa3_end')

# monitor 
sa3_bpme = Monitor(eid= 'sa3_bpme')

# sextupoles 

# octupole 

# undulator 

# cavity 

# rfcavity 

# Matrices 
sa3_u68 = Matrix(l = 4.896, rm11 = 1.0, rm12 = 4.896, rm13 = 0.0, rm21 = 0.0, rm22 = 1.0, rm33 = 0.999302091797, rm34 = 4.89486096081, rm43 = -0.000285060054048, rm44 = 0.999302091797, eid= 'sa3_u68')

# Solenoids 

# lattice 
SA3 = (sa3_start, d0058, d0230, d000472, d0025, d0025, d004778,
sa3_u00, d00467, d0025, d0025, d0050, sa3_absp, d01723, sa3_bpme, 
d01935, sa3_qa_1, d0047, d0058, sa3_bps, d000472, d0025, d0025, 
d004778, sa3_u00, d00467, d0025, d0025, d0050, sa3_absp, d01723, 
sa3_bpme, d01935, sa3_qa_2, d0047, d0058, sa3_bps, d000472, sa3_cxa, 
sa3_cya, d004778, d0052, sa3_u68, d0052, d00467, sa3_cxa, sa3_cya, 
d0050, sa3_absp, d01723, sa3_bpme, d01935, sa3_qa_1, d0047, d0058, 
sa3_bps, d000472, sa3_cxa, sa3_cya, d004778, d0052, sa3_u68, d0052, 
d00467, sa3_cxa, sa3_cya, d0050, sa3_absp, d01723, sa3_bpme, d01935, 
sa3_qa_2, d0047, d0058, sa3_bps, d000472, sa3_cxa, sa3_cya, d004778, 
d0052, sa3_u68, d0052, d00467, sa3_cxa, sa3_cya, d0050, sa3_absp, 
d01723, sa3_bpme, d01935, sa3_qa_1, d0047, d0058, sa3_bps, d000472, 
sa3_cxa, sa3_cya, d004778, d0052, sa3_u68, d0052, d00467, sa3_cxa, 
sa3_cya, d0050, sa3_absp, d01723, sa3_bpme, d01935, sa3_qa_2, d0047, 
d0058, sa3_bps, d000472, sa3_cxa, sa3_cya, d004778, d0052, sa3_u68, 
d0052, d00467, sa3_cxa, sa3_cya, d0050, sa3_absp, d01723, sa3_bpme, 
d01935, sa3_qa_1, d0047, d0058, sa3_bps, d000472, sa3_cxa, sa3_cya, 
d004778, d0052, sa3_u68, d0052, d00467, sa3_cxa, sa3_cya, d0050, 
sa3_absp, d01723, sa3_bpme, d01935, sa3_qa_2, d0047, d0058, sa3_bps, 
d000472, sa3_cxa, sa3_cya, d004778, d0052, sa3_u68, d0052, d00467, 
sa3_cxa, sa3_cya, d0050, sa3_absp, d01723, sa3_bpme, d01935, sa3_qa_1, 
d0047, d0058, sa3_bps, d000472, sa3_cxa, sa3_cya, d004778, d0052, 
sa3_u68, d0052, d00467, sa3_cxa, sa3_cya, d0050, sa3_absp, d01723, 
sa3_bpme, d01935, sa3_qa_2, d0047, d0058, sa3_bps, d000472, sa3_cxa, 
sa3_cya, d004778, d0052, sa3_u68, d0052, d00467, sa3_cxa, sa3_cya, 
d0050, sa3_absp, d01723, sa3_bpme, d01935, sa3_qa_1, d0047, d0058, 
sa3_bps, d000472, sa3_cxa, sa3_cya, d004778, d0052, sa3_u68, d0052, 
d00467, sa3_cxa, sa3_cya, d0050, sa3_absp, d01723, sa3_bpme, d01935, 
sa3_qa_2, d0047, d0058, sa3_bps, d000472, sa3_cxa, sa3_cya, d004778, 
d0052, sa3_u68, d0052, d00467, sa3_cxa, sa3_cya, d0050, sa3_absp, 
d01723, sa3_bpme, d01935, sa3_qa_1, d0047, d0058, sa3_bps, d000472, 
sa3_cxa, sa3_cya, d004778, d0052, sa3_u68, d0052, d00467, sa3_cxa, 
sa3_cya, d0050, sa3_absp, d01723, sa3_bpme, d01935, sa3_qa_2, d0047, 
d0058, sa3_bps, d000472, sa3_cxa, sa3_cya, d004778, d0052, sa3_u68, 
d0052, d00467, sa3_cxa, sa3_cya, d0050, sa3_absp, d01723, sa3_bpme, 
d01935, sa3_qa_1, d0047, d0058, sa3_bps, d000472, sa3_cxa, sa3_cya, 
d004778, d0052, sa3_u68, d0052, d00467, sa3_cxa, sa3_cya, d0050, 
sa3_absp, d01723, sa3_bpme, d01935, sa3_qa_2, d0047, d0058, sa3_bps, 
d000472, sa3_cxa, sa3_cya, d004778, d0052, sa3_u68, d0052, d00467, 
sa3_cxa, sa3_cya, d0050, sa3_absp, d01723, sa3_bpme, d01935, sa3_qa_1, 
d0047, d0058, sa3_bps, d000472, sa3_cxa, sa3_cya, d004778, d0052, 
sa3_u68, d0052, d00467, sa3_cxa, sa3_cya, d0050, sa3_absp, d01723, 
sa3_bpme, d01935, sa3_qa_2, d0047, d0058, sa3_bps, d000472, sa3_cxa, 
sa3_cya, d004778, d0052, sa3_u68, d0052, d00467, sa3_cxa, sa3_cya, 
d0050, sa3_absp, d01723, sa3_bpme, d01935, sa3_qa_1, d0047, d0058, 
sa3_bps, d000472, sa3_cxa, sa3_cya, d004778, d0052, sa3_u68, d0052, 
d00467, sa3_cxa, sa3_cya, d0050, sa3_absp, d01723, sa3_bpme, d01935, 
sa3_qa_2, d0047, d0058, sa3_bps, d000472, sa3_cxa, sa3_cya, d004778, 
d0052, sa3_u68, d0052, d00467, sa3_cxa, sa3_cya, d0050, sa3_absp, 
d01723, sa3_bpme, d01935, sa3_qa_1, d0047, d0058, sa3_bps, d000472, 
sa3_cxa, sa3_cya, d004778, d0052, sa3_u68, d0052, d00467, sa3_cxa, 
sa3_cya, d0050, sa3_absp, d01723, sa3_bpme, d01935, sa3_qa_2, d0047, 
d0058, sa3_bps, d000472, sa3_cxa, sa3_cya, d004778, d0052, sa3_u68, 
d0052, d00467, sa3_cxa, sa3_cya, d0050, sa3_absp, d01723, sa3_bpme, 
d01935, sa3_qa_1, d0047, sa3_end)