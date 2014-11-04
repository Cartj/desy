import h5py
import numpy as np
import pylab
from xframework.common.math import *

def plot_1d(profile, title_fig, title_x, title_y):
    pylab.plot(profile[0], profile[1])
    pylab.xlabel(title_x)
    pylab.ylabel(title_y)
    pylab.title(title_fig)
    pylab.grid(True)

#################################################################
###################                          ####################
################### Parameters to be defined ####################
###################        by the user       ####################
###################                          ####################
#################################################################


where  = 'Source_analysis'
zpos = 'z_pos'
maxi = 'max_i'
rmsx = 'rms_x'
rmsy = 'rms_y'
fwhmx = 'fwhm_x'
fwhmy = 'fwhm_y'


f=h5py.File('./Source.h5','r') 

#################################################################





z_list= f[where+'/'+zpos].value
i_list= f[where+'/'+maxi].value
x_rmslist= f[where+'/'+rmsx].value
y_rmslist= f[where+'/'+rmsy].value
x_fwhmlist= f[where+'/'+fwhmx].value
y_fwhmlist= f[where+'/'+fwhmy].value

plot_1d([z_list,i_list],'Intensity','','')

pylab.show()

plot_1d([z_list,x_rmslist],'rmsx','','')

pylab.show()

plot_1d([z_list,y_rmslist],'rmsy','','')

pylab.show()

plot_1d([z_list,x_fwhmlist],'fwhmx','','')

pylab.show()

plot_1d([z_list,y_fwhmlist],'fwhmy','','')

pylab.show()
    
