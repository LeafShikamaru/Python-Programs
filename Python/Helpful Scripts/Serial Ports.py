import serial

ser1 = serial.Serial(
    port = 'COM3',
    baudrate = 115200,
    timeout = 0.1
)

#method for reading incoming bytes on serial
def read_serial(ser1):
    while True:
        ser1.open()
        ser1.write(b'hello\n')
        ser1.read(6)
        ser1.close()


'''
        received_data = ser.read()              #read serial port
        sleep(0.03)
        data_left = ser.inWaiting()             #check for remaining byte
        received_data += ser.read(data_left)
        print (received_data)                   #print received data
        ser.write(received_data)                #transmit data serially
'''

#todo implement packet buffer / send data
ser2 = serial.Serial(
    port = 'COM4',
    baudrate = 115200,
    timeout = 0.1
)

def write_serial(ser2):
    while True:
        ser2.open()
        #read data from serial port
        serBarCode = ser2.readline()

        #if there is smth do smth
        if len(serBarCode) >= 1:
            print(serBarCode.decode("utf-8"))
            print(data)
        ser2.close()
