import os
from datetime import datetime

class BatteryStatus:
    def __init__(self):
        time = datetime.now()
        currentTime = str(time.hour) + ":" + str(time.minute) + "_"
        self.LOG_TAG = currentTime + self.__class__.__name__
        self.path_capacity = "/sys/class/power_supply/BAT0/capacity"
        self.path_status = "/sys/class/power_supply/BAT0/status"
        self.path_source = "/sys/class/power_supply/ADP0/online"
        path_bat = "/sys/class/power_supply/"
        self.bat = os.listdir(path_bat)

    def getStatus(self):
        info = {'battery': u''}
        if "BAT0" in self.bat:
            file = open(self.path_source)
            for line in file :
                if "1" in line:
                    info['battery'] = u'Подключено к ЗУ\n'
                else :
                    info['battery'] = u'ЗУ не подключено\n'
            file = open(self.path_status)
            for line in file :
                info['battery'] = info['battery'] + u'Статус: ' + line
            file = open(self.path_capacity)
            for line in file :
                info['battery'] = info['battery'] + u'Заряд: ' + line
        print(info)
        return info