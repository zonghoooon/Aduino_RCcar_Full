
import time
import cv2
import serial
import QR
from PIL import Image
from picamera import PiCamera
camera = PiCamera()
camera.resolution = (320,320)
camera.start_preview()
while True:
    
    camera.capture('qrimg.jpg')
    img = Image.open('qrimg.jpg')
    result = QR.is_qr(img)
    print(result)
    time.sleep(0.5)