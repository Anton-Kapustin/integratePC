import subprocess
import re
LOG_TAG = "NetworkStatus: "
class NetworkStatus:

    def getNetworkStatus(self):
        cmd = "nmcli dev status"
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        output = proc.stdout.read().decode('utf-8')
        list = output.split('\n')
        for item in list:
            if ("подкл" in item) or ("conn" in item):
                status = re.sub(' +', ' ', item)
        return status
