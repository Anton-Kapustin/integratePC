import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QThread
from mainwindow import Ui_MainWindow
from Commands import Commands
from Srv import SRV
from multiprocessing import Process
from ImageUrl import ImageUrl
import time


class Window(QMainWindow, Ui_MainWindow):

	def __init__(self):
		self.LOG_TAG = "Window: "
		super(Window, self).__init__()
		self.setupUi(self)
		self.lable_batteryStatus
		# self.setGeometry(50, 50, 500, 300)
		self.setWindowTitle("Integrate")
		self.setWindowIcon(QIcon('1.png'))
		self.UI_tools()
		self.show()

	def UI_tools(self):
		self.qThread = MyProcess(self)
		exitAction = QAction('Exit', self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip('Exit application')
		exitAction.triggered.connect(self.close)
		connectAction = QAction('Start', self)
		connectAction.triggered.connect(self.startSrv)
		stopAction = QAction('Stop', self)
		stopAction.triggered.connect(self.stopSrv)

		self.icon_battery.setStyleSheet("background: url('res/ic_battery_full_black_24dp.png') no-repeat center; border: none")
		self.statusBar()
		menu = self.menuBar()
		fileMenu = menu.addMenu('&File')
		# fileMenu.addAction(exitAction)
		# fileMenu.addAction(connectAction)
		# fileMenu.addAction(stopAction)


		toolbar = self.addToolBar('Start')
		toolbar.addAction(connectAction)
		toolbar = self.addToolBar('Stop')
		toolbar.addAction(stopAction)
		toolbar = self.addToolBar('Exit')
		toolbar.addAction(exitAction)

		# self.button_connect.clicked.connect(self.startSrv)
		# self.button_stop.clicked.connect(self.stopSrv)

	def setUiUpdate(self):
		self.uiUpdate.signBattery.connect(self.lable_batteryStatus.setText)
		self.uiUpdate.signBatteryIcon.connect(self.setBatteryIcon)
		self.uiUpdate.signCarrier.connect(self.setCarrierName)

	def setCarrierName(self, carrier):
		print(self.LOG_TAG + "carrier name: " + carrier)
		self.lable_carrier.setText(carrier)


	def setBatteryIcon(self, level, charge):
		imageUrl = ImageUrl()
		print(level)
		url = imageUrl.getImageUrl(level, charge)
		self.icon_battery.setStyleSheet(url)

	def updateBatteryIcon(self, charge):
		self.icon_battery.setStyleSheet("background: url('res/ic_battery_charging_full_black_24dp.png') no-repeat center; border: none")

	def startSrv(self):
		self.uiUpdate = self.qThread.getClass()
		self.qThread.start()
		self.setUiUpdate()

	def stopSrv(self):
		self.qThread.srvStop()
		self.qThread.terminate()
		while self.qThread.isRunning():
			if self.qThread.isRunning():
				print(self.LOG_TAG + "Остановлено")
				break    

	def closeEvent(self, event):
		self.stopSrv()
		event.accept()

class MyProcess(QThread):
	
	def __init__(self, parent = None):
		self.LOG_TAG = "MyProcess: "
		QThread.__init__(self, parent)
		self.commands = Commands()
		self.uiUpdate = self.commands.getClass()
		self.srv = SRV(self.commands)		

	def run(self):
		print(self.LOG_TAG + "SRV Создан")
		self.connection = True
		while self.connection:
			print(self.LOG_TAG + "Start")
			self.srv.start()
			print(self.LOG_TAG + "Stop")
		print(self.LOG_TAG + "SRV остановлен")

	def getClass(self):
		return self.uiUpdate

	def srvStop(self):
		self.connection = False
		print(self.LOG_TAG + "STOP")

if __name__ == "__main__":
	app = QApplication(sys.argv)
	GUI = Window()
	print("!!!!")
	GUI.show()
	try:
		sys.exit(app.exec_())
		sys.exit(0)
	except SystemExit as err:
		print(GUI.LOG_TAG + str(err))
	except Exception as err:
		print(GUI.LOG_TAG + str(err))