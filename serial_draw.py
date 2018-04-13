import serial
import struct
import sys
import sip
from PyQt5.Qt import *
import numpy as np
import time

a = QApplication(sys.argv)
#create label
label = QLabel()
label.showFullScreen()
screenWidth = 1920
screenHeight = 1080

#create serial
ser = serial.Serial()
ser.baudrate = 115200
ser.port = '/dev/serial0'
ser.open()

while True:
    start_check = ord(ser.read())
    if start_check == 169:

        #read time
        hour = ord(ser.read())
        minute = ord(ser.read())
        second = ord(ser.read())
        mili_sec = ord(ser.read())
        #print "@ %shr %smin %ssec %s0ms" % (hour, minute, second, mili_sec)

        #read number of float
        float_num = struct.unpack('f', ser.read(4))[0]

        if float_num > 0 and int(float_num%5) == 0 and float_num <= 100:
            face_num = int(float_num/5)
            #print "Detected number: %s" % face_num

            #create pixmap
            image = QPixmap(screenWidth, screenHeight)
            image.fill(Qt.transparent)

            #create painter
            painter = QPainter()
            painter.begin(image)
            painter.setPen(QPen(Qt.red, 2))

            #paint
            for i in range(0, face_num):
                score = struct.unpack('f', ser.read(4))[0]
                #print score
                if int(score) == 1:
                        min_x = struct.unpack('f', ser.read(4))[0]
                        min_y = struct.unpack('f', ser.read(4))[0]
                        max_x = struct.unpack('f', ser.read(4))[0]
                        max_y = struct.unpack('f', ser.read(4))[0]
                        #print "(%s, %s) (%s, %s)" % (min_x, min_y, max_x, max_y)
                        min_x_coord = int(min_x*screenWidth)
                        min_y_coord = int(min_y*screenHeight)
                        max_x_coord = int(max_x*screenWidth)
                        max_y_coord = int(max_y*screenHeight)
                        painter.drawRect(min_x_coord, min_y_coord,
                                max_x_coord - min_x_coord, max_y_coord - min_y_coord)
                else:
                    break

            painter.end()

            #show rectangle
            label.setPixmap(image)
            label.setMask(image.mask())
            label.show()
            a.processEvents()
            #time.sleep(0.01)


ser.close()
a.exec_()
