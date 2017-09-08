import subprocess

class Share:

	def __intit__(self):
		self.LOG_TAG = "Share: "

	def shareLink(self, link):
		lnk = link.replace("share ", "")
		cmd = "xdg-open " + lnk
		proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
		output = proc.stdout.read().decode('utf-8')