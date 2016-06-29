__author__ = 'Igor Zagorodnov'

from ocelot.cpbd.wake3D import *
from ocelot.gui import *

drive='d:/'
Ns=500              # wake sampling
NF=20               # smoothing filter order    

beam = Beam()
beam.E = 17.5 #in GeV
beam.beta_x = 22.5995
beam.beta_y = 22.5995
beam.alpha_x =  -1.4285
beam.alpha_y = 1.4285
beam.emit_xn = 1e-6
beam.emit_yn = 1e-6
beam.emit_x = beam.emit_xn / (beam.E / m_e_GeV)
beam.emit_y = beam.emit_yn / (beam.E / m_e_GeV)

tw0 = Twiss(beam)
from lattice0 import *
lat = MagneticLattice(lattice)

tws=twiss(lat, tw0, nPoints=None)
#plot_opt_func(lat, tws, top_plot=["E"])

drive='d:/'
filename=drive+'TEST_DECHIRPER/ASTRA/XFEL01_ideal/LCLS.ast'
p_array, charge_array, z0,gamref = astraBeam2particleArray(filename)


# plot current
bins_start, hist_start = get_current(p_array, charge=charge_array[0], num_bins=200)


dz = 0.2
order = 2
bWake = True
bDebug = False
bKick = True

#Z = np.linspace(0, 2, num=int(2.0/dz)+1)
Z = np.linspace(0, lat.totalLen, num=int(lat.totalLen/dz)+1)

twsi=twiss(lat, tw0, nPoints=len(Z) )
tw0 = get_envelope(p_array, tws_i = twsi[0])
tws_track = [tw0]

if bDebug:
    f=plt.figure()
    plt.ion()
    plt.hold(False)

Ps = p_array.particles.view()
Np = len(Ps)/6
Ps.shape = (Np, 6)
if bWake:
    wakeFile=drive+'TEST_DECHIRPER/ECHO/Wakes/wake_hor_1m.txt'
    THh=LoadWakeTable (wakeFile)
    wakeFile=drive+'TEST_DECHIRPER/ECHO/Wakes/wake_vert_1m.txt'
    THv=LoadWakeTable (wakeFile)


navi = Navigator(lattice=lat)
for i, zi in enumerate(Z[1:]):
    dz = zi - Z[i]
    tracking_step(lat=lat, particle_list=p_array, dz=dz, navi=navi, order=order)
    
    if bWake:
        Px=0
        Py=0
        Pz=0
        ziw=zi-dz*0.5
        if (1.0<ziw<=3.0)or(5.0<ziw<=7.0):# or(10.0<ziw<=12.0):
            Px,Py,Pz,I00=AddTotalWake (Ps[:,0],Ps[:,2],Ps[:,4],charge_array,THv,Ns,NF)
        if (3.0<ziw<=5.0): #or(8.0<ziw<=10.0)or(12.0<ziw<=14.0):
            Px,Py,Pz,I00=AddTotalWake (Ps[:,0],Ps[:,2],Ps[:,4], charge_array,THh,Ns,NF)
        print (zi, dz, ziw)
        p_array.particles[5::6]=p_array.particles[5::6]+Pz*dz/(p_array.E*1e9)
        p_array.particles[3::6]=p_array.particles[3::6]+Py*dz/(p_array.E*1e9)
        p_array.particles[1::6]=p_array.particles[1::6]+Px*dz/(p_array.E*1e9)
    tw = get_envelope(p_array,tws_i=twsi[i+1])
    tw.s = navi.z0
    #print tw.s, twsi[i+1].s
    tws_track.append(tw)
    if bDebug:
        f.add_subplot(211)
        plt.plot(p_array.particles[::6], p_array.particles[2::6], '.')
        f.add_subplot(212)
        plt.plot(p_array.particles[4::6],p_array.particles[5::6],'.')
        plt.draw()
        plt.pause(0.1)
plt.ioff()

plt.figure(1)
plt.plot(p_array.particles[4::6],p_array.particles[5::6]+p_array.E,'.')

#output
s_p=[t.s for t in tws_track]
n_out=len(s_p)
out=np.zeros((n_out,3))
out[:,0]=s_p
out[:,1]=[t.beta_x for t in tws_track]
out[:,2]=[t.beta_y for t in tws_track]
#np.savetxt('D:/pyoptics.txt',out)
np.savetxt('pyoptics_withoutSC.txt',out)

particleArray2astraBeam(p_array,charge_array,0,'d:/ocelot.ast')

# plot current at the beginning of accelerator
#plt.figure(1)
#plt.title("current: start")
#plt.plot(bins_start, hist_start)
#plt.xlabel("s, m")
#plt.ylabel("I, A")
#plt.grid(True)

# plot current at the end of accelerator
#bins, hist = get_current(p_array, charge=charge_array[0], num_bins=200)
#plt.figure(2)
#plt.title("current: end")
#plt.plot(bins, hist)
#plt.xlabel("s, m")
#plt.ylabel("I, A")
#plt.grid(True)


st=[p.s for p in tws_track]
s=[p.s for p in tws]
plt.figure(3)
plt.title(r"$\beta - functions$")
plt.plot(st, [p.beta_x for p in tws_track], "ro-")
plt.hold(True)
plt.plot(s, [p.beta_x for p in tws], "r-")
plt.plot(st, [p.beta_y for p in tws_track], "bo-")
plt.plot(s, [p.beta_y for p in tws], "b-")
plt.legend()
plt.grid(True)

em_x=[p.emit_x for p in tws_track]
em_y=[p.emit_y for p in tws_track]
em_x=em_x/em_x[0]
em_y=em_y/em_y[0]
plt.figure(4)
#plt.title(r"$\emittances$")
plt.plot(st, em_x, "ro-")
plt.hold(True)
plt.plot(st, em_y, "bo-")
#plt.ylim(0.95,1.05)
plt.legend()
plt.grid(True)
plt.show()

