import sys
from datetime import datetime

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class SystemTrayIcon(QSystemTrayIcon):

    def __init__(self, icon, parent):
        time = datetime.now()
        currentTime = str(time.hour) + ":" + str(time.minute) + "_"
        self.LOG_TAG = currentTime + self.__class__.__name__ + ": "
        super(SystemTrayIcon, self).__init__(icon, parent)
        self.lable = "Батарея: "
        self.charge = "ϟ"
        menu = QMenu(parent)
        exitAction = menu.addAction("Exit")
        exitAction.triggered.connect(parent.close)
        self.setContextMenu(menu)
        self.menu1 = QMenu()
        self.menu1.setStyleSheet("padding: 10px")
        self.menu_battery = QLabel('Батарея: ___%')
        self.menu_battery.setStyleSheet("font-family: 'Roboto', sans-serif; font-size: 12px; padding: 0;")
        self.menu_battery_action = QWidgetAction(self.menu_battery)
        self.menu_battery_action.setDefaultWidget(self.menu_battery)
        self.menu1.addAction(self.menu_battery_action)

        self.menu_carrier = QLabel('Оператор')
        self.menu_carrier.setStyleSheet("font-family: 'Roboto', sans-serif; font-size: 12px; padding: 0;")
        self.menu_carrier_action = QWidgetAction(self.menu_carrier)
        self.menu_carrier_action.setDefaultWidget(self.menu_carrier)
        self.menu1.addAction(self.menu_carrier_action)
        self.activated.connect(self.iconActivated)

    def about_fun(self):
        QtGui.QMessageBox.about(self.parent(), "about", "pyqt system tray")

    def quit(self):
        sys.exit(0)

    def iconActivated(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            print(self.LOG_TAG + "Tray activated")
            self.menu1.exec(self.geometry().center())

    def updateCarrierLable(self, lable):
        print(self.LOG_TAG + "lable carrier: " + lable)
        self.menu_carrier.setText(lable)

    def updateBatteryCharge(self, level, charge):
        if "charge" in charge:
            lable = self.lable + self.charge + str(level) + "%"
        else:
            lable = self.lable + str(level) + "%"
        print(self.LOG_TAG + "battery: " + lable)
        self.menu_battery.setText(lable)
