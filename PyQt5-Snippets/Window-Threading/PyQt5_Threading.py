from PyQt5 import QtWidgets, QtCore
from PyQt5.uic import loadUi
import sys
import time
import threading

class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main,self).__init__()
        loadUi("mainwindow.ui", self)
        self.ctr=0
        self.ctr2=0
       
        thread = threading.Thread(target=self.updateTimer)
        thread.start()

        thread2 = threading.Thread(target=self.updateTimer2)
        thread2.start()
        

    def updateTimer(self):

        while 1:
            self.label.setText(str(self.ctr))
            self.ctr = self.ctr+1
            time.sleep(1)

    def updateTimer2(self):

        while 1:
            self.label_2.setText(str(self.ctr2))
            self.ctr2 = self.ctr2+1
            time.sleep(5)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = Main()
    w.show()
    app.exec_()
