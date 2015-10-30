#from xls2xcode import *
from pylab import *

from ocelot.adaptors.eleg2xcode import *
from ocelot.cpbd.beam import *
from ocelot.cpbd.optics import *
from ocelot.cpbd.io import *

#import pickle


beam = Beam()
beam.E = 2.4000047
beam.sigma_E = 0.0
beam.I = 2.5e-10
beam.emit_x = 1.752e-9
beam.emit_y = 1.752e-9

beam.beta_x =  41.1209
beam.beta_y = 86.3314
beam.alpha_x = 1.9630
beam.alpha_y = 4.0972


dir_name='./xfel/'
file_flo=dir_name+'XFEL_BC2_flo.txt'
file_par=dir_name+'XFEL_BC2_par.txt'
lat_def = read_lattice_elegant(file_flo,file_par)

z_shift=0
z_start=0-z_shift
z_stop=50.1917045455325-z_shift

lat_def=insert_drifts(z_start,z_stop,lat_def)

#f=open('dump.txt','wt')
#pickle.dump(lat_def, f)
#f.close() 
 
    
tw0 = Twiss(beam)

lat = MagneticLattice(lat_def, beam.E)
lat.printElements()
write_lattice(lat, file_name = "lattice_Igor.txt")

tws=twiss(lat, tw0, nPoints = 10000)



file_opt=dir_name+'XFEL_BC2_twi.txt'    
#f=open(file_opt,'rb')
#dd=csv.reader(f)
#for row in dd:
#    print row
#f.close()

dd = np.genfromtxt(file_opt)
s_dd=dd[:,0]
betax_dd=dd[:,1]
betay_dd=dd[:,7]


f=plt.figure()
f.add_subplot(111)
p1, = plt.plot(map(lambda p: p.s, tws), map(lambda p: p.beta_x, tws))
p2, = plt.plot(s_dd-z_start-z_shift,betax_dd,'--')
plt.grid(True)
p3, = plt.plot(map(lambda p: p.s, tws), map(lambda p: p.beta_y, tws))
p4, = plt.plot(s_dd-z_start-z_shift,betay_dd,'--')
plt.legend([p1,p2,p3,p4], [r'$\beta_x [m]$',r'design $\beta_x [m]$'])

#xlim(0, 100)
#ylim(0, 70)
plt.show()

#for tw in tws:
#    print tw.s







    
