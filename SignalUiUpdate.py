import re
from datetime import datetime
from PyQt5 import QtCore

class SignalUiUpdate(QtCore.QObject):
    signBattery = QtCore.pyqtSignal(str)
    signBatteryIcon = QtCore.pyqtSignal(int, str)
    signCarrier = QtCore.pyqtSignal(str)
    signNotify = QtCore.pyqtSignal(str)

    time = datetime.now()
    currentTime = str(time.hour) + ":" + str(time.minute) + "_"
    LOG_TAG = currentTime + __name__ + ": "

    def setPhoneBatteryState(self, battery): 
        command = re.findall(r'\d+', battery)
        lable = (str(command[0]) + "%").strip()
        print(self.LOG_TAG + "battery phone: " + lable)
        self.signBattery.emit(lable)
        if "charging" in battery:
            self.signBatteryIcon.emit(int(command[0]), "charge")
            print(self.LOG_TAG + "send charge")
        else:
            self.signBatteryIcon.emit(int(command[0]), "evaluation")
            print(self.LOG_TAG + "send evaluation")

    def setPhoneNetworkState(self, network):
        array = network.split(" ")
        print(self.LOG_TAG + str(array))
        for name in array:
            if "network" in name:
                pass
            else:
                carrier = name.strip()
        self.signCarrier.emit(carrier)

    def setPhoneNotification(self, notify):
        self.signNotify.emit(notify)

            