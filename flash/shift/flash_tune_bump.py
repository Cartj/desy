'''
main tuning script, LCLS
'''

from lattice_rf_red import *
import ocelot
from pylab import *
import numpy as np

from ocelot.utils.mint.mint import Optimizer, Action, TestInterface
from ocelot.utils.mint.flash1_interface_pydoocs import FLASH1MachineInterface, FLASH1DeviceProperties
import machine_setup as log
#from flash1_interface import FLASH1DeviceProperties


#import json

mi = FLASH1MachineInterface()
dp = FLASH1DeviceProperties()
#opt = Optimizer(mi, dp)
opt = Optimizer(TestInterface(), dp)
opt.debug = True
opt.logging = True
opt.log_file = 'test.log'
opt.timeout = 1.2



def apply_bump(names, currents, dIs, alpha):
    mi.set_value(names, currents+dIs*alpha)



cors = ['H3DBC3', 'H10ACC4','H9ACC5', 'H10ACC5', 'H9ACC6', 'H10ACC6', 'H10ACC7']

dI =  np.array([-0.0114768844711, -0.183727960466, 0.325959042831, 0.318743893708, 0.15280311903, 0.130996600233, -0.831909116508])

currents = np.array([ -0.0229914523661, 0.0250000003725, 0.985000014305, 0.0, -1.17299997807,  0.0, 0.148000001907])



bump = {"correctors":cors, "dI": dI, "currents":currents}

alpha = 0.1

seq_bump = [Action(func=opt.max_sase_bump, args=[ bump, alpha, 'simplex' ] )]

opt.eval(seq_bump)
#apply_bump(cors, currents, dI, alpha=0.1)


#opt.eval(seq5 + seq3 + seq6 + seq8 + seq9)
 

