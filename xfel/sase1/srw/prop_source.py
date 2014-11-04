from prop_utils import *
from prop_io	import *

from xframework.common import math

def fwhm_gauss_fit(X,Y):

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



#################################################################
###################						  ####################
################### Parameters to be defined ####################
###################		by the user	   ####################
###################						  ####################
#################################################################

dat_dir = '../../../data/PROP/'			 #Genesis data

# file names definition

outgenfile = 'sase2.4p1keV.tap.1.out'
#outgenfile = 'run.0.gout'
filename = 'Source.h5' #h5 output file
genfile = outgenfile+'.dfl'

zin   = -20.0
zfin  = -40.0
zstep = 1.0 


zprop_list = np.arange(zfin,zin+1,zstep)
 

##################################################################




if rank == 0:
	print('*SRW*')
	print('Simulating propagation of an FEL X-ray beam through the SPB line at SASE1')	
	f = h5py.File(filename, 'w')
	f.close()   
	list_inte = []
	list_rms_x = []
	list_rms_y = []
	list_fwhm_x = []
	list_fwhm_y = []

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

Tmesh=Xmesh
w0	= np.sqrt(zrayl*xlamds/np.pi)
sigrB = np.sqrt(rxbeam**2 + rybeam**2)
sigrF = w0
dgrid = rmax0*(sigrB+sigrF)/2.0 #Mesh from -grid to +grid; This is the genesis input parameter dgrid/2

h_planck   = 6.62606957e-34
conv_to_ev = 6.24150934e18
c_light	= 299792458.0
PhEne = h_planck*c_light/xlamds * conv_to_ev

if not out('dgrid') == 0.0: 
	dgrid = out('dgrid')

[wfrG, field] = GeneRead(comm = comm, filename = dat_dir+genfile, Tmesh = Tmesh, PhEne = PhEne, dgrid = dgrid)
Nzprop	 = len(zprop_list)


for DeltaSource in zprop_list:

	n_slices = len(field)  
	n_slices = comm.bcast(n_slices, root=0)
	#XMESH_list  = comm.bcast(XMESH_list, root=0)
	#YMESH_list  = comm.bcast(YMESH_list, root=0)
	n1	   = Xmesh
	n2	   = Ymesh

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

	comm.barrier()

	for slicen in range(slices_to_proc):

		print 'rank ',rank,' processing slice ',slicen+1,' out of ',slices_to_proc
	
		if rank == 0: sl = field[slicen]
		else: sl = tmp_buf[slicen]
		
		count = 0

	for j in xrange(Tmesh):
		for k in xrange(Tmesh):
			wfrG.arEx[count] = np.float(np.real(sl[j][k]))
			count = count + 1
			wfrG.arEx[count] = np.float(np.imag(sl[j][k]))
			count = count + 1

	# Find source wavefront
	[wfrS, arIS, arPS] = Source_Prop(Len_drft = DeltaSource, Wfrin = wfrG)			 
	if slicen == 0:
			arI_aveS = np.array(arIS)	 	  
			isfirstslice = 1
	else:
			arI_aveS = arI_aveS + np.array(arIS)	   
			isfirstslice = 0	

	print 'rank ',rank,' has happily finished.'
	comm.barrier()

	print 'Now rank ',rank,' will start the gathering'
	parzialeI_S = comm.reduce(arI_aveS, root = 0)

	if rank == 0: 
		print filename
		f = h5py.File(filename, 'r+')
		XMESHS = np.array([wfrS.mesh.xStart,wfrS.mesh.xFin,wfrS.mesh.nx])

		YMESHS = np.array([wfrS.mesh.yStart,wfrS.mesh.yFin,wfrS.mesh.ny])

	nameG = 'Intensity_z='+str(DeltaSource)
	g = f.create_group(nameG)
	data_i=parzialeI_S.reshape(XMESHS[2],YMESHS[2])
	g.create_dataset('Inte', data = data_i)
	g.create_dataset('msh',  data = np.concatenate([XMESHS,YMESHS]))
	f.close()

	x=np.linspace(XMESHS[0],XMESHS[1],XMESHS[2])
	y=np.linspace(YMESHS[0],YMESHS[1],YMESHS[2])
	mu_x, mu_y, rms_x, rms_y, rho = math.fit_gauss_2d(x,y,data_i)


	isumy=np.sum(data_i,1)
	isumx=np.sum(data_i,0)
	gisumy, fwhmy=fwhm_gauss_fit(y,isumy)				
	gisumx, fwhmx=fwhm_gauss_fit(x,isumx)		
		
	
	max_inte = np.max(data_i)/n_slices
	list_inte.append(max_inte)
	list_rms_x.append(rms_x)
	list_rms_y.append(rms_y)
	list_fwhm_x.append(fwhmx)
	list_fwhm_y.append(fwhmy)
		
if rank == 0: 	
	f = h5py.File(filename, 'r+')
	nameG = 'Source_analysis'
	g = f.create_group(nameG)	
	
	g.create_dataset('z_pos', data = zprop_list)
	g.create_dataset('max_i', data = list_inte)
	g.create_dataset('rms_x', data = list_rms_x)
	g.create_dataset('rms_y', data = list_rms_y)
	g.create_dataset('fwhm_x', data = list_fwhm_x)
	g.create_dataset('fwhm_y', data = list_fwhm_y)
	
	f.close()
	
