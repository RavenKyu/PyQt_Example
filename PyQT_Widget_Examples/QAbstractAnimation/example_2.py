# coding: utf-8

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
import time
from PyQt5.QtCore import pyqtSlot
import random

class Form(QtWidgets.QWidget):
    def __init__(self):
        super(Form, self).__init__()
        self.setGeometry(QtCore.QRect(10, 10, 640, 480))
        lb = QtWidgets.QPushButton('Hello', self)
        self.show()

        self.ani = QtCore.QPropertyAnimation(lb, "geometry")
        self.ani.setDuration(1000)

        self.ani.setKeyValueAt(0, QtCore.QRect(0, 0, 100, 30))
        self.ani.setKeyValueAt(0.5, QtCore.QRect(250, 250, 100, 30))
        self.ani.setKeyValueAt(1, QtCore.QRect(0, 0, 100, 30))
        self.ani.start()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.processEvents(QtCore.QEventLoop.AllEvents)
    w = Form()
    sys.exit(app.exec())