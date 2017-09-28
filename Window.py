import sys, time, threading
from datetime import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QThread, QRect
from Mainwindow import Ui_MainWindow
from Commands import Commands
from Srv import SRV
from multiprocessing import Process
from ImageUrl import ImageUrl
from Notification import Notification
from PyQt5 import QtCore
from Tray import SystemTrayIcon

#============================================================================================
class Window(QMainWindow, Ui_MainWindow):

    def __init__(self):
        time = datetime.now()
        currentTime = str(time.hour) + ":" + str(time.minute) + "_"
        self.LOG_TAG = currentTime + self.__class__.__name__ + ": "
        super(Window, self).__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setupUi(self)
        self.lable_batteryStatus
        self.setWindowTitle("Integrate")
        self.setWindowIcon(QIcon('1.png'))
        self.UI_tools()

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        # painter.drawPixmap(self.rect(), QPixmap("phone.png"))
        pixmap = QPixmap("phone1.png")
        painter.drawPixmap(QRect(0, 10, 200, 400), pixmap)


    def UI_tools(self):
        self.qThread = MyProcess(self)
        self.notify = Notification()

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

        # menu = self.menuBar() #Верхнее меню
        # fileMenu = menu.addMenu('&File')
        # fileMenu.addAction(exitAction)
        # fileMenu.addAction(connectAction)
        # fileMenu.addAction(stopAction)

        toolbar = self.addToolBar('Start') # Панель инструментов
        toolbar.addAction(connectAction)
        toolbar = self.addToolBar('Stop')
        toolbar.addAction(stopAction)
        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)

        self.tray = SystemTrayIcon(QIcon("1.png"), self)
        self.tray.show()

    def startSrv(self):
        self.signalUiUpdate = self.qThread.initServices(self.notify)
        self.qThread.start()
        self.setUiUpdate()

    def setUiUpdate(self):
        self.signalUiUpdate.signBattery.connect(self.lable_batteryStatus.setText)
        self.signalUiUpdate.signBatteryIcon.connect(self.setBatteryIcon)
        self.signalUiUpdate.signCarrier.connect(self.setCarrierName)
        self.signalUiUpdate.signBatteryIcon.connect(self.tray.updateBatteryCharge)
        self.signalUiUpdate.signCarrier.connect(self.tray.updateCarrierLable)
        self.signalUiUpdate.signNotify.connect(self.notificationSignals)

    def notificationSignals(self, notify):
        self.notify.setNotify(notify)

    def setCarrierName(self, carrier):
        print(self.LOG_TAG + "carrier name: " + carrier)
        self.lable_carrier.setText(carrier)

    def setBatteryIcon(self, level, charge):
        imageUrl = ImageUrl()
        print(self.LOG_TAG + "Заряд батареи телефона: " + str(level))
        url = imageUrl.getImageUrl(level, charge)
        self.icon_battery.setStyleSheet(url)

    def updateBatteryIcon(self, charge):
        self.icon_battery.setStyleSheet("background: url('res/ic_battery_charging_full_black_24dp.png') no-repeat center; border: none")

    def stopSrv(self):
        self.qThread.srvStop()
        self.qThread.terminate()
        while self.qThread.isRunning():
            if not self.qThread.isRunning():
                print(self.LOG_TAG + "Остановлено")
                break    

    def closeEvent(self, event):
        self.stopSrv()
        event.accept()

#============================================================================================

class StackedWidget(QStackedWidget):
    def __init__(self, parent=None):
        QStackedWidget.__init__(self, parent=parent)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), QPixmap("ninja.png"))
        QStackedWidget.paintEvent(self, event)

#============================================================================================

class MyProcess(QThread):
    
    def __init__(self, parent = None):
        time = datetime.now()
        currentTime = str(time.hour) + ":" + str(time.minute) + "_"
        self.LOG_TAG = currentTime + self.__class__.__name__ + ": "
        QThread.__init__(self, parent)

    def initServices(self, notify):
        self.commands = Commands(notify)
        self.signalUiUpdate = self.commands.getClass()
           
        return self.signalUiUpdate

    def run(self):
        self.srv = SRV(self.commands)
        print(self.LOG_TAG + "SRV Создан")
        self.connection = True
        while self.connection:
            print(self.LOG_TAG + "Start")
            self.srv.start()
            print(self.LOG_TAG + "Stop")
        print(self.LOG_TAG + "SRV остановлен")

    def getClass(self):
        return self.signalUiUpdate

    def srvStop(self):
        self.connection = False
        self.srv.stop()
        print(self.LOG_TAG + "STOP")
#============================================================================================

if __name__ == "__main__":
    LOG_TAG = "Main: "
    app = QApplication(sys.argv)
    GUI = Window()
    GUI.show()
    try:
        sys.exit(app.exec_())
        sys.exit(0)
    except SystemExit as err:
        print("Error " + LOG_TAG  + str(err))
    except Exception as err:
        print("Error " + LOG_TAG  + str(err))