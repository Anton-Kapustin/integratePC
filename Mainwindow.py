# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(216, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.lable_batteryStatus = QtWidgets.QLabel(self.centralwidget)
        self.lable_batteryStatus.setText('N/A')
        self.lable_batteryStatus.setGeometry(QtCore.QRect(180, 30, 35, 24))
        self.lable_batteryStatus.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignBottom)
        self.lable_batteryStatus.setContentsMargins(0, 0, 0, 1)
        self.lable_batteryStatus.setObjectName("lable_batteryStatus")
        # self.lable_batteryStatus.setText("40%")
        self.icon_battery = QtWidgets.QGraphicsView(self.centralwidget)
        self.icon_battery.setGeometry(QtCore.QRect(155, 30, 24, 24))
        self.icon_battery.setObjectName("icon_battery")

        self.lable_carrier = QtWidgets.QLabel(self.centralwidget)
        self.lable_carrier.setGeometry(QtCore.QRect(5, 30, 85, 24))
        self.lable_carrier.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignBottom)
        self.lable_carrier.setContentsMargins(0, 0, 0, 1)
        self.lable_carrier.setObjectName("lable_carrier")
        self.lable_carrier.setText("No Signal")
        # self.button_connect = QtWidgets.QPushButton(self.centralwidget)
        # self.button_connect.setGeometry(QtCore.QRect(20, 0, 75, 24))
        # self.button_connect.setObjectName("button_connect")
        # self.button_stop = QtWidgets.QPushButton(self.centralwidget)
        # self.button_stop.setGeometry(QtCore.QRect(120, 0, 75, 24))
        # self.button_stop.setObjectName("button_stop")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 270, 171, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.gridLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.pushButton_5, 0, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_2.addWidget(self.pushButton_6, 1, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_2.addWidget(self.pushButton_7, 2, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_10 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout.addWidget(self.pushButton_10)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_3.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_3.addWidget(self.pushButton_9)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_3.addWidget(self.pushButton_4)
        self.horizontalLayout.addLayout(self.verticalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 216, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")


        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # self.lable_batteryStatus.setText(_translate("MainWindow", "Bat"))
        # self.button_connect.setText(_translate("MainWindow", "Start"))
        # self.button_stop.setText(_translate("MainWindow", "Stop"))
        self.pushButton_5.setText(_translate("MainWindow", "1"))
        self.pushButton_6.setText(_translate("MainWindow", "4"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_3.setText(_translate("MainWindow", "5"))
        self.pushButton.setText(_translate("MainWindow", "8"))
        self.pushButton_10.setText(_translate("MainWindow", "0"))
        self.pushButton_8.setText(_translate("MainWindow", "3"))
        self.pushButton_9.setText(_translate("MainWindow", "6"))
        self.pushButton_4.setText(_translate("MainWindow", "8"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))

