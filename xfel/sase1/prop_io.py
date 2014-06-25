from mpi4py import MPI

comm  = MPI.COMM_WORLD   #Creates one common object "communicator" knwoning about processes
rank  = comm.Get_rank()  #Process number
nproc = comm.Get_size()  #Total number of processes


import numpy as np
import h5py

def save_wfr_h5(wfr = None, n_slice= None, subgroup = None, n_extra = 0, filename = None, local_data_len = 0):    
    
    #Xs=wfr.mesh.xStart
    #Xf=wfr.mesh.xFin
    nx=wfr.mesh.nx
    #Ys=wfr.mesh.yStart
    #Yf=wfr.mesh.yFin
    ny=wfr.mesh.ny
    
    EX = np.empty(shape=(nx,ny) ,dtype=complex)
    EY = np.empty(shape=(nx,ny) ,dtype=complex)
    xmesh = np.array([wfr.mesh.xStart,wfr.mesh.xFin,wfr.mesh.nx])
    ymesh = np.array([wfr.mesh.yStart,wfr.mesh.yFin,wfr.mesh.ny])
    
    np.real(EX)[::] = np.reshape(wfr.arEx[::2] ,(nx,ny))
    np.imag(EX)[::] = np.reshape(wfr.arEx[1::2],(nx,ny))
    np.real(EY)[::] = np.reshape(wfr.arEy[::2] ,(nx,ny))
    np.imag(EY)[::] = np.reshape(wfr.arEy[1::2],(nx,ny))
      

    if rank == 0:
        ##if n_slice < n_extra:
        ##wfrout.append(wfr)
        ##if n_slice > n_extra -1:
        ##tmp_buf2.append(wfr)
        group_name = str(n_slice+1)+'.slice'

    #ifname = os.path.join(strOutputDataFolder,name0)		
    else:
        ##tmp_buf2.append(wfr)	
        #print ('loclen=',local_data_len)
        group_name = str(rank * local_data_len + n_extra + n_slice+1)+'.slice'
        #ifname = os.path.join(strOutputDataFolder,group_name)
    
    
    
    for i in xrange(nproc):
        if rank == i:
            f = h5py.File(filename, 'r+')
            if not group_name in f.keys():
                g =  f.create_group(group_name)
        else:
            g = f[group_name]	
            if not subgroup in g.keys():
                sg = g.create_group(subgroup)
            else: 
                sg = g[subgroup]

           
            sg.create_dataset(group_name+'.fld_X', data = EX)
            sg.create_dataset(group_name+'.fld_Y', data = EY)
            sg.create_dataset(group_name+'.msh_X', data = xmesh)
            sg.create_dataset(group_name+'.msh_Y', data = ymesh)
            f.close()
        
    if n_slice < local_data_len: comm.barrier()
    return   #[tmp_buf2] 
    
    
def save_intensity_h5(inte = '', mesh = '', group_name = ''):
    
    
    for i in xrange(nproc):
        if rank == i:
            subgroup=str(rank)
            f = h5py.File(filename, 'r+')
            if not group_name in f.keys():
                g =  f.create_group(group_name)
            else:
                g = f[group_name]	

        if not 'msh' in g.keys():	        
            g.create_dataset('msh', data = MESHw)

            g.create_dataset(subgroup, data = inte)
            f.close()
            
    comm.barrier()
    return

def AuxReadInDataColumns(filePath, nCol, strSep):
    f = open(filePath, 'r')
    resCols = []
    for iCol in range(nCol):
        resCols.append([])

    curLine = f.readline()
    while len(curLine) > 0:
        curLineParts = curLine.split(strSep)
        for iCol in range(nCol):
            if(iCol < len(curLineParts)):
                resCols[iCol].append(float(curLineParts[iCol]))
        curLine = f.readline()
    f.close()
    return resCols #attn: returns lists, not arrays!



#Setup Transmission optical element with 1D heght profile data
def AuxTransmAddSurfHeightProfile(optSlopeErr, heightProfData, dim, ang):
    argHeightProfData = heightProfData[0]
    valHeightProfData = heightProfData[1]
    sinAng = np.sin(ang)
    npData = len(heightProfData[0])
    
    #xStep = optSlopeErr.rx/(optSlopeErr.nx - 1)
    #yStep = optSlopeErr.ry/(optSlopeErr.ny - 1)
    #y = optSlopeErr.y - 0.5*optSlopeErr.ry

    auxMesh = optSlopeErr.mesh
    xStep = (auxMesh.xFin - auxMesh.xStart)/(auxMesh.nx - 1)
    yStep = (auxMesh.yFin - auxMesh.yStart)/(auxMesh.ny - 1)

    y = auxMesh.yStart
    hApprox = 0
    ipStart = 0
    #for iy in range(optSlopeErr.ny):
    for iy in range(auxMesh.ny):
        if('y' in dim):
            hApprox = 0
            y1 = argHeightProfData[ipStart]*sinAng
            for i in range(ipStart + 1, npData):
                y2 = argHeightProfData[i]*sinAng
                if((y1 <= y) and (y < y2)):
                    hApprox = ((valHeightProfData[i] - valHeightProfData[i-1])/((argHeightProfData[i] - argHeightProfData[i-1])*sinAng))*(y - y1) + valHeightProfData[i-1]
                    #print(ipStart, i, iy, y1, y, y2, argHeightProfData[i-1], argHeightProfData[i], valHeightProfData[i-1], valHeightProfData[i], hApprox)
                    ipStart = i - 1
                    break
                y1 = y2

        #x = optSlopeErr.x - 0.5*optSlopeErr.rx
        x = auxMesh.xStart
        
        #for ix in range(optSlopeErr.nx):
        for ix in range(auxMesh.nx):
            if('x' in dim):
                if(ix == 0): ipStart = 0
                hApprox = 0
                x1 = argHeightProfData[ipStart]*sinAng
                for i in range(ipStart + 1, npData):
                    x2 = argHeightProfData[i]*sinAng
                    if((x1 <= x) and (x < x2)):
                        hApprox = ((valHeightProfData[i] - valHeightProfData[i-1])/((argHeightProfData[i] - argHeightProfData[i-1])*sinAng))*(x - x1) + valHeightProfData[i-1]
                        ipStart = i - 1
                        break
                    x1 = x2
            #ofst = 2*ix + (2*optSlopeErr.nx)*iy
            ofst = 2*ix + (2*auxMesh.nx)*iy

            optSlopeErr.arTr[ofst] = 1. #Amplitude Transmission
            optSlopeErr.arTr[ofst + 1] = 0. #Optical Path Difference
            if(hApprox != 0):
                optSlopeErr.arTr[ofst + 1] = -2*sinAng*hApprox #Optical Path Difference (to check sign!)
                #print(ix, iy, optSlopeErr.arTr[ofst + 1])
            x += xStep
        y += yStep


