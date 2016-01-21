__author__ = 'Sergey Tomin'
import pickle
from converter import *
import numpy as np



def save_currents(lat, filename):
    data = {}
    for elem in lat.sequence:
        try:
            I = elem.I
        except:
            continue
        data[elem.id] = {}
        data[elem.id]["type"] = elem.type
        data[elem.id]["mi_id"] = elem.mi_id
        data[elem.id]["dev_type"] = elem.dev_type
        data[elem.id]["I"] = I
    pickle.dump(data, open(filename, "wb"))
    return data

def load_currents(filename, lat):
    data = pickle.load(open(filename, "rb"))
    for elem in lat.sequence:
        if elem.id in data.keys():
            params = data[elem.id]
            elem.I = params["I"]
            elem.mi_id = params["mi_id"]
            elem.dev_type = params["dev_type"]

class MachineSetup:
    def __init__(self):
        pass

    def get_elem_type_currents(self, lat, type):
        data = {}
        for elem in lat.sequence:
            if elem.type in type:
                try:
                    I = elem.I
                except:
                    print (elem.type, elem.id, " No current!")
                    continue
                data[elem.id] = {}
                data[elem.id]["type"] = elem.type
                data[elem.id]["mi_id"] = elem.mi_id
                data[elem.id]["dev_type"] = elem.dev_type
                data[elem.id]["I"] = I
        #pickle.dump(data, open(filename, "wb"))
        return data

    def get_cav_params(self, lat):
        data = {}
        for elem in lat.sequence:
            if elem.type == "cavity":
                try:
                    v = elem.v
                    phi = elem.phi
                except:
                    print (elem.type, elem.id, " No elem.v or elem.phi!")
                    continue
                data[elem.id] = {}
                data[elem.id]["type"] = elem.type
                data[elem.id]["mi_id"] = elem.mi_id
                data[elem.id]["phi"] = phi
                data[elem.id]["v"] = v
        #pickle.dump(data, open(filename, "wb"))
        return data

    def get_orbit(self, lat):
        data = {}
        for bpm in lat.sequence:
            if bpm.type == "monitor":
                try:
                    mi_id = bpm.mi_id
                except:
                    print ("bpm: ", bpm.id, " No mi_id")
                    continue
                data[bpm.id] = {}
                data[bpm.id]["type"] = "monitor"
                data[bpm.id]["mi_id"] = bpm.mi_id
                data[bpm.id]["x"] = bpm.x
                data[bpm.id]["y"] = bpm.y
        #pickle.dump(data, open(filename, "wb"))
        return data

    def save_orbit(self, lat, filename):
        print "getting beam positions ... "
        self.dict_orbit = self.get_orbit(lat)
        print "OK"
        pickle.dump(self.dict_orbit, open(filename, "wb"))

    def load_orbit(self, filename, lat):
        data = pickle.load(open(filename, "rb"))
        for elem in lat.sequence:
            if elem.type == "monitor":
                if elem.id in data.keys():
                    elem.mi_id = data[elem.id]["mi_id"]
                    elem.x = data[elem.id]["x"]
                    elem.y = data[elem.id]["y"]
        return lat

    def save_lattice(self, lat, filename):
        print "getting currents of quad ... "
        self.dict_quad = self.get_elem_type_currents(lat, ["quadrupole"])
        print "OK"

        print "getting currents of bend ... "
        self.dict_bend = self.get_elem_type_currents(lat, ["sbend", "rbend", "bend"])
        print "OK"

        print "getting currents of correctors ... "
        self.dict_cor = self.get_elem_type_currents(lat, ["hcor", "vcor"])
        print "OK"

        print "getting params of cavities ... "
        self.dict_cav = self.get_cav_params(lat)
        print "OK"

        print "getting beam positions ...  "
        self.dict_orbit = self.get_orbit(lat)
        print "OK"

        print "getting currents of sext  ...  "
        self.dict_sext = self.get_elem_type_currents(lat, ["sextupole"])
        print "OK"

        #print ("getting orbit ... ", )
        #self.dict_orbit = self.get_cav_params(lat)
        #print ("OK")
        data = {}
        data["quad"] = self.dict_quad
        data["bend"] = self.dict_bend
        data["cor"] = self.dict_cor
        data["cav"] = self.dict_cav
        data["orbit"] = self.dict_orbit
        data["sext"] = self.dict_sext
        pickle.dump(data, open(filename, "wb"))

    def load_lattice(self, filename, lat):
        data = pickle.load(open(filename, "rb"))
        self.dict_quad = data["quad"]
        self.dict_bend = data["bend"]
        self.dict_cor = data["cor"]
        self.dict_cav = data["cav"]
        self.dict_orbit = data["orbit"]
        self.dict_sext = data["sext"]

        for elem in lat.sequence:

            if elem.type == "quadrupole" and elem.id in self.dict_quad.keys():
                elem.mi_id = self.dict_quad[elem.id]["mi_id"]
                elem.dev_type = self.dict_quad[elem.id]["dev_type"]
                elem.I = self.dict_quad[elem.id]["I"]

            if elem.type in ["bend", "rbend", "sbend"] and elem.id in self.dict_bend.keys():
                elem.mi_id = self.dict_bend[elem.id]["mi_id"]
                elem.dev_type = self.dict_bend[elem.id]["dev_type"]
                elem.I = self.dict_bend[elem.id]["I"]

            if elem.type in ["hcor", "vcor"] and elem.id in self.dict_cor.keys():
                elem.mi_id = self.dict_cor[elem.id]["mi_id"]
                elem.dev_type = self.dict_cor[elem.id]["dev_type"]
                elem.I = self.dict_cor[elem.id]["I"]

            if elem.type == "cavity" and elem.id in self.dict_cav.keys():
                elem.mi_id = self.dict_cav[elem.id]["mi_id"]
                elem.v = self.dict_cav[elem.id]["v"]
                elem.phi = self.dict_cav[elem.id]["phi"]

            if elem.type == "monitor" and elem.id in self.dict_orbit.keys():
                elem.mi_id = self.dict_orbit[elem.id]["mi_id"]
                elem.x = self.dict_orbit[elem.id]["x"]
                elem.y = self.dict_orbit[elem.id]["y"]

            if elem.type == "sextupole" and elem.id in self.dict_sext.keys():
                elem.mi_id = self.dict_sext[elem.id]["mi_id"]
                elem.dev_type = self.dict_sext[elem.id]["dev_type"]
                elem.I = self.dict_sext[elem.id]["I"]

    def convert_currents(self, lat, init_energy):
        E = init_energy
        for elem in lat.sequence:
            E += elem.transfer_map.delta_e
            elem.E = E
            if elem.type == "quadrupole":

                k1 = tpi2k(elem.dev_type, elem.E, elem.I)
                k1 = abs(k1)*np.sign(elem.k1)
                #if elem.mi_id in ["Q4DBC2","Q9ACC2", 'Q3.5ECOL', 'Q5UND1.3.5', "Q5UND2.4", 'Q6UND1']:
                #    k1 = abs(k1)*sign(elem.k1)
                #K1 = k1
                #print elem.id,  "i.k1=", elem.k1, " r.k1=", k1, "I=", elem.I, "E=", E
                #print(elem.id,  "ideal: k1 = ", elem.k1, " real k1 = ", K1, " dk/k = ", (K1-elem.k1)/elem.k1*100.)
                elem.k1 = k1
            elif elem.type == "sextupole":
                #pass

                k2 = tpi2k(elem.dev_type, elem.E, elem.I)
                #print elem.id,  "i.k1=", elem.k2, " r.k1=", k2, "I=", elem.I, "E=", E
                elem.k2 = k2
                #print elem.id, elem.k2
            elif elem.type in ["bend", "sbend", "rbend"]:
                try:
                    elem.dev_type
                except:
                    continue
                angle = tpi2k(elem.dev_type, elem.E, elem.I)
                angle = abs(angle)*np.sign(elem.angle)*np.pi/180.
                #print elem.id,  "i.a=", elem.angle, " r.a=", angle, "I=", elem.I, "E=", E
                elem.angle = angle

            #elif elem.type in ["hcor", "vcor"]:
            #    angle = tpi2k(elem.dev_type, E, elem.I)
            #    if angle == None:
            #        print(elem.id,  elem.I, E, angle, elem.dev_type)
            #    else:
            #        elem.angle = angle*0.001
