from srwlib import *
from prop_io import *
import numpy as np



def SASE1_SPB_line(Zprop):
    '''
    Defines the SASE1 line:
    Zprop: position up to which propagation has to take place
    Output: element_list, parameter_list to be used to build a container up to Zprop
    '''

    # Directories definition
    sur_dir = '../../../../data/PROP/roughness/'                            

    # Mirror surface file names definition
    surf1 = 'surface1.dat'
    surf2 = 'surface2.dat'
    surf3 = 'surface3.dat'
    surf4 = 'surface4.dat'

    
    #Optical Elements and Propagation Parameters
    Source_KB1_distance=930.0 #Source to first KB mirror
    Source_OM1_distance=270.0 #Source to first Offset mirror
    OM1_OM2_distance=10.0     #Distance between centers of 1 and 2 OM
    KB1_KB2_distance=1.1      #Distance between centers of Vertically and Horizontally focusing K-B mirrors 
    image_distance=1.9        #last mirror center to image
    angVKB = 6e-03            #grazing angle at VKB center [rad]
    angHKB = 6e-03            #grazing angle at HKB center[rad]
    RoughRMS=1.0              #roughness rms in nm
    OMlen=0.8                 #offset mirror length in [m]
    OMang=3.6e-3              #offset mirror incidence angle [rad]
    KBlen=0.95                #KB mirror length

    #Definition of optical elements
    heightProfData1  = AuxReadInDataColumns(sur_dir+surf1, 2, '\t')
    heightProfData2  = AuxReadInDataColumns(sur_dir+surf2, 2, '\t')
    heightProfData3  = AuxReadInDataColumns(sur_dir+surf3, 2, '\t')
    heightProfData4  = AuxReadInDataColumns(sur_dir+surf4, 2, '\t')
    heightProfDataV1 = [heightProfData1[0],[x/np.std(heightProfData1[1])/1e9*RoughRMS for x in heightProfData1[1]]]
    heightProfDataV2 = [heightProfData2[0],[x/np.std(heightProfData2[1])/1e9*RoughRMS for x in heightProfData2[1]]]
    heightProfDataV3 = [heightProfData3[0],[x/np.std(heightProfData3[1])/1e9*RoughRMS for x in heightProfData3[1]]]
    heightProfDataH1 = [heightProfData4[0],[x/np.std(heightProfData4[1])/1e9*RoughRMS for x in heightProfData4[1]]]

    OMap       = OMlen*OMang                   #size of effective OM aperture
    KBap       = KBlen*angVKB                  #size of effective KB aperture
    OM_density = np.size(heightProfData1)/OMap #density of roughness profile data points within OM aperture
    KB_density = np.size(heightProfData3)/KBap

    rough_aperture_OM = OMap;
    rough_aperture_KB = KBap;
    N_points_OM       = int(rough_aperture_OM*OM_density)
    N_points_KB       = int(rough_aperture_KB*KB_density)

    OTE_OM1_V = SRWLOptT(_nx=2, _ny=N_points_OM, _rx=rough_aperture_OM, _ry=rough_aperture_OM)
    AuxTransmAddSurfHeightProfile(OTE_OM1_V, heightProfDataV1, 'y', OMang)
    OTE_OM2_V = SRWLOptT(_nx=2, _ny=N_points_OM, _rx=rough_aperture_OM, _ry=rough_aperture_OM)
    AuxTransmAddSurfHeightProfile(OTE_OM2_V, heightProfDataV2, 'y', OMang)
    OTE_KB1_V = SRWLOptT(_nx=2, _ny=N_points_KB, _rx=rough_aperture_KB, _ry=rough_aperture_KB)
    AuxTransmAddSurfHeightProfile(OTE_KB1_V, heightProfDataV3, 'y', angVKB)
    OTE_KB2_H = SRWLOptT(_nx=N_points_KB, _ny=2, _rx=rough_aperture_KB, _ry=rough_aperture_KB)
    AuxTransmAddSurfHeightProfile(OTE_KB2_H, heightProfDataH1, 'x', angHKB)

    OM1A = SRWLOptA('r', 'a', 0.1, OMap) # 1-st offset mirror effective aperture element
    OM2A = SRWLOptA('r', 'a', 0.1, OMap) # 2-nd offset mirror effective aperture element

    Drift_1 = SRWLOptD(Source_OM1_distance) #Drift    
    Drift_OM = SRWLOptD(OM1_OM2_distance) #Drift
    Drift_OM_KB = SRWLOptD(Source_KB1_distance-Source_OM1_distance-OM1_OM2_distance);
    VKB = SRWLOptMirEl(_p=Source_KB1_distance, _q=image_distance+KB1_KB2_distance, _ang_graz=angVKB, _r_sag=1.e+40, _size_tang=0.95, _nvx=0, _nvy=cos(angVKB), _nvz=-sin(angVKB), _tvx=0, _tvy=-sin(angVKB), _x=0, _y=0, _treat_in_out=1) #VKB Ellipsoidal Mirror
    Drift_VKB_HKB = SRWLOptD(KB1_KB2_distance) #Distance between centers of Vertically and Horizontally focusing K-B mirrors 
    HKB = SRWLOptMirEl(_p=Source_KB1_distance+KB1_KB2_distance, _q=image_distance, _ang_graz=angHKB, _r_sag=1.e+40, _size_tang=0.95, _nvx=cos(angHKB), _nvy=0, _nvz=-sin(angHKB), _tvx=-sin(angHKB), _tvy=0, _x=0, _y=0, _treat_in_out=1) #HKB Ellipsoidal Mirror
    Drift_2 = SRWLOptD(image_distance)

                           

    #Wavefront Propagation Parameters with OM:
    #                    [ 0] [1] [2]  [3] [4] [5]  [6]  [7]  [8]  [9] [10] [11]     
    
    ppDrift_1 =          [ 0,  0, 1.0,  0,  0, 7.0, 1.0, 7.0, 1.0,  0,  0,   0]
    ppOTE_OM1_V=         [ 0,  0, 1.0,  0,  0, 1.0, 1.0, 1.0, 1.0,  0,  0,   0]
    ppOM1A=              [ 0,  0, 1.0,  0,  0, 1.0, 1.0, 1.0, 1.0,  0,  0,   0]
    ppDrift_OM=          [ 0,  0, 1.0,  0,  0, 1.0, 1.0, 1.0, 1.0,  0,  0,   0]
    ppOTE_OM2_V=         [ 0,  0, 1.0,  0,  0, 1.0, 1.0, 1.0, 1.0,  0,  0,   0]
    ppOM2A=              [ 0,  0, 1.0,  0,  0, 1.0, 1.0, 1.0, 1.0,  0,  0,   0] 
    ppDrift_OM_KB=       [ 0,  0, 1.0,  0,  0, 5.0, 0.3, 5.0, 0.3,  0,  0,   0] # Uncomment to obtain Fig1 Fig2 Fig3 Fig4
    ppVKB =              [ 0,  0, 1.0,  1,  0, 1.0, 1.0, 1.0, 1.0,  0,  0,   0]
    ppOTE_KB1_V =        [ 0,  0, 1.0,  1,  0, 1.0, 1.0, 1.0, 1.0,  0,  0,   0]
    ppDrift_VKB_HKB =    [ 0,  0, 1.0,  1,  0, 1.0, 1.0, 1.0, 1.0,  0,  0,   0]
    ppHKB =              [ 0,  0, 1.0,  1,  0, 1.0, 1.0, 1.0, 1.0,  0,  0,   0]
    ppOTE_KB2_H =        [ 0,  0, 1.0,  1,  0, 1.0, 1.0, 1.0, 1.0,  0,  0,   0]
    ppDrift_2 =          [ 0,  0, 1.0,  1,  0, 1.0, 1.0, 1.0, 1.0,  0,  0,   0]
    
    
    #[ 0]: Auto-Resize (1) or not (0) Before propagation
    #[ 1]: Auto-Resize (1) or not (0) After propagation
    #[ 2]: Relative Precision for propagation with Auto-Resizing (1. is nominal)
    #[ 3]: Allow (1) or not (0) for semi-analytical treatment of the quadratic (leading) phase terms at the propagation
    #[ 4]: Do any Resizing on Fourier side, using FFT, (1) or not (0)
    #[ 5]: Horizontal Range modification factor at Resizing (1. means no modification)
    #[ 6]: Horizontal Resolution modification factor at Resizing
    #[ 7]: Vertical Range modification factor at Resizing
    #[ 8]: Vertical Resolution modification factor at Resizing
    #[ 9]: Type of wavefront Shift before Resizing (not yet implemented)
    #[10]: New Horizontal wavefront Center position after Shift (not yet implemented)
    #[11]: New Vertical wavefront Center position after Shift (not yet implemented)

    elements       = [ Drift_1          ,
                       OTE_OM1_V        ,
                       OM1A             ,
                       Drift_OM         ,
                       OTE_OM2_V        ,
                       OM2A             ,
                       Drift_OM_KB      ,
                       VKB              ,
                       OTE_KB1_V        ,
                       Drift_VKB_HKB    ,
                       HKB              ,
                       OTE_KB2_H        ,
                       Drift_2 ]

    parameters      = [ ppDrift_1        ,
                       ppOTE_OM1_V      ,
                       ppOM1A           ,
                       ppDrift_OM       ,
                       ppOTE_OM2_V      ,
                       ppOM2A           ,
                       ppDrift_OM_KB    ,
                       ppVKB            ,
                       ppOTE_KB1_V      ,
                       ppDrift_VKB_HKB  ,
                       ppHKB            ,
                       ppOTE_KB2_H      ,
                       ppDrift_2 ]

    positions        = [ Source_OM1_distance,
                       Source_OM1_distance,
                       Source_OM1_distance,
                       Source_OM1_distance+OM1_OM2_distance,
                       Source_OM1_distance+OM1_OM2_distance,
                       Source_OM1_distance+OM1_OM2_distance,
                       Source_KB1_distance,
                       Source_KB1_distance,
                       Source_KB1_distance,
                       Source_KB1_distance+KB1_KB2_distance,
                       Source_KB1_distance+KB1_KB2_distance,
                       Source_KB1_distance+KB1_KB2_distance,
                       Source_KB1_distance+KB1_KB2_distance+image_distance ]

    drifts      = [ [Source_OM1_distance,  ppDrift_1],                     
                       [Source_OM1_distance+OM1_OM2_distance, ppDrift_OM],                                             
                       [Source_KB1_distance, ppDrift_OM_KB],                      
                       [Source_KB1_distance+KB1_KB2_distance, ppDrift_VKB_HKB],
                       [Source_KB1_distance+KB1_KB2_distance+image_distance, ppDrift_2] ]		       


    
    element_list  = []
    parameter_list = []
    
    for k in range(len(positions)):              
        if (Zprop > positions[k]):              
            element_list.append(  elements[k]  )
            parameter_list.append( parameters[k] )
            
    ppDrift_fin = drifts[0][1]
    Delta = Zprop	
    for dr in range(len(drifts)): 	
        if (Zprop > drifts[dr][0]):	 
            Delta = Zprop - drifts[dr][0]
            ppDrift_fin = drifts[min(dr+1,len(drifts)-1)][1]


    
    if Delta > 0:
    
        drift_fin   = SRWLOptD(Delta)        
        element_list.append( drift_fin )
        parameter_list.append( ppDrift_fin )
   

    return element_list, parameter_list 


