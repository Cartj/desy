import h5py
import numpy as np
from xframework.common.math import *

def round_sig(x, sig=2):
    from math import log10, floor
    return round(x, sig-int(floor(log10(x)))-1)

def fwhm_gauss_fit(X,Y):
    '''
    Should use common.math here
    '''
    import numpy as np
    import scipy.optimize as opt
    
    def gauss(x, p): # p[0]==mean, p[1]==stdev p[2]==peak
        return p[2]/(p[1]*np.sqrt(2*np.pi))*np.exp(-(x-p[0])**2/(2*p[1]**2))
        
    p0 = [0,max(X)/2,max(Y)]
    errfunc = lambda p, x, y: gauss(x, p) - y
    p1, success = opt.leastsq(errfunc, p0[:], args=(X, Y))
    fit_mu,fit_stdev,ampl = p1
    Y1=gauss(X,p1)
    FWHM = 2*np.sqrt(2*np.log(2))*fit_stdev
    return (Y1, FWHM)

def plotfield(name ,Xs, Xf, nx, Ys, Yf, ny, arI, arP):
  import matplotlib.pyplot as plt
  from matplotlib.colors import BoundaryNorm
  from matplotlib.ticker import MaxNLocator
  import numpy as np
  import math  
  from pylab import clf, axis

  # generate 2 2d grids for the x & y bounds

  x = 1e6 * np.linspace(Xs, Xf, nx)
  y = 1e6 * np.linspace(Ys, Yf, ny)
  dataI = np.array( arI )
  zI=dataI.reshape( ny, nx ) 
  dataP = np.array( arP )
  zP=dataP.reshape( ny, nx )    
  levelsI = MaxNLocator(nbins=50).tick_values(zI.min(), zI.max())  
  levelsP = MaxNLocator(nbins=50).tick_values(-math.pi, math.pi)
  
  
  # pick the desired colormap, sensible levels, and define a normalization
  # instance which takes data values and translates those into levels.
  cmapI = plt.get_cmap('jet')
  cmapP = plt.get_cmap('hsv')
  normI = BoundaryNorm(levelsI, ncolors=cmapI.N, clip=True)
  normP = BoundaryNorm(levelsP, ncolors=cmapP.N, clip=True)
  
  fig = plt.figure(name)
  clf()
  
  # plt.subplot(2, 2, 1)-------------------------------------
  p1=fig.add_subplot(2, 2, 1)
  p1.clear()  
  pp1=p1.pcolormesh(x, y, zI, cmap=cmapI)#, norm=normI)    
  # set the limits of the plot to the limits of the data
  p1.axis([x.min(), x.max(), y.min(), y.max()])  
  plt.title('Intensity')
  axis('equal')  
  p1.set_xlabel(r'[$\mu m$]')
  p1.set_ylabel(r'[$\mu m$]')
  # axis([Xs*1e6, Xf*1e6, Ys*1e6, Yf*1e6])
  
  # plt.subplot(2, 2, 2)--------------------------------------
  p2=fig.add_subplot(2, 2, 2, sharey=p1)
  p2.clear()      
  arIpy=np.sum(zI,1)
  p2.plot(arIpy,y)
  arIpyf, fwhmy=fwhm_gauss_fit(y,arIpy)
  p2.plot(arIpyf,y)  
  p2.text(0.95, 0.95,'FWHM= '+str(round_sig(fwhmy,3))+r'$\mu m$',
  horizontalalignment='right',
  verticalalignment='top',
  transform = p2.transAxes)  
       
  # plt.subplot(2, 2, 3)--------------------------------------
  p3=fig.add_subplot(2, 2, 3, sharex=p1)
  p3.clear()      
  arIpx=np.sum(zI,0)  
  p3.plot(x,arIpx)
  arIpxf, fwhmx=fwhm_gauss_fit(x,arIpx)
  p3.plot(x,arIpxf)  
  p3.text(0.95, 0.95,'FWHM= '+str(round_sig(fwhmx,3))+r'$\mu m$',
  horizontalalignment='right',
  verticalalignment='top',
  transform = p3.transAxes)
  
  # plt.subplot(2, 2, 4)--------------------------------------
  p4=fig.add_subplot(2, 2, 4, sharex=p1)
  p4.clear()  
  p4.pcolormesh(x, y, zP, cmap=cmapP, norm=normP)  
  plt.title('Phase')
  axis('equal')
  
  fig.subplots_adjust(top=0.95, bottom=0.05, right=0.9, left=0.1)
  cbar_int = fig.add_axes([0.93, 0.15, 0.02, 0.7])
  plt.colorbar(pp1, cax=cbar_int)# pad = -0.05 ,fraction=0.01)  
  plt.show()  
  
  return fig

def plotinte(name ,Xs, Xf, nx, Ys, Yf, ny, arI):
    import matplotlib.pyplot as plt
    from matplotlib.colors import BoundaryNorm
    from matplotlib.ticker import MaxNLocator
    import numpy as np
    import math    
    from pylab import clf, axis

    # generate 2 2d grids for the x & y bounds
    x = 1e6 * np.linspace(Xs, Xf, nx)
    y = 1e6 * np.linspace(Ys, Yf, ny)
    dataI = np.array( arI )
    print 'sizearI',np.size(arI)
    print 'sizedataI=',np.size(dataI)
    print 'prodotto=',ny*nx
    zI=dataI.reshape( ny, nx ) 
    
    # x and y are bounds, so z should be the value *inside* those bounds.
    # Therefore, remove the last value from the z array.            
    levelsI = MaxNLocator(nbins=50).bin_boundaries(zI.min(), zI.max())    
    cmapI = plt.get_cmap('jet')   
    normI = BoundaryNorm(levelsI, ncolors=cmapI.N, clip=True)
       
    fig = plt.figure(1)
    clf()

    # plt.subplot(2, 2, 1)-------------------------------------
    p1=fig.add_subplot(2, 2, 1)
    p1.clear()
    p1.tick_params(axis='both', labelsize=8)
    pp1=p1.pcolormesh(x, y, zI, cmap=cmapI)#, norm=normI)  
    p1.axis([x.min(), x.max(), y.min(), y.max()])  
    plt.title('Intensity', fontsize=9)
    axis('equal')  
    p1.set_xlabel(r'[$\mu m$]')
    p1.set_ylabel(r'[$\mu m$]')

    # plt.subplot(2, 2, 2)--------------------------------------
    p2=fig.add_subplot(2, 2, 2, sharey=p1)
    p2.clear()
    p2.tick_params(axis='both', labelsize=8)
    arIpy=np.sum(zI,1)
    p2.plot(arIpy,y)
    arIpyf, fwhmy=fwhm_gauss_fit(y,arIpy)
    p2.plot(arIpyf,y)  
    p2.text(0.95, 0.95,'FWHM= '+str(round_sig(fwhmy,3))+r'$\mu m$', horizontalalignment='right', verticalalignment='top', transform = p2.transAxes, fontsize=9)  
       
    # plt.subplot(2, 2, 3)--------------------------------------
    p3=fig.add_subplot(2, 2, 3, sharex=p1)
    p3.tick_params(axis='both', labelsize=8)
    p3.clear()  
    arIpx=np.sum(zI,0)  
    p3.plot(x,arIpx)
    arIpxf, fwhmx=fwhm_gauss_fit(x,arIpx)  
    p3.plot(x,arIpxf)  
    p3.text(0.95, 0.95,'FWHM= '+str(round_sig(fwhmx,3))+r'$\mu m$', horizontalalignment='right', verticalalignment='top', transform = p3.transAxes, fontsize=9)

    fig.subplots_adjust(top=0.95, bottom=0.05, right=0.9, left=0.1)
    cbar_int = fig.add_axes([0.93, 0.15, 0.02, 0.7])
    cbar_int.ticklabel_format(style='sci', scilimits=(0,0), axis='y')

    cbar_int.tick_params(labelsize=8) 
    plt.colorbar(pp1, cax=cbar_int)# pad = -0.05 ,fraction=0.01)

    #savefig(res_dir+name+'.png')
    plt.show()
    return fig


#################################################################
###################                          ####################
################### Parameters to be defined ####################
###################        by the user       ####################
###################                          ####################
#################################################################

slno = 801
zpos = 933.05
where_slice = str(slno)+'.slice/z='+str(zpos)+'/'+str(slno)
where_inte  = 'Intensity_z='+str(zpos)

f=h5py.File('./Output.h5','r') 

#################################################################

'''
lista = []
f.visit(lista.append)
print lista
q = []
for sl in range(2000):
	matching = []
	matching = [s for s in lista if '/'+str(sl)+'.slice.msh_X' in s]
	if not matching == []: 
		q.append(sl)
print q	
matching = [s for s in lista if '40.slice/z=' in s]
print matching
'''


Xs= f[where_slice+'.slice.msh_X'].value[0]
Xf= f[where_slice+'.slice.msh_X'].value[1]
nx= f[where_slice+'.slice.msh_X'].value[2]
Ys= f[where_slice+'.slice.msh_Y'].value[0]
Yf= f[where_slice+'.slice.msh_Y'].value[1]
ny= f[where_slice+'.slice.msh_Y'].value[2]

arI = (np.absolute(f[where_slice+'.slice.fld_X'].value))**2
arP =     np.angle(f[where_slice+'.slice.fld_X'].value)    
    
plotfield('slice.'+str(slno)+'.z='+str(zpos) ,Xs, Xf, nx, Ys, Yf, ny, arI, arP)


Xs= f[where_inte+'/msh'].value[0]
Xf= f[where_inte+'/msh'].value[1]
nx= f[where_inte+'/msh'].value[2]
Ys= f[where_inte+'/msh'].value[3]
Yf= f[where_inte+'/msh'].value[4]
ny= f[where_inte+'/msh'].value[5]
arI=   f[where_inte+'/Inte'].value

plotinte('Inte'+'.z='+str(zpos), Xs, Xf, int(nx), Ys, Yf, int(ny), arI)




    
