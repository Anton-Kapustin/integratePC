import Client
from NetworkStatus import NetworkStatus
from BatteryStatus import BatteryStatus
from backlight import Backlight
from sound import SoundControl
from PyQt5 import QtCore
from notify import Notify
import re, subprocess

LOG_TAG = "Commands: "
class Commands:

    def __init__(self):
        self.uiUpdate = UiUpdate()
        self.backlight = Backlight()

    def analyze(self, cmd):

        if "info" in cmd:
            status = BatteryStatus.getStatus(BatteryStatus)
            status['network'] = NetworkStatus.getNetworkStatus(NetworkStatus)
            # backlight = Backlight()
            status['backlight'] = self.backlight.getBacklight()
            status['phone'] = 'get'
            sound = SoundControl()
            status['sound'] = sound.getSoundVol()
            print(LOG_TAG + status['battery'])
            print(LOG_TAG + status['network'])
            Client.client.conneсtion()
            print(LOG_TAG + "Отправка: ")
            Client.client.sending(status)
            print(LOG_TAG + "Отправлено: ")
            Client.client.closing()
        elif "backlight" in cmd:
            backl = re.findall(r'\d+', cmd)
            print(LOG_TAG + backl[0])
            backlight = backl[0]
            self.backlight.setBacklight(backlight)
        elif "sound" in cmd:
            sound = SoundControl()
            snd = re.findall(r'\d+', cmd)
            print(snd[0])
            sound.setSoundVol(snd[0])

        elif "&" in cmd:
            command = cmd.split("&")
            print(LOG_TAG + cmd)
            for i in command:
                if "battery" in i:
                    self.uiUpdate.sendSignal(i)
                elif "network" in i:
                    self.uiUpdate.sendSignal(i)
        elif "notify" in cmd:
            notify = Notify()
            notify.notifySend(cmd)

    def getClass(self):
        return self.uiUpdate

class UiUpdate(QtCore.QObject):
    signBattery = QtCore.pyqtSignal(str)
    signBatteryIcon = QtCore.pyqtSignal(int, str)
    signCarrier = QtCore.pyqtSignal(str)

    TAG = "UiUpdate: "

    def sendSignal(self, cmd):

        if "battery" in cmd:
            command = re.findall(r'\d+', cmd)
            lable = (str(command[0]) + "%").strip()
            print(self.TAG + lable)
            self.signBattery.emit(lable)
            if "charging" in cmd:
                self.signBatteryIcon.emit(int(command[0]), "charge")
                print("send charge")
            else:
                self.signBatteryIcon.emit(int(command[0]), "evaluation")
                print("send evaluation")
        elif "network" in cmd:
            array = cmd.split(" ")
            print(array)
            for name in array:
                if "network" in name:
                    pass
                else:
                    carrier = name.strip()
            self.signCarrier.emit(carrier)


            
            


    # def __init__(self):
    #     super(UiUpdate, self).__init__()
    #     self.running = False
    #     print(self.TAG + "Класс Создан")

    # def run(self):
    #     print(self.TAG + "Run")
    #     self.running = True
    #     i = 0
    #     print(self.TAG + "Отправка сигнала")
    #     self.sign.emit(i)
    #     print(self.TAG + "Отправлено")

            # time.sleep(str)

    