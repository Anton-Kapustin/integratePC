import subprocess
from datetime import datetime

class Share:

    def __init__(self):
        time = datetime.now()
        currentTime = str(time.hour) + ":" + str(time.minute) + "_"
        self.LOG_TAG = currentTime + self.__class__.__name__ + ": "

    def shareLink(self, link):
        cmd = "xdg-open " + link
        self.openApp(cmd)

    def shareText(self, text):
        # homeVar = self.openApp("echo $HOME")
        # cmd = homeVar + "/integrate.tmp"
        cmd = "/tmp/integrate.tmp"
        file = open(cmd, 'w+')
        file.write(text)
        file.close()
        # cmd = "xdg-open " + homeVar + "/integrate.tmp &"
        cmd = "xdg-open " + cmd + " &"
        print(self.LOG_TAG + str(self.openApp(cmd)))

    def openApp(self, cmd):

        print(self.LOG_TAG + "Команда: " + cmd)
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        output = proc.stdout.read().decode('utf-8').rstrip()
        print(self.LOG_TAG + "Output: " + output)
        return output