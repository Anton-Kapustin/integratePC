from Client import Client
from NetworkStatus import NetworkStatus
from BatteryStatus import BatteryStatus
from Backlight import Backlight
from Sound import SoundControl
from PyQt5 import QtCore
from Notify import Notify
from Share import Share
import re, subprocess

class Commands:

    def __init__(self):
        self.uiUpdate = UiUpdate()
        self.backlight = Backlight()
        self.LOG_TAG = "Commands: "

    def analyze(self, cmd, ip):

        command = cmd.split("////")
        print(self.LOG_TAG + str(command))
        if command[0] == "info":
            status = BatteryStatus.getStatus(BatteryStatus)
            status["PC_info"] = ""
            status['network'] = NetworkStatus.getNetworkStatus(NetworkStatus)
            status['backlight'] = self.backlight.getBacklight()
            status['phone'] = 'get'
            sound = SoundControl()
            status['sound'] = sound.getSoundVol()
            print(self.LOG_TAG + status['battery'])
            print(self.LOG_TAG + status['network'])
            client = Client()
            client.conneсtion(ip)
            print(self.LOG_TAG + "Отправка: ")
            client.sending(status)
            print(self.LOG_TAG + "Отправлено: ")
            client.closing()
        elif "backlight" == command[0]:
            backl = re.findall(r'\d+', command[1])
            print(self.LOG_TAG + backl[0])
            backlight = backl[0]
            self.backlight.setBacklight(backlight)
        elif "sound" == command[0]:
            sound = SoundControl()
            snd = re.findall(r'\d+', command[1])
            print(snd[0])
            sound.setSoundVol(snd[0])

        elif "phone_info" == command[0]:
            command = command[1].split("&")
            print(self.LOG_TAG + cmd)
            for i in command:
                if "battery" in i:
                    self.uiUpdate.sendSignal(i)
                elif "network" in i:
                    self.uiUpdate.sendSignal(i)
        elif "notify" == command[0]:
            notify = Notify()
            notify.notifySend(command[1])

        elif "share" in command[0]:
            share = Share()
            string = command[0].split("_")
            print(self.LOG_TAG + string[1])
            if ("link" == string[1]):
                share.shareLink(command[1])
            elif ("text" in string[1]):
                share.shareText(command[1])


            

    def getClass(self):
        return self.uiUpdate

class UiUpdate(QtCore.QObject):
    signBattery = QtCore.pyqtSignal(str)
    signBatteryIcon = QtCore.pyqtSignal(int, str)
    signCarrier = QtCore.pyqtSignal(str)

    def sendSignal(self, cmd):
        self.LOG_TAG = "UiUpdate: "
        if "battery" in cmd:
            command = re.findall(r'\d+', cmd)
            lable = (str(command[0]) + "%").strip()
            print(self.LOG_TAG + lable)
            self.signBattery.emit(lable)
            if "charging" in cmd:
                self.signBatteryIcon.emit(int(command[0]), "charge")
                print(self.LOG_TAG + "send charge")
            else:
                self.signBatteryIcon.emit(int(command[0]), "evaluation")
                print(self.LOG_TAG + "send evaluation")
        elif "network" in cmd:
            array = cmd.split(" ")
            print(self.LOG_TAG + str(array))
            for name in array:
                if "network" in name:
                    pass
                else:
                    carrier = name.strip()
            self.signCarrier.emit(carrier)