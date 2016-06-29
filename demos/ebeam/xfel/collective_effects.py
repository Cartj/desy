__author__ = 'tomins'

from ocelot import *
from ocelot.cpbd.sc2 import *
from ocelot.adaptors import *
import matplotlib.pyplot as plt

class PhysicsProcess:
    def __init__(self):
        pass

    def apply(self, dz):
        print("apply")


class SCRProcess():
    def __init__(self):
        self.step = 1
        #PhysicsProcess.__init__(self)

    def apply(self, p_array, dz):
        print("apply CSR")

"""
class ProcessTable:
    def __init__(self, lattice):
        self.proc_list = []
        self.lat = lattice

    def add_physics_proc(self, physics_proc, elem1, elem2):
        physics_proc.start_elem = elem1
        physics_proc.end_elem = elem2
        physics_proc.indx0 = self.lat.sequence.index(elem1)
        physics_proc.indx1 = self.lat.sequence.index(elem2)
        physics_proc.counter = physics_proc.step
        self.proc_list.append(physics_proc)


class Navigator2:
    def __init__(self, lattice=None):
        if lattice != None:
            self.lat = lattice
        self.process_table = ProcessTable(lattice)

        self.z0 = 0.             # current position of navigator
        self.n_elem = 0          # current index of the element in lattice
        self.sum_lengths = 0.    # sum_lengths = Sum[lat.sequence[i].l, {i, 0, n_elem-1}]

    def add_physics_proc(self, physics_proc, elem1, elem2):
        self.process_table.add_physics_proc(physics_proc, elem1, elem2)


    def get_proc_list(self):

        proc_list = []
        for p in self.process_table.proc_list:
            if p.indx0 <= self.n_elem <  p.indx1:
                proc_list.append(p)
        return proc_list


    def get_next(self):

        #if len(self.process_table.proc_list) == 0:
        #    # there are not physics processes
        #    dz = self.lat.totalLen - self.z0
        #   return dz, []
        print("self.z0 = ", self.z0, " self.n_elem = ", self.n_elem, " self.sum_lengths = ", self.sum_lengths)

        proc_list = self.get_proc_list()
        if len(proc_list) > 0:

            counters = np.array([p.counter for p in proc_list])
            step = counters.min()

            inxs = np.where(counters == step)
            processes = [proc_list[i] for i in inxs[0]]
            for p in proc_list:
                p.counter -= step
                if p.counter == 0:
                    p.counter = p.step
            dz = step*self.unit_step
        else:
            print("Else: self.z0 = ", self.z0, " self.n_elem = ", self.n_elem, " self.sum_lengths = ", self.sum_lengths)
            processes = proc_list
            #indexes_0 = np.array([p.indx0 for p in self.process_table.proc_list])
            #print("indexes_0", indexes_0)
            #print("where",self.n_elem, np.where(indexes_0 > self.n_elem))
            #inx = np.where(indexes_0 > self.n_elem)[0]
            #print(inx)#, [elem.l for elem in lat.sequence[:inx]])
            n_elems = len(self.lat.sequence)
            print("n elems = ", n_elems)
            if n_elems >= self.n_elem+1:
                print(np.array([elem.l for elem in lat.sequence[:self.n_elem+1]]))
                L = np.sum(np.array([elem.l for elem in lat.sequence[:self.n_elem+1]]))
            else:
                L = lat.totalLen
            dz = L - self.z0
        #print("dz = ", dz, "   process = ", processes)
        return dz, processes
"""

def track(lattice, p_array, navi):

    #for elem in lattice.sequence:
    tw0 = get_envelope(p_array)
    tws_track = [tw0]
    L = 0.
    while np.abs(navi.z0 - lattice.totalLen) > 1e-10:
        dz, proc_list = navi.get_next()
        tracking_step(lat=lat, particle_list=p_array, dz=dz, navi=navi)
        for p in proc_list:
            p.apply(p_array, dz)
        print("z0=", navi.z0, dz)
        tw = get_envelope(p_array)
        L += dz
        tw.s += L
        #print (tw.s)
        tws_track.append(tw)
    return tws_track, p_array

csr = SCRProcess()
csr.step = 2
sc = SpaceCharge()

d1 = Drift(l=1)
q1 = Quadrupole(l=0.3, k1=3)
d2 = Drift(l=1)
q2 = Quadrupole(l=0.3, k1=-3)

lat = MagneticLattice([d1, q1, d2, q2])
p_list = [Particle(x=0.001, E=0.15), Particle(y=0.001, E=0.15)]
#p_array = ParticleArray()
#p_array.q_array = np.array([1e-15, 1e-15 ])
p_array, charge_array = astraBeam2particleArray(filename='Exfel.0320.ast')
p_array.q_array = charge_array
#p_array.list2array(p_list)

navi = Navigator(lat)

navi.add_physics_proc(sc, d1, q1)
#navi.add_physics_proc(csr, d1, d2)
navi.unit_step = 0.1

tws_track, p_array = track(lat, p_array, navi)

plt.figure(3)
plt.title(r"$\beta_y - functions$")
plt.plot([p.s for p in tws_track], [p.beta_y for p in tws_track], "ro-", label = "ocelot")
#plt.plot(s_b, betay_b, "bo-", label = "elegant")
plt.legend()
plt.grid(True)
plt.figure(4)
plt.title(r"$\beta_x - functions$")
plt.plot([p.s for p in tws_track], [p.beta_x for p in tws_track], "ro-", label = "ocelot")
#plt.plot(s_b, betax_b, "bo-", label = "elegant")
plt.legend()
plt.grid(True)

plt.show()
