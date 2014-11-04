import os, sys
from xframework.utils.launcher import *

Hostnames  = 'it-hpc.hosts'

if __name__ == "__main__":

	cmd = 'export PYTHONPATH=/data/netapp/xfel/gianluca/srw_python/:/data/netapp/xfel/products/xcode;export MPI_PYTHON_SITEARCH= '
	os.system(cmd)

	
	if sys.argv[1] == '-par':
		launcher = MpiLauncher()
		launcher.mpiParameters = "-x PYTHONPATH=/data/netapp/xfel/gianluca/srw_python/:/data/netapp/xfel/products/xcode: -x MPI_PYTHON_SITEARCH=: -x LD_LIBRARY_PATH=/usr/local/lib:/opt/intel/2011/lib/intel64:/usr/lib64/openmpi-intel/lib -hostfile it-hpc.hosts"		
		launcher.nproc = 200 #361 #3 #32 *  sum(1 for line in open('./'+Hostnames)) #Number of processor is 64 multiplied by number of nodes used that is the number of lines in the hostfile
		ARGS   =   ''.join([''])	    
		
		
	else:
		launcher = LocalLauncher()
		launcher.outputfile("log.txt")            	            			
	
	launcher.program = "python2.7 prop_par_v2.py "
	#launcher.program = "python2.7 prop_source.py "
	
	launcher.dir = "./"
	launcher.prepare()
	launcher.launch()  	
