__author__ = 'Sergey Tomin'
from ocelot import *
from ocelot.gui import *
from ocelot.adaptors import *
import csv
import sys
import numpy as np
from .converter import *


def read_file(filename):
    if sys.version_info[0] < 3:
        f=open(filename, 'rb')
    else:
        f = open(filename, 'r', newline='', encoding='utf8')
    data=csv.reader(f, delimiter='\t')
    data=[row for row in data]
    f.close()
    return data


def read_twi_file(namefile):
    data = read_file(namefile)
    S = []
    Bx = []
    By = []
    for d in data[59:]:
        S.append(float(d[0]))
        Bx.append(float(d[1]))
        By.append(float(d[7]))
    return S, Bx, By

def cut_lattice(old_seq, elem_id):
    seq = []
    for elem in old_seq:
        seq.append(elem)
        if elem.id == elem_id:
            return seq
    return seq


beam = Beam()
beam.E = 5e-3 #in GeV ?!

beam.beta_x = 14.9286
beam.beta_y = 15.3373
beam.alpha_x =  7.4896
beam.alpha_y = 7.6972
beam.emit_xn = 1.5e-6
beam.emit_yn = 1.5e-6
beam.emit_x = beam.emit_xn / (beam.E / m_e_GeV)
beam.emit_y = beam.emit_yn / (beam.E / m_e_GeV)
"""
sequence = read_lattice_elegant(file_flo="elegant_files/FLASH1_flo.txt", file_par="elegant_files/FLASH1_par.txt")
lat = MagneticLattice(sequence)
for elem in lat.sequence:
    print elem.type, elem.id
tw0 = Twiss(beam)
tws=twiss(lat, tw0, nPoints=None)
plot_opt_func(lat, tws, top_plot=["E"])
write_lattice(lat, file_name="lattice_und.inp")
"""
#exec(open('lattice_und.inp'))
from  .lattice_und_inp import *
#seq = cut_lattice(old_seq=lattice, elem_id="D6DUMP")

tw0 = Twiss(beam)
lat = MagneticLattice(lattice)

#for e in lattice.sequence:
#    obj = e.transfer_map*obj
E = beam.E
for elem in lat.sequence:
    E += elem.transfer_map.delta_e
    if elem.type in ["quadrupole"]:
        print( elem.id , tpk2i(elem.dev_type, E, elem.k1), " A", " E = ", E, "GeV")
    if elem.type in ["hcor", "vcor"]:
        print( elem.id , tpk2i(elem.dev_type, E, elem.angle), " A", " E = ", E, "GeV")

#names = []
#ID = []
#for elem in lat.sequence:
#    if elem.type == "vcor":
#        name = elem.id
#        #print elem.id, tpi2k(elem.dev_type, 0.7, elem.k1)
#        #name = name.replace("_U", "")
#        #name = name.replace("_D", "")
#        name = name.replace("_", ".")
#        if name in names:
#            continue
#        names.append(name)
#        print name
#        ID.append(elem.id)
#
#print len(ID), len(names)
#f=open("elegant_files/FLASH_LATTICE.mad", 'rb')
#lines = f.readlines()
#f.close()
#
#for name, id in zip(names,ID):
#    #print "********  QUAD *********** ", name
#    for line in lines:
#        if name in line:
#            if "!" in line:
#                continue
#            #print line
#            parts = line.split(",")
#            p = parts[0].split(":")
#            #print p
#            type = "".join(p[1].split())
#
#            #print parts.remove("")
#            #type = type.replace(".H","")
#            #type = type.replace("QTSE", "QTS_E")
#            #type = type.replace("QTSI", "QTS_I")
#            #type = type.replace("H", "")
#            print id + ".dev_type = '"+type+"'"
#    #print "'"+name+"',"



tw0 = Twiss(beam)
tws=twiss(lat, tw0)
plot_opt_func(lat, tws, top_plot="E")

S, Bx, By = read_twi_file("elegant_files/FLASH1_twi.txt")

plt.plot(S, Bx, "r")
plt.plot([p.s for p in tws], [p.beta_x for p in tws], "b")
plt.show()






exit()
p_array, charge_array = astraBeam2particleArray(filename='../demos/ebeam/flash/elegant_files/flash_out_200000.ast')

#p_array.particles[4::6] = sc.smooth_z(p_array.particles[4::6], mslice=10000)

# plot current
bins_start, hist_start = get_current(p_array, charge=charge_array[0], num_bins=200)

dz = 1.
order = 2
SC = False
debug = False

Z = np.linspace(0, lat.totalLen, num=int(lat.totalLen/dz))

twsi=twiss(lat, tw0, nPoints=len(Z) )
tw0 = get_envelope(p_array, tws_i = twsi[0])
tws_track = [tw0]
"""
if debug:
    f=plt.figure()
    plt.ion()
    plt.hold(False)

navi = Navigator(lattice=lat)
for i, zi in enumerate(Z[1:]):
    print zi
    dz = zi - Z[i]
    track(lat=lat, particle_list=p_array, dz=dz, navi=navi, order=order)
    #p_array.particles[4::6] = sc.smooth_z(p_array.particles[4::6], mslice=10000)
    if SC:
        sc_apply(p_array, q_array=charge_array, zstep=dz, nmesh_xyz=[63, 63, 63], low_order_kick=True)
    tw = get_envelope(p_array,tws_i=twsi[i+1])
    tw.s = navi.z0
    #print tw.s, twsi[i+1].s
    tws_track.append(tw)
    if debug:
        f.add_subplot(211)
        plt.plot(p_array.particles[::6], p_array.particles[2::6], '.')
        f.add_subplot(212)
        plt.plot(p_array.particles[4::6],p_array.particles[5::6],'.')
        plt.draw()
        plt.pause(0.1)
plt.ioff()
"""
L = 0.
for elem in lat.sequence:
    tw0 = elem.transfer_map*tw0
    elem.transfer_map.apply(p_array, order=2)
    tw = get_envelope(p_array, tws_i=tw0)
    L += elem.l
    tw.s += L
    print( tw.s)
    tws_track.append(tw)

# plot current at the beginning of accelerator
plt.figure(1)
plt.title("current: start")
plt.plot(bins_start, hist_start)
plt.xlabel("s, m")
plt.ylabel("I, A")
plt.grid(True)

# plot current at the end of accelerator
bins, hist = get_current(p_array, charge=charge_array[0], num_bins=200)
plt.figure(2)
plt.title("current: end")
plt.plot(bins, hist)
plt.xlabel("s, m")
plt.ylabel("I, A")
plt.grid(True)




plt.figure(3)
plt.title(r"$\beta_y - functions$")
plt.plot([p.s for p in tws_track], [p.beta_y for p in tws_track], "ro-", label = "ocelot")
plt.plot([p.s for p in tws], [p.beta_y for p in tws], "bo-", label = "1-order")
#plt.plot(s_b, betay_b, "bo-", label = "elegant")
plt.legend()
plt.grid(True)
plt.figure(4)
plt.title(r"$\beta_x - functions$")
plt.plot([p.s for p in tws_track], [p.beta_x for p in tws_track], "ro-", label = "2-order")
plt.plot([p.s for p in tws], [p.beta_x for p in tws], "bo-", label = "1-order")
#plt.plot(s_b, betax_b, "bo-", label = "elegant")
plt.legend()
plt.grid(True)

plt.show()

