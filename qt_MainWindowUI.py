# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_MainWindowUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(855, 625)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.radioButton_1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_1.setGeometry(QtCore.QRect(90, 30, 86, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_1.setFont(font)
        self.radioButton_1.setChecked(True)
        self.radioButton_1.setObjectName("radioButton_1")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(240, 30, 86, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(370, 30, 86, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(530, 30, 86, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_5.setGeometry(QtCore.QRect(90, 90, 86, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_6.setGeometry(QtCore.QRect(240, 90, 86, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_6.setFont(font)
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_7.setGeometry(QtCore.QRect(370, 90, 86, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_7.setFont(font)
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_8 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_8.setGeometry(QtCore.QRect(530, 90, 86, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_8.setFont(font)
        self.radioButton_8.setObjectName("radioButton_8")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 130, 140, 40))
        self.pushButton.setObjectName("pushButton")
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(230, 180, 140, 40))
        self.clearButton.setObjectName("clearButton")
        self.labelResponce = QtWidgets.QLabel(self.centralwidget)
        self.labelResponce.setGeometry(QtCore.QRect(100, 249, 400, 160))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelResponce.setFont(font)
        self.labelResponce.setFrameShape(QtWidgets.QFrame.Box)
        self.labelResponce.setText("")
        self.labelResponce.setAlignment(QtCore.Qt.AlignCenter)
        self.labelResponce.setObjectName("labelResponce")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 855, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuClose = QtWidgets.QAction(MainWindow)
        self.menuClose.setObjectName("menuClose")
        self.menu.addAction(self.menuClose)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.radioButton_1.toggled['bool'].connect(MainWindow.r_buttonSlot1)
        self.radioButton_2.toggled['bool'].connect(MainWindow.r_buttonSlot2)
        self.radioButton_3.toggled['bool'].connect(MainWindow.r_buttonSlot3)
        self.radioButton_4.toggled['bool'].connect(MainWindow.r_buttonSlot4)
        self.radioButton_5.toggled['bool'].connect(MainWindow.r_buttonSlot5)
        self.radioButton_6.toggled['bool'].connect(MainWindow.r_buttonSlot6)
        self.radioButton_7.toggled['bool'].connect(MainWindow.r_buttonSlot7)
        self.radioButton_8.toggled['bool'].connect(MainWindow.r_buttonSlot8)
        self.pushButton.pressed.connect(MainWindow.pushButtonSlot)
        self.clearButton.pressed.connect(MainWindow.clearButtonSlot)
        self.menuClose.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton_1.setText(_translate("MainWindow", "RadioButton"))
        self.radioButton_2.setText(_translate("MainWindow", "RadioButton"))
        self.radioButton_3.setText(_translate("MainWindow", "RadioButton"))
        self.radioButton_4.setText(_translate("MainWindow", "RadioButton"))
        self.radioButton_5.setText(_translate("MainWindow", "RadioButton"))
        self.radioButton_6.setText(_translate("MainWindow", "RadioButton"))
        self.radioButton_7.setText(_translate("MainWindow", "RadioButton"))
        self.radioButton_8.setText(_translate("MainWindow", "RadioButton"))
        self.pushButton.setText(_translate("MainWindow", "天気予報を取得"))
        self.clearButton.setText(_translate("MainWindow", "表示をクリア"))
        self.menu.setTitle(_translate("MainWindow", "ファイル"))
        self.menuClose.setText(_translate("MainWindow", "Close"))

