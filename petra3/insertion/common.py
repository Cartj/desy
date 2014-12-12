'''
MBA-type var delay achromat
'''
from ocelot.gui.accelerator import *

def show_optics(tws, lat, beam, scale = 20.0):
    f=plt.figure()
    ax = f.add_subplot(211)
    ax.set_xlim(0, lat.totalLen)
    
    f.canvas.set_window_title('Betas [m]') 
    p1, = ax.plot(map(lambda p: p.s, tws), map(lambda p: p.beta_x, tws), lw=2.0)
    p2, = ax.plot(map(lambda p: p.s, tws), map(lambda p: p.beta_y, tws), lw=2.0)
    ax2 = ax.twinx()
    p3, = ax2.plot(map(lambda p: p.s, tws), map(lambda p: p.Dx, tws), 'r-', lw=2.0)
    plt.grid(True)
    plt.legend([p1,p2,p3], [r'$\beta_x$',r'$\beta_y$', r'$D_x$'], fancybox=True, framealpha=0.5)
    
    ax2 = f.add_subplot(212)
    plot_lattice(lat, ax2, alpha=0.5)
    
    # add beam size (arbitrary scale)
    
    s = np.array(map(lambda p: p.s, tws)) - tws[0].s
        
    sig_x = scale * np.array(map(lambda p: np.sqrt(p.beta_x*beam.emit_x), tws)) # 0.03 is for plotting same scale
    sig_y = scale * np.array(map(lambda p: np.sqrt(p.beta_y*beam.emit_y), tws))
    
    x = scale * np.array(map(lambda p: p.x, tws))
    y = scale * np.array(map(lambda p: p.y, tws))
    
    
    plt.plot(s, x + sig_x, color='#0000AA', lw=2.0)
    plt.plot(s, x-sig_x, color='#0000AA', lw=2.0)
    
    plt.plot(s, sig_y, color='#00AA00', lw=2.0)
    plt.plot(s, -sig_y, color='#00AA00', lw=2.0)
    
    #f=plt.figure()
    plt.plot(s, x, 'r--', lw=2.0)
    #plt.plot(s, y, 'r--', lw=2.0)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    p1, = plt.plot(s, np.array(map(lambda p: p.tau, tws)) * 1.e4)
    ax.set_xlabel('[m]')
    ax.set_ylabel('[cm]')
    plt.show()

