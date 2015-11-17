__author__ = 'Sergey Tomin'

from ocelot.adaptors.elegant2ocelot import *
from ocelot.cpbd.beam import *
from ocelot.cpbd.elements import *
from ocelot.cpbd.optics import *
from ocelot.gui.accelerator import *
from ocelot.cpbd.io import *
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

sequence = read_lattice_elegant(file_flo="elegant_files/flash_s2e_flo.txt", file_par="elegant_files/flash_s2e_par.txt")

lat = MagneticLattice(sequence)

tw0 = Twiss(beam)

tws=twiss(lat, tw0, nPoints=None)
plot_opt_func(lat, tws, top_plot=["E"])
plt.show()

write_lattice(lat, file_name="lattice.inp")
exec(open("lattice.inp"))

lat = MagneticLattice(lattice)

tw0 = Twiss(beam)

tws=twiss(lat, tw0, nPoints=None)
plot_opt_func(lat, tws, top_plot=["Dx"])
plt.show()