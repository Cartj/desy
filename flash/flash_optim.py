__author__ = 'Sergey Tomin'
from ocelot import *
from ocelot.gui import *
from ocelot.adaptors import *
import csv
import sys
import numpy as np
from desy.flash.converter import *
from ocelot.utils.flash_read_log import *
from ocelot.cpbd.elements import *
from ocelot.rad.undulator_params import *
from ocelot.cpbd.track import lattice_track
from copy import copy
from lattice_rf_mod import *
from ocelot.gui.accelerator import *
from scipy.optimize._differentialevolution import DifferentialEvolutionSolver
print DifferentialEvolutionSolver
#plot_log("exp_files/h3-v3dbc3_1.txt")
#dict_data = read_log("exp_files/h3-v3dbc3_1.txt")

plot_log("exp_files/h3-v3dbc3_1.txt")
dict_data = read_log("exp_files/h3-v3dbc3_1.txt")


new_dict = rm_nonwork_devices(dict_data, debug=True, rm_devices=["H3UND4"])
plot_dict(new_dict, filename=None, interval=1, mode="%")
#save_new_dict(new_dict, "new_optim.txt")
print ("E = ", lambda2Ebeam(Lambda=13.4e-9, lu=0.0272634730539, K=1.2392))

#def cut_lattice(old_seq, elem_id):
#    seq = []
#    for elem in old_seq:
#        seq.append(elem)
#        if elem.id == elem_id:
#            return seq
#    return seq

"""
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

lat = MagneticLattice(lattice)
E = beam.E
for elem in lat.sequence:
    elem.e_ref = E
    E += elem.transfer_map.delta_e

"""

beam = Beam()
beam.E = 148.3148e-3 #in GeV ?!
beam.beta_x = 14.8821
beam.beta_y = 18.8146
beam.alpha_x =  -0.61309
beam.alpha_y = -0.54569
beam.emit_xn = 1.5e-6
beam.emit_yn = 1.5e-6
beam.emit_x = beam.emit_xn / (beam.E / m_e_GeV)
beam.emit_y = beam.emit_yn / (beam.E / m_e_GeV)

tw0 = Twiss(beam)
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

#seq = cut_lattice(old_seq=lattice, elem_id="D6DUMP")


lat = MagneticLattice(lattice, start=STARTACC39)
#lat = MagneticLattice(lattice)
tws=twiss(lat, tw0)
plot_opt_func(lat, tws, top_plot="E")
#for e in lattice.sequence:
#    obj = e.transfer_map*obj
E = beam.E
L = 0

for elem in lat.sequence:

    #if "ACC1" in elem.id and elem.type == "cavity":
    #    elem.v = elem.v*0.923
    #    elem.transfer_map = create_transfer_map(elem)
    #    print elem.v
    if "ACC45" in elem.id and elem.type == "cavity":
        #elem.v = elem.v*0.87
        elem.v = elem.v*0.63
        elem.transfer_map = create_transfer_map(elem)
        #print elem.v
    if "ACC67" in elem.id and elem.type == "cavity":
        elem.v = 0.
        elem.transfer_map = create_transfer_map(elem)
        #print elem.v
    #if elem.type == "quadrupole":
    #    elem.k1 = elem.k1*E/elem.e_ref
    #    print E, elem.e_ref
    E += elem.transfer_map.delta_e
    L+=elem.l
    #if elem.id == "C8_M1_ACC1":
    #print "**********************", E
    #if elem.type in ["quadrupole"]:
    #    print( elem.id , tpk2i(elem.dev_type, E, elem.k1), " A", " E = ", E, "GeV", " s = ", L)
    #if elem.type in ["hcor", "vcor"]:
    #    print( elem.id , tpk2i(elem.dev_type, E, elem.angle), " A", " E = ", E, "GeV", " s = ", L)


N = range(0, len(new_dict["time"]), 10)
devices = list(new_dict.keys())
devices.remove("time")
devices.remove("sase")
#devices.remove('H3DBC3')
#devices.remove('V3DBC3')
#devices.remove('V7SMATCH')
#devices.remove('H10SMATCH')
#devices.remove('V14SMATCH')
#devices.remove('H12SMATCH')
#print(devices)
n_end = N[-1]
ax = plot_API(lat)
for i in N:
    E = beam.E
    p = Particle(E=beam.E)
    for elem in lat.sequence:
        if elem.id in devices:

            elem.angle = tpi2k(elem.dev_type, E, new_dict[elem.id][i])*1e-3 - tpi2k(elem.dev_type, E, new_dict[elem.id][0])*1e-3
            #print elem.angle
            elem.transfer_map = create_transfer_map(elem)
    plist = lattice_track(lat, copy(p), order=1)

    if i == N[-1]:
        #plot_trajectory(lat, plist)
        ax.plot([p.s for p in plist], [p.x for p in plist], "ro-", lw=2)
        ax.plot([p.s for p in plist], [p.y for p in plist], "bo-", lw=2)

    else:
        ax.plot([p.s for p in plist], [p.x for p in plist], "r", alpha = 0.3)
        ax.plot([p.s for p in plist], [p.y for p in plist], "b", alpha = 0.3)

ax.set_xlabel("X/Y, m")
plt.xlim([0, lat.totalLen])

ax.legend(["X", "Y"], loc=1)
plt.show()
#plt.grid(True)
#plt.legend(["X", "Y"])
#plt.xlabel("S, m")
#plt.ylabel("X/Y, m")
#plt.show()

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

#for elem in lat.sequence:
#    print elem.type, elem.id
#    if elem.type == "cavity":
#        print elem.v, elem.delta_e
tws=twiss(lat, tw0)
plot_opt_func(lat, tws, top_plot="E")



S, Bx, By = read_twi_file("elegant_files/FLASH1_twi.txt")

plt.plot(S, By, "r")
plt.plot([p.s for p in tws], [p.beta_y for p in tws], "b")
plt.show()






exit(0)
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

