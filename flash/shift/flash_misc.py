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
def get_dict(lat, bpms):
    dict_bpms = {}
    for elem in lat.sequence:
        if elem.type == "monitor" and elem.mi_id in bpms:
            dict_bpms[elem.mi_id] = {}
            dict_bpms[elem.mi_id]["x"] = elem.x
            dict_bpms[elem.mi_id]["y"] = elem.y
    return dict_bpms

#dp = FLASH1DeviceProperties()

mi = FLASH1MachineInterface()
dp = FLASH1DeviceProperties()
#opt = Optimizer(mi, dp)
opt = Optimizer(TestInterface(), dp)
opt.debug = True
opt.logging = True
opt.log_file = 'test.log'
opt.timeout = 1.2

seq1 = [Action(func=opt.max_sase, args=[ ['H10SMATCH','H12SMATCH'], 'simplex'] ) ]

seq2 = [Action(func=opt.max_sase, args=[ ['V14SMATCH','V7SMATCH'], 'simplex' ] )]
seq3 = [Action(func=opt.max_sase, args=[ ['V14SMATCH','V7SMATCH','H10SMATCH','H12SMATCH'], 'simplex' ] )]

seq4 = [Action(func=opt.max_sase, args=[ ['Q13SMATCH','Q15SMATCH'], 'simplex' ] )]
seq5 = [Action(func=opt.max_sase, args=[ ['H3DBC3','V3DBC3'], 'simplex' ] )]

seq6 = [Action(func=opt.max_sase, args=[ ['H3DBC3','V3DBC3','H10ACC7','V10ACC7'], 'simplex' ] )]

seq7 = [Action(func=opt.max_sase, args=[ ['Q5UND1.3.5','Q5UND2.4'], 'simplex' ] )]

seq8 = [Action(func=opt.max_sase, args=[ ['H3UND1','H3UND3','H3UND4','H3UND5'], 'simplex' ] )]

seq9 = [Action(func=opt.max_sase, args=[ ['H8TCOL','V8TCOL'], 'simplex' ] )]
seq10 = [Action(func=opt.max_sase, args=[ ['H3DBC3'], 'simplex' ] )]


seq0 = [Action(func=opt.max_sase, args=[ ['H10SMATCH','H12SMATCH'], 'cg', {'maxiter':15}] ), 
        Action(func=opt.max_sase, args=[ ['H10SMATCH','H12SMATCH'], 'simplex', {'maxiter':25}] )]


def apply_bump(names, currents, dIs, alpha):
        mi.set_value(names, currents+dIs*alpha)

cors = ['H3DBC3', 'H10ACC4','H9ACC5', 'H10ACC5', 'H9ACC6', 'H10ACC6', 'H10ACC7']
dI =  np.array([-0.0114768844711, -0.183727960466, 0.325959042831, 0.318743893708, 0.15280311903, 0.130996600233, -0.831909116508])
currents = np.array([ -0.0229914523661, 0.0250000003725, 0.985000014305, 0.0, -1.17299997807,  0.0, 0.148000001907])

bump = {"correctors":cors, "dI": dI, "currents":currents}
alpha = 0.1
seq_bump = [Action(func=opt.max_sase_bump, args=[ bump, alpha, 'simplex' ] )]


orbit = {}
orbit["correctors"] = ['H3SFELC', 'H4SFELC', 'H10SMATCH', 'D11SMATCH', 'H12SMATCH']
orbit["correctors"] = ['V6_4ORS', 'V7ORS', 'V9ORS', 'V11ORS', 'V12ORS', 'V2SFELC', 'V3SFELC','V4SFELC', 'V6SFELC', 'V7SMATCH', 'V14SMATCH']

bpms = ['13SMATCH','14SMATCH','2UND1','4UND1','5UND1','2UND2','4UND2','5UND2','2UND3','4UND3','5UND3','2UND4',
'4UND4','5UND4','2UND5','4UND5','5UND5','2UND6','4UND6','5UND6']

setup = log.MachineSetup()
#setup.save_lattice(lat, "init.txt")
lat_all = MagneticLattice(lattice)
setup.load_lattice("init.txt", lat_all)

orbit["bpms"] = get_dict(lat_all, bpms)

print orbit["bpms"]


seq_min_orb = [Action(func=opt.min_orbit, args=[orbit, 'simplex' ] )]

opt.eval(seq_min_orb)
#apply_bump(cors, currents, dI, alpha=0.1)


#opt.eval(seq5 + seq3 + seq6 + seq8 + seq9)
 

