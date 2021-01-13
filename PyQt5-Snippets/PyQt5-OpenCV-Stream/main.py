from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.uic import loadUi
import sys
import imageprocessing

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("mainwindow.ui",self)

        self.rgbButton.clicked.connect(self.rgbButtonClicked)
        self.grayButton.clicked.connect(self.grayButtonClicked)
        self.binButton.clicked.connect(self.binButtonClicked)
        self.exitButton.clicked.connect(self.exitButtonClicked)

        self.imgObject=imageprocessing.ImageProcessing(webcam=True)
        self.imgObject.changeView(1)

        self.timer=QtCore.QTimer(self)
        self.timer.timeout.connect(self.updateFrames)
        self.timer.start(5)

    def updateFrames(self):
        self.image=self.imgObject.getFrames()

        # If there is only 2 items in shape, it means the
        # image is one channel.
        if(len(self.image.shape)==2):
            imageFormat=QtGui.QImage.Format_Indexed8
        # Else, it may be 3 or 4
        else:
            # Get third item which is the number of channels.
            numChannels=self.image.shape[2]
            if numChannels==1:
                #print("Debug1")
                imageFormat=QtGui.QImage.Format_Indexed8
            elif numChannels==3:
                #print("Debug2")
                imageFormat=QtGui.QImage.Format_RGB888
            elif numChannels==4:
                #print("Debug3")
                imageFormat=QtGui.QImage.Format_RGBA8888

        outImage=QtGui.QImage(self.image,self.image.shape[1],self.image.shape[0],self.image.strides[0],imageFormat)

        self.imageLabel.setPixmap(QtGui.QPixmap.fromImage(outImage))
        self.imageLabel.setScaledContents(True)

    def rgbButtonClicked(self):
        self.imgObject.changeView(1)

    def grayButtonClicked(self):
        self.imgObject.changeView(2)

    def binButtonClicked(self):
        self.imgObject.changeView(3)

    def exitButtonClicked(self):
        if self.timer.isActive():
            self.timer.stop()
            self.imgObject.closeCam()
            self.close()

    def closeEvent(self, event):
        if self.timer.isActive():
            self.timer.stop()
            self.imgObject.closeCam()
            self.close()


if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    w=MainWindow()
    w.show()
    app.exec_()
