from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import window_one

class WindowTwo(QtWidgets.QMainWindow):

    def __init__(self):
        super(WindowTwo,self).__init__()
        loadUi("window_two.ui", self)

        self.pushButton.clicked.connect(self.openPrevWindow)

    def openPrevWindow(self):
        self.w = window_one.WindowOne()
        self.w.show()
        self.close()
        


if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w=WindowTwo()
    w.show()
    app.exec_()
