__author__ = 'Sergey Tomin'

from ocelot import *
from ocelot.gui import *
from pylab import *


exec( open("lattice_FLASH_S2E.py" ))

beam = Beam()
beam.E = 148.3148e-3 #in GeV ?!
beam.beta_x = 14.8821
beam.beta_y = 18.8146
beam.alpha_x =  -0.61309
beam.alpha_y = -0.54569
beam.emit_xn = 1.5e-6
beam.emit_yn = 1.5e-6
beam.emit_x = beam.emit_xn / (beam.E / m_e_GeV)
beam.emit_y = beam.emit_yn / (beam.E / m_e_GeV)
beam.tlen=2e-3 # in m


tw0 = Twiss(beam)

lat = MagneticLattice(lattice)
tws_m=twiss(lat, tw0, nPoints=None)
plot_opt_func(lat, tws_m, top_plot = ["Dx", "Dy"], fig_name="optics")
#plt.show()
mx = 1.
my = 1.
Mx_b = []
My_b = []
S = []
for elem, tws in zip(lat.sequence,tws_m[1:]):
    dk = 0.
    if elem.type == "quadrupole":
        dk_k = -0.05
        #if elem.id in ["Q8TCOL", "Q2UBC3", "Q6DBC2"]:
        #    dk_k = np.random.rand()/100.
        dk = dk_k*elem.k1
        elem.k1 = elem.k1*(1. + dk_k)
        mx += 0.5*((dk*elem.l*tws.beta_x*cos(2*tws.mux))**2 + (dk*elem.l*tws.beta_x*sin(2*tws.mux))**2)
        my += 0.5*((dk*elem.l*tws.beta_y*cos(2*tws.muy))**2 + (dk*elem.l*tws.beta_y*sin(2*tws.muy))**2)
        Mx_b.append(mx)
        My_b.append(my)
        S.append(tws.s)



lat = MagneticLattice(lattice)
tws_e=twiss(lat, tw0, nPoints=None)


t = tw0
x = linspace(-sqrt(t.beta_x-1e-7), sqrt(t.beta_x-1e-7), num=200)
#print t.beta_x - x*x
x1 = (sqrt(t.beta_x - x*x) - t.alpha_x*x)/t.beta_x
x2 = (-sqrt(t.beta_x - x*x) - t.alpha_x*x)/t.beta_x
a = sqrt(0.5*((t.beta_x + t.gamma_x) + sqrt((t.beta_x + t.gamma_x)**2 - 4.)))
theta = arctan(-2.*t.alpha_x/(t.beta_x - t.gamma_x))/2.

t = linspace(0, 2*pi, num=100)
xe = a*cos(t)*cos(theta) - 1./a*sin(t)*sin(theta)
ye = a*cos(t)*sin(theta) + 1./a*sin(t)*cos(theta)
plt.plot(x, x1, x, x2)
plt.plot(xe, ye)
plt.show()

Mx = []
My = []
Mx2 = []
My2 = []
for tm, te in zip(tws_m, tws_e):
    bx_n = te.beta_x/tm.beta_x
    by_n = te.beta_y/tm.beta_y

    ax_n = -te.alpha_x + tm.alpha_x*bx_n
    ay_n = -te.alpha_y + tm.alpha_y*by_n

    gx_n = -2.*te.alpha_x*tm.alpha_x + tm.alpha_x**2*bx_n + tm.beta_x*te.gamma_x
    gy_n = -2.*te.alpha_y*tm.alpha_y + tm.alpha_y**2*by_n + tm.beta_y*te.gamma_y

    mx = 0.5*(bx_n + gx_n) + sqrt((bx_n + gx_n)**2 - 4.)
    #print (by_n + gy_n)**2 - 4.
    my = 0.5*(by_n + gy_n) + sqrt((by_n + gy_n)**2 - 4.)

    Mx.append(sqrt(mx))
    My.append(sqrt(my))
    Mx2.append(sqrt(0.5*(tm.beta_x*te.gamma_x - 2.*te.alpha_x*tm.alpha_x + te.beta_x*tm.gamma_x)))
    My2.append(sqrt(0.5*(tm.beta_y*te.gamma_y - 2.*te.alpha_y*tm.alpha_y + te.beta_y*tm.gamma_y)))
s = [p.s for p in tws_m]
bx_e = [p.beta_x for p in tws_e]
bx_m = [p.beta_x for p in tws_m]
plt.plot(s, bx_m,"r", s, bx_e, "b")
plt.show()
plt.plot(s, Mx, "r", s, My, "b")
#plt.plot(s, Mx2, "r.", s, My2, "b.")
plt.plot(S, Mx_b, "ro-", S, My_b, "bo-")
plt.show()

