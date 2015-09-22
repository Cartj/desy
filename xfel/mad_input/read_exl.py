__author__ = 'Sergey Tomin'

from ocelot.cpbd.beam import Twiss
from ocelot.gui.accelerator import *
from matplotlib import pylab as plt
import numpy as np
import xlrd
rb = xlrd.open_workbook('component_list.xls',formatting_info=True)
sheet = rb.sheet_by_index(1)

tw = Twiss()
tws_L1 = []
L = 0.
tws_I1 = []
for rownum in range(2, 4246):
    row = sheet.row_values(rownum)
    tw = Twiss()
    length = row[7]
    L += length
    strength = row[8]
    lag = row[9]
    freq = row[10]
    tilt = row[11]
    s = row[12]
    st = row[13]
    x, y, z = row[14], row[15], row[16]
    energy = row[26]

    tw.beta_x = row[27]
    tw.alpha_x = row[28]
    tw.mu_x = row[29]

    tw.beta_y = row[30]
    tw.alpha_y = row[31]
    tw.muy = row[32]

    tw.Dx = row[33]
    tw.Dxp = row[34]
    tw.Dy = row[35]
    tw.Dyp = row[36]
    tw.E = energy
    tw.s = s
    if row[0] == "I1":
        #print rownum, row[0], tw.s
        tws_I1.append(tw)
    if row[0] == "L3":
        print z
        tws_L1.append(tw)
tws = tws_L1# np.append(tws_I1, tws_L1)
s = [tw.s for tw in tws]
beta_x = [tw.beta_x for tw in tws]
beta_y = [tw.beta_y for tw in tws]
alpha_x = [tw.alpha_x for tw in tws]
alpha_y = [tw.alpha_y for tw in tws]
Dx = [tw.Dx for tw in tws]
Dy = [tw.Dy for tw in tws]
#print s
plt.figure(1)
plt.plot(s, beta_x, "r.-", s, beta_y, "b.-")
plt.grid(True)
plt.figure(2)
plt.plot(s, Dx, "r.-", s, Dy, "b.-")
plt.grid(True)
plt.show()
