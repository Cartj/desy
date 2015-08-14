__author__ = 'Sergey Tomin'

from ocelot.cpbd.elements import *
from ocelot.cpbd.optics import *
from ocelot.cpbd.track import *
from ocelot.gui.accelerator import *
import matplotlib.pyplot as plt
from copy import deepcopy

Q1 = Quadrupole(l=0.2, k1=5)
Q2 = Quadrupole(l=0.2, k1=-5)
Db = Drift(l=2)
Dc = Drift(l=3/2.)

# to get non dispersive section
angle = 45.*pi/180.
phi = Q1.l*sqrt(Q1.k1)
Lc = 2.*Dc.l + Q2.l
ro = (1./sqrt(Q1.k1)*(Lc*sqrt(Q1.k1)*cos(phi) + 2.*sin(phi))/(Lc*sqrt(Q1.k1)*sin(phi) - 2.*cos(phi)) - Db.l)/tan(angle/2.)


B1 = SBend(l = ro*angle, angle=-angle)
B2 = SBend(l = ro*angle, angle=angle)
lattice = [B1, Db, Q1, Dc, Q2, Dc, Q1, Db, B2]

lat = MagneticLattice(lattice)
tw0 = Twiss()
tw0.beta_x = 5.
tw0.alpha_x = 1.4
tw0.beta_y = 16
tw0.alpha_y = 5.1

tws = twiss(lat, tw0, nPoints=500)

plot_opt_func(lat, tws)
plt.show()


def H2(vec_x, h, k1, beta=1.):
    """
    H2 = (px**2 + py**2)/2 + (h**2 + k1)*x**2/2 - (k1*y**2)/2 - (h*pt*x)/beta
    :param vec_x: [x, px, y, py, sigma, psigma]
    :param h: curvature
    :param k1: quadrupole strength
    :param beta: = 1, velocity
    :return: [x', px', y', py', sigma', psigma']
    """
    x = vec_x[0]
    px = vec_x[1]
    y = vec_x[2]
    py = vec_x[3]
    ps = vec_x[5]

    x1 = px
    px1 = -(h*h + k1)*x + (h*ps)/beta
    y1 = py
    py1 = k1*y
    sigma1 = -(h*x)/beta
    return array([x1, px1, y1, py1, sigma1, 0.])


def H3(vec_x, h, k1, k2, beta=1., g_inv=0.):
    """
    H3 = (h*x - ps/beta)*(px**2 + py**2)/2 + (2*h*k1 + k2)*(x**3)/6 - (h*k1 + k2)*(x*y**2)/2 - ps/(beta*gamma**2*(1. + beta))
    :param vec_x: [x, px, y, py, sigma, psigma]
    :param h: curvature
    :param k1: quadrupole strength
    :param k2: sextupole strength
    :param beta: = 1, velocity
    :param g_inv: 1/gamma, by default 0.
    :return: [x', px', y', py', sigma', psigma']
    """
    x = vec_x[0]
    px = vec_x[1]
    y = vec_x[2]
    py = vec_x[3]
    ps = vec_x[5]
    px2 = px*px
    py2 = py*py
    x1 = px*(h*x - ps/beta)
    px1 = (-h*(px2 + py2) - (2.*h*k1 + k2)*x*x + (h*k1 + k2)*y*y)/2.
    y1 = py*(h*x - ps/beta)
    py1 = (h*k1 + k2)*x*y
    sigma1 = -((px2 + py2)/(2.*beta)) - g_inv*g_inv/(beta*(1. + beta))
    return array([x1, px1, y1, py1, sigma1, 0.])


def H4(vec_x, h, k1, k2, k3, beta=1., g_inv=0.):
    """
    H4 = (px**2 + py**2)**2/8 + (3*h*k2 + k3)*(x**4)/24 - (2*h*k2 + k3)*(x**2*y**2)/4 -
            y**4/24*(h**2*k1 - h*k2 - k3) - pt/(2*beta)*(h*x - pt*beta)*(px**2 + py**2) +
            pt**2/(2*beta**2*gamma**2)
    :param vec_x: [x, px, y, py, sigma, psigma]
    :param h: curvature
    :param k1: quadrupole strength
    :param k2: sextupole strength
    :param k3: octupole strength
    :param beta: = 1, velocity
    :param g_inv: 1/gamma, by default 0.
    :return: [x', px', y', py', sigma', psigma']
    """
    b2 = beta*beta
    x = vec_x[0]
    px = vec_x[1]
    y = vec_x[2]
    py = vec_x[3]
    ps = vec_x[5]
    x2 = x*x
    y2 = y*y
    px2 = px*px
    py2 = py*py
    ps2 = ps*ps
    x1 = (px*(2.*ps2 - 2.*h*ps*x*beta + (px2 + py2)*b2))/(2.*b2)
    px1 = (-(3.*h*k2 + k3)*x2*x + 3.*(2.*h*k2 + k3)*x*y2 + (3.*h*ps*(px2 + py2))/beta)/6.
    y1 = py*(2.*ps2 - 2.*h*ps*x*beta + (px2 + py2)*b2)/(2.*b2)
    py1 = y*(3.*(2.*h*k2 + k3)*x2 + (h**2*k1 - h*k2 - k3)*y2)/6.
    sigma1 = ps*(px2 + py2)/(2.*b2) - (px2 + py2)*(h*x - ps/beta)/(2.*beta) + g_inv*g_inv*ps/b2
    return array([x1, px1, y1, py1, sigma1, 0.])


def H_exact(vec_x, h, k1, k2, k3, beta=1., g_inv=0):
    """
    H = pt - (1 + h*x)*sqrt(1 + 2*pt/beta + pt**2 - px**2 - py**2) - (1 + h*x)*As
    As = -h*(x - h*x**2/2 + h**2*x**3/2 - h**3*x**4/2) -
         k1*((x**2 - y**2)/2 - h*x**3/6 + h**2*(4*x**4 - y**4)/24) -
         k2*((x**3 - 3*x*y**2)/6 - h*(x**4 - y**4)/24) -
         k3*((x**4 - 6*x**2*y**2 + y**4)/24);
    :param vec_x: [x, px, y, py, sigma, psigma]
    :param h: curvature
    :param k1: quadrupole strength
    :param k2: sextupole strength
    :param k3: octupole strength
    :param beta: = 1, velocity
    :param g_inv: 1/gamma, by default 0.
    :return: [x', px', y', py', sigma', psigma']
    """
    b2 = beta*beta
    x = vec_x[0]
    px = vec_x[1]
    y = vec_x[2]
    py = vec_x[3]
    ps = vec_x[5]
    x2 = x*x
    y2 = y*y
    px2 = px*px
    py2 = py*py
    ps2 = ps*ps
    sq_p = sqrt(1. + ps2 - px2 - py2 + (2.*ps)/beta)
    x1 = (px*(1 + h*x))/sq_p
    px1 = (60*h**5*x2*x2 - 4.*(6.*k1*x + 3.*k2*x2 + k3*x2*x - 3.*k2*y2 - 3.*k3*x*y2) +
                h**3*k1*(-20.*x2*x2 + y2*y2) + h*h*(-24.*x + 5.*k2*x**4 - k2*y2*y2) +
                h*(-24. - 12.*k2*x2*x - 5.*k3*x2*x2 + 24.*k2*x*y2 + 18.*k3*x2*y2 -
                k3*y2*y2 + 12.*k1*(-2.*x2 + y2) + 24.*sq_p))/24.
    y1 = (py*(1 + h*x))/sq_p
    py1 = (1 + h*x)*y*(6*k2*x + 3*k3*x2 - h*k2*y2 - k3*y2 + k1*(6. + h*h*y2))/6.
    sigma1 = 1. - (1. + h*x)*(2.*ps + 2./beta)/(2.*sq_p)
    return array([x1, px1, y1, py1, sigma1, 0])

def eq_second(vec_x, h, k1, k2, k3, beta=1., g_inv=0):
    """
    :param vec_x: [x, px, y, py, sigma, psigma]
    :param h: curvature
    :param k1: quadrupole strength
    :param k2: sextupole strength
    :param k3: octupole strength
    :param beta: = 1, velocity
    :param g_inv: 1/gamma, by default 0.
    :return: [x', px', y', py', sigma', psigma']
    """
    x = vec_x[0]
    px = vec_x[1]
    y = vec_x[2]
    py = vec_x[3]
    ps = vec_x[5]
    x2 = x*x
    y2 = y*y
    px2 = px*px
    py2 = py*py
    ps2 = ps*ps
    x1 = px
    x11 = -(h*h +k1)*x + h*ps - x2*(h**3 + 2.*h*k1 + k2/2.) + (2.*h*h +k1)*ps*x + y2*(h*k1+k2)/2. - h*ps2 + h*(px2 - py2)/2.
    y1 = py
    y11 = k1*y + x*y*(2*h*k1 + k2) + h*px*py - k1*ps*y
    return array([x1, x11, y1, y11, 0., 0.])


def eq_second_from_H(vec_x, h, k1, k2, k3, beta=1., g_inv=0):
    """
    :param vec_x: [x, px, y, py, sigma, psigma]
    :param h: curvature
    :param k1: quadrupole strength
    :param k2: sextupole strength
    :param k3: octupole strength
    :param beta: = 1, velocity
    :param g_inv: 1/gamma, by default 0.
    :return: [x', px', y', py', sigma', psigma']
    """
    x = vec_x[0]
    px = vec_x[1]
    y = vec_x[2]
    py = vec_x[3]
    ps = vec_x[5]
    x2 = x*x
    y2 = y*y
    px2 = px*px
    py2 = py*py
    ps2 = ps*ps
    x1 = px
    x11 = px2*h/(1. + h*x - ps) + (1. + h*x - ps)*(-h*(px2 + py2) - 2.*(h*h + k1)*x - (2.*h*k1 + k2)*x2 + (h*k1 + k2)*y2 + (2.*h*ps)/beta)/2.
    y1 = py
    y11 = py*px*h/(1. + h*x - ps) + (1.+h*x-ps)*(k1 + h*k1*x + k2*x)*y
    return array([x1, x11, y1, y11, 0., 0.])

def H2H3(vec_x, h, k1, k2, k3, beta=1., g_inv=0):
    """
    :param vec_x: [x, px, y, py, sigma, psigma]
    :param h: curvature
    :param k1: quadrupole strength
    :param k2: sextupole strength
    :param k3: octupole strength
    :param beta: = 1, velocity
    :param g_inv: 1/gamma, by default 0.
    :return: [x', px', y', py', sigma', psigma']
    """
    x = vec_x[0]
    px = vec_x[1]
    y = vec_x[2]
    py = vec_x[3]
    ps = vec_x[5]
    x2 = x*x
    y2 = y*y
    px2 = px*px
    py2 = py*py
    ps2 = ps*ps
    x1 = px*(1. + h*x - ps)
    x11 = (-h*(px2 + py2) - 2.*(h*h + k1)*x - (2.*h*k1 + k2)*x2 + (h*k1 + k2)*y2 + (2.*h*ps)/beta)/2.
    y1 = py*(1. + h*x - ps)
    y11 = (k1 + h*k1*x + k2*x)*y
    return array([x1, x11, y1, y11, 0., 0.])


p1 = Particle(x=0.00, p=0.05)
p2 = Particle(x=0.00, p=0.05)
P1 = [copy(p1)]
P2 = [copy(p2)]
navi1 = Navigator()
navi2 = Navigator()
dz = 0.01

for i in range(int(lat.totalLen/dz)):
    step(lat, [p1], dz=dz, navi=navi1, order=1)  # R only
    step(lat, [p2], dz=dz, navi=navi2, order=2)  # R + T
    P1.append(copy(p1))
    P2.append(copy(p2))

s = [p.s for p in P1]
x1_tr = [p.x for p in P1]
x2_tr = [p.x for p in P2]
px1_tr = [p.px for p in P1]
px2_tr = [p.px for p in P2]
tau1_tr = [p.tau for p in P1]
tau2_tr = [p.tau for p in P2]

Btest = SBend(l = 5, angle=30.*pi/180., k1=1)
lat_test = MagneticLattice([Btest])

p3 = Particle(x=0.00, p=0.05)
P3 = [copy(p3)]
navi3 = Navigator()

dz_test = 0.001

for i in range(int(lat_test.totalLen/dz_test)):
    step(lat_test, [p3], dz=dz, navi=navi3, order=2)
    P3.append(copy(p3))
s_test = [p.s for p in P3]
x_test = [p.x for p in P3]


from scipy.integrate import odeint

l = 0.
L = [l]
for elem in lat.sequence:
    l += elem.l
    L.append(l)

def params(s, L):
    inx = np.where(array(L)<=s)[0]
    if len(inx) == 0:
        inx = 0
    else:
        inx = inx[-1]

    if inx == len(L)-1:
        inx -= 1

    h = lat.sequence[inx].transfer_map.hx
    k1 = lat.sequence[inx].k1
    #print s, inx, L[inx+1]
    return [h, k1]


h = lambda t: params(t, L)[0]
k1 = lambda t: params(t, L)[1]

def func_H234(vec_x, s, d3, d4):
    vec_x1 = H2(vec_x, h(s), k1(s)) + d3*H3(vec_x, h(s), k1(s), k2=0) + d4*H4(vec_x, h(s), k1(s), k2=0, k3=0)
    return vec_x1

def func_Hexact(vec_x, s, d3, d4):
    vec_x1 = H_exact(vec_x, h(s), k1(s), k2=0., k3=0.)
    return vec_x1

def func_sec_eq(vec_x, s):
    vec_x1 = eq_second(vec_x, h = Btest.angle/Btest.l, k1=Btest.k1, k2=0., k3=0.)
    return vec_x1

def func_H_eq(vec_x, s):
    vec_x1 = eq_second_from_H(vec_x, h = Btest.angle/Btest.l, k1=Btest.k1, k2=0., k3=0.)
    return vec_x1


z = np.arange(0.000, lat.totalLen, dz)

vec_x0 = array([0, 0, 0, 0, 0, 0.05])

y1 = odeint(func_H234, vec_x0, z, args=(0., 0.), hmax=0.01, rtol=1e-12, atol=1e-14)
y2 = odeint(func_H234, vec_x0, z, args=(1., 0.), hmax=0.01, rtol=1e-12, atol=1e-14)
y3 = odeint(func_H234, vec_x0, z, args=(1., 1.), hmax=0.01, rtol=1e-12, atol=1e-14)
y4 = odeint(func_Hexact, vec_x0, z, args=(1., 1.), hmax=0.01, rtol=1e-12, atol=1e-14)
y5 = odeint(func_sec_eq, vec_x0, s_test, hmax=0.01, rtol=1e-14, atol=1e-14)
y6 = odeint(func_H_eq, vec_x0, s_test, hmax=0.01, rtol=1e-14, atol=1e-14)

plt.figure(1)
plt.title("Tracks $\Delta p/p = 0.05$")
plt.xlabel("S, m")
plt.ylabel("X, m")
plt.plot(s, x1_tr - y1[:, 0], 'r', label="$R-H_2$")
plt.plot(s, x2_tr - y2[:, 0], 'b', label="$(R+T)-H_{2+3}$")
plt.legend()

plt.figure(2)
plt.title("Tracks $\Delta p/p = 0.05$")
plt.xlabel("S, m")
plt.ylabel("X, m")
plt.plot(s, y2[:, 0] - y3[:, 0], 'y', label="$H_{2+3}-H_{2+3+4}$")
plt.plot(s, y3[:, 0] - y4[:, 0], 'k', label="$H_{2+3+4}-H_{exact}$")
plt.legend()

plt.figure(3)
plt.title("Tracks in dipole $\Delta p/p = 0.05$")
plt.xlabel("S, m")
plt.ylabel("X, m")
plt.plot(s_test, x_test- y5[:, 0], 'y', label="(R+T)-Brown's eq.")
plt.plot(s_test,  y5[:, 0] - y6[:, 0], 'k', label="Brown's eq - $H_{2+3}$")
plt.legend(loc=3)

plt.figure(4)
plt.title("Tracks $\Delta p/p = 0.05$")
plt.xlabel("S, m")
plt.ylabel("X, m")
plt.plot(s, x1_tr, 'r', label="$R$")
plt.plot(s, x2_tr, 'b', label="$R+T$")
plt.plot(s, y2[:, 0], 'g', label="$H_{2+3}$")
plt.plot(s, y3[:, 0], 'k', label="$H_{2+3+4}$")
plt.legend()
plt.show()

