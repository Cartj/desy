#from __future__ import unicode_literals
import sys
import os
import random
import pickle

from worker import SimInfo

    
from PyQt4 import QtGui, QtCore

from numpy import arange, sin, pi
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

progname = os.path.basename(sys.argv[0])

class MyData:
    def __init__(self):
        self.i = 0


class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        # We want the axes cleared every time plot() is called
        self.axes.hold(False)

        self.compute_initial_figure()

        #
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass


class MyStaticMplCanvas(MyMplCanvas):
    """Simple canvas with a sine plot."""
    def compute_initial_figure(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2*pi*t)
        self.axes.plot(t, s)


class MyDynamicMplCanvas(MyMplCanvas):
    """A canvas that updates itself every second with a new plot."""
    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(100)

    def compute_initial_figure(self):
        self.axes.bar(range(14), range(14), width=0.2, color='b')

    def update_figure(self):
        # Build a list of 4 random integers between 0 and 10 (both inclusive)
        
        #l = [random.randint(0, self.data.i) for i in range(14)]
        
        data = pickle.load(open('dump.dat', 'rb'))
        
        self.axes.bar(data.x, data.y, width=0.2, color='b')
            
        self.axes.set_title('plot title')
        self.draw()


class ApplicationWindow(QtGui.QMainWindow):
    def __init__(self):
        
        self.data = MyData()
        
        QtGui.QMainWindow.__init__(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("application main window")

        self.file_menu = QtGui.QMenu('&File', self)
        self.file_menu.addAction('&Quit', self.fileQuit,
                                 QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        self.menuBar().addMenu(self.file_menu)

        self.help_menu = QtGui.QMenu('&Help', self)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.help_menu)

        self.main_widget = QtGui.QWidget(self)

        l = QtGui.QVBoxLayout(self.main_widget)
        sc = MyStaticMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        dc = MyDynamicMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        dc2 = MyDynamicMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        dc.data = self.data
        dc2.data = self.data
        l.addWidget(sc)
        l.addWidget(dc)
        l.addWidget(dc2)

        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        self.statusBar().showMessage("All hail matplotlib!", 2000)
        
        
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_data)
        timer.start(1000)

        

    def fileQuit(self):
        self.close()

    def closeEvent(self, ce):
        self.fileQuit()


    def update_data(self):
        self.data.i += 1
        print self.data.i
    

qApp = QtGui.QApplication(sys.argv)

aw = ApplicationWindow()
aw.setWindowTitle("%s" % progname)
aw.show()
sys.exit(qApp.exec_())
#qApp.exec_()
