import sys
from PyQt6 import uic, QtCore, QtGui, QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    ServerAdress = "http://localhost:5000"
    MessageID = 0

    def __ini__(self, *args, **kwargs):
        super(MainWindow, self).__ini__(*args, **kwargs)
        uic.loadUi("messenger.ui", self)
       # self.pushButton1.clicked.connect(self.pushButton1_clicked)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
