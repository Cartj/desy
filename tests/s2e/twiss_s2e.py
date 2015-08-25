#from xls2xcode import *
from eleg2xcode import *
from ocelot.cpbd.beam import *
from ocelot.cpbd.optics import *
from ocelot.cpbd.io import *
from pylab import *
import csv

E00=5.109986258350895e+05

beam = Beam()
beam.sigma_E = 0.0
beam.I = 2.5e-10
beam.emit_x = 1.5e-6
beam.emit_y = 1.5e-6

beam.E = 148.3148e-3 #in GeV
beam.beta_x = 14.8821  
beam.beta_y = 18.8146   
beam.alpha_x =  -0.61309   
beam.alpha_y = -0.54569
s_start=0
z_start=0
z_stop=190

dir_name='./flash/elegant_old/'
file_flo=dir_name+'FLASH_S2E_flo.txt'
file_par=dir_name+'FLASH_S2E_par.txt'
lat_def = read_lattice_elegant(file_flo,file_par)


lat_def=insert_drifts(z_start,z_stop,lat_def)  
    
tw0 = Twiss(beam)

lat = MagneticLattice(lat_def, beam.E)

write_lattice(lat, file_name = "lattice_FLASH_S2E.txt")




tws=twiss(lat, tw0)
lat.update_transfer_maps()
tws=twiss(lat, tw0, nPoints = 10000)

file_opt=dir_name+'FLASH_S2E_twi.txt'    


dd = np.genfromtxt(file_opt)
s_dd=dd[:,0]
betax_dd=dd[:,1]
alphax_dd=dd[:,2]
betay_dd=dd[:,7]
alphay_dd=dd[:,8]
energy_dd=dd[:,13]*E00*1e-6


f=plt.figure()
f.add_subplot(311)
s =  np.array(map(lambda p: p.s, tws))+s_start;
p1, = plt.plot(s, map(lambda p: p.beta_x, tws))
#p2, = plt.plot(map(lambda p: p.s, tws), map(lambda p: p.beta_y, tws), '--')
p2, = plt.plot(s_dd,betax_dd,'--.')

p3, = plt.plot(s, map(lambda p: p.beta_y, tws))
p4, = plt.plot(s_dd,betay_dd,'--.')
plt.grid(True)
plt.legend([p1,p2,p3,p4], [r'$\beta_x [m]$',r'design $\beta_x [m]$'])

xlim(z_start,z_stop)
ylim(0, 50)



f.add_subplot(312)
p5, = plt.plot(s, map(lambda p: p.alpha_x, tws))
p6, = plt.plot(s_dd,alphax_dd,'--.')

p7, = plt.plot(s, map(lambda p: p.alpha_y, tws))
p8, = plt.plot(s_dd,alphay_dd,'--.')
plt.grid(True)
plt.legend([p5,p6,p7,p8], [r'$\alpha_x [m]$',r'design $\alpha_x [m]$'])

xlim(z_start,z_stop)
ylim(-10, 10)


f.add_subplot(313)
p9, = plt.plot(s_dd,energy_dd,'--')
Energy =  np.array(map(lambda p: p.E, tws))
p10, = plt.plot(s,Energy*1e3)
plt.grid(True)
plt.legend([p10], [r'$energy$'])

xlim(z_start,z_stop)


plt.show()








    
