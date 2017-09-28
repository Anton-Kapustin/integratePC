import sys, threading, re
from datetime import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5.QtCore import QCoreApplication, QSize

class Notification(QWidget):
    # signNotifyClose = pyqtSignal(str)
    def __init__(self, parent = None):
        time = datetime.now()
        currentTime = str(time.hour) + ":" + str(time.minute) + "_"
        self.LOG_TAG = currentTime + self.__class__.__name__ + ": "
        super(QWidget, self).__init__(parent)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)

        resolution = QDesktopWidget().screenGeometry(-1)
        screenWidth = resolution.width()
        screenHeight = resolution.height()
        print(self.LOG_TAG + "width: " + str(resolution.width()) + " height: " + str(resolution.height()))
        self.nMessages = 0
        self.mainLayout = QVBoxLayout(self)
        self.move(screenWidth, 0)

    def setNotify(self, message):
        command = message.split("/")
        name = ''
        title = ''
        msg = ''

        for string in command:
            if "name" in string:
                name = string.replace("name: ", "\"")
                name += "\""
            elif "title" in string:
                title = string.replace("title: ", "\"")
                # title += "\""
            elif "text" in string:
                msg = string.replace("text: ", "")
                msg += "\""
        print(self.LOG_TAG + "title: " + title)
        print(self.LOG_TAG + "text: " + msg)
        title = name + title
        m = Message(title, msg)
        self.mainLayout.addWidget(m)
        m.buttonClose.clicked.connect(self.onClicked)
        self.nMessages += 1
        self.show()
        threading.Timer(3, m.buttonClose.click).start()

    def onClicked(self):
        self.mainLayout.removeWidget(self.sender().parent())
        self.sender().parent().deleteLater()
        self.nMessages -= 1
        self.adjustSize()
        if self.nMessages == 0:
            self.close()

class Message(QWidget):
    def __init__(self, title, message, parent=None):
        QWidget.__init__(self, parent)
        self.setWindowState(QtCore.Qt.WindowMinimized | QtCore.Qt.WindowActive) # Появляется поверх окон при неактивном основном окне
        self.setLayout(QGridLayout())
        self.titleLabel = QLabel(title, self)
        self.titleLabel.setStyleSheet(
            "font-family: 'Roboto', sans-serif; font-size: 14px; font-weight: bold; padding: 0;")
        self.messageLabel = QLabel(message, self)
        self.messageLabel.setStyleSheet(
            "font-family: 'Roboto', sans-serif; font-size: 12px; font-weight: normal; padding: 0;")
        self.buttonClose = QPushButton(self)
        self.buttonClose.setIcon(QIcon("res/close1.png"))
        self.buttonClose.setFixedSize(14, 14)
        self.layout().addWidget(self.titleLabel, 0, 0)
        self.layout().addWidget(self.messageLabel, 1, 0)
        self.layout().addWidget(self.buttonClose, 0, 1, 2, 1)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    n = Notification()
    n.setNotify("temp", "Hello")
    n.setNotify("notification", "setHeaderLabel toJson IMPLEMENT_READING")
    try:
        sys.exit(app.exec_())
        sys.exit(0)
    except SystemExit as err:
        print("Error " + str(err))
    except Exception as err:
        print("Error " + str(err))