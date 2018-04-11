import sys
import sip
from PyQt5.Qt import *
import cv2
import numpy as np
import time

a = QApplication(sys.argv)

w = QWidget()

w.setWindowTitle("Corerain Car Detection")
label = QLabel(w)


for i in range(0,100):
    #Set full screen and get screen size
    w.showFullScreen()
    screenWidth = w.width()
    screenHeight = w.height()

    #load dummy jpeg
    if i%2 == 0:
        Img = cv2.imread('testing.jpg')
    elif i%2 == 1:
        Img = cv2.imread('testing01.jpg')

    #CV mat to QImage
    cvImg = cv2.cvtColor(Img, cv2.COLOR_BGR2RGB)
    cvImg = cv2.resize(cvImg, (screenWidth, screenHeight))
    height, width, channel = cvImg.shape
    bytesPerLine = channel * width
    qImg = QImage(cvImg.data, width, height, bytesPerLine, QImage.Format_RGB888)

    #Set label of the widget
    pixmap = QPixmap.fromImage(qImg)
    #pixmap.scaled(1920, 1080, Qt.IgnoreAspectRatio)
    label.setPixmap(pixmap)
    label.resize(screenWidth, screenHeight)
    w.show()
    a.processEvents()

    #Add a delay between frames
    time.sleep(0.01)
a.exec_()

