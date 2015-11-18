__author__ = 'Sergey Tomin'

from ocelot import *
from ocelot.adaptors import *


#def RFcavity(l, volt, lag, harmon):
#    rf = Cavity(l = l, volt=volt, id = id)
#    rf.lag = lag
#    rf.harmon = harmon
#    return rf

sequence = madx2ocelot(file_seq="p3x_v16.seq", exclude_elems= ["puh","dunl", "duns", "duu", "puv"])
#lines = lattice_str_from_madx("p3x_v16.seq")
#print lines
#file = "\n"
#exec(file.join(lines))
#
#seq = madx_seq2ocelot_seq(lattice, tot_length = ring.l, exclude_elems = ["puh","dunl", "duns", "duu", "puv"])

lat = MagneticLattice(sequence)
write_lattice(lat, file_name = "petra3.inp")