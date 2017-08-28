import subprocess

class Backlight:
	LOG_TAG = "Backlight: "
	# __init__():
		# path_backlight = "/sys/class/backlight/"
		# dir = os.listdir(path_backlight)
		# for i in dir:
		# 	if "back" in i:
		# 		path_backlight += i + "/"
		# filesInDir = os.listdir(path_backlight)
		# for i in filesInDir:
		# 	if "max" in i:
		# 		path_maxBacklight = path_backlight + i
		# 	elif "actual" in i:
		# 		path_currentBacklight = path_backlight + i

	def getBacklight(self):

		# f = open(path_maxBacklight)
		# maxBacklight = f.read()
		# f = open(path_currentBacklight)
		# currentBacklight = f.read()
		cmd = "xbacklight"
		proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
		output = proc.stdout.read().decode('utf-8')
		print(self.LOG_TAG + output)
		return output

	def setBacklight(self, val):
		cmd = "xbacklight -set " + val
		print(cmd)
		roc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)


# if __name__ == "__main__":
# 	backlight = Backlight()
# 	backlight.getBacklight()
