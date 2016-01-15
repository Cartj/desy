__author__ = 'Sergey Topmin'

import time
import numpy as np

def read_quads(lat, mi, dp):
    id2I_dict = {}
    for elem in lat.sequence:
        if elem.type == "quadrupole":
            name = elem.id
            #if "_U" in name:
            #    continue
            name = name.replace("_U", "")
            name = name.replace("_D", "")
            name = name.replace("_", ".")
            #print(name)
            try:
                elem.mi_id
            except:
                elem.mi_id = name
            #print(elem.mi_id)
            elem.I = 0
            elem.polarity = 1
            if elem.mi_id in id2I_dict.keys():
                elem.I = id2I_dict[elem.mi_id]
            else:
                try:
                    #time.sleep(0.01)
                    elem.I = mi.get_quads_current([elem.mi_id])[0]
                    elem.polarity = dp.get_polarity([elem.mi_id])[0]
                    id2I_dict[elem.mi_id] = elem.I

                    #type_magnet = dp.get_type_magnet([elem.mi_id])
                    #print(type_magnet, elem.dev_type)
                    #print(elem.id, name, mi.get_quads_current([elem.mi_id]))
                except:
                    print(name, "  CAN MOT FIND")
            #print(elem.id, elem.mi_id, elem.I)


def read_cavs(lat, mi):
    for elem in lat.sequence:
        if elem.type == "cavity":
            name = elem.id.split("_")
            elem.mi_id = name[-1]
            try:
                ampls, phases = mi.get_cavity_info([elem.mi_id])
                print "read =", elem.mi_id, ampls, phases, ampls[0]*np.cos(phases[0]*np.pi/180.)
            except:
                print ("UNKNOWN cav", elem.mi_id, elem.id)
                continue
            elem.v = ampls[0]*0.001 # MeV -> GeV
            elem.phi = phases[0]
            if elem.mi_id == "ACC1":
                elem.v = elem.v/8.
            elif elem.mi_id == "ACC39":
                elem.v = elem.v/4.
            elif elem.mi_id == "ACC23":
                elem.v = elem.v/16.
            elif elem.mi_id == "ACC45":
                elem.v = elem.v/16.
            elif elem.mi_id == "ACC67":
                elem.v = elem.v/16.
    lat.update_transfer_maps()
    return lat


def read_cors(lat, mi):
    for elem in lat.sequence:
        if elem.type in ["hcor", "vcor"]:
            name = elem.id
            name = name.replace("_", ".")
            try:
                elem.mi_id
            except:
                elem.mi_id = name
            try:
                #print(elem.mi_id, )
                vals = mi.init_corrector_vals([elem.mi_id])
                elem.I = vals[0]
            except:
                print(elem.mi_id, "UNKNOW")
                elem.type = "drift"


def read_bpms(orbit, mi):
    for bpm in orbit.bpms:
        name = bpm.id.replace("BPM", "")

        bpm.mi_id = name
        #X, Y = mi.get_bpms_xy([bpm.mi_id])
        try:
            X, Y = mi.get_bpms_xy([bpm.mi_id])
            bpm.x = X[0]
            bpm.y = Y[0]
            print (bpm.s, bpm.x, bpm.y)
        except:
            print(name, "  CAN MOT FIND")
