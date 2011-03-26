#!/usr/bin/env python

import gui
from PyQt4 import QtCore, QtGui
import sys, os, time
import subprocess
import string

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Zenmap(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = gui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_2.setEnabled(False)
        self.timer = QtCore.QTimer()
        QtCore.QObject.connect(self.timer, QtCore.SIGNAL('timeout()'), self.update)
        self.ui.lineEdit.setText('192.168.1.*')
        self.ui.lineEdit_2.setText('nmap -T4 -A -v 192.168.1.*')
        
    def changeCommand(self):
	print ("changeCommand()")
	
    def startScan(self):
	self.ui.textBrowser.clear()
	cmd = string.split(str(self.ui.lineEdit_2.text()), sep=' ')
	print cmd
	self.process = subprocess.Popen(cmd, shell = False, bufsize=1, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	self.ui.pushButton_2.setEnabled(True)
	self.ui.pushButton.setEnabled(False)
	self.timer.start(1)
	
    def update(self):
	if self.process.stdout.readline() == '' and self.process.poll() != None:
	    self.timer.stop()
	    self.process.stdout.flush()
	    self.ui.pushButton.setEnabled(True)
	    self.ui.pushButton_2.setEnabled(False)
	else:
	    self.ui.textBrowser.insertPlainText(self.process.stdout.readline())
	
    def stopScan(self):
	self.process.terminate()
	while True:
	    if self.process.poll() != None :
		self.ui.textBrowser.insertPlainText("\nScanning aborted\n")
		break

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Zenmap()
    myapp.show()
    sys.exit(app.exec_())