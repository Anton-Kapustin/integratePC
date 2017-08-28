from PyQt5 import QtCore, QtWidgets, QtGui
import sys

class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self, icon, parent = None):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        menu = QtWidgets.QMenu(parent)
        exitAction = menu.addAction("exit")
        exitAction.triggered.connect(self.close)
        self.setContextMenu(menu)
        self.lable = QtWidgets.QLabel()
        self.lable.setObjectName("Battery status")


def main(image):
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    trayIcon = SystemTrayIcon(QtGui.QIcon(image), w)
    trayIcon.show()
    sys.exit(app.exec_())
# if __name__== '__main__':
#     on = r'1.png'
#     main(on)