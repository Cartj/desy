'''
main tuning script, LCLS
'''

from desy.flash.lattices.lattice_rf_red import *

from ocelot.utils.mint.mint import Optimizer, Action
from ocelot.utils.mint.flash1_interface_pydoocs import FLASH1MachineInterface, FLASH1DeviceProperties
from ocelot.utils.mint import machine_setup as log
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
opt = Optimizer(mi, dp)
opt.debug = True
opt.logging = True
opt.log_file = 'test.log'
opt.timeout = 1.2


orbit = {}


"""
orbit["correctors"] = ['H3SFELC', 'H4SFELC', 'H10SMATCH', 'D11SMATCH', 'H12SMATCH']
orbit["correctors"] = ['V6_4ORS', 'V7ORS', 'V9ORS', 'V11ORS', 'V12ORS', 'V2SFELC', 'V3SFELC','V4SFELC', 'V6SFELC', 'V7SMATCH', 'V14SMATCH']

bpms = ['13SMATCH','14SMATCH','2UND1','4UND1','5UND1','2UND2','4UND2','5UND2','2UND3','4UND3','5UND3','2UND4',
'4UND4','5UND4','2UND5','4UND5','5UND5','2UND6','4UND6','5UND6']
"""

orbit["correctors"] = [ 'H10SMATCH',  'H12SMATCH', 'V7SMATCH', 'V14SMATCH']
#orbit["correctors"] = ['V7SMATCH', 'V14SMATCH']

#bpms = ['9ACC4', '9ACC5', '11ACC7','15ACC7', '19ACC7',  '13SMATCH','14SMATCH','5UND1','5UND2','5UND3','5UND4','5UND5','5UND6']

#bpms = ['9ACC4', '9ACC5', '11ACC7','15ACC7', '19ACC7', '3ECOL']

bpms = [ '13SMATCH','14SMATCH','5UND1','5UND2','5UND3','5UND4','5UND5','5UND6']
#orbit["correctors"]  =  ['H3DBC3', 'H10ACC4', 'H10ACC5', 'H10ACC6', 'H10ACC7']
orbit["correctors"]  =  ['V3DBC3', 'V10ACC4', 'H10ACC5', 'H10ACC6', 'H10ACC7']
setup = log.MachineSetup()
lat_all = MagneticLattice(lattice)
setup.load_lattice("orbit_acc.txt", lat_all)

orbit["bpms"] = get_dict(lat_all, bpms)

print orbit["bpms"]


seq_min_orb = [Action(func=opt.min_orbit, args=[orbit, 'simplex' ] )]

opt.eval(seq_min_orb)


#opt.eval(seq5 + seq3 + seq6 + seq8 + seq9)