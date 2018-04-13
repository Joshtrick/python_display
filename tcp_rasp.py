import serial
import struct
import sys
import time
import socket

#create tcp client
HOST = '192.168.123.123'    # The remote host
PORT = 50000              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print "server reached"

#create serial
ser = serial.Serial()
ser.baudrate = 115200
ser.port = '/dev/serial0'
ser.open()

screenWidth = 1920
screenHeight = 1080

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

        if float_num > 0 and int(float_num%5) == 0 and float_num <= 500:
            face_num = int(float_num/5)
            data = str(face_num)
            for i in range(0, 5-len(data)):
                data = '0' + data
            print "face number: %s" % face_num
            s.send(data)
            #paint
            for i in range(0, face_num):
                score = struct.unpack('f', ser.read(4))[0]

                #print score
                if int(score) == 1:
                        min_x = struct.unpack('f', ser.read(4))[0]
                        min_y = struct.unpack('f', ser.read(4))[0]
                        max_x = struct.unpack('f', ser.read(4))[0]
                        max_y = struct.unpack('f', ser.read(4))[0]
                        print "(%s, %s) (%s, %s)" % (min_x, min_y, max_x, max_y)
                        
                        min_x_coord = int(min_x*screenWidth)
                        min_y_coord = int(min_y*screenHeight)
                        max_x_coord = int(max_x*screenWidth)
                        max_y_coord = int(max_y*screenHeight)
                        
                        print "send started"
                        data = str(min_x_coord)
                        for i in range(0, 5-len(data)):
                            data = '0' + data
                        s.send(data)
                        data = str(min_y_coord)
                        for i in range(0, 5-len(data)):
                            data = '0' + data
                        s.send(data)
                        data = str(max_x_coord)
                        for i in range(0, 5-len(data)):
                            data = '0' + data
                        s.send(data)
                        data = str(max_y_coord)
                        for i in range(0, 5-len(data)):
                            data = '0' + data
                        s.send(data)
			print "send ended"
                else:
                    break

s.close()
ser.close()
