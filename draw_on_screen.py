import sys
import sip
from PyQt5.Qt import *
import cv2
import numpy as np
import time

a = QApplication(sys.argv)

w = QWidget()

#w.setWindowTitle("Corerain Car Detection")
#label = QLabel(w)
label = QLabel()
label.showFullScreen()
screenWidth = 1920
screenHeight = 1080

#Set full screen and get screen size
#w.showFullScreen()
#w.setWindowOpacity(0.1)
#screenWidth = w.width()
#screenHeight = w.height()

for i in range(0,100):


    image = QPixmap(screenWidth, screenHeight)
    #image = QPixmap(1920, 1080)
    image.fill(Qt.transparent)

    painter = QPainter()
    print "begin"
    painter.begin(image)
    painter.setPen(QPen(Qt.red, 2))
    #painter.setBrush(QColor(255, 0, 0))
    if i%2 == 0:
        painter.drawRect(0, 0, 100, 100)
        painter.drawRect(150, 150, 100, 100)
        painter.drawRect(700, 700, 100, 100)
    elif i%2 ==1:
        painter.drawRect(500, 500, 200, 200)
    painter.end()
    print "finished"
    print i

    label.setPixmap(image)
    #label.resize(screenWidth, screenHeight)
    #w.show()
    label.setMask(image.mask())
    label.show()
    a.processEvents()
    time.sleep(0.01)
a.exec_()

