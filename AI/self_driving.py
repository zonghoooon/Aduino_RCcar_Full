# Copyright Reserved (2020).
# Donghee Lee, Univ. of Seoul
#
__author__ = 'will'

from rc_car_interface import RC_Car_Interface
from tf_learn import DNN_Driver
import numpy as np
import time
import cv2
import serial
import QR
from PIL import Image
ser = serial.Serial('/dev/serial/by-id/usb-Arduino_Srl_Arduino_Uno_75439313737351617181-if00',9600)

class SelfDriving:

    def __init__(self):
        self.rc_car_cntl = RC_Car_Interface()
        self.dnn_driver = DNN_Driver()

        self.rc_car_cntl.set_left_speed(0)
        self.rc_car_cntl.set_right_speed(0)
    
        self.velocity = 0
        self.direction = 0
    
        self.dnn_driver.tf_learn()
    
    def rc_car_control(self, direction):
        #calculate left and right wheel speed with direction
        # if direction < -1.0:
        #     direction = -1.0
        # if direction > 1.0:
        #     direction = 1.0
        # if direction < 0.0:
        #     left_speed = 1.0+direction
        #     right_speed = 1.0
        # else:
        #     right_speed = 1.0-direction
        #     left_speed = 1.0
        
        
        cmd = ''
        if (-0.5 < direction < 0.5):
            cmd = "F255"+ '\n'
            print("F")
        elif (0.5 <= direction):
            cmd = "R255"+ '\n'
            print("R")
        elif (direction <= -0.5):
            cmd = "L255"+ '\n'
            print("L")
        #print('My cmd is %s' % cmd)
        ser.write(cmd.encode('ascii'))


    def drive(self):
        while True:

# For test only, get image from DNN test images
#            img from get_test_img() returns [256] array. Do not call np.reshape()
#            img = self.dnn_driver.get_test_img()
#            direction = self.dnn_driver.predict_direction(img)

            img = self.rc_car_cntl.get_image_from_camera()
# predict_direction wants [256] array, not [16,16]. Thus call np.reshape to convert [16,16] to [256] array
            img = np.reshape(img,img.shape[0]**2)

            direction = self.dnn_driver.predict_direction(img)         # predict with single image
#             print(direction[0][0])
            self.rc_car_control(direction[0][0])

            # For debugging, show image
#            cv2.imshow("target",  cv2.resize(img, (280, 280)) )
#            cv2.waitKey(0)
#             read_serial = ser.readline()
#             print(read_serial)
            time.sleep(0.1)
            cmd = 'F000' + '\n'
            ser.write(cmd.encode('ascii'))
#             read_serial = ser.readline()
#             print(read_serial)
            #time.sleep(0.7)
#             time.sleep(0.2)

        self.rc_car_cntl.stop()
        cv2.destroyAllWindows()


SelfDriving().drive()
