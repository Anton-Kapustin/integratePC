import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

from mainwindow import Ui_MainWindow


class Gui(QMainWindow, Ui_MainWindow) :

    def __init__(self):
        QtWidgets.QApplication.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.lable_batteryStatus





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Gui()
    window.show()

    sys.exit(app.exec_())

