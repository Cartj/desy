'''
main tuning script, LCLS
'''

from ocelot.utils.mint.mint import Optimizer, Action
from ocelot.utils.mint.flash1_interface_pydoocs3 import FLASH1MachineInterface, FLASH1DeviceProperties, TestInterface
#from flash1_interface import FLASH1DeviceProperties


#import json


mi = FLASH1MachineInterface()
mi = TestInterface()
dp = FLASH1DeviceProperties()
#opt = Optimizer(mi, dp)
opt = Optimizer(mi, dp)
opt.debug = True
opt.logging = True
opt.log_file = 'test.log'
opt.timeout = 1.2

seq1 = [Action(func=opt.max_sase, args=[ ['H10SMATCH','H12SMATCH'], 'simplex'] ) ]

seq2 = [Action(func=opt.max_sase, args=[ ['V14SMATCH','V7SMATCH'], 'simplex' ] )]
seq3 = [Action(func=opt.max_sase, args=[ ['V14SMATCH','V7SMATCH','H10SMATCH','H12SMATCH'], 'simplex' , {'maxiter':60}] )]

seq4 = [Action(func=opt.max_sase, args=[ ['Q13SMATCH','Q15SMATCH'], 'simplex' ] )]
seq5 = [Action(func=opt.max_sase, args=[ ['H3DBC3','V3DBC3'], 'simplex' ] )]

seq6 = [Action(func=opt.max_sase, args=[ ['H3DBC3','V3DBC3','H10ACC7','V10ACC7'], 'simplex' ] )]

seq7 = [Action(func=opt.max_sase, args=[ ['Q5UND1.3.5','Q5UND2.4'], 'simplex' ] )]

seq8 = [Action(func=opt.max_sase, args=[ ['H3UND1','H3UND3','H3UND4','H3UND5'], 'simplex' ] )]

seq9 = [Action(func=opt.max_sase, args=[ ['H8TCOL','V8TCOL'], 'simplex' ] )]
seq10 = [Action(func=opt.max_sase, args=[ ['H3DBC3'], 'simplex' ] )]


seq0 = [Action(func=opt.max_sase, args=[ ['H10SMATCH','H12SMATCH'], 'cg', {'maxiter':15}] ), 
        Action(func=opt.max_sase, args=[ ['H10SMATCH','H12SMATCH'], 'simplex', {'maxiter':25}] )]
cors =  ['H3DBC3', 'H10ACC4', 'H10ACC5', 'H10ACC6', 'H10ACC7']
seq12 = [Action(func=opt.max_sase, args=[ ['H3DBC3', 'H10ACC4', 'H10ACC5', 'H10ACC6', 'H10ACC7'], 'simplex' ] )]

seq13 = [Action(func=opt.max_sase, args=[ ['V3DBC3', 'V10ACC4', 'V10ACC5', 'V10ACC7'], 'simplex' ] )]
opt.eval(seq4)
#apply_bump(cors, currents, dI, alpha=0.1)

#opt.eval(seq5 + seq3 + seq6 + seq8 + seq9)

