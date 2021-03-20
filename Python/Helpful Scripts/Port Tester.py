import sys, os
import serial, time
from serial import *
import random

ser = serial.Serial(
     port='COM3',
     baudrate=115200,
     bytesize=5,
     parity='N',
     stopbits=1,
     timeout=5,
     xonxoff=0,
     rtscts=0,
     writeTimeout = 1)

ser1 = serial.Serial(
     port='COM4',
     baudrate=115200,
     bytesize=5,
     parity='N',
     stopbits=1,
     timeout=5,
     xonxoff=0,
     rtscts=0,
     writeTimeout = 1)
     
#data = '\x10\x02\x00\x00\x01\x4e\xf0\x04\x01\xff\x10\x17\x02\x4e\xf0\x04\x02\xff\x10\x17\x10\x03\xff'
#data_utf = data.encode()

while True:
    def randbytes(n):
            yield random.getrandbits(8)

    my_random_bytes = bytearray(randbytes(1000000))

    ser.write(my_random_bytes)
    print(my_random_bytes)

    ser1.read()
