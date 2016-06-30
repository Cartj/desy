from ocelot import MagneticLattice

__author__ = 'Sergey Tomin'

from ocelot.gui import *
from ocelot.adaptors import *
#from desy.demos.ebeam.flash.BC2_csr import *
from desy.demos.ebeam.flash.lattice_FLASH_S2E import *
#from arcline import *
from ocelot.cpbd.csr_old import *




beam = Beam()
beam.E = 130.3148e-3 #in GeV ?!
#beam.beta_x = 22.220928956876175
#beam.beta_y =  24.862675023233528
#beam.alpha_x = -0.9443235467729223
#beam.alpha_y = -0.7496068140092198
beam.beta_x = 14.8821
beam.beta_y = 18.8146
beam.alpha_x =  -0.61309
beam.alpha_y = -0.54569
beam.emit_xn = 1.5e-6
beam.emit_yn = 1.5e-6
beam.emit_x = beam.emit_xn / (beam.E / m_e_GeV)
beam.emit_y = beam.emit_yn / (beam.E / m_e_GeV)


tw0 = Twiss(beam)
method = MethodTM()
method.global_method = SecondTM
#lat = MagneticLattice(lattice, method=method)
#tws=twiss(lat, tw0, nPoints=None)
#
#plot_opt_func(lat, tws, top_plot=["Dx"])
#plt.show()
#particle = Particle(E=beam.E)



#p_array, charge_array = astraBeam2particleArray(filename='elegant_files/flash_out_200000.ast')
#particleArray2astraBeam(p_array,charge_array, filename="start_BC3.ast")
p_array, charge_array = astraBeam2particleArray(filename='start_BC3.ast')
bins_start, hist_start = get_current(p_array, charge=charge_array[0], num_bins=200)


from ocelot.cpbd.csr import *

lat = MagneticLattice(lattice, stop=WATCHBC3_2, method=method)
csr = CSR()
csr.step = 1
#sc = SpaceCharge()


p_array.q_array = charge_array
#p_array.list2array(p_list)

navi = Navigator(lat)

#navi.add_physics_proc(sc, lat.sequence[0], lat.sequence[-1])
navi.add_physics_proc(csr, D00982, WATCHBC3_2)
navi.unit_step = 0.05
print("### ", csr.z_csr_start, lat.totalLen)
tws_track, p_array = track(lat, p_array, navi)

p_array_csrtr, charge_array_csrtr = astraBeam2particleArray(filename='elegant_files/bc2_out_CSR.ast')
plt.figure(1)
plt.title("Trajectory")
plt.xlabel("z, m")
plt.ylabel("x, m")
plt.grid(True)
plt.plot(csr.csr_traj[3,:], csr.csr_traj[1,:], "r")

plt.figure(2)
plt.title("energy: end")
plt.plot(p_array_csrtr.particles[4::6], p_array_csrtr.particles[5::6], "r.")
plt.plot(p_array.particles[4::6], p_array.particles[5::6], "b.")
plt.xlabel("s, m")
plt.ylabel("dp/p")
plt.grid(True)

#p_array, charge_array = astraBeam2particleArray(filename='after_BC3.ast')
#plt.figure(4)
#plt.title("energy: end")
#plt.plot(p_array.particles[4::6], p_array.particles[5::6], "r.")
#plt.xlabel("s, m")
#plt.ylabel("dp/p")
#plt.grid(True)

# plot current at the end of accelerator
bins, hist = get_current(p_array, charge=charge_array[0], num_bins=200)
plt.figure(3)
plt.title("current: end")
plt.plot(bins, hist)
plt.xlabel("s, m")
plt.ylabel("I, A")
plt.grid(True)
plt.show()

