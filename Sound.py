
import subprocess, os, re
from datetime import datetime

class SoundControl:

    def __init__(self):
        time = datetime.now()
        currentTime = str(time.hour) + ":" + str(time.minute) + "_"
        self.LOG_TAG = currentTime + self.__class__.__name__ + ": "

    def getSoundVol(self):
        arr = self.getSoundOutputs()
        volumes = {}
        snd = ''
        if self.getHdmiState():
            print(arr)
            for i in arr:
                if "hdmi" in i:
                    snd = i
            print(snd)
            return snd
        else:
            for i in arr:
                if "hdmi" in i:
                    pass
                else:
                    volumes[i] = arr[i]
            for i in volumes:
                str = volumes[i] + "\n"
            return str

    def setSoundVol(self, vol):
        size = len(self.getSoundOutputs())      
        for i in range(size):
            count = str(i)
            cmd = "pactl set-sink-volume " + count + " " + str(vol) + "%"
            print(cmd)
        proc = subprocess.Popen(cmd, stdout = subprocess.PIPE, shell=True)
        output = proc.stdout.read().decode('utf-8')
        print(self.LOG_TAG + output)

    def getHdmiState(self):
        path = "/sys/class/drm/"
        dirs = os.listdir(path)
        for directory in dirs:
            if "HDMI" in directory:
                path_hdmi = path + directory + "/"
        path_hdmi += "enabled"
        f = open(path_hdmi)
        hdmiState = f.read()
        if "disable" in hdmiState:
            print(self.LOG_TAG + "f " + hdmiState)
            return False
        else:
            print(self.LOG_TAG + "t " + hdmiState)
            return True

    def getSoundOutputs(self):
        cmd = "pacmd list-sinks"
        proc = subprocess.Popen(cmd, stdout = subprocess.PIPE, shell=True)
        output = proc.stdout.read().decode('utf-8')
        array = output.split('\n')
        arr = {}
        mass = []
        i = 0
        for name in array:
            if "name:" in name:
                str = name.split('.')
                count = len(str)
                mass.append(str[count-1])
                i = i + 1
                i = 0
        for vol in array:
            if "volume:" in vol:
                str = vol.split(',')
                # print(str[0])
                if "base volume:" in str[0]:
                    pass
                else:
                    sound = re.findall(r'\d+%', str[0])
                    # print(sound)
                    arr[mass[i]] = sound[0]
                    i += 1
        return arr

if __name__ == "__main__":
    s = SoundControl()

    s.setSoundVol(30)
    print(s.getSoundOutputs())