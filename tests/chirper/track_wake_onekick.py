__author__ = 'Igor Zagorodnov'

from ocelot.cpbd.wake3D import *
from ocelot.gui import *

drive='d:/'
Ns=500              # wake sampling
NF=20               # smoothing filter order    

filename=drive+'TEST_DECHIRPER/ASTRA/XFEL01_ideal/LCLS.ast'
p_array, charge_array, z0,gamref = astraBeam2particleArray(filename)


# plot current
bins_start, hist_start = get_current(p_array, charge=charge_array[0], num_bins=200)


ds=2.0
Ps = p_array.particles.view()
Np = len(Ps)/6
Ps.shape = (Np, 6)
wakeFile=drive+'TEST_DECHIRPER/ECHO/Wakes/wake_vert_1m_0.txt'
THv=LoadWakeTable (wakeFile)


Px,Py,Pz,I00=AddTotalWake (Ps[:,0],Ps[:,2],Ps[:,4],charge_array,THv,Ns,NF)
p_array.particles[5::6]=p_array.particles[5::6]+Pz/(p_array.E*1e9)*ds
p_array.particles[3::6]=p_array.particles[3::6]+Py/(p_array.E*1e9)*ds
p_array.particles[1::6]=p_array.particles[1::6]+Px/(p_array.E*1e9)*ds

particleArray2astraBeam(p_array,charge_array,0,'d:/ocelot.ast')

