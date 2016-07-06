from ocelot import *
tws_SA1 = Twiss()
tws_SA1.beta_x = 39.080100000
tws_SA1.beta_y = 27.292900
tws_SA1.alpha_x = 1.349600
tws_SA1.alpha_y = -1.334700
tws_SA1.E = 17.625300000
tws_SA1.s = 2212.821517


d0058 = Drift(l = 0.058, eid= 'd0058')
d0230 = Drift(l = 0.23, eid= 'd0230')
d000472 = Drift(l = 0.00472, eid= 'd000472')
d0025 = Drift(l = 0.025, eid= 'd0025')
d004778 = Drift(l = 0.04778, eid= 'd004778')
sa1_u00 = Drift(l = 5.0, eid= 'sa1_u00')
d00467 = Drift(l = 0.0467, eid= 'd00467')
d0050 = Drift(l = 0.05, eid= 'd0050')
sa1_absp = Drift(l = 0.05, eid= 'sa1_absp')
d01723 = Drift(l = 0.1723, eid= 'd01723')
d01935 = Drift(l = 0.1935, eid= 'd01935')
d0047 = Drift(l = 0.047, eid= 'd0047')
sa1_bps = Drift(l = 0.23, eid= 'sa1_bps')
sa1_cxa = Drift(l = 0.025, eid= 'sa1_cxa')
sa1_cya = Drift(l = 0.025, eid= 'sa1_cya')
ud0020 = Drift(l = 0.02, eid= 'ud0020')

# quadrupoles 
sa1_qa_1 = Quadrupole(l = 0.1, k1 = -0.6339604, eid= 'sa1_qa_1')
sa1_qa_2 = Quadrupole(l = 0.1, k1 = 0.6354469, eid= 'sa1_qa_2')

# bending magnets 

# correctors 

# markers 
sa1_start = Marker(eid= 'sa1_start')
sa1_end = Marker(eid= 'sa1_end')

# monitor 
sa1_bpme = Monitor(eid= 'sa1_bpme')

# sextupoles 

# octupole 

# undulator 

# cavity 

# rfcavity 

# Matrices 
sa1_u40 = Matrix(l = 4.96, rm11 = 1.0, rm12 = 4.96, rm13 = 0.0, rm21 = 0.0, rm22 = 1.0, rm33 = 0.999626080602, rm34 = 4.95938177118, rm43 = -0.000150764553993, rm44 = 0.999626080602, eid= 'sa1_u40')
#sa1_u40 =  Undulator(lperiod = 0.04, nperiods = 124, Kx = 1., Ky=0, field_file=None, id='sa1_u40')
# Solenoids 

# lattice 
SA1 = (sa1_start, d0058, d0230, d000472, d0025, d0025, d004778,
sa1_u00, d00467, d0025, d0025, d0050, sa1_absp, d01723, sa1_bpme, 
d01935, sa1_qa_1, d0047, d0058, sa1_bps, d000472, d0025, d0025, 
d004778, sa1_u00, d00467, d0025, d0025, d0050, sa1_absp, d01723, 
sa1_bpme, d01935, sa1_qa_2, d0047, d0058, sa1_bps, d000472, sa1_cxa, 
sa1_cya, d004778, ud0020, sa1_u40, ud0020, d00467, sa1_cxa, sa1_cya, 
d0050, sa1_absp, d01723, sa1_bpme, d01935, sa1_qa_1, d0047, d0058, 
sa1_bps, d000472, sa1_cxa, sa1_cya, d004778, ud0020, sa1_u40, ud0020, 
d00467, sa1_cxa, sa1_cya, d0050, sa1_absp, d01723, sa1_bpme, d01935, 
sa1_qa_2, d0047, d0058, sa1_bps, d000472, sa1_cxa, sa1_cya, d004778, 
ud0020, sa1_u40, ud0020, d00467, sa1_cxa, sa1_cya, d0050, sa1_absp, 
d01723, sa1_bpme, d01935, sa1_qa_1, d0047, d0058, sa1_bps, d000472, 
sa1_cxa, sa1_cya, d004778, ud0020, sa1_u40, ud0020, d00467, sa1_cxa, 
sa1_cya, d0050, sa1_absp, d01723, sa1_bpme, d01935, sa1_qa_2, d0047, 
d0058, sa1_bps, d000472, sa1_cxa, sa1_cya, d004778, ud0020, sa1_u40, 
ud0020, d00467, sa1_cxa, sa1_cya, d0050, sa1_absp, d01723, sa1_bpme, 
d01935, sa1_qa_1, d0047, d0058, sa1_bps, d000472, sa1_cxa, sa1_cya, 
d004778, ud0020, sa1_u40, ud0020, d00467, sa1_cxa, sa1_cya, d0050, 
sa1_absp, d01723, sa1_bpme, d01935, sa1_qa_2, d0047, d0058, sa1_bps, 
d000472, sa1_cxa, sa1_cya, d004778, ud0020, sa1_u40, ud0020, d00467, 
sa1_cxa, sa1_cya, d0050, sa1_absp, d01723, sa1_bpme, d01935, sa1_qa_1, 
d0047, d0058, sa1_bps, d000472, sa1_cxa, sa1_cya, d004778, ud0020, 
sa1_u40, ud0020, d00467, sa1_cxa, sa1_cya, d0050, sa1_absp, d01723, 
sa1_bpme, d01935, sa1_qa_2, d0047, d0058, sa1_bps, d000472, sa1_cxa, 
sa1_cya, d004778, ud0020, sa1_u40, ud0020, d00467, sa1_cxa, sa1_cya, 
d0050, sa1_absp, d01723, sa1_bpme, d01935, sa1_qa_1, d0047, d0058, 
sa1_bps, d000472, sa1_cxa, sa1_cya, d004778, ud0020, sa1_u40, ud0020, 
d00467, sa1_cxa, sa1_cya, d0050, sa1_absp, d01723, sa1_bpme, d01935, 
sa1_qa_2, d0047, d0058, sa1_bps, d000472, sa1_cxa, sa1_cya, d004778, 
ud0020, sa1_u40, ud0020, d00467, sa1_cxa, sa1_cya, d0050, sa1_absp, 
d01723, sa1_bpme, d01935, sa1_qa_1, d0047, d0058, sa1_bps, d000472, 
sa1_cxa, sa1_cya, d004778, ud0020, sa1_u40, ud0020, d00467, sa1_cxa, 
sa1_cya, d0050, sa1_absp, d01723, sa1_bpme, d01935, sa1_qa_2, d0047, 
d0058, sa1_bps, d000472, sa1_cxa, sa1_cya, d004778, ud0020, sa1_u40, 
ud0020, d00467, sa1_cxa, sa1_cya, d0050, sa1_absp, d01723, sa1_bpme, 
d01935, sa1_qa_1, d0047, d0058, sa1_bps, d000472, sa1_cxa, sa1_cya, 
d004778, ud0020, sa1_u40, ud0020, d00467, sa1_cxa, sa1_cya, d0050, 
sa1_absp, d01723, sa1_bpme, d01935, sa1_qa_2, d0047, d0058, sa1_bps, 
d000472, sa1_cxa, sa1_cya, d004778, ud0020, sa1_u40, ud0020, d00467, 
sa1_cxa, sa1_cya, d0050, sa1_absp, d01723, sa1_bpme, d01935, sa1_qa_1, 
d0047, d0058, sa1_bps, d000472, sa1_cxa, sa1_cya, d004778, ud0020, 
sa1_u40, ud0020, d00467, sa1_cxa, sa1_cya, d0050, sa1_absp, d01723, 
sa1_bpme, d01935, sa1_qa_2, d0047, d0058, sa1_bps, d000472, sa1_cxa, 
sa1_cya, d004778, ud0020, sa1_u40, ud0020, d00467, sa1_cxa, sa1_cya, 
d0050, sa1_absp, d01723, sa1_bpme, d01935, sa1_qa_1, d0047, d0058, 
sa1_bps, d000472, sa1_cxa, sa1_cya, d004778, ud0020, sa1_u40, ud0020, 
d00467, sa1_cxa, sa1_cya, d0050, sa1_absp, d01723, sa1_bpme, d01935, 
sa1_qa_2, d0047, d0058, sa1_bps, d000472, sa1_cxa, sa1_cya, d004778, 
ud0020, sa1_u40, ud0020, d00467, sa1_cxa, sa1_cya, d0050, sa1_absp, 
d01723, sa1_bpme, d01935, sa1_qa_1, d0047, d0058, sa1_bps, d000472, 
sa1_cxa, sa1_cya, d004778, ud0020, sa1_u40, ud0020, d00467, sa1_cxa, 
sa1_cya, d0050, sa1_absp, d01723, sa1_bpme, d01935, sa1_qa_2, d0047, 
d0058, sa1_bps, d000472, sa1_cxa, sa1_cya, d004778, ud0020, sa1_u40, 
ud0020, d00467, sa1_cxa, sa1_cya, d0050, sa1_absp, d01723, sa1_bpme, 
d01935, sa1_qa_1, d0047, d0058, sa1_bps, d000472, sa1_cxa, sa1_cya, 
d004778, ud0020, sa1_u40, ud0020, d00467, sa1_cxa, sa1_cya, d0050, 
sa1_absp, d01723, sa1_bpme, d01935, sa1_qa_2, d0047, d0058, sa1_bps, 
d000472, sa1_cxa, sa1_cya, d004778, ud0020, sa1_u40, ud0020, d00467, 
sa1_cxa, sa1_cya, d0050, sa1_absp, d01723, sa1_bpme, d01935, sa1_qa_1, 
d0047, d0058, sa1_bps, d000472, sa1_cxa, sa1_cya, d004778, ud0020, 
sa1_u40, ud0020, d00467, sa1_cxa, sa1_cya, d0050, sa1_absp, d01723, 
sa1_bpme, d01935, sa1_qa_2, d0047, d0058, sa1_bps, d000472, sa1_cxa, 
sa1_cya, d004778, ud0020, sa1_u40, ud0020, d00467, sa1_cxa, sa1_cya, 
d0050, sa1_absp, d01723, sa1_bpme, d01935, sa1_qa_1, d0047, d0058, 
sa1_bps, d000472, sa1_cxa, sa1_cya, d004778, ud0020, sa1_u40, ud0020, 
d00467, sa1_cxa, sa1_cya, d0050, sa1_absp, d01723, sa1_bpme, d01935, 
sa1_qa_2, d0047, d0058, sa1_bps, d000472, sa1_cxa, sa1_cya, d004778, 
ud0020, sa1_u40, ud0020, d00467, sa1_cxa, sa1_cya, d0050, sa1_absp, 
d01723, sa1_bpme, d01935, sa1_qa_1, d0047, d0058, sa1_bps, d000472, 
sa1_cxa, sa1_cya, d004778, ud0020, sa1_u40, ud0020, d00467, sa1_cxa, 
sa1_cya, d0050, sa1_absp, d01723, sa1_bpme, d01935, sa1_qa_2, d0047, 
d0058, sa1_bps, d000472, sa1_cxa, sa1_cya, d004778, ud0020, sa1_u40, 
ud0020, d00467, sa1_cxa, sa1_cya, d0050, sa1_absp, d01723, sa1_bpme, 
d01935, sa1_qa_1, d0047, d0058, sa1_bps, d000472, sa1_cxa, sa1_cya, 
d004778, ud0020, sa1_u40, ud0020, d00467, sa1_cxa, sa1_cya, d0050, 
sa1_absp, d01723, sa1_bpme, d01935, sa1_qa_2, d0047, d0058, sa1_bps, 
d000472, sa1_cxa, sa1_cya, d004778, ud0020, sa1_u40, ud0020, d00467, 
sa1_cxa, sa1_cya, d0050, sa1_absp, d01723, sa1_bpme, d01935, sa1_qa_1, 
d0047, d0058, sa1_bps, d000472, sa1_cxa, sa1_cya, d004778, ud0020, 
sa1_u40, ud0020, d00467, sa1_cxa, sa1_cya, d0050, sa1_absp, d01723, 
sa1_bpme, d01935, sa1_qa_2, d0047, d0058, sa1_bps, d000472, sa1_cxa, 
sa1_cya, d004778, ud0020, sa1_u40, ud0020, d00467, sa1_cxa, sa1_cya, 
d0050, sa1_absp, d01723, sa1_bpme, d01935, sa1_qa_1, d0047, d0058, 
sa1_bps, d000472, sa1_cxa, sa1_cya, d004778, ud0020, sa1_u40, ud0020, 
d00467, sa1_cxa, sa1_cya, d0050, sa1_absp, d01723, sa1_bpme, d01935, 
sa1_qa_2, d0047, d0058, sa1_bps, d000472, sa1_cxa, sa1_cya, d004778, 
ud0020, sa1_u40, ud0020, d00467, sa1_cxa, sa1_cya, d0050, sa1_absp, 
d01723, sa1_bpme, d01935, sa1_qa_1, d0047, sa1_end)