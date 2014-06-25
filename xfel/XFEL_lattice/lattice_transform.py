__author__ = 'Sergey Tomin'
import sys
ind = sys.path[0].find("desy")
sys.path.append(sys.path[0][:ind])
print sys.path[0][:ind]
from ocelot.adaptors.txm2ocelot import xfel2ocelot
from ocelot.cpbd.elements import *
from ocelot.adaptors.lat2inp import lat2input
from numpy import *


emass = 0.511e-3

name = "desy/xfel/input_files/XFEL_DEFS.txm"
#xfel2ocelot(sys.path[0][:ind] + name) # convert MAD input file to XCODE input file

name = "desy/xfel/input_files/XFEL_LINAC.txm"
xfel2ocelot(sys.path[0][:ind] + name) # convert MAD input file to XCODE input file

name = "desy/xfel/input_files/XFEL_I1.txm"
xfel2ocelot(sys.path[0][:ind] + name) # convert MAD input file to XCODE input file

name = "desy/xfel/input_files/XFEL_DEFS.inp"
exec( open(sys.path[0][:ind] + name))

name = "desy/xfel/input_files/XFEL_LINAC.inp"
exec( open(sys.path[0][:ind] + name))
name = "desy/xfel/input_files/XFEL_I1.inp"

exec( open(sys.path[0][:ind] + name))

#tw0 = Twiss(Beam())
lat = MagneticLattice(i1, energy = 2.5)
print lat.totalLen, len(lat.sequence)

#for elem in lat.sequence:
#    print elem.id, elem.type, elem.l

def collect_drifts(lat):
    drift = 0
    L = 0.
    seq =[]
    for i, elem in enumerate(lat.sequence):
        if elem.type in ["drift", "monitor"]:
            drift = 1
            L += elem.l
            if i == len(lat.sequence) -1:
                L =  around(L, decimals = 6)
                seq.append(Drift(l = L, id = "d" + str(int(L*100000 + 10000000))[1:]))
        else:
            if drift > 0 and L>0.:
                L =  around(L, decimals = 6)
                seq.append(Drift(l = L, id = "d" + str(int(L*100000 + 10000000))[1:]))
                drift = 0
            seq.append(elem)
            L = 0.
    return MagneticLattice(seq)


#def find_drifts(lat):
#    drift_lengs = []
#    drifts = []
#    for elem in lat.sequence:
#        if elem.type == "drift":
#            elem_l = around(elem.l, decimals = 6)
#            if elem_l not in drift_lengs:
#                drifts.append(elem)
#                drift_lengs.append(elem_l)
#    return drifts



#def find_objects(lat, types):
#    obj_id = []
#    objs = []
#    for elem in lat.sequence:
#        if elem.type in types:
#            if elem.id not in obj_id:
#                objs.append(elem)
#                obj_id.append(elem.id)
#    return objs
lat = collect_drifts(lat)
#drifts = find_drifts(lat)

#print len(drifts)
#for elem1 in drifts:
#    for elem2 in drifts:
#        if elem1.id == elem2.id:
#            print elem1.id, elem2.id, elem1.l, elem2.l, elem1.l == elem2.l


#drifts = find_objects(lat, types = ["drift"])
#quads = find_objects(lat, types = ["quadrupole"])
#sexs = find_objects(lat, types = ["sextupole"])
#cavs = find_objects(lat, types = ["cavity"])
#bends = find_objects(lat, types = ["bend","rbend", "sbend"])
#print lat.totalLen, len(lat.sequence)

#def lat2input(lat):
#    drifts = find_objects(lat, types = ["drift"])
#    quads = find_objects(lat, types = ["quadrupole"])
#    sexts = find_objects(lat, types = ["sextupole"])
#    print "sext = ", len(sexts)
#    cavs = find_objects(lat, types = ["cavity"])
#    bends = find_objects(lat, types = ["bend","rbend", "sbend"])
#    lines = []
#    for drift in drifts:
#        line = drift.id + " = Drift(l = " + str(drift.l)+ ", id = '"+ drift.id+ "')"
#        lines.append(line)
#    lines.append("# quadrupoles ")
#    for quad in quads:
#        line = quad.id + " = Quadrupole(l = " + str(quad.l) +", k1 = "+ str(quad.k1) +", id = '"+ quad.id+ "')"
#        lines.append(line)
#    lines.append("# bending magnets ")
#    for bend in bends:
#        if bend.type == "rbend":
#            type = " = RBend(l = "
#        elif bend.type == "sbend":
#            type = " = SBend(l = "
#        else:
#            type = " = Bend(l = "
#        if bend.k1 == 0 or bend.k1 == None:
#            k = ''
#        else:
#            k = ", k1 = "+ str(bend.k1)
#        line = bend.id + type + str(bend.l) + k + ", angle = "+ str(bend.angle)+ ", e1 = " + str(bend.e1) + ", e2 = " + str(bend.e2) +", id = '"+ bend.id+ "')"
#        lines.append(line)
#    lines.append("# sextupoles ")
#    for sext in sexts:
#        line = sext.id + " = Sextupole(l = " + str(sext.l) +", k2 = "+ str(sext.k2) +", tilt = "+ str(sext.tilt) +", id = '"+ sext.id+ "')"
#        lines.append(line)
#    lines.append("# cavity ")
#    for cav in cavs:
#        line = cav.id + " = Cavity(l = " + str(cav.l) +", volt = "+ str(cav.v) +", delta_e = "+ str(cav.delta_e)+\
#               ", freq = "+ str(cav.f) +", volterr = "+ str(cav.volterr) +", id = '"+ cav.id+ "')"
#        lines.append(line)
#    lines.append("# lattice ")
#    names = map(lambda p: p.id, lat.sequence)
#    new_names = []
#    for i, name in enumerate(names):
#        if i%8 == 7:
#            new_names.append("\n"+name)
#        else:
#            new_names.append(name)
#    line = "lattice = (" + ", ".join(new_names) +")"
#    lines.append(line)
#    return lines

#m12=lundlh_10, rm13=0.0, rm22=1.0, rm33=cos(omegalh*lundlh_10), rm34=sin(omegalh*lundlh_10)/omegalh, rm43=-sin(omegalh*lundlh_10)*omegalh, rm44=cos(omegalh*lundlh_10), id = 'i1_undu')

print emass

lines = lat2input(lat)
#for line in lines:
#    print line

f = open("injector.inp", 'w')
f.writelines(lines)
f.close()
#print len(drifts), len(quads), len(cavs), len(bends), len(sexs)
#for elem in drifts:
#    print elem.id, elem.l #, elem.type, elem.angle, elem.e1, elem.e2

    #print elem.type, elem.l, elem.id
#lat = MagneticLattice(superperiod, energy = 2.5)
#tws = twiss(lat,tw0,nPoints=1000 )