__author__ = 'Sergey Tomin'

from ocelot.cpbd.elements import *
from ocelot.adaptors.madx import lattice_str_from_madx, madx_seq2ocelot_seq
from ocelot.cpbd.io import *

def RFcavity(l, volt, lag, harmon):
    rf = Cavity(l = l, id = id)
    rf.volt = volt
    rf.lag = lag
    rf.harmon = harmon
    return rf


lines = lattice_str_from_madx("p3x_v16.seq")

file = "\n"
exec(file.join(lines))

seq = madx_seq2ocelot_seq(lattice, tot_length = ring.l, exclude_elems = ["puh","dunl", "duns", "duu", "puv"])

lat = MagneticLattice(seq, energy = 6)
write_lattice(lat, file_name = "petra3.inp")