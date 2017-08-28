import sys
from PyQt5 import QtGui, QtWidgets
from tmp import Example1

class Example(QtWidgets.QMainWindow):
	print('1')
	def __init__(self):

		super(Example, self).__init__()
		self.initUI()

	def initUI(self):
		print('2')

		self.setGeometry(300, 300, 290, 150)
		self.setWindowTitle('Emit signal')
		self.example1 = Example1(1)
		self.example1.sign.connect(self.update)
		self.example1.start()
		self.show()


	def update(self):
		print('YES')


app = QtWidgets.QApplication(sys.argv)
window = Example()
window.show()
app.exec_()