'''
machine interface
includes online optimizer, response measurement and other stuff
'''
#try:
#    # in server "doocsdev12" set environment
#    #  $ export PYTHONPATH=/home/ttflinac/user/python-2.7/Debian/
#    import doocs
#except:
#    print 'error importing doocs library'
import re
#from pylab import *
import converter
from ocelot.cpbd.orbit_correction import *

class FLASH1VirtualInterface():
    def __init__(self, lattice, gun_energy=0):
        
        self.debug = False
        
        self.blm_names = ['14L.SMATCH','14R.SMATCH',
                          '1L.UND1', '1R.UND1',
                          '1L.UND2', '1R.UND2', 
                          '1L.UND3', '1R.UND3', 
                          '1L.UND4', '1R.UND4',
                          '1L.UND5', '1R.UND5',
                          '1L.UND6', '1R.UND6',
                          '10SMATCH','3SDUMP']
        self.lattice = lattice
        self.def_mi_id()
        self.gun_energy = gun_energy
        self.insert_misalignment()
        self.Orbit = Orbit(self.lattice)


    def insert_misalignment(self):
        for elem in self.lattice.sequence:
            if elem.type in ["bend", "rbend", "sbend"]:
                elem.dx = tgauss(0, sigma=0.0001 ,trunc=3)
                elem.dy = tgauss(0, sigma=0.0001 ,trunc=3)
                elem.dtilt = tgauss(0, sigma=0.0001,trunc=3)
            elif elem.type == "quadrupole":
                elem.dx = tgauss(0, sigma=0.0001,trunc=3)
                elem.dy = tgauss(0, sigma=0.0001,trunc=3)
                elem.dtilt = tgauss(0, sigma=0.0001,trunc=3)
            elif elem.type == "cavity":
                elem.dx = tgauss(0, sigma=0.0001,trunc=3)
                elem.dy = tgauss(0, sigma=0.0001,trunc=3)
            if elem.id in ["V2DBC2","V4DBC2", "V6DBC2", "V10DBC2" ]:
                elem.type = "drift"
        self.lattice.update_transfer_maps()

    def def_mi_id(self):
        for elem in self.lattice.sequence:
            if elem.type in ["hcor", "vcor"]:
                try:
                    elem.mi_id
                except:
                    name = elem.id
                    name = name.replace("_", ".")
                    elem.mi_id = name
            elif elem.type == "quadrupole":

                #print(name)
                try:
                    elem.mi_id
                except:
                    name = elem.id
                    #if "_U" in name:
                    #    continue
                    name = name.replace("_U", "")
                    name = name.replace("_D", "")
                    name = name.replace("_", ".")
                    elem.mi_id = name
            elif elem.type == "monitor":
                name = elem.id.replace("BPM", "")
                elem.mi_id = name

    def init_corrector_vals(self, correctors):


        vals = [0.0]*len(correctors)#np.zeros(len(correctors))
        for i in range(len(correctors)):
            I = 0.
            for elem in self.lattice.sequence:
                if elem.type in ["hcor", "vcor"] and correctors[i] == elem.mi_id:
                    #print correctors, elem.mi_id, elem.dev_type
                    I = converter.tpk2i(elem.dev_type, elem.E, elem.angle/0.001)
                    if I == None:
                        I = 0.
            vals[i] = I
        return vals

    def get_cavity_info(self, cavs):
        ampls = [0.0]*len(cavs)#np.zeros(len(correctors))
        phases = [0.0]*len(cavs)#np.zeros(len(correctors))
        #print cavs
        for i in range(len(cavs)):
            ampl = 0.
            phase = 0.
            for elem in self.lattice.sequence:
                if elem.type == "cavity":
                    name = elem.id.split("_")
                    elem.mi_id = name[-2] + "." + name[-1]

                    if cavs[i] == elem.mi_id:
                        ampl += elem.v
                        #print ampl, elem.v
                        phase = elem.phi
                        if "ACC39" in cavs[i]:
                            phase -= 180
            #print(ampl_channel)
            #print(phase_channel)
            ampls[i] = ampl*1000.
            #print ampl
            phases[i] = phase
        return ampls, phases

    def get_bpms_xy(self, bpms):
        try:
            self.Orbit.read_obit_true
        except:
            self.Orbit.read_virtual_orbit(self.lattice, Particle(E=self.gun_energy))
            self.Orbit.read_obit_true = True
        X = [0.0]*len(bpms)#np.zeros(len(correctors))
        Y = [0.0]*len(bpms)
        for i in range(len(bpms)):
            x = 0.
            y = 0.

            for bpm in self.Orbit.bpms:
                #for elem in self.lattice.sequence:
                name = bpm.id.replace("BPM", "")
                if bpms[i] == name:
                    x = bpm.x
                    y = bpm.y
                    #if elem.type == "monitor" and bpms[i] == elem.mi_id:
                    #x = elem.dx
                    #y = elem.dy

            X[i] = x
            Y[i] = y
        return X, Y

    def get_quads_current(self, quads):
        vals = [0.0]*len(quads)#np.zeros(len(correctors))
        for i in range(len(quads)):
            I = 0.
            for elem in self.lattice.sequence:
                if elem.type == "quadrupole" and quads[i] == elem.mi_id:
                    I = converter.tpk2i(elem.dev_type, elem.E, elem.k1)*(1.+np.random.randn(1)*0.001)
            vals[i] = I
        return vals

    def get_gun_energy(self):
        return 0.005

    def get_alarms(self):
        alarm_vals = np.zeros(len(self.blm_names))
        for i in xrange(len(self.blm_names)):
            blm_channel = 'TTF2.DIAG/BLM/'+self.blm_names[i]+'/CH00.TD'
            blm_alarm_ch  = ('TTF2.DIAG/BLM/'+self.blm_names[i]).replace('BLM', 'BLM.ALARM') + '/THRFHI'
            if (self.debug): print 'reading alarm channel', blm_alarm_ch
            alarm_val = doocs.read(blm_alarm_ch) * 1.25e-3 # alarm thr. in Volts
            if (self.debug): print 'alarm:', alarm_val
    
            h = np.array(doocs.read(blm_channel))
    
            alarm_vals[i] = np.max( np.abs(h) ) / alarm_val 
            
        return alarm_vals

    def get_sase(self, detector='gmd_default'):
        
        if detector == 'mcp':
            # incorrect
            return doocs.read('TTF2.DIAG/MCP.HV/MCP.HV1/HV_CURRENT')
            #return np.abs( np.mean(h) )
        if detector == 'gmd_fl1_slow':
            return doocs.read('TTF2.FEL/BKR.FLASH.STATE/BKR.FLASH.STATE/SLOW.INTENSITY' )

        # default 'BKR' gmd
        h = np.array(doocs.read('TTF2.FEL/BKR.FLASH.STATE/BKR.FLASH.STATE/ENERGY.CLIP.SPECT'))
        val = np.mean(h)
        return val



    def get_sase_pos(self):

        x1 = doocs.read('TTF2.FEL/GMDPOSMON/TUNNEL/IX.POS')
        y1 = doocs.read('TTF2.FEL/GMDPOSMON/TUNNEL/IY.POS')

        x2 = doocs.read('TTF2.FEL/GMDPOSMON/BDA/IX.POS')
        y2 = doocs.read('TTF2.FEL/GMDPOSMON/BDA/IY.POS')
    
        return [ (x1,y1), (x2,y2) ] 

    def get_spectrum(self, f=None, detector='tunnel_default'):

        f_min = 13.0 # spectrum window (nm). TODO: replace with readout
        f_max = 14.0
        
        spec = np.array(doocs.read('TTF2.EXP/PBD.PHOTONWL.ML/WAVE_LENGTH/VAL.TD'))
    
        if f == None:
            f = np.linspace(f_min, f_max, len(spec))
    
        return f, spec
 
    def get_value(self, device_name):
        ch = 'TTF2.MAGNETS/STEERER/' + device_name + '/PS.RBV'
        return doocs.read(ch)
    
    def set_value(self, device_name, val):
        ch = 'TTF2.MAGNETS/STEERER/' + device_name + '/PS'
        return dcs.set_device_val(ch, val)
 
 
class FLASH1VirtualProperties:
    def __init__(self):
        self.patterns = {}
        self.limits = {}
        self.patterns['launch_steerer'] = re.compile('[HV][0-9]+SMATCH')
        self.limits['launch_steerer'] = [-4,4]
        
        self.patterns['intra_steerer'] = re.compile('H3UND[0-9]')
        self.limits['intra_steerer'] = [-5.0,-2.0]
        
        self.patterns['QF'] = re.compile('Q5UND1.3.5')
        self.limits['QF'] = [4,9]
        
        self.patterns['QD'] = re.compile('Q5UND2.4')
        self.limits['QD'] = [-9,-4]
        
        self.patterns['Q13MATCH'] = re.compile('Q13SMATCH')
        self.limits['Q13MATCH'] = [47.0,49.0]

        self.patterns['Q15MATCH'] = re.compile('Q15SMATCH')
        self.limits['Q15MATCH'] = [-16.0,-14.0]

        self.patterns['H3DBC3'] = re.compile('H3DBC3')
        self.limits['H3DBC3'] = [-0.15,-0.07]

        self.patterns['V3DBC3'] = re.compile('V3DBC3')
        self.limits['V3DBC3'] = [0.046,0.106]

        self.patterns['H10ACC7'] = re.compile('H10ACC7')
        self.limits['H10ACC7'] = [0.8,1.3]

        self.patterns['V10ACC7'] = re.compile('V10ACC7')
        self.limits['V10ACC7'] = [-2.6,-1.8]

        self.patterns['H8TCOL'] = re.compile('H8TCOL')
        self.limits['H8TCOL'] = [0.02,0.06]

        self.patterns['V8TCOL'] = re.compile('V8TCOL')
        self.limits['V8TCOL'] = [0.09,0.15]
        
        
    def get_limits(self, device):
        for k in self.patterns.keys():
            #print 'testing', k
            if self.patterns[k].match(device) != None:
                return self.limits[k]
        return [-0.11, -0.08]   

    def get_polarity(self, quads):
        vals = [0.0]*len(quads)#np.zeros(len(correctors))
        for i in range(len(quads)):
            #mag_channel = 'TTF2.MAGNETS/QUAD/' + quads[i]# + '/PS'
            vals[i] = 1
        return vals

    def get_type_magnet(self, quads):
        vals = [0.0]*len(quads)#np.zeros(len(correctors))
        for i in range(len(quads)):
            mag_channel = 'TTF2.MAGNETS/QUAD/' + quads[i]# + '/PS'
            vals[i] = doocs.get(mag_channel + "/DEVTYPE")
        return vals