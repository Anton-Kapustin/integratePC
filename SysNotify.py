import subprocess
# from gi.repository import Notify, GdkPixbuf
from notification import Notification

class SysNotify:
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
				text += "\""

		cmd = "notify-send " + name + title + " " + text + " -i Integrate"
		print(self.LOG_TAG + "notification command: " + cmd)
		proc = subprocess.Popen(cmd, stdout = subprocess.PIPE, shell=True)
		output = proc.stdout.read().decode('utf-8')
		print(self.LOG_TAG + output)

	# def acceptNotify(self):
	# 	Notify.init("App Name")
	# 	notify = Notify.Notification.new("Hi")
	# 	image = GdkPixbuf.Pixbuf.new_from_file("1.png")
	# 	notify.set_icon_from_pixbuf(image)
	# 	notify.set_image_from_pixbuf(image)
	# 	notify.add_action("action_click", "Принять", "accept.png")
	# 	notify.add_action("action_click", "Отбой", self.accept)
	# 	notify.show()
		

	def accept(self):
		pass

	def notificationSend(self, msg):
		notify = Notification(msg)

if __name__ == "__main__":
	notify = SysNotify()
	# notify.notifySend("notify, name: kate, title: Отладка по USB разрешена, text: Нажмите, чтобы отключить отладку по USB.")
	# notify.acceptNotify()
	notify.notificationSend("msg")