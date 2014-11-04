from mpi4py import MPI

comm  = MPI.COMM_WORLD   #Creates one common object "communicator" knwoning about processes
rank  = comm.Get_rank()  #Process number
nproc = comm.Get_size()  #Total number of processes

from srwlib import *
from xframework.adaptors.genesis import *

from prop_lines import *


import copy
from scipy import interpolate


'''

#################################################################################################
####################             Routines NOT used in prop_par.py           #####################
####################          but useful for near-future extensions         #####################
#################################################################################################

def fluence(field,Xdim,Ydim,nx,ny,Ntotph):

    Dx = Xdim/nx
    Dy = Ydim/ny
    print('Dx = ',Dx,' m')
    print('Dy = ',Dy,' m')
    integral = 0    
    maxintens = field[0]*field[0] + field[1]*field[1]    
    for j in np.arange(0,len(field),2):        
        intens = field[j]*field[j] + field[j+1]*field[j+1]
        integral = integral + intens * Dx * Dy
        if maxintens < intens: maxintens = intens        
    result = Ntotph*maxintens/integral
    print('max intensity = ',maxintens,' A.U.')
    print('integrated intensity = ',integral,' A.U.')
    print('Xdim = ',Xdim,' m')
    print('Ydim = ',Ydim,' m')
                        
    return result


def fluenceI(Inte,Xdim,Ydim,nx,ny,Ntotph):

    Dx = Xdim/nx
    Dy = Ydim/ny
    print('Dx = ',Dx,' m')
    print('Dy = ',Dy,' m')
    integral = 0    
    maxintens = Inte[0]    
    for j in np.arange(0,len(Inte),1):        
        intens = Inte[j]
        integral = integral + intens * Dx * Dy
        if maxintens < intens: maxintens = intens        
    result = Ntotph*maxintens/integral
    print('max intensity = ',maxintens,' A.U.')
    print('integrated intensity = ',integral,' A.U.')
    print('Xdim = ',Xdim,' m')
    print('Ydim = ',Ydim,' m')
                        
    return result






def writeres(namef, dataX, dataY):

    f1 = open(namef, 'w')
    for i in range(len(dataX)):
        f1.write('%s ' %(dataX[i]) + '%s' %(dataY[i]) +'\n')        
    f1.close()
    




def findsourceave(field, wfr0, zini, zfin, zstep, slicein, slicefin):
    
    reg_arzi = []
    wfrini = copy.deepcopy(wfr0)
    NX = wfrini.mesh.nx
    NY = wfrini.mesh.ny
    
    #print('nx0',nx0)
    #print('ny0',ny0)
    R_Xs0=[]
    R_Xf0=[]
    R_nx0=[]
    R_Ys0=[]
    R_Yf0=[]
    R_ny0=[]
    
    for qsl in range(slicein,slicefin):

        print('Finding the source. Processing slice nr ',qsl-slicein+1,' out of ',slicefin-slicein) 
        sl = field[qsl]
        count = 0
        for j in range(NY):
            for k in range(NX):
                wfrini.arEx[count] = np.float(np.real(sl[j][k]))
                count = count + 1
                wfrini.arEx[count] = np.float(np.imag(sl[j][k]))
                count = count + 1
        OUT = findsource(wfrini, zini, zfin, zstep)
        registerARZI = OUT[5]
        registerMESH = OUT[8]

        
        
        inte_registerARZI = []
        
        
        if qsl == slicein:
            for num in range(len(registerARZI)):
                R_Xs0.append(registerMESH[num].xStart)
                R_Xf0.append(registerMESH[num].xFin)
                R_nx0.append(registerMESH[num].nx)
                R_Ys0.append(registerMESH[num].yStart)
                R_Yf0.append(registerMESH[num].yFin)
                R_ny0.append(registerMESH[num].ny)

        for num in range(len(registerARZI)):

            Xs0 = R_Xs0[num]
            Xf0 = R_Xf0[num]
            nx0 = R_nx0[num]
            Ys0 = R_Ys0[num]
            Yf0 = R_Yf0[num]
            ny0 = R_ny0[num]
            
                  
            XMESH = np.linspace(Xs0, Xf0, nx0)
            YMESH = np.linspace(Ys0, Yf0, ny0)
            
            #print(Xs0, ' ', Xf0, ' ',nx0, ' ',ny0)                
            Xs=registerMESH[num].xStart
            Xf=registerMESH[num].xFin
            nx=registerMESH[num].nx
            Ys=registerMESH[num].yStart
            Yf=registerMESH[num].yFin
            ny=registerMESH[num].ny
            Xact = np.linspace(Xs, Xf, nx)
            Yact = np.linspace(Ys, Yf, ny)
            dataI = np.array( registerARZI[num] )
            zI    = dataI.reshape( ny, nx )
            Interdata = interpolate.interp2d(Xact, Yact, zI)
            zI_inte    = Interdata(XMESH, YMESH)
            INT_arI   = zI_inte.reshape(ny0,nx0)
            inte_registerARZI.append(np.array(INT_arI))
            #print('slice ',qsl,' len = ',len(inte_registerARZI),' with ',len(np.array(INT_arI)))


            
            #plotinte(str(qsl)+'_'+str(num)+'old_pos' ,Xs,  Xf,  nx,  Ys,  Yf,  ny,  zI)
            #plotinte(str(qsl)+'_'+str(num)+'new_pos' ,Xs0, Xf0, nx0, Ys0, Yf0, ny0, INT_arI)
            
        
        if qsl == slicein:
            reg_arzi=np.array(inte_registerARZI)
        else:
            reg_arzi = reg_arzi + np.array(inte_registerARZI)
            

    InteWaist = 0  
    registerI = []
    registerZ = OUT[1]    
    register_fwhm_X = []
    register_fwhm_Y = []


    #print(len(reg_arzi))
    #print(len(reg_arzi[0]))
    #print(len(reg_arzi[0][0]))

    #print(len(reg_arzi),'... e` 19?')
    
    InteWaist = 0
    for k in range(len(reg_arzi)):        
        intens = np.max(reg_arzi[k])
        registerI.append(intens)        
        if intens > InteWaist:
            InteWaist = intens                       
            WaistPos = OUT[1][k]
            xwaist = 1e6 * np.linspace(R_Xs0[k], R_Xf0[k], R_nx0[k] )
            ywaist = 1e6 * np.linspace(R_Ys0[k], R_Yf0[k], R_ny0[k] )
            
        x = 1e6 * np.linspace(R_Xs0[k], R_Xf0[k], R_nx0[k] )
        y = 1e6 * np.linspace(R_Ys0[k], R_Yf0[k], R_ny0[k] )
        arIpy=np.sum(reg_arzi[k],1)
        arIpyf, fwhmy=fwhm_gauss_fit(y,arIpy)        
        arIpx=np.sum(reg_arzi[k],0)
        arIpxf, fwhmx=fwhm_gauss_fit(x,arIpx)        
        register_fwhm_X.append(fwhmx)
        register_fwhm_Y.append(fwhmy) 
          
    return [registerZ,registerI,WaistPos,InteWaist,register_fwhm_X,register_fwhm_Y,reg_arzi, xwaist, ywaist]
        





def findsource(wfrini1, zini, zfin, zstep):

    Zpos = zini-zstep
    flagf    = 0
    j = 1
    registerI = []
    registerZ = []
    registerARZI = []
    register_fwhm_X = []
    register_fwhm_Y = []
    register_mesh   = []
    print('Initial wavefront position = ',wfrini1.mesh.zStart)

    while Zpos>zfin:
        
        Drift_1 = SRWLOptD(-j*zstep+zini) #Drift    
        #Wavefront Propagation Parameters with OM:
        #                    [ 0] [1] [2]  [3] [4] [5]  [6]  [7]  [8]  [9] [10] [11]         
        ppDrift_1 =          [ 1,  1, 1.0,  0,  0, 1.0, 1.0, 1.0, 1.0,  0,  0,   0]   
        ppFinal =            [ 0,  0, 1.0,  0,  0, 1.0, 1.0, 1.0, 1.0,  0,  0,   0]

        #ppDrift_1 =          [ 0,  0, 1.0,  0,  0, 1.0, 2.0, 1.0, 2.0,  0,  0,   0]   
        #ppFinal =            [ 0,  0, 1.0,  0,  0, 0.5, 0.5, 0.5, 0.5,  0,  0,   0]
        
        optBL = SRWLOptC([Drift_1],  [ppDrift_1, ppFinal])
        wfr1c = copy.deepcopy(wfrini1)                
        srwl.PropagElecField(wfr1c, optBL)
        arI = array('f', [0]*wfr1c.mesh.nx*wfr1c.mesh.ny) #"flat" array to take 2D intensity data
        srwl.CalcIntFromElecField(arI, wfr1c, 6, 0, 3, wfr1c.mesh.eStart, 0, 0) #extracts intensity        
        arP = array('d', [0]*wfr1c.mesh.nx*wfr1c.mesh.ny) #"flat" array to take 2D phase data (note it should be 'd')
        srwl.CalcIntFromElecField(arP, wfr1c, 0, 4, 3, wfr1c.mesh.eStart, 0, 0) #extracts radiation phase
        register_mesh.append(wfr1c.mesh)
        dataI = np.array( arI )
        zI=dataI.reshape( wfr1c.mesh.ny, wfr1c.mesh.nx )
        registerARZI.append(zI)
        x = 1e6 * np.linspace(wfr1c.mesh.xStart, wfr1c.mesh.xFin, wfr1c.mesh.nx )
        y = 1e6 * np.linspace(wfr1c.mesh.yStart, wfr1c.mesh.yFin, wfr1c.mesh.ny )
        arIpy=np.sum(zI,1)
        arIpyf, fwhmy=fwhm_gauss_fit(y,arIpy)        
        arIpx=np.sum(zI,0)
        arIpxf, fwhmx=fwhm_gauss_fit(x,arIpx)        
        register_fwhm_X.append(fwhmx)
        register_fwhm_Y.append(fwhmy) 
        field = wfr1c.arEx
        maxintens = field[0]*field[0] + field[1]*field[1]    
        for k in np.arange(0,len(field),2):        
            intens = field[k]*field[k] + field[k+1]*field[k+1]
            if maxintens < intens: maxintens = intens
        registerI.append(maxintens)
        registerZ.append(Zpos)           
        Zpos = Zpos - zstep
        j = j+1
        #plotinte('singlePOS'+str(j) ,wfr1c.mesh.xStart, wfr1c.mesh.xFin, wfr1c.mesh.nx,  wfr1c.mesh.yStart, wfr1c.mesh.yFin, wfr1c.mesh.ny,   zI)

    InteWaist = np.max(registerI)    
    maxind = np.argmax(registerI)
    WaistPos = registerZ[maxind]

    [wfr1d, arI, arP] = Source_Prop(Len_drft = WaistPos-zini, Wfrin = wfrini1) 

    
    return [wfr1d,registerZ,registerI,WaistPos,InteWaist,registerARZI,register_fwhm_X,register_fwhm_Y,register_mesh]




def Source_slice(wfrG=[], zin = 0.0, zfin = -40., zstep=1.0):

    # ****************************** Finds the source position for slice slicen ************************************

    OUT    = findsource(wfrG, zin, zfin, zstep)
    registerZ       = OUT[1]
    registerI       = OUT[2]
    register_fwhm_X = OUT[6]
    register_fwhm_Y = OUT[7]
    writeres(res_dir+'IvsZ_sl'+str(slicen+1)+'.dat',registerZ,registerI)
    writeres(res_dir+'fwhmXvsZ_sl'+str(slicen+1)+'.dat',registerZ,register_fwhm_X)
    writeres(res_dir+'fwhmYvsZ_sl'+str(slicen+1)+'.dat',registerZ,register_fwhm_Y)

    WfrGTempl = OUT[0]

    arIP = array('f', [0]*WfrGTempl.mesh.nx*WfrGTempl.mesh.ny) #"flat" array to take 2D intensity data
    srwl.CalcIntFromElecField(arIP, WfrGTempl, 6, 0, 3, WfrGTempl.mesh.eStart, 0, 0) #extracts intensity    
    arPP = array('d', [0]*WfrGTempl.mesh.nx*WfrGTempl.mesh.ny) #"flat" array to take 2D phase data (note it should be 'd')
    srwl.CalcIntFromElecField(arPP, WfrGTempl, 0, 4, 3, WfrGTempl.mesh.eStart, 0, 0) 
    plotfield("Source_sl"+str(sample+1), WfrGTempl.mesh.xStart, WfrGTempl.mesh.xFin, WfrGTempl.mesh.nx, WfrGTempl.mesh.yStart, WfrGTempl.mesh.yFin, WfrGTempl.mesh.ny, arIP, arPP)

  


def xyprofave(pulse, tgrid, slicein, slicefin):
   
    print('Finding the average profile')
    for j in range(slicein,slicefin):
        slices = pulse[j]
        OUT = xyprofile(slices,tgrid)
        if j == slicein :
            Xcutave = OUT[0][1]
            Ycutave = OUT[1][1]
        else :
            Xcutave = Xcutave + OUT[0][1]
            Ycutave = Ycutave + OUT[1][1]
    Xcoord = OUT[0][0]
    Ycoord = OUT[1][0]
    Xcutave = Xcutave/(slicefin-slicein)
    Ycutave = Ycutave/(slicefin-slicein)

    return [[Xcoord, Xcutave],[Ycoord, Ycutave]]





def xydivave(pulse, tgrid, slicein, slicefin, lambd):
   
    print('Finding the average divergence')
    for j in range(slicein,slicefin):
        slices = pulse[j]
        OUT = xydiv(slices,tgrid,lambd)
        if j == slicein :
            Xcutave = OUT[0][1]
            Ycutave = OUT[1][1]
        else :
            Xcutave = Xcutave + OUT[0][1]
            Ycutave = Ycutave + OUT[1][1]
    Xcoord = OUT[0][0]
    Ycoord = OUT[1][0]
    Xcutave = Xcutave/(slicefin-slicein)
    Ycutave = Ycutave/(slicefin-slicein)

    return [[Xcoord, Xcutave],[Ycoord, Ycutave]]





def xyprofile(slices, tgrid):

    Xpos = int(np.argmax(np.abs(slices))/len(slices))
    Ypos = len(slices) -1 - int(np.argmax(np.abs(slices))/len(slices))
    ##print('max = ',np.max(np.abs(slices)),' maxpos = ',np.argmax(slices))
    ##print('XPOS = ',Xpos,' YPOS = ',Ypos,' MIDDLE = ',int(len(slices)/2))
    ##print('slmax = ',slices[Xpos,Ypos],' ',slices[Ypos,Xpos])
    #Xcut = np.abs(slices[int(len(slices)/2),:])**2
    #Ycut = np.abs(slices[:,int(len(slices)/2)])**2
    Xcut = np.abs(slices[Xpos,:])**2
    Ycut = np.abs(slices[:,Ypos])**2
    Xcoord = np.linspace(-tgrid,tgrid,len(Xcut))
    Ycoord = np.linspace(-tgrid,tgrid,len(Xcut))    
    #matplotlib.pyplot.figure()
    #matplotlib.pyplot.plot(Xcoord,Xcut)
    #matplotlib.pyplot.show()
    #matplotlib.pyplot.figure()
    #matplotlib.pyplot.plot(Ycoord,Ycut)
    #matplotlib.pyplot.show()

    return [[Xcoord, Xcut],[Ycoord, Ycut]]





def xydiv(slices, tgrid, lambd):    

    fslices = np.fft.fftshift(np.fft.fft2(slices))

    KXpos = int(np.argmax(np.abs(fslices))/len(fslices))
    KYpos = len(fslices) - 1 - int(np.argmax(np.abs(fslices))/len(fslices))
    ##print('KXPOS = ',KXpos,' KYPOS = ',KYpos,' MIDDLE = ',int(len(fslices)/2))
                  
    #KXcut = np.abs(fslices[int(len(slices)/2),:])**2
    #KYcut = np.abs(fslices[:,int(len(slices)/2)])**2
    KXcut = np.abs(fslices[KXpos,:])**2
    KYcut = np.abs(fslices[:,KYpos])**2  
    KXmax = 2*pi/(2*tgrid/len(KXcut))/2.0 #Total range is 2pi/(smallest size); smallest size is 2tgrid/len(KXcut); Max is total range/2
    KYmax = 2*pi/(2*tgrid/len(KYcut))/2.0
    THXmax = KXmax * lambd/(2*np.pi)
    THYmax = KYmax * lambd/(2*np.pi)        
    THXcoord = np.linspace(-THXmax,THXmax,len(KXcut))
    THYcoord = np.linspace(-THYmax,THYmax,len(KYcut))    
    #matplotlib.pyplot.figure()
    #matplotlib.pyplot.plot(THXcoord,KXcut)
    #matplotlib.pyplot.show()
    #matplotlib.pyplot.figure()
    #matplotlib.pyplot.plot(THYcoord,KYcut)
    #matplotlib.pyplot.show()
    
    return [[THXcoord, KXcut],[THYcoord, KYcut]]



def ProDiv_slice(sl = [], dgrid = 1.0, xlamds = 1.0):

    # ****************************** Calculates profile and divergence of slice slicen ************************************

    xy   = xyprofile(sl,dgrid)
    writeres(res_dir+'X_prof_sl'+str(slicen+1)+'.dat',xy[0][0],xy[0][1])
    writeres(res_dir+'Y_prof_sl'+str(slicen+1)+'.dat',xy[1][0],xy[1][1])
    matplotlib.pyplot.figure()
    matplotlib.pyplot.plot(xy[0][0],xy[0][1])
    savefig(res_dir+'X_prof_sl'+str(slicen+1)+'.png')
    matplotlib.pyplot.figure()
    matplotlib.pyplot.plot(xy[1][0],xy[1][1])
    savefig(res_dir+'Y_prof_sl'+str(slicen+1)+'.png')

    thxy = xydiv(sl,dgrid,xlamds)
    writeres(res_dir+'X_div_sl'+str(slicen+1)+'.dat',thxy[0][0],thxy[0][1])
    writeres(res_dir+'Y_div_sl'+str(slicen+1)+'.dat',thxy[1][0],thxy[1][1])
    matplotlib.pyplot.figure()
    matplotlib.pyplot.plot(thxy[0][0],thxy[0][1])
    savefig(res_dir+'X_div_sl'+str(slicen+1)+'.png')
    matplotlib.pyplot.figure()
    matplotlib.pyplot.plot(thxy[1][0],thxy[1][1])
    savefig(res_dir+'Y_div_sl'+str(slicen+1)+'.png')

def GenWfr_slice(wfrG = []):

    # **********************Calculating Genesis Wavefront and extracting Intensity for slice slicen:

    XsG=wfrG.mesh.xStart
    XfG=wfrG.mesh.xFin
    nxG=wfrG.mesh.nx
    YsG=wfrG.mesh.yStart
    YfG=wfrG.mesh.yFin
    nyG=wfrG.mesh.ny

    arIG = array('f', [0]*nxG*nyG) #"flat" array to take 2D intensity data
    srwl.CalcIntFromElecField(arIG, wfrG, 6, 0, 3, wfrG.mesh.eStart, 0, 0) #extracts intensity
    arPG = array('d', [0]*nxG*nyG) #"flat" array to take 2D phase data (note it should be 'd')
    srwl.CalcIntFromElecField(arPG, wfrG, 0, 4, 3, wfrG.mesh.eStart, 0, 0) #extracts radiation phase
    plotfield("Gen_out_sl"+str(slicen+1), XsG, XfG, nxG, YsG, YfG, nyG, arIG, arPG)



def AveSourcePos(field = [], wfrG=[], zin = -20.0, zfin = -40.0, step = 1.0, slicein=-20.0, slicefin=-40.0):


    # ****************************** Finds the average source position ************************************

    OUTAVE = findsourceave(field, wfrG, -20.0, -40.0, 1.0, slicein, slicefin)
    registerZ_ave       = OUTAVE[0]
    registerI_ave       = OUTAVE[1]
    register_fwhm_X_ave = OUTAVE[4]
    register_fwhm_Y_ave = OUTAVE[5]
    reg_arzi_ave        = OUTAVE[6]
    writeres(res_dir+'IvsZ_ave.dat',registerZ_ave,registerI_ave)
    writeres(res_dir+'fwhmXvsZ_ave.dat',registerZ_ave,register_fwhm_X_ave)
    writeres(res_dir+'fwhmYvsZ_ave.dat',registerZ_ave,register_fwhm_Y_ave)
    maxind = np.argmax(registerI_ave)

    x = OUTAVE[7]
    y = OUTAVE[8]
    arIpy=np.sum(reg_arzi_ave[maxind],1)
    arIpx=np.sum(reg_arzi_ave[maxind],0)
    #These are summed! The previous ones are cut 
    writeres(res_dir+'IvsX_ave.dat',x,arIpx)
    writeres(res_dir+'IvsY_ave.dat',y,arIpy)

    return OUTAVE[2]   


      
def prtfluence(wfr = [], arI=[], MESH = [] ):

    Xs = MESH[0]
    Xf = MESH[1]
    nx = MESH[2]
    Ys = MESH[3]
    Yf = MESH[4]        
    ny = MESH[5]
    pixel_area=(Xf-Xs)*(Yf-Ys)/nx/ny
    integral=sum([x*pixel_area for x in arI])
    np.disp('integral_area(a.u.)= '+str(integral/1000000))

    np.disp('max_intensity= '+str(round_sig(max(arI),3)))
    np.disp('pixel_area= '+str(pixel_area))
    Ntotph = 1
    flux = fluence(wfr.arEx, Xf-Xs, Yf-Ys, nx, ny, 1)
    print('X size = ',Xf-Xs,' m')
    print('Y size = ',Yf-Ys,' m')
    print('X mesh = ',nx,' points')
    print('Y mesh = ',ny,' points')
    print('Total fluence is ',flux,'*Nph in ph/m2')
    print('also corresponding to ',flux/1.0e6,'*Nph in ph/mm2')


def AVE_prtfluence(INT_arI_ave_P = [], MESH = []):

    XsP0 = MESH[0]
    XfP0 = MESH[1]
    nxP0 = MESH[2]
    YsP0 = MESH[3]
    YfP0 = MESH[4]        
    nyP0 = MESH[5]
    pixel_area=(XfP0-XsP0)*(YfP0-YsP0)/nxP0/nyP0
    integral=sum([x*pixel_area for x in INT_arI_ave_P])    
    np.disp('integral_area(a.u.)= '+str(integral/1000000))

    np.disp('max_intensity= '+str(round_sig(max(INT_arI_ave_P),3)))
    np.disp('pixel_area= '+str(pixel_area))
    Ntotph = 1
    flux = fluenceI(INT_arI_ave_P, XfP0-XsP0, YfP0-YsP0, nxP0, nyP0, 1)
    print('X size = ',XfP0-XsP0,' m')
    print('Y size = ',YfP0-YsP0,' m')
    print('X mesh = ',nxP0,' points')
    print('Y mesh = ',nyP0,' points')
    print('Total fluence is ',flux,' ph/m2')
    print('also corresponding to ',flux/1.0e6,' ph/mm2')
    

'''

#################################################################################################
####################           Routines strictly used in prop_par.py        #####################
#################################################################################################

def GeneRead(comm=[], filename='D:\prog\data\PROP\sase2.4p1keV.tap.1.out.dfl', Tmesh=301, PhEne = 4100.0, dgrid = 1.0):
    '''
    Reads the Genesis file and gives back wavefront backbone and field as a np.array
    '''
    
    
    wfrG = SRWLWfr()               #Initial Electric Field Wavefront
    wfrG.allocate(1, Tmesh, Tmesh) #Numbers of points vs Photon Energy (1), Horizontal and Vertical Positions (dummy)
    wfrG.mesh.zStart =  0.0        #Longitudinal Position [m] at which Electric Field has to be calculated, i.e. the position of the first optical element
    wfrG.mesh.eStart =  PhEne      #Initial Photon Energy [eV]
    wfrG.mesh.eFin   =  PhEne      #Final Photon Energy [eV]
    wfrG.mesh.xStart = -dgrid      #Initial Horizontal Position [m]
    wfrG.mesh.xFin   =  dgrid      #Final Horizontal Position [m]
    wfrG.mesh.yStart = -dgrid      #Initial Vertical Position [m]
    wfrG.mesh.yFin   =  dgrid      #Final Vertical Position [m]

    wfrG.partBeam.partStatMom1.x  = 0.0     #Some information about the source in the Wavefront structure
    wfrG.partBeam.partStatMom1.y  = 0.0
    wfrG.partBeam.partStatMom1.z  = 0.0
    wfrG.partBeam.partStatMom1.xp = 0.0
    wfrG.partBeam.partStatMom1.yp = 0.0

    #Reading Genesis field file
    print('Reading Genesis field file...')
    field=readRadiationFile_mpi(comm=comm, fileName=filename, npoints=Tmesh)
    print('...Done.',rank,'. ',len(field))
    
    return [wfrG, field]


def Source_Prop(Len_drft = 0.1, Wfrin = []):
    
    #**********************Calculating virtual Source Wavefront and extracting Intensity:

    Drift_1 = SRWLOptD(Len_drft) #Drift    
    #Wavefront Propagation Parameters with OM:
    #                    [ 0] [1] [2]  [3] [4] [5]  [6]  [7]  [8]  [9] [10] [11] 
    ####ppDrift_1 =          [ 1,  1, 1.0,  0,  0, 1.0, 1.0, 1.0, 1.0,  0,  0,   0]   
    ####ppFinal =            [ 0,  0, 1.0,  0,  0, 1.0, 1.0, 1.0, 1.0,  0,  0,   0]

    ppDrift_1 =          [ 0,  0, 1.0,  0,  0, 1.0, 2.0, 1.0, 2.0,  0,  0,   0]   
    ppFinal =            [ 0,  0, 1.0,  0,  0, 0.5, 0.5, 0.5, 0.5,  0,  0,   0]
    optBL = SRWLOptC([Drift_1],  [ppDrift_1, ppFinal])
    wfr1d = copy.deepcopy(Wfrin)
    srwl.PropagElecField(wfr1d, optBL)
    arI = array('f', [0]*wfr1d.mesh.nx*wfr1d.mesh.ny) #"flat" array to take 2D intensity data
    srwl.CalcIntFromElecField(arI, wfr1d, 6, 0, 3, wfr1d.mesh.eStart, 0, 0) #extracts intensity    
    arP = array('d', [0]*wfr1d.mesh.nx*wfr1d.mesh.ny) #"flat" array to take 2D phase data (note it should be 'd')
    srwl.CalcIntFromElecField(arP, wfr1d, 0, 4, 3, wfr1d.mesh.eStart, 0, 0) #extracts radiation phase

    return [wfr1d, arI, arP]
    
    

def FullProp(zprop = 933.0, wfrS = [], line = SASE1_SPB_line, ppFinal = [ 0,  0, 1.0,  1,  0, 1.0, 1.0, 1.0, 1.0,  0,  0,   0]):
    
    [ Act_Elem_box, Act_Param_box ] = line(zprop)
    Act_Param_box.append( ppFinal )
    OptBL = SRWLOptC(Act_Elem_box, Act_Param_box)
    wfrP = copy.deepcopy(wfrS) #Genesis backpropagated    
    srwl.PropagElecField(wfrP, OptBL)
    
    return wfrP
    
    
def AVE_Save_Inte(wfrP=[], MESH = [], INT_arI_ave_P = [],  firstslice = 1):

    XsP=wfrP.mesh.xStart
    XfP=wfrP.mesh.xFin
    nxP=wfrP.mesh.nx
    YsP=wfrP.mesh.yStart
    YfP=wfrP.mesh.yFin
    nyP=wfrP.mesh.ny
    
    arIP = array('f', [0]*nxP*nyP) #"flat" array to take 2D intensity data
    srwl.CalcIntFromElecField(arIP, wfrP, 6, 0, 3, wfrP.mesh.eStart, 0, 0) #extracts intensity
    if firstslice == 1:        
        INT_arI_ave_P = np.array(arIP)        
        XsP0 = XsP
        XfP0 = XfP
        YsP0 = YsP
        YfP0 = YfP
        nxP0 = nxP
        nyP0 = nyP
    else:
        XsP0 = MESH[0]
        XfP0 = MESH[1]
        nxP0 = MESH[2]
        YsP0 = MESH[3]
        YfP0 = MESH[4]        
        nyP0 = MESH[5]
        XMESH = np.linspace(XsP0, XfP0, nxP0)
        YMESH = np.linspace(YsP0, YfP0, nyP0)
        dataI = np.array( arIP )
        zI    = dataI.reshape( nyP, nxP )
        Xact = np.linspace(XsP, XfP, nxP)
        Yact = np.linspace(YsP, YfP, nyP)
        Interdata = interpolate.interp2d(Xact, Yact, zI)
        zI_inte    = Interdata(XMESH, YMESH)
        INT_arIP   = zI_inte.reshape(nyP*nxP)
        INT_arI_ave_P = INT_arI_ave_P + np.array(INT_arIP)

    wfrP.mesh.xStart = XsP0
    wfrP.mesh.xFin   = XfP0
    wfrP.mesh.nx     = nxP0
    wfrP.mesh.yStart = YsP0
    wfrP.mesh.yFin   = YfP0
    wfrP.mesh.ny     = nyP0
    wfrP.mesh.ne     = 1
    

    return [INT_arI_ave_P, [XsP0,XfP0,nxP0,YsP0,YfP0,nyP0]]


    

      
