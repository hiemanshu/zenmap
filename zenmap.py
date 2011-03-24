#!/usr/bin/env python

import gui
from PyQt4 import QtCore, QtGui
import sys, os, time
import subprocess

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Zenmap(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = gui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.timer = QtCore.QTimer()
        QtCore.QObject.connect(self.timer, QtCore.SIGNAL('timeout()'), self.update)
        
    def changeCommand(self):
	print "changeCommand()"
	
    def startScan(self):
	self.ui.textBrowser.clear()
	self.process = subprocess.Popen(['nmap', '-T4', '-A', '-v', '192.168.1.*'], shell = False, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	self.timer.start(5)
	
    def update(self):
	if self.process.stdout.readline() == '' and self.process.poll() != None:
	    self.timer.stop()
	else:
	    self.ui.textBrowser.insertPlainText(self.process.stdout.readline())
	self.process.stdout.flush()
	

    def stopScan(self):
	print "Stop Scan"

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Zenmap()
    myapp.show()
    sys.exit(app.exec_())