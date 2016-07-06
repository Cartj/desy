'''
main tuning script, LCLS
'''

from desy.flash.lattices.lattice_rf_red import *

from ocelot.mint.mint import Optimizer, Action
from ocelot.mint.flash1_interface import FLASH1MachineInterface, FLASH1DeviceProperties
from ocelot.mint import machine_setup as log
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


horizantal = [#'H3DBC3',
              #'H10ACC4', 'H10ACC5', 'H10ACC6', 'H10ACC7', 'H18ACC7',
              #'H1TCOL', 'H4TCOL',
              'H8TCOL',
              #'H2ECOL', 'H4ECOL', 'H6ECOL',                     # in dogleg
              'H5ORS', 'H10ORS',
# 'H3SFELC', 'H4SFELC',
              'H10SMATCH', 'H12SMATCH'
              ]
hcor_und = ["H3UND1", "H3UND2", "H3UND3", "H3UND4", "H3UND5", "H3UND6"]

vertical = [#'V3DBC3',
            #'V10ACC4', 'V10ACC5', 'V10ACC6', 'V10ACC7',
            #'V1TCOL', 'V2TCOL', 'V4TCOL',
            'V8TCOL',
            #'V4ECOL',                                                  #in dogleg
            #'V5ORS', 'V6.4ORS', 'V7ORS', 
'V1ORS',
#'V9ORS', 'V11ORS', 
'V12ORS',
           # 'V2SFELC', 'V4SFELC', 'V6SFELC',
            'V7SMATCH', 'V14SMATCH'
            ]

bpms = [#'1DBC3', '3DBC3', '9ACC4', '9ACC5', '9ACC6', '11ACC7', '15ACC7', '19ACC7',
        #'1TCOL', '6TCOL', '8TCOL',
        #'3ECOL', '5ECOL',                              # dogleg
        '2ORS', '7ORS', '9ORS', '12ORS',
       # '1SFUND2', 
'1SFUND3', '1SFUND4', '1SFELC', '1SMATCH', '6SMATCH',
        '13SMATCH', '14SMATCH', '5UND1', '5UND2', '5UND3', '5UND4', '5UND5', '5UND6'  #undulator section
        ]






#bpms = ['9ACC4', '9ACC5', '11ACC7','15ACC7', '19ACC7', '3ECOL']

#bpms = [ '13SMATCH','14SMATCH','5UND1','5UND2','5UND3','5UND4','5UND5','5UND6']
#orbit["correctors"]  =  ['H3DBC3', 'H10ACC4', 'H10ACC5', 'H10ACC6', 'H10ACC7']
orbit["correctors"]  =  horizantal + vertical #['V3DBC3', 'V10ACC4', 'H10ACC5', 'H10ACC6', 'H10ACC7']

lat_all = MagneticLattice(lattice)
setup = log.MachineSetup(lat_all, mi, dp)
setup.load_lattice("new_ref_orbit.txt", lat_all)

orbit["bpms"] = get_dict(lat_all, bpms)

print( orbit["bpms"])


seq_min_orb = [Action(func=opt.min_orbit, args=[orbit, 'simplex' ] )]

opt.eval(seq_min_orb)


#opt.eval(seq5 + seq3 + seq6 + seq8 + seq9)
