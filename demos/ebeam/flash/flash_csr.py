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
lat = MagneticLattice(lattice, method=method)
tws=twiss(lat, tw0, nPoints=None)

#plot_opt_func(lat, tws, top_plot=["E"])
#plt.show()
particle = Particle(E=beam.E)



#p_array, charge_array = astraBeam2particleArray(filename='elegant_files/flash_out_200000.ast')
#particleArray2astraBeam(p_array,charge_array, filename="start_BC3.ast")
p_array, charge_array = astraBeam2particleArray(filename='start_BC3.ast')
bins_start, hist_start = get_current(p_array, charge=charge_array[0], num_bins=200)

dz = 0.2
order = 2
CSR = True

#start_csr = D1BC3
start_csr = D00982
stop_csr = WATCHBC3_2

csr_traj = csr_track(particle, lat, start=start_csr, stop=stop_csr)

idx_start = lat.sequence.index(start_csr)
idx_stop = lat.sequence.index(stop_csr)

csr_z = sum([p.l for p in lat.sequence[:idx_start]])
print("indexes = ", idx_start, idx_stop, csr_z)

lat = MagneticLattice(lattice, stop=stop_csr, method=method)
print("lat.totalLen = ", lat.totalLen)
navi = Navigator(lattice=lat)
print("####", csr_z, lat.totalLen, int((lat.totalLen - csr_z)/dz+1.))
Z = np.linspace(csr_z, lat.totalLen, num=int((lat.totalLen - csr_z)/dz+1.))
Z = np.append([0, csr_z], Z)
print( Z)
#particleArray2astraBeam(p_array,charge_array, filename="before_BC3.ast")
for i, zi in enumerate(Z[1:]):
    dz = zi - Z[i]
    print("z = ", zi, navi.n_elem, idx_start <= navi.n_elem <= idx_stop)
    tracking_step(lat=lat, particle_list=p_array, dz=dz, navi=navi)
    print("z0=", navi.z0)
    #p_array.particles[4::6] = sc.smooth_z(p_array.particles[4::6], mslice=10000)
    #if zi == csr_z :
    #    particleArray2astraBeam(p_array, charge_array, filename="before_BC3.ast")
    if CSR and idx_start <= navi.n_elem <= idx_stop:
        if zi-csr_z <= 0:
            continue
        else:
            print(navi.z0, csr_z, zi-csr_z, dz)
            csr_apply(particle_list=p_array, charge_array=charge_array, delta_s=dz, s_cur=zi-csr_z, csr_traj=csr_traj)
        #print(zi-csr_z, idx_start <= navi.n_elem <= idx_stop)
    #print(np.around(zi, decimals=3))
    #if np.around(zi, decimals=3) == 68.278:
    #    particleArray2astraBeam(p_array, charge_array,  filename="after_BC3.ast")

#bins_end, hist_end = get_current(p_array, charge=charge_array[0], num_bins=200)

p_array_csrtr, charge_array_csrtr = astraBeam2particleArray(filename='elegant_files/bc2_out_CSR.ast')
plt.figure(1)
plt.title("Trajectory")
plt.xlabel("z, m")
plt.ylabel("x, m")
plt.grid(True)
plt.plot(csr_traj[3,:], csr_traj[1,:], "r")

plt.figure(2)
plt.title("energy: end")
plt.plot(p_array_csrtr.particles[4::6], p_array_csrtr.particles[5::6], "r.")
plt.plot(p_array.particles[4::6], p_array.particles[5::6], "b.")
plt.xlabel("s, m")
plt.ylabel("dp/p")
plt.grid(True)

#p_array, charge_array = astraBeam2particleArray(filename='after_BC3.ast')
plt.figure(4)
plt.title("energy: end")
plt.plot(p_array.particles[4::6], p_array.particles[5::6], "r.")
plt.xlabel("s, m")
plt.ylabel("dp/p")
plt.grid(True)

# plot current at the end of accelerator
bins, hist = get_current(p_array, charge=charge_array[0], num_bins=200)
plt.figure(3)
plt.title("current: end")
plt.plot(bins, hist)
plt.xlabel("s, m")
plt.ylabel("I, A")
plt.grid(True)
plt.show()

