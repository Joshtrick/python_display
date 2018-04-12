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

counter = 0

while True:
    #Set full screen and get screen size
    if counter == 0:
        w.showFullScreen()
    elif counter == 500:
        counter = 0
    counter = counter +1
    screenWidth = w.width()
    screenHeight = w.height()

    #load dummy jpeg
    if counter%2 == 0:
        Img = cv2.imread('testing.jpg')
    elif counter%2 == 1:
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
    time.sleep(0.05)
a.exec_()

