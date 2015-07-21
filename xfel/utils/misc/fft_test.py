from pylab import *
import time
import pyfftw
import multiprocessing
import fftw3
import sharedmem as shm
import copy
from scipy.fftpack import fft, ifft

n1 = 101 * 101
n2 = 13100
ncores = multiprocessing.cpu_count()/8

def threadfft(data,filt, i,ncores,n1,n2):
    """Transform"""
    sp = np.roll(fft(data[i,:]), n2/2)
    sp = sp * filt
    sp = np.roll( sp, n2/2)
    data[i,:] = ifft(sp)

def test1():
	f = np.zeros([n1,n2], dtype=complex)

	print 'init'

	for i1 in xrange(n1):
		f[i1,:] = np.random.random_sample(n2) + 1j * np.random.random_sample(n2)

	t1 = time.time()	
	for i in xrange(n1/100):
		print 'averaging', i
		sp = np.roll(np.fft.fft(f[i,:]), n2/2)
		sp = np.roll( sp, n2/2)
		f[i,:] = np.fft.ifft(sp)

	print time.time() - t1, 'sec'

def test2():
	f = np.zeros([n1,n2], dtype=complex)
	data = shm.empty((n1,n2,), np.complex)
	print 'init'

	for i1 in xrange(n1):
		data[i1,:] = np.random.random_sample(n2) + 1j * np.random.random_sample(n2)

	t1 = time.time()


	filt = np.random.random_sample(n2) + 1j * np.random.random_sample(n2)

	pyfftw.interfaces.cache.enable()

	pool = multiprocessing.Pool()
	tasks = [pool.apply_async(threadfft, filt, (data, i, ncores, n1, n2))	 for i in range(n1)]
        #print '[pool tasks running] ', len(tasks)
	for t in tasks:
		t.wait()
	pool.close()
	pool.join()
	
	print data[32,14]

	print time.time() - t1, 'sec'


if __name__ == "__main__":
	test2()
