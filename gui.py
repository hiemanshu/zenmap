# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zenmap.ui'
#
# Created: Thu Mar 24 12:40:36 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(644, 567)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 621, 501))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.comboBox = QtGui.QComboBox(self.layoutWidget)
        self.comboBox.setMinimumSize(QtCore.QSize(200, 0))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.horizontalLayout.addWidget(self.comboBox)
        self.pushButton = QtGui.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.lineEdit_2 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(0, 40))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.textBrowser = QtGui.QTextBrowser(self.layoutWidget)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout.addWidget(self.textBrowser)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 1, -1, -1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushButton_2 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_3.setMaximumSize(QtCore.QSize(300, 16777215))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 644, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuScan = QtGui.QMenu(self.menubar)
        self.menuScan.setObjectName(_fromUtf8("menuScan"))
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        self.menuOptions = QtGui.QMenu(self.menubar)
        self.menuOptions.setObjectName(_fromUtf8("menuOptions"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Windows = QtGui.QAction(MainWindow)
        self.actionNew_Windows.setObjectName(_fromUtf8("actionNew_Windows"))
        self.actionOpen_Scan_in_New_Window = QtGui.QAction(MainWindow)
        self.actionOpen_Scan_in_New_Window.setObjectName(_fromUtf8("actionOpen_Scan_in_New_Window"))
        self.actionSave_scan = QtGui.QAction(MainWindow)
        self.actionSave_scan.setObjectName(_fromUtf8("actionSave_scan"))
        self.actionSave_all_scans = QtGui.QAction(MainWindow)
        self.actionSave_all_scans.setObjectName(_fromUtf8("actionSave_all_scans"))
        self.actionPrint = QtGui.QAction(MainWindow)
        self.actionPrint.setObjectName(_fromUtf8("actionPrint"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionSave_and_Quit = QtGui.QAction(MainWindow)
        self.actionSave_and_Quit.setObjectName(_fromUtf8("actionSave_and_Quit"))
        self.actionCompare_Scans = QtGui.QAction(MainWindow)
        self.actionCompare_Scans.setObjectName(_fromUtf8("actionCompare_Scans"))
        self.actionFind_in_Scans = QtGui.QAction(MainWindow)
        self.actionFind_in_Scans.setObjectName(_fromUtf8("actionFind_in_Scans"))
        self.actionFilter_Hosts = QtGui.QAction(MainWindow)
        self.actionFilter_Hosts.setObjectName(_fromUtf8("actionFilter_Hosts"))
        self.actionEdit_Profile_Settings = QtGui.QAction(MainWindow)
        self.actionEdit_Profile_Settings.setObjectName(_fromUtf8("actionEdit_Profile_Settings"))
        self.actionPreferences = QtGui.QAction(MainWindow)
        self.actionPreferences.setObjectName(_fromUtf8("actionPreferences"))
        self.actionPreferences_2 = QtGui.QAction(MainWindow)
        self.actionPreferences_2.setObjectName(_fromUtf8("actionPreferences_2"))
        self.actionDocumentation = QtGui.QAction(MainWindow)
        self.actionDocumentation.setObjectName(_fromUtf8("actionDocumentation"))
        self.actionAbout_nmap = QtGui.QAction(MainWindow)
        self.actionAbout_nmap.setObjectName(_fromUtf8("actionAbout_nmap"))
        self.actionAbout_zenmap = QtGui.QAction(MainWindow)
        self.actionAbout_zenmap.setObjectName(_fromUtf8("actionAbout_zenmap"))
        self.menuScan.addAction(self.actionNew_Windows)
        self.menuScan.addAction(self.actionOpen_Scan_in_New_Window)
        self.menuScan.addSeparator()
        self.menuScan.addAction(self.actionSave_scan)
        self.menuScan.addAction(self.actionSave_all_scans)
        self.menuScan.addSeparator()
        self.menuScan.addAction(self.actionPrint)
        self.menuScan.addSeparator()
        self.menuScan.addAction(self.actionQuit)
        self.menuScan.addAction(self.actionSave_and_Quit)
        self.menuTools.addAction(self.actionCompare_Scans)
        self.menuTools.addAction(self.actionFind_in_Scans)
        self.menuTools.addAction(self.actionFilter_Hosts)
        self.menuOptions.addAction(self.actionEdit_Profile_Settings)
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionPreferences_2)
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuHelp.addAction(self.actionAbout_nmap)
        self.menuHelp.addAction(self.actionAbout_zenmap)
        self.menubar.addAction(self.menuScan.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.comboBox, QtCore.SIGNAL(_fromUtf8("activated(QString)")), MainWindow.changeCommand)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.startScan)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.stopScan)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Zenmap", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Target : ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Profile : ", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Start Scan", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Command : ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Scanning Console", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "Stop Scan", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "Open current scan in new window", None, QtGui.QApplication.UnicodeUTF8))
        self.menuScan.setTitle(QtGui.QApplication.translate("MainWindow", "Scan", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTools.setTitle(QtGui.QApplication.translate("MainWindow", "Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.menuOptions.setTitle(QtGui.QApplication.translate("MainWindow", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Windows.setText(QtGui.QApplication.translate("MainWindow", "New Window", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_Scan_in_New_Window.setText(QtGui.QApplication.translate("MainWindow", "Open Scan in New Window", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_scan.setText(QtGui.QApplication.translate("MainWindow", "Save scan", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_all_scans.setText(QtGui.QApplication.translate("MainWindow", "Save all scans", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrint.setText(QtGui.QApplication.translate("MainWindow", "Print", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_and_Quit.setText(QtGui.QApplication.translate("MainWindow", "Save and Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCompare_Scans.setText(QtGui.QApplication.translate("MainWindow", "Compare Scans", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFind_in_Scans.setText(QtGui.QApplication.translate("MainWindow", "Find in Scans", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFilter_Hosts.setText(QtGui.QApplication.translate("MainWindow", "Filter Hosts", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEdit_Profile_Settings.setText(QtGui.QApplication.translate("MainWindow", "Edit Profile Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setText(QtGui.QApplication.translate("MainWindow", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences_2.setText(QtGui.QApplication.translate("MainWindow", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDocumentation.setText(QtGui.QApplication.translate("MainWindow", "Documentation", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_nmap.setText(QtGui.QApplication.translate("MainWindow", "About nmap", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_zenmap.setText(QtGui.QApplication.translate("MainWindow", "About zenmap", None, QtGui.QApplication.UnicodeUTF8))

