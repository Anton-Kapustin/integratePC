import subprocess, re
from datetime import datetime

class NetworkStatus:
    def __init__(self):
        time = datetime.now()
        currentTime = str(time.hour) + ":" + str(time.minute) + "_"
        self.LOG_TAG = currentTime + self.__class__.__name__

    def getNetworkStatus(self):
        cmd = "nmcli dev status"
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        output = proc.stdout.read().decode('utf-8')
        list = output.split('\n')
        for item in list:
            if ("подкл" in item) or ("conn" in item):
                status = re.sub(' +', ' ', item)
        return status
