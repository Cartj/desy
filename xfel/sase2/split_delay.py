'''
split/delay line at MID
without geometry
'''

from copy import deepcopy
from ocelot.optics.utils import *

cr1 = Crystal(r=[0,0,0*cm], size=[5*cm,5*cm,1.8*mum], no=[0,0,-1], id="cr1")
cr1.lattice =  CrystalLattice('Si') 
cr1.psi_n = -pi/2. #input angle psi_n according to Authier (symmetric reflection, Si)

cr2 = Crystal(r=[0,0.1*m,1*m], size=[5*cm,5*cm,150*mum], no=[0,0,-1], id="cr2")
cr2.lattice =  CrystalLattice('Si') 
cr2.psi_n = -pi/2. #input angle psi_n according to Authier (symmetric reflection, Si)


cr3 = Crystal(r=[0,0,0*cm], size=[5*cm,5*cm,500*mum], no=[0,0,-1], id="cr1")
cr3.lattice =  CrystalLattice('Si') 
cr3.psi_n = -pi/2. #input angle psi_n according to Authier (symmetric reflection, Si)



r = Ray()
E_ev = 7000.0 
r.lamb = 2 * pi * hbar * c / E_ev
print 'wavelength', r.lamb


w0 = read_signal(file_name='test/pulse_9kev_20fs.txt', E_ref = E_ev, npad =10) 
w1 = deepcopy(w0) # reflected branch
w2 = deepcopy(w0) # transmitted branch

filter1 = get_crystal_filter(cr1, r, ref_idx=(2,2,0), k = w1.freq_k)
f_test1 = get_crystal_filter(cr1, r, ref_idx=(2,2,0), nk=3000)

filter2 = get_crystal_filter(cr2, r, ref_idx=(2,2,0), k = w1.freq_k)
f_test2 = get_crystal_filter(cr2, r, ref_idx=(2,2,0), nk=3000)

filter3 = get_crystal_filter(cr3, r, ref_idx=(2,2,0), k = w1.freq_k)
f_test3 = get_crystal_filter(cr3, r, ref_idx=(2,2,0), nk=3000)


filter_tot = TransferFunction()
filter_tot.k = filter1.k
filter_tot.ev = filter1.ev
filter_tot.tr = filter1.ref * filter2.ref * filter2.ref * filter1.ref

filter_tot_2 = TransferFunction()
filter_tot_2.k = filter1.k
filter_tot_2.ev = filter1.ev
filter_tot_2.tr = filter1.tr * filter3.ref * filter3.ref * filter3.ref * filter3.ref * filter1.tr

'''
fig = plt.figure()
plot_filters(filter1, f_test1, ax=fig.add_subplot(221))
plot_filters(filter2, f_test2, ax=fig.add_subplot(222))
plot_filters(filter_tot, ax=fig.add_subplot(223))
plot_spec_filt(w1, filter_tot, ax=fig.add_subplot(224))
'''

i1=np.sum(w1.sp*np.conj(w1.sp))*(w1.freq_ev[1] - w1.freq_ev[0])

''' field transformation -- reflected branch'''
w1.sp = w1.sp * filter_tot.tr
w1.f = w1.f_ = np.fft.ifft(w1.sp)

''' field transformation -- transmission branch'''
w2.sp = w2.sp * filter_tot_2.tr
w2.f = w2.f_ = np.fft.ifft(w2.sp)


i2=np.sum(w1.sp*np.conj(w1.sp))*(w1.freq_ev[1] - w1.freq_ev[0])

i1_=np.sum(w0.f*np.conj(w0.f))*(w0.t[1] - w0.t[0])
i2_ = np.sum(w1.f*np.conj(w1.f))*(w1.t[1] - w1.t[0])

print 'branch 1 transmission (%)', 100*np.real(i2/i1), 100*np.real(i2_/i1_) 

i2=np.sum(w2.sp*np.conj(w2.sp))*(w2.freq_ev[1] - w0.freq_ev[0])

i1_=np.sum(w0.f*np.conj(w0.f))*(w0.t[1] - w0.t[0])
i2_ = np.sum(w2.f*np.conj(w2.f))*(w2.t[1] - w2.t[0])

print 'branch 2 transmission (%)', 100*np.real(i2/i1), 100*np.real(i2_/i1_) 


fig=plt.figure()
plt.grid(True)
ax = fig.add_subplot(111)
ax.plot(w1.t, np.abs(w1.f), 'b-', lw=3)
ax.plot(w0.t, np.abs(w0.f), 'r--', lw=3)
fig=plt.figure()
plt.grid(True)
ax = fig.add_subplot(111)    
ax.plot(w1.freq_ev, np.abs(w1.sp), 'b-', lw=3)
ax.plot(w0.freq_ev, np.abs(w0.sp), 'r--', lw=3)


fig=plt.figure()
plt.grid(True)
ax = fig.add_subplot(111)
ax.plot(w2.t, np.abs(w2.f), 'b-', lw=3)
ax.plot(w0.t, np.abs(w0.f), 'r--', lw=3)
fig=plt.figure()
plt.grid(True)
ax = fig.add_subplot(111)    
ax.plot(w2.freq_ev, np.abs(w2.sp), 'b-', lw=3)
ax.plot(w0.freq_ev, np.abs(w0.sp), 'r--', lw=3)


plt.show()
