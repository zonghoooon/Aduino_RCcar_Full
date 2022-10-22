import time
import serial
ser = serial.Serial('/dev/serial/by-id/usb-Arduino_Srl_Arduino_Uno_75439313737351617181-if00',9600)


cmd = "000"
# print(type(cmd))
cmd = cmd +'\n'
ser.write(cmd.encode('ascii'))
# read_serial = ser.readline()
# print(read_serial)
while(1):
        
    cmd= "R255"
# print(type(cmd))
    cmd = cmd +'\n'
    ser.write(cmd.encode('ascii'))
    print("MY cmd : " + cmd)
#     read_serial = ser.readline()
#     print(read_serial)
    time.sleep(0.2)
    
    cmd= "F000"
# print(type(cmd))
    cmd = cmd +'\n'
    ser.write(cmd.encode('ascii'))
    print("MY cmd : " + cmd)
#     read_serial = ser.readline()
#     print(read_serial)
    time.sleep(0.2)
    
    