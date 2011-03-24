#!/usr/bin/env python

import gui
from PyQt4 import QtCore, QtGui
import sys

class Zenmap(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = gui.Ui_MainWindow()
        self.ui.setupUi(self)
        
    def changeCommand(self):
	print "changeCommand()"
	
    def startScan(self):
	print "Start Scan"

    def stopScan(self):
	print "Stop Scan"

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Zenmap()
    myapp.show()
    sys.exit(app.exec_())