from pylab import *
import time
import pyfftw
import multiprocessing
import fftw3
import sharedmem as shm
import copy
from scipy.fftpack import fft, ifft


def threadfft(data,i,ncores,n1,n2):
    """Transform"""
    sp = np.roll(fft(data[i,:]), n2/2)
    sp = np.roll( sp, n2/2)
    data[i,:] = ifft(sp)

def threadfftw(dataw,i,ncores,n1,n2):
    """Transform"""
    sp = np.roll(pyfftw.interfaces.numpy_fft.fft(dataw[i,:], threads=1), n2/2)
    sp = np.roll( sp, n2/2)
    dataw[i,:] = pyfftw.interfaces.numpy_fft.ifft(sp, threads=1 )

ncores = multiprocessing.cpu_count()/8
#print 'Number of cores: ', ncores

#
# initialize matrix and shared-memory matrix
# for multiprocessing matrix has to be in shared memory
#
n1 = 101 * 101
n2 = 13000

f = np.zeros([n1,n2], dtype=complex)
data = shm.empty((n1,n2,), np.complex)

t1 = time.time()

for i1 in xrange(n1):
	data[i1,:] = np.random.random_sample(n2) + 1j * np.random.random_sample(n2)

print 'Initialization..........: {0:8.3f} sec'.format(time.time() - t1)
t1 = time.time()

#
# initialize aligned shared-memory matrix
# has to be aligned or pyfftw will become incredibly slow
#
dtype = np.dtype(np.complex)
nbytes = n1 * n2 * dtype.itemsize
buf = shm.empty(nbytes + 16, dtype=np.uint8)
start_index = -buf.ctypes.data % 16
dataw = buf[start_index:start_index + nbytes].view(dtype).reshape(n1, n2)

for i1 in xrange(n1):
        dataw[i1,:] = np.random.random_sample(n2) + 1j * np.random.random_sample(n2)

print 'Initialization (aligned): {0:8.3f} sec'.format(time.time() - t1)
t1 = time.time()
#
# copy matrix
#
f = copy.deepcopy(data)	
print 'matrix copy.............: {0:8.3f} sec'.format(time.time() - t1)
t1 = time.time()

#
#  fft with numpy
#
for i in xrange(n1):
    sp = np.roll(np.fft.fft(f[i,:]), n2/2)
    sp = np.roll( sp, n2/2)
    f[i,:] = np.fft.ifft(sp)

print 'numpy...................: {0:8.3f} sec'.format(time.time() - t1)

# print np.subtract(data, f)

#
#  fft with pools & scipy
#
t1 = time.time()
pyfftw.interfaces.cache.enable()

pool = multiprocessing.Pool()
tasks = [pool.apply_async(threadfft, (data, i, ncores, n1, n2))	 for i in range(n1)]
#print '[pool tasks running] ', len(tasks)
for t in tasks:
	t.wait()
pool.close()
pool.join()

print 'pool (scipy)............: {0:8.3f} sec'.format(time.time() - t1)
# print np.subtract(data, f)  - should be all zeros.

#
#  fft with pools & pyfftw
#
t1 = time.time()

pool = multiprocessing.Pool()
tasks = [pool.apply_async(threadfftw, (dataw, i, ncores, n1, n2))	 for i in range(n1)]
#print '[pool tasks running] ', len(tasks)
for t in tasks:
	t.wait()
pool.close()
pool.join()

print 'pool (pyfftw)...........: {0:8.3f} sec'.format(time.time() - t1)

#
#  fft with scipack
#
t1 = time.time()
for i in xrange(n1):
    sp = np.roll(fft(f[i,:]), n2/2)
    sp = np.roll( sp, n2/2)
    f[i,:] = ifft(sp)

print 'scipy...................: {0:8.3f} sec'.format(time.time() - t1)

#
#  fft with pyfftw
#  create aligned matrix. would work on shm matrix as well, but slower
#
pyfftw.interfaces.cache.enable()
f = pyfftw.n_byte_align_empty((n1,n2), 16, 'complex')
for i1 in xrange(n1):
        f[i1,:] = np.random.random_sample(n2) + 1j * np.random.random_sample(n2)

print 'Initialization (aligned): {0:8.3f} sec'.format(time.time() - t1)
t1 = time.time()

for i in xrange(n1):
    sp = np.roll(pyfftw.interfaces.numpy_fft.fft(f[i,:], threads=4), n2/2)
    sp = np.roll( sp, n2/2)
    f[i,:] = pyfftw.interfaces.numpy_fft.ifft(sp, threads=4 )

print 'pyfftw(1) using 4 cores.: {0:8.3f} sec'.format(time.time() - t1)

#
#  fft with pyfftw and accumulated wisdom
#
for ncores in range(1,2):
	t1 = time.time()
	for i in xrange(n1):
		sp = np.roll(pyfftw.interfaces.numpy_fft.fft(f[i,:], threads=ncores), n2/2)
		sp = np.roll( sp, n2/2)
		f[i,:] = pyfftw.interfaces.numpy_fft.ifft(sp, threads=ncores)
		
	print("pyfftw(2) using 1 core..: {0:8.3f} sec ").format(time.time()-t1)
	t1 = time.time()

