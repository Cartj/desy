__author__ = 'Sergey Tomin'

from ocelot.adaptors.elegant2ocelot import *
from ocelot.cpbd.beam import *
from ocelot.cpbd.track import *
from ocelot.gui.accelerator import *

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
    return S, Bx, By


def write_sdds_file(namefile):
    f=open(namefile, 'rb')
    data=f.readlines()
    f.close()
    lines = data[:20]
    for d in data[20:]:
        numbers = d.split(" ")
        #numbers[-2] = '+0.0000000000000000E+00'
        #numbers[-1] = '+0.0000000000000000E+00\r\n'
        line = " ".join(numbers)
        lines.append(line)
    fn=open("flash_new.txt", 'w')
    fn.writelines(lines)
    fn.close()
    return 0


write_sdds_file("flash.sdds")
S, Bx, By = read_twi_file("flash_s2e_twi.txt")
#S, Bx, By = read_sig_file("flash_s2e_sig.txt")

beta_x = np.array([t.beta_x for t in tws])
beta_y = np.array([t.beta_y for t in tws])
print "d_beta_x/beta_x = ", (Bx[-1] - beta_x[-1])/beta_x[-1]
print "d_beta_y/beta_y = ", (By[-1] - beta_y[-1])/beta_y[-1]
print len(S), len([t.s for t in tws])
plt.title(r"$\beta_x$")
plt.plot(S, Bx, "b", [t.s for t in tws], beta_x, "r")
plt.grid(True)
plt.legend(["elegant", "ocelot"])
plt.show()
plt.title(r"$\beta_y$")
plt.plot(S, By, "b", [t.s for t in tws], beta_y, "r")
plt.grid(True)
plt.legend(["elegant", "ocelot"])
plt.show()

