from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.uic import loadUi
import sys
import serial

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("test.ui",self)
        self.timedMessageBox = timedMessageBox(5,"Hello")
        self.timedMessageBox.show()
        

class timedMessageBox(QtWidgets.QMessageBox):
    def __init__(self, timeout, message):
        super(timedMessageBox, self).__init__()
        self.timeout = timeout
        timeoutMessage = "Closing in {} seconds".format(timeout)
        self.setText('\n'.join((message, timeoutMessage)))

    def showEvent(self, event):
        QtCore.QTimer().singleShot(self.timeout*1000, self.close)
        super(timedMessageBox, self).showEvent(event)

 
if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    w=MainWindow()
    w.show()
    app.exec_()
