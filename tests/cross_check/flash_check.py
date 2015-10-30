__author__ = 'Sergey Tomin'

from ocelot.adaptors.elegant2ocelot import *
from ocelot.cpbd.optics import *
from ocelot.cpbd.beam import *
from ocelot.gui.accelerator import *
from ocelot.cpbd.io import *

#lat_def = read_lattice_elegant(file_flo="flash_s2e_flo.txt", file_par="flash_s2e_par.txt")
#for elem in lat_def:
#    print elem.id, elem.type, elem.l
##lat = insert_drifts(0., 189.318565601672, lat_def)
#
#lat = MagneticLattice(lat_def)
#print lat.totalLen
#write_lattice(lat, file_name="flash.inp")
exec(open("flash.inp"))
lat = MagneticLattice(lattice)
beam = Beam()
beam.E = 148.3148e-3
beam.beta_x = 14.8821
beam.alpha_x = -0.61309
beam.beta_y = 18.8146
beam.alpha_y = -0.54569
tws0 = Twiss(beam)
tws = twiss(lat, tws0=tws0)

plot_opt_func(lat, tws, top_plot="E")
plt.show()

def read_file(filename):
    f=open(filename, 'rb')
    data=csv.reader(f, delimiter='\t')
    data=[row for row in data]
    f.close()
    return data



def read_sig_file(namefile):
    data = read_file(namefile)
    S = []
    Bx = []
    By = []
    for d in data[11:]:
        S.append(float(d[0]))
        Bx.append(float(d[68]))
        By.append(float(d[70]))
    return S, Bx, By

def read_twi_file(namefile):
    data = read_file(namefile)
    S = []
    Bx = []
    By = []
    for d in data[59:]:
        S.append(float(d[0]))
        Bx.append(float(d[1]))
        By.append(float(d[7]))

#S, Bx, By = read_twi_file("flash_s2e_twi1.txt")
S, Bx, By = read_sig_file("flash_s2e_sig.txt")

plt.plot(S, Bx, [t.s for t in tws], np.array([t.beta_x for t in tws]))
plt.plot(S, By, [t.s for t in tws], np.array([t.beta_y for t in tws]))
plt.show()
