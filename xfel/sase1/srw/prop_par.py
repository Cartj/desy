from prop_utils import *
from prop_io    import *

#################################################################
###################                          ####################
################### Parameters to be defined ####################
###################        by the user       ####################
###################                          ####################
#################################################################

dat_dir = '../../../../data/PROP/'             #Genesis data

# file names definition

outgenfile = 'sase2.4p1keV.tap.1.out'
#outgenfile = 'run.0.gout'
filename = '../../../../data/PROP/Output/Output.h5' #h5 output file
genfile = outgenfile+'.dfl'

lineprop = SASE1_SPB_line


sample   = 800 #5               #'Sample' slice to define boundaries when interpolating; use 800 with sase2.4p1keV.tap.1.out

DeltaSource = -26.0

zafterOM = 285.0
zKB      = 930.0
zfocus   = 933.0
zafterf  = 933.05

ppFinal1 =  [ 0,  0, 1.0,  0,  0, 0.01, 40.0, 0.020, 40.0,  0,  0,   0] #Uncomment to obtain Fig1 - Genesis - starts with backprop source 
ppFinal2 =  [ 0,  0, 1.0,  0,  0,  0.5,  0.2, 0.5,    0.2,  0,  0,   0] 
ppFinal3 =  [ 0,  0, 1.0,  0,  0, 0.4, 0.4, 0.4, 0.4,  0,  0,   0]
ppFinal4 =  [ 0,  0, 1.0,  0,  0, 0.1, 0.8, 0.1, 0.8,  0,  0,   0]


zprop_list = [zafterOM, zKB, zfocus, zafterf]
ppFin_list = [ppFinal4, ppFinal2, ppFinal1, ppFinal3]
##zprop_list = [zfocus, zKB]
##ppFin_list = [ppFinal1, ppFinal2]

##################################################################



if rank == 0:
    print('*SRW*')
    print('Simulating propagation of an FEL X-ray beam through the SPB line at SASE1')
    



print 'Hello, I am ',rank

out = readGenesisOutput(dat_dir+outgenfile)

# Parameters from the Genesis input file

Xmesh = int(out('ncar'))
Ymesh = int(out('ncar'))
zrayl =  out('zrayl')
zwaist=  out('zwaist')
rmax0 =  out('rmax0')
xlamds=  out('xlamds')
rxbeam=  out('rxbeam')
rybeam=  out('rybeam')
zstop =  out('zstop')

print rank, '      ', zstop

Tmesh=Xmesh
w0    = np.sqrt(zrayl*xlamds/np.pi)
sigrB = np.sqrt(rxbeam**2 + rybeam**2)
sigrF = w0
dgrid = rmax0*(sigrB+sigrF)/2.0 #Mesh from -grid to +grid; This is the genesis input parameter dgrid/2

h_planck   = 6.62606957e-34
conv_to_ev = 6.24150934e18
c_light    = 299792458.0
PhEne = h_planck*c_light/xlamds * conv_to_ev

if not out('dgrid') == 0.0: 
    dgrid = out('dgrid')

[wfrG, field] = GeneRead(comm = comm, filename = dat_dir+genfile, Tmesh = Tmesh, PhEne = PhEne, dgrid = dgrid)
Nzprop     = len(zprop_list)



####################################   First goes through the sample slice   ###################################

XMESH_list = []
YMESH_list = []

if rank == 0:
    
	sl = field[sample]
	count = 0
	for j in range(Tmesh):
		for k in range(Tmesh):
			wfrG.arEx[count] = np.float(np.real(sl[j][k]))
	                count = count + 1
        	        wfrG.arEx[count] = np.float(np.imag(sl[j][k]))
                	count = count + 1

	[wfrS, arIS, arPS] = Source_Prop(Len_drft = DeltaSource, Wfrin = wfrG)
	        
	XMESHS = np.array([wfrS.mesh.xStart,wfrS.mesh.xFin,wfrS.mesh.nx])
	YMESHS = np.array([wfrS.mesh.yStart,wfrS.mesh.yFin,wfrS.mesh.ny])	
	
	for pos in xrange(Nzprop):    
        	wfr_Z = FullProp(zprop = zprop_list[pos], wfrS = wfrS, line = lineprop, ppFinal = ppFin_list[pos])
		XMESH_list.append(np.array([wfr_Z.mesh.xStart,wfr_Z.mesh.xFin,wfr_Z.mesh.nx]))
		YMESH_list.append(np.array([wfr_Z.mesh.yStart,wfr_Z.mesh.yFin,wfr_Z.mesh.ny]))	
    
  
comm.Barrier()    

################################################################################################################

n_slices = len(field)  
n_slices = comm.bcast(n_slices, root=0)
XMESH_list  = comm.bcast(XMESH_list, root=0)
YMESH_list  = comm.bcast(YMESH_list, root=0)
n1       = Xmesh
n2       = Ymesh

local_data_len = comm.bcast(int(n_slices / nproc), root=0)

print 'rank ',rank,'has loclen = ',local_data_len

n_extra = n_slices - local_data_len * nproc
print n_slices
tmp_buf = np.zeros([local_data_len,n1,n2], dtype=complex) 

if rank == 0:
    slice_start  = rank * local_data_len
    slices_to_proc = local_data_len + n_extra    
else:
    slice_start = rank * local_data_len + n_extra
    slices = []
    slices_to_proc = local_data_len   

comm.Barrier()    
comm.Scatter([field[n_extra:],  MPI.COMPLEX], [tmp_buf, MPI.COMPLEX])

tmp_buf_list = []
tmp_int_list = []
wfrout   = []
INT_arI_ave_P = []
INT_arI_ave_P_list = [None] * Nzprop
mesh_list_p = [None] * Nzprop



if rank == 0:
    f = h5py.File(filename, 'w')
    f.close()
        
comm.barrier()

for slicen in range(slices_to_proc):

    print 'rank ',rank,' processing slice ',slicen+1,' out of ',slices_to_proc
    if rank == 0:    	
    	sl = field[slicen]
    else:
    	sl = tmp_buf[slicen]
    count = 0
    for j in range(Tmesh):
        for k in range(Tmesh):
            wfrG.arEx[count] = np.float(np.real(sl[j][k]))
            count = count + 1
            wfrG.arEx[count] = np.float(np.imag(sl[j][k]))
            count = count + 1
    
    ####ADDED
    arIG = array('f', [0]*wfrG.mesh.nx*wfrG.mesh.ny) #"flat" array to take 2D intensity data
    srwl.CalcIntFromElecField(arIG, wfrG, 6, 0, 3, wfrG.mesh.eStart, 0, 0) #extracts intensity   

    XMESHG = np.array([wfrG.mesh.xStart,wfrG.mesh.xFin,wfrG.mesh.nx])    ###added tge genesis mesh
    YMESHG = np.array([wfrG.mesh.yStart,wfrG.mesh.yFin,wfrG.mesh.ny])	
    
    
    # Find source wavefront
    [wfrS, arIS, arPS] = Source_Prop(Len_drft = DeltaSource, Wfrin = wfrG)             
    if slicen == 0:
        arI_aveS = np.array(arIS)     	  
	isfirstslice = 1
    else:
        arI_aveS = arI_aveS + np.array(arIS)	   
	isfirstslice = 0    
    Save_To_h5(wfr = wfrS, slicen= slicen, n_extra = n_extra, subgroup = 'z='+str(DeltaSource), filename = filename,local_data_len =local_data_len )   
    
    
    ########### ADDS the output genesis file as well! ############
    if slicen == 0:
        arI_aveG = np.array(arIG)     	  
	isfirstslice = 1
    else:
        arI_aveG = arI_aveG + np.array(arIG)	   
	isfirstslice = 0    
    Save_To_h5(wfr = wfrG, slicen= slicen, n_extra = n_extra, subgroup = 'z=0', filename = filename,local_data_len =local_data_len )    
    ##############################################################
                 
    for pos in xrange(Nzprop):    
        wfr_Z = FullProp(zprop = zprop_list[pos], wfrS = wfrS, line = lineprop, ppFinal = ppFin_list[pos])		
	[INT_arI_ave_P_list[pos], mesh_list_p[pos]] = AVE_Save_Inte(wfrP=wfr_Z, MESH = np.concatenate([XMESH_list[pos],YMESH_list[pos]]), INT_arI_ave_P = INT_arI_ave_P_list[pos],  firstslice = isfirstslice)   #uses _list now
	Save_To_h5(wfr = wfr_Z, slicen= slicen, n_extra = n_extra, subgroup = 'z='+str(zprop_list[pos]),filename = filename,local_data_len =local_data_len )      
	
print 'rank ',rank,' has happily finished.'
comm.barrier()

print 'Now rank ',rank,' will start the gathering'
parzialeI_S = comm.reduce(arI_aveS, root = 0)
parzialeI_G = comm.reduce(arI_aveG, root = 0)   ####added the output from genesis

parzialeI_int = [None] * Nzprop

for pos in xrange(Nzprop):    
    parzialeI_int[pos] = comm.reduce(INT_arI_ave_P_list[pos], root=0)   ###uses _list now
    
if rank == 0: 
        print 'finalsize=',np.size(parzialeI_int)
	f = h5py.File(filename, 'r+')
	nameG = 'Intensity_z='+str(DeltaSource)
	g = f.create_group(nameG)
	g.create_dataset('Inte', data = parzialeI_S)
	g.create_dataset('msh',  data = np.concatenate([XMESHS,YMESHS]))
	f.close()
	################ and the undulator exit
	f = h5py.File(filename, 'r+')
	nameG = 'Intensity_z=0'
	g = f.create_group(nameG)
	g.create_dataset('Inte', data = parzialeI_G)
	g.create_dataset('msh',  data = np.concatenate([XMESHG,YMESHG]))
	f.close()
	for pos in xrange(Nzprop):
		f = h5py.File(filename, 'r+')
		nameG = 'Intensity_z='+str(zprop_list[pos])
		g = f.create_group(nameG)
		g.create_dataset('Inte', data = parzialeI_int[pos])  ###now it's an array
		g.create_dataset('msh',  data = mesh_list_p[pos])
		f.close    
	print xrange(Nzprop)
	print mesh_list_p
	
