from pylab import *
import pickle
import time

class SimInfo:
    def __init__(self, n=10):
        self.x = np.linspace(0,1,n)
        self.y = np.sin(self.x)
        
        
if __name__ == "__main__":
    o = SimInfo()
    t = 0
    while True:
        o.x = np.linspace(0, t)
        o.y = np.sin(o.x)  
        print 'saving ', t
        f_obj = open('dump.dat', 'wb')
        pickle.dump(o, f_obj)
        f_obj.close()
        t += 1
        time.sleep(2)

