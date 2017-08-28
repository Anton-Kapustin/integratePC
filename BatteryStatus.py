import os

LOG_TAG = "BatteryStatus: "
class BatteryStatus:
    path_capacity = "/sys/class/power_supply/BAT0/capacity"
    path_status = "/sys/class/power_supply/BAT0/status"
    path_source = "/sys/class/power_supply/ADP0/online"
    path_bat = "/sys/class/power_supply/"
    bat = os.listdir(path_bat)

    def getStatus(self):
        info = {'battery': u''}
        if "BAT0" in BatteryStatus.bat:
            file = open(BatteryStatus.path_source)
            for line in file :
                if "1" in line:
                    info['battery'] = u'Подключено к ЗУ\n'
                else :
                    info['battery'] = u'ЗУ не подключено\n'
            file = open(BatteryStatus.path_status)
            for line in file :
                info['battery'] = info['battery'] + u'Статус: ' + line
            file = open(BatteryStatus.path_capacity)
            for line in file :
                info['battery'] = info['battery'] + u'Заряд: ' + line
        print(info)
        return info