import subprocess

class Notify:
	def __init__(self):
		self.LOG_TAG = "Notify: "

	def notifySend(self, notify):
		print(self.LOG_TAG + notify)
		command = notify.split("/")
		name = ''
		title = ''
		text = ''

		for string in command:
			if "name" in string:
				name = string.replace("name: ", "\"")
				name += "\""
			elif "title" in string:
				title = string.replace("title: ", "\"")
		        # title += "\""
			elif "text" in string:
				text = string.replace("text: ", "")
				text = string
				text += "\""

		cmd = "notify-send " + name + title + " " + text + " -i Integrate"
		print(self.LOG_TAG + "notification command: " + cmd)
		proc = subprocess.Popen(cmd, stdout = subprocess.PIPE, shell=True)
		output = proc.stdout.read().decode('utf-8')
		print(self.LOG_TAG + output)

if __name__ == "__main__":
	notify = Notify()
	notify.notifySend("notify, name: kate, title: Отладка по USB разрешена, text: Нажмите, чтобы отключить отладку по USB.")