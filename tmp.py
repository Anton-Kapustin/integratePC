import sys, time
from PyQt5 import QtCore
import re
import subprocess
import os


# cmd = "pactl list short sinks"
# proc = subprocess.Popen(cmd, stdout = subprocess.PIPE, shell=True)
# output = proc.stdout.read().decode('utf-8')
# print(output)
# arr = output.split('\n')
# print(arr)
# for i in arr:
# 	str = re.findall(r'\d+\t', i)
# 	print(str)

# path = "/sys/class/drm/"
# dirs = os.listdir(path)
# for directory in dirs:
# 	if "HDMI" in directory:
# 		path_hdmi = path + directory + "/"
# path_hdmi += "enabled"
# f = open(path_hdmi)
# hdmiState = f.read()
# return hdmiState

	# def avancedSoundControl(self):
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
print(arr)
volumes = {}
snd = ''
# if self.getHdmiState():
# 	print(arr)
# 	for i in arr:
# 		snd += i + " " + arr[i] + "\n"
# 	print(snd)
# 	return snd
# else:
# 	for i in arr:
# 		if "hdmi" in i:
# 			pass
# 		else:
# 			volumes[i] = arr[i]
# 	for i in volumes:
# 		# str = i + " " + volumes[i] + "\n"
# 		str = volumes[i] + "\n"
# 	print(str)
			# return str

