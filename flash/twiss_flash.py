from ocelot.cpbd.beam import *
from ocelot.cpbd.elements import *
from ocelot.cpbd.optics import *
from ocelot.cpbd.io import *
from pylab import *
import csv
from ocelot.gui.accelerator import plot_lattice

E00=5.109986258350895e+05

beam = Beam()
beam.sigma_E = 0.0
beam.I = 2.5e-10
beam.emit_x = 1.752e-6
beam.emit_y = 1.752e-6


#20.236    21.5451611025405    4.22017522554549    4.1536706751481    0    0    10    16.8893495037859    -0.157515104668462    4.09289993317716    0    0    10    313.161522378336    BPM2UBC2    1    MONI
#beam.E = 0.16
#beam.beta_x = 21.5451611025405  
#beam.beta_y = 16.8893495037859   
#beam.alpha_x =  4.22017522554549   
#beam.alpha_y = -0.157515104668462
#s_start=20.236
#z_start=20.236
#z_stop=70


#134.3806    3.3468262673592    -0.279089998616206    17.7194869420802    -3.95575614252603e-011    -3.70422242130536e-011    10    39.9219299844044    -2.20432941093178    20.3432164242085    0    0    10    2348.39165408049    WAKE10ACC7    1    MARK
#134.3806    7.29347046376193e-005    0    134.271581455747
beam.E = 1.2
beam.beta_x = 3.3468262673592  
beam.beta_y = 39.9219299844044   
beam.alpha_x =  -0.279089998616206   
beam.alpha_y = -2.20432941093178

s_start=20.236
s_stop=233.821836974389


beam.E = 0.16
beam.beta_x = 21.5451611025405  
beam.beta_y = 16.8893495037859   
beam.alpha_x =  4.22017522554549   
beam.alpha_y = -0.157515104668462



    
tw0 = Twiss(beam)


exec( open('flash.lat'))
lat = MagneticLattice(lattice, beam.E)



#tws=twiss(lat, tw0, nPoints = 1000)



tws=twiss(lat, tw0)
lat.update_transfer_maps()
tws=twiss(lat, tw0)


f=plt.figure()
ax=f.add_subplot(211)
s =  np.array(map(lambda p: p.s, tws))+s_start;
p1, = plt.plot(s, map(lambda p: p.beta_x, tws))
p3, = plt.plot(s, map(lambda p: p.beta_y, tws))
ax2 = ax.twinx()
p4, = ax2.plot(s, map(lambda p: p.Dx, tws), 'r--')
plt.grid(True)
xlim(s_start, s_stop)




ax2 = f.add_subplot(212)
p5, = ax2.plot(s, map(lambda p: 1.e-12*p.alpha_x, tws))
#p2, = plt.plot(map(lambda p: p.s, tws), map(lambda p: p.beta_y, tws), '--')
xlim(s_start, s_stop)
ax2.set_ylim(-100, 100)

p7, = plt.plot(s, map(lambda p: 1.e-12*p.alpha_y, tws))
plt.grid(True)
plot_lattice(lat, ax2, alpha=0.5, params={'kmax':10.0, 'ang_max':4.0e-1}, s_start = s_start)

ax3 = ax2.twinx()
xlim(s_start, s_stop)
ax3.set_ylabel('E [GeV]')
p8, = ax3.plot(s, map(lambda p: p.E, tws), 'g--', lw=4, alpha = 0.4)


'''
aperture plot [mm]
'''
sig_x = 1.e3*np.array(map(lambda p: np.sqrt(p.beta_x*beam.emit_x / ( p.E / 0.000511 ) ), tws)) # 0.03 is for plotting same scale
sig_y = 1.e3*np.array(map(lambda p: np.sqrt(p.beta_y*beam.emit_y / ( p.E / 0.000511 )), tws))

x = 1.e3*np.array(map(lambda p: p.x, tws))
y = 1.e3*np.array(map(lambda p: p.y, tws))


f=plt.figure()
f.add_subplot(111)
s =  np.array(map(lambda p: p.s, tws))+s_start;
plt.plot(s, x+sig_x, 'b-')
plt.plot(s, x-sig_x, 'b-')
plt.plot(s, y+sig_y, 'g-')
plt.plot(s, y-sig_y, 'g-')

#p3, = plt.plot(s, map(lambda p: p.y, tws), 'g-')
plt.grid(True)

xlim(s_start, s_stop)



plt.show()






    
