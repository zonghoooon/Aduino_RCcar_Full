import time
import serial
ser = serial.Serial('/dev/serial/by-id/usb-Arduino_Srl_Arduino_Uno_75439313737351617181-if00',9600)


while(1):

    read_serial = ser.readline()
    print(read_serial)
    time.sleep(0.2)