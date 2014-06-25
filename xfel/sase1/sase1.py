'''
input deck for XFEL SASE3 beamline
'''

from xframework.cpbd.elements import *
from xframework.cpbd.beam import *
import numpy as np



und = Undulator (nperiods=125,lperiod=0.040,Kx=0.0, id = "und"); voodoo=0.69

d = Drift (l=1.0, id = "d")

d1 = Drift (l=0.55, id = "d1")
d2 = Drift (l=0.45, id = "d2")
d3 = Drift (l=0.27, id = "d0.05nm3")

b1 = RBend (l=0.0575, angle=0.0, id = "b1")
b2 = RBend (l=0.0575, angle=-0.0, id = "b2")

#psu=(b1,b2,b2,b1,d3)
psu= Drift (l=b1.l*2 + b2.l*2 + d3.l, id = "d1")

qf = Quadrupole (l=0.1, id = "qf")
qd = Quadrupole (l=0.1, id = "qd")
qfh = Quadrupole (l=0.05, id = "qf")
qdh = Quadrupole (l=0.05, id = "qf")

cell_ps = (und, d2, qf, psu, und, d2, qd, psu)

sase1 = (und, d2, qd, psu) + 17*cell_ps
sase1_cell = (und, d2, qf, psu, und)
def sase1_segment(n=0): return (und, d2, qd, psu) + n*cell_ps

# for matching
extra_fodo = (und, d2, qdh)
l_fodo = qf.l / 2 + (b1.l + b2.l + b2.l + b1.l + d3.l) + und.l + d2.l + qf.l / 2 

# uncomment this for simplified SR calculation
## und = Undulator (nperiods=125*35,lperiod=0.040,Kx=1.9657, id = "und")
## sase1=(und)


# example settings 28m beta, 0.05nm wavelength
und.Kx = 1.9657
qf.k1 = 0.7181242
qd.k1 = -0.7181242
qfh.k1 = 0.7181242
qdh.k1 = -0.7181242
b1.angle = 1.7926311e-5
b2.angle =-1.7926311e-5


# setting xxxnm wavelength
#und.Kx = 1.8

und.Kx = 2.395

beam = Beam()
beam.E = 14.0
beam.sigma_E = 0.002
beam.emit_xn = 0.4e-6 
beam.emit_yn = 0.4e-6 
beam.gamma_rel = beam.E / (0.511e-3)
beam.emit_x = beam.emit_xn / beam.gamma_rel
beam.emit_y = beam.emit_yn / beam.gamma_rel
beam.beta_x = 33.7
beam.beta_y = 23.218
beam.alpha_x = 1.219
beam.alpha_y = -0.842

beam.tpulse = 80    # electron bunch length in fs (rms)
beam.C = 1.0        # bunch charge (nC)
beam.I = 1.0e-9 * beam.C / ( np.sqrt(2*pi) * beam.tpulse * 1.e-15 ) 

#beam.emit = {0.02: [0.32e-6,0.32e-6], 0.1: [0.39e-6,0.39e-6], 0.25: [0.6e-6,0.6e-6], 0.5: [0.7e-6,0.7e-6], 1.0: [0.97e-6,0.97e-6]}
beam.emit = {0.02: [0.2e-6,0.18e-6], 0.1: [0.32e-6,0.27e-6], 0.25: [0.4e-6,0.36e-6], 0.5: [0.45e-6,0.42e-6], 1.0: [0.8e-6,0.84e-6]}

