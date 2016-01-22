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


"""
cors =  ['H3DBC3', 'H10ACC4', 'H9ACC5', 'H10ACC5', 'H9ACC6', 'H10ACC6', 'H10ACC7', 'H18ACC7',
          'H1TCOL', 'H4TCOL', 'H8TCOL', 'H2ECOL', 'H4ECOL', 'H6ECOL', 'H5ORS', 'H3SFELC', 'H4SFELC', 'H10SMATCH', 'H12SMATCH']

currents =  [-0.022991452366113663, 0.02500000037252903, 0.9850000143051147, 0.0, -1.1729999780654907,
             0.0, 0.14800000190734863, 0.07863248139619827, 0.004273504484444857, -0.01452991459518671,
             0.017094017937779427, 0.0033333334140479565, 0.0, 0.0, 0.01598290540277958,
             -0.14803418517112732, -0.06324786692857742, -2.0529913902282715, -1.8897435665130615]

dI =  [-0.011477471012558966, -0.18382715319330656, 0.32616427362591532, 0.31882501481096603,
       0.14852084774739041, 0.12826640944998005, -0.77071195563058825, -0.010138365392752419, 0.013011027816962159,
       0.0056200469861475352, -0.0037601804301915279, -0.01245468039908122, 0.028415379814228935,
       -0.011652730436574162, -0.0013284012287226852, 0.0030047656426212474, -0.014667082706999365,
       -0.029759521372007252, 0.011730666513869455]
"""


cors = ['H3DBC3', 'H10ACC4','H9ACC5', 'H10ACC5', 'H9ACC6', 'H10ACC6', 'H10ACC7']

dI =  np.array([-0.0114768844711, -0.183727960466, 0.325959042831, 0.318743893708, 0.15280311903, 0.130996600233, -0.831909116508])

currents = np.array([ -0.0229914523661, 0.0250000003725, 0.985000014305, 0.0, -1.17299997807,  0.0, 0.148000001907])



bump = {"correctors":cors, "dI": dI, "currents":currents}

alpha = 0.1

seq_bump = [Action(func=opt.max_sase_bump, args=[ bump, alpha, 'simplex' ] )]

opt.eval(seq_bump)
#apply_bump(cors, currents, dI, alpha=0.1)


#opt.eval(seq5 + seq3 + seq6 + seq8 + seq9)
 

