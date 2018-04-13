import struct
import sys
import sip
from PyQt5.Qt import *
import numpy as np
import time
import socket

a = QApplication(sys.argv)
#create label
label = QLabel()
label.showFullScreen()
screenWidth = 1920
screenHeight = 1080

#create socket server
HOST = '192.168.123.123'
PORT = 50000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print "client connected"

while True:

    face_num = int(conn.recv(5))
    print "Detected number: %s" % face_num

    #create pixmap
    image = QPixmap(screenWidth, screenHeight)
    image.fill(Qt.transparent)

    #create painter
    painter = QPainter()
    painter.begin(image)
    painter.setPen(QPen(Qt.red, 2))

    #paint
    for i in range(0, face_num):

        min_x_coord = int(conn.recv(5))
        min_y_coord = int(conn.recv(5))
        max_x_coord = int(conn.recv(5))
        max_y_coord = int(conn.recv(5))
        print "begin to draw"
        painter.drawRect(min_x_coord, min_y_coord,
                max_x_coord - min_x_coord, max_y_coord - min_y_coord)

    painter.end()

    #show rectangle
    label.setPixmap(image)
    label.setMask(image.mask())
    label.show()
    a.processEvents()
    #time.sleep(0.01)


s.close()
a.exec_()
