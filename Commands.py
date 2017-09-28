from Client import Client
from datetime import datetime
from NetworkStatus import NetworkStatus
from BatteryStatus import BatteryStatus
from Backlight import Backlight
from Sound import SoundControl
from PyQt5 import QtCore
from Notification import Notification
from Share import Share
from SignalUiUpdate import SignalUiUpdate
import re, subprocess

class Commands:

    def __init__(self, notify):
        time = datetime.now()
        currentTime = str(time.hour) + ":" + str(time.minute) + "_"
        self.LOG_TAG = currentTime + self.__class__.__name__ +": "
        self.signalUiUpdate = SignalUiUpdate()
        self.backlight = Backlight()
        self.stateBatteryPC = BatteryStatus()
        self.stateNetworkPC = NetworkStatus()
        self.sound = SoundControl()
        self.share = Share()
        self.notify = notify

    def analyze(self, cmd, ip):

        command = cmd.split("////")
        print(self.LOG_TAG + str(command))
        
        if command[0] == "info":
            status = self.stateBatteryPC.getStatus()
            status["PC_info"] = ""
            status['network'] = self.stateNetworkPC.getNetworkStatus()
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
            snd = re.findall(r'\d+', command[1])
            print(self.LOG_TAG + "Изменить громкость: " + snd[0])
            self.sound.setSoundVol(snd[0])

        elif "phone_info" == command[0]:
            command = command[1].split("&")
            print(self.LOG_TAG + cmd)
            for i in command:
                if "battery" in i:
                    self.signalUiUpdate.setPhoneBatteryState(i)
                elif "network" in i:
                    self.signalUiUpdate.setPhoneNetworkState(i)

        elif "notify" == command[0]:
            print(self.LOG_TAG + "notification: " + command[1])
            self.signalUiUpdate.setPhoneNotification(command[1])

        elif "share" in command[0]:
            string = command[0].split("_")
            print(self.LOG_TAG + string[1])

            if ("link" == string[1]):
                self.share.shareLink(command[1])

            elif ("text" in string[1]):
                self.share.shareText(command[1])          

    def getClass(self):
        return self.signalUiUpdate

