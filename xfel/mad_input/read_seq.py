from ocelot import MagneticLattice

__author__ = 'Sergey Tomin'
import sys
ind = sys.path[0].find("desy")
sys.path.append(sys.path[0][:ind])
print sys.path[0][:ind]
from numpy import *
from ocelot.cpbd.io import *
from ocelot.gui.accelerator import *
exec(open("injector.inp"))
emass = 0.511e-3

#name = "desy/xfel/mad_input/XFEL.seq"
#lines = lattice_str_from_mad8("XFEL.seq") # convert MAD input file to XCODE input file

#save_lattice_str(lines, "XFEL_old.inp")
#name = "desy/xfel/mad_input/XFEL_old.inp"

exec( open("XFEL_old.inp"))

tws0 = Twiss()
tws0.beta_x = 9.546300000
tws0.beta_y = 35.277700
tws0.alpha_x = 0.603900
tws0.alpha_y = -1.929500
#tws0.s = 2002.19

tws0.E = 17.625300000
#0.500600000	-1.332200	2.371600	0.133500
tws0.beta_x = 0.500600000
tws0.beta_y = 2.371600
tws0.alpha_x = -1.332200
tws0.alpha_y = 0.133500
tws0.s = 1831.200233
#tl_ks_1.angle = 0.0
#tl_ks_1.angle = 0.0
#TLD.HELP.1a[ANGLE],  0.0
#TLD.HELP.1a[TILT],   0.0
#TLD.HELP.1b[ANGLE],  0.0
#TLD.HELP.1b[TILT],   0.0
#TLD.HELP.2a[ANGLE],  0.0
#TLD.HELP.2a[TILT],   0.0
#TLD.HELP.2b[ANGLE],  0.0
#TLD.HELP.2b[TILT],   0.0
#TLD.HELP.3a[ANGLE],  0.0
#TLD.HELP.3a[TILT],   0.0
#TLD.HELP.3b[ANGLE],  0.0
#TLD.HELP.3b[TILT],   0.0
#T1.HELP.1a[ANGLE],  0.0
#T1.HELP.1a[TILT],   0.0
#T1.HELP.1b[ANGLE],  0.0
#T1.HELP.1b[TILT],   0.0
#T1.HELP.2a[ANGLE],  0.0
#T1.HELP.2a[TILT],   0.0
#t1_help_2b.angle =  0.0
#t1_help_2b.tilt =  0.0
#tld_bz_1.l =          len_bz
#tld_bz_1.angle =      0.0
#tld_bz_1.e1  =        0.0
#tld_bz_1.e2 =          0.0
#tld_bz_2.l   =       len_bz
#tld_bz_2.angle =       0.0
#tld_bz_2.e1  =       0.0
#tld_bz_2.e2 =          0.0
"""
t1_bz_1.l = arc_bz_td1
t1_bz_1.angle =       ang_bz_td1
t1_bz_1.e1 =          e12_bz_td1
t1_bz_1.e2    =      e12_bz_td1
t1_bz_1.tilt =         tilt_bz1_td1
t1_bz_2.l =         arc_bz_td1
t1_bz_2.angle =        ang_bz_td1
t1_bz_2.e1 =        e12_bz_td1
t1_bz_2.e2 =          e12_bz_td1
"""
#t20_bz_1.l =            len_bz
#t20_bz_1.angle  =    0.0
#t20_bz_1.e1     =     0.0
#t20_bz_1.e2     =     0.0

#t20_bz_1.l     = arc_bz1_td20
#t20_bz_1.angle = ang_bz1_td20
#t20_bz_1.e1   = e12_bz1_td20
#t20_bz_1.e1    = e12_bz1_td20
#t20_bz_1.tilt  = tilt_bz1_td20

#xQK1_TD1 =  +7.2197740604e-03*1.00067
#xQK2_TD1 =  +9.1218401096e-03*0.99976
#yQK1_TD1 =  +2.3348937648e-02*1.00071
#yQK2_TD1 =  +2.3727377870e-02*0.99988
#t1_help_2a.angle =  tl_qkh_2.k1*tl_qkh_2.l*xQK1_TD1/cos(arctan(yQK1_TD1/xQK1_TD1))
#t1_help_2a.tilt = -arctan(yQK1_TD1/xQK1_TD1)
#t1_help_2b.angle =  tl_qkh_2.k1*tl_qkh_2.l*xQK2_TD1/cos(arctan(yQK2_TD1/xQK2_TD1))
#t1_help_2b.tilt = -arctan(yQK2_TD1/xQK2_TD1)

file_name = "xfelall.inp"
#tw0 = Twiss(Beam())
#i1 = i1[75:]
lat = MagneticLattice((tl1,tl2,tl3,tl4,tl5,t2))
#lat = MagneticLattice((tl4,t1))




#lat = MagneticLattice(lat.sequence[72:])
write_lattice(lat, file_name = "CL2SA1.inp")

#Ei = 0.005
#Ef = 0.005
#for elem in lat.sequence:
#    if elem.type == "cavity":
#        Ef += elem.delta_e
#    if elem.type == "quadrupole":
#        elem.k1 = elem.k1*Ei/Ef
#lat.update_transfer_maps()
print lat.totalLen, len(lat.sequence)
#Q = lat.sequence[74]
#Q.l = 0.15
#Q.k1 = Q.k1/30.
#seq = [Q , lat.sequence[75:]]
#
#lat = MagneticLattice(seq)
L = tws0.s
for i, elem in enumerate(lat.sequence):
    L+=elem.l
    if elem.type in ["bend", "sbend", "rbend"]:
        print i, L - elem.l/2., elem.type, elem.id, elem.l, " angle = ", elem.angle, "tilt = ", elem.tilt
    elif elem.type == "quadrupole":
        print i, L - elem.l/2., elem.type, elem.id, elem.l, " k1 = ", elem.k1
    else:
        print i, L - elem.l/2., elem.type, elem.id, elem.l
#lat = MagneticLattice(seq)


tws = twiss(lat, tws0, nPoints=None)
plot_opt_func(lat, tws, top_plot=["Dy", "Dx"])
print "beta_x = ", tws[-1].beta_x, "beta_y = ", tws[-1].beta_y, "alpha_x = ", tws[-1].alpha_x, "alpha_y = ", tws[-1].alpha_y
print "Dx = ", tws[-1].Dx, "Dy = ", tws[-1].Dy, "Dxp = ", tws[-1].Dxp, "Dyp = ", tws[-1].Dyp
plt.show()
#for elem in lat.sequence:
#    if elem.tilt != 0:
#        print elem.id, elem.type, elem.l, elem.tilt

def collect_drifts(lat):
    drift = 0
    L = 0.
    seq =[]
    for i, elem in enumerate(lat.sequence):
        if elem.type in ["drift", "monitor"]:
            #print elem.id, elem.tilt, elem.l
            drift = 1
            L += elem.l
            if i == len(lat.sequence) -1:
                L =  around(L, decimals = 6)
                seq.append(Drift(l = L, eid= "d" + str(int(L*100000 + 10000000))[1:]))
        else:
            if drift > 0 and L>0.:
                L =  around(L, decimals = 6)
                seq.append(Drift(l = L, eid= "d" + str(int(L*100000 + 10000000))[1:]))
                drift = 0
            seq.append(elem)
            L = 0.
    return MagneticLattice(seq)


"""
lat = collect_drifts(lat)

print emass

lines = lat2input(lat)

f = open(file_name, 'w')
f.writelines(lines)
f.close()



exec(open(file_name))

lat = MagneticLattice(lattice)

print lat.totalLen
tws0 = Twiss()
tws0.beta_x = 30
tws0.beta_y = 30
tws0.alpha_x = 7
tws0.alpha_y = 7.5

tws0.E = 0.0001 * GeV
L = 0.
for elem in lat.sequence:
    L+=elem.l
    print L, elem.type, elem.id
# first assign energies to elements
tws = twiss(lat, tws0, nPoints=None)
plot_opt_func(lat, tws, top_plot=["Dy", "Dx"])

lat.update_transfer_maps()

#tws = twiss(lat, tws0, nPoints=None)
#plot_opt_func(lat, tws, top_plot=["Dy"])

plt.show()
"""