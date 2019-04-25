import sys
import random
from PyQt5 import QtCore,QtWidgets, QtGui, uic
from PyQt5.QtWidgets import QApplication


class MyWindowClass(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MyWindowClass, self).__init__()
        uic.loadUi('historia_clinica.ui', self)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MyWindow = MyWindowClass(None)
    MyWindow.show()
    app.exec_()

