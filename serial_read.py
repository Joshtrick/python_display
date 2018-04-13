import serial
import numpy as np
import struct
ser = serial.Serial()
ser.baudrate = 115200
ser.port = '/dev/serial0'
ser.open()
while True:
    start_check = ord(ser.read())
    if start_check == 169:
        hour = ord(ser.read())
        minute = ord(ser.read())
        second = ord(ser.read())
        mili_sec = ord(ser.read())
        print "@ %shr %smin %ssec %s0ms" % (hour, minute, second, mili_sec)

        float_num = struct.unpack('f', ser.read(4))[0]
        print float_num

        if float_num > 0 and int(float_num%5) == 0 and float_num <= 100:
            face_num = int(float_num/5)
            print "Detected number: %s" % face_num
            for i in range(0, face_num):
                score = struct.unpack('f', ser.read(4))[0]
                print score
                if int(score) == 1:
                        min_x = struct.unpack('f', ser.read(4))[0]
                        min_y = struct.unpack('f', ser.read(4))[0]
                        max_x = struct.unpack('f', ser.read(4))[0]
                        max_y = struct.unpack('f', ser.read(4))[0]
                        print "(%s, %s) (%s, %s)" % (min_x, min_y, max_x, max_y)
                else:
                    break

ser.close()
