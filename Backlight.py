import subprocess

class Backlight:

	def __init__(self):
		self.LOG_TAG = "Backlight: "

	def getBacklight(self):

		cmd = "xbacklight"
		proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
		output = proc.stdout.read().decode('utf-8')
		print(self.LOG_TAG + output)
		return output

	def setBacklight(self, val):
		cmd = "xbacklight -set " + val
		print(self.LOG_TAG + cmd)
		roc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)


# if __name__ == "__main__":
# 	backlight = Backlight()
# 	backlight.getBacklight()
