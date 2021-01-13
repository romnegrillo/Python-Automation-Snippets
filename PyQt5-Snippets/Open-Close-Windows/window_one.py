from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import window_two

class WindowOne(QtWidgets.QMainWindow):

    def __init__(self):
        super(WindowOne,self).__init__()
        loadUi("window_one.ui", self)

        self.pushButton.clicked.connect(self.openNewWindow)

    def openNewWindow(self):
        self.w = window_two.WindowTwo()
        self.w.show()
        self.close()
        


if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w=WindowOne()
    w.show()
    app.exec_()
