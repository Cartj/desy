import numpy as np
from ocelot.gui.accelerator import *
import pickle
#f = open("da_test.txt")
#lines = f.readlines()
#da = []
#for line in lines:
#    if line[0] == "#":
#        parts = line.split(":")
#        params = parts[1].split(",")
#        if parts[0].find("x") > 0:
#            print params
#            x_array = np.linspace(params[0], params[1], params[2])
#        else:
#            y_array = np.linspace(params[0], params[1], params[2])
#    else:
#        da.append(float(line))
#
with open("da.txt", 'r') as f:
     data = pickle.load(f)

#print data
x_array = data["x_array"]
y_array = data["y_array"]
da = data["da"]
#da = np.loadtxt("da.txt")
#xy = np.loadtxt("da_axis.txt")
#x_array = xy[:,0]
#y_array = xy[:,1]
#print x_array
#print y_array

show_da(da, x_array, y_array)
