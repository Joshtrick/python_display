import serial
import numpy as np
ser = serial.Serial()
ser.baudrate = 115200
ser.port = ''
ser.open()
while True:
    start_check = ord(ser.read())
    if start_check = 169:
        hour = ord(ser.read())
        minute = ord(ser.read())
        second = ord(ser.read())
        mili_sec = ord(ser.read())
        print "@ %shr %smin %ssec %s0ms" % (hour, miniute, second, mili_sec)
        float_num = float(ser.read(4))
        if float_num > 0 and int(float_num%5) == 0:
            face_num = int(float_num/5)
            print "Detected number: %s" % face_num
            for i in range(0, face_num):
                score = float(ser.read(4))
                print score
                if int(score) == 1:
                    for i in range(0, 5):
                            min_x = float(ser.read(4))
                            min_y = float(ser.read(4))
                            max_x = float(ser.read(4))
                            max_y = float(ser.read(4))
                            print "(%s, %s) (%s, %s)" % (min_x, min_y, max_x, max_y)
                else:
                    break

ser.close()
