from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

class now_camera():
# initialize the camera and grab a reference to the raw camera capture
    camera =PiCamera()
    camera.resolution= (640,480)
    camera.framerate= 32
    rawCapture= PiRGBArray (camera, size=(640,480))
# allow the camera to warmup
    time.sleep(0.1)
# capture frames from the camera
    for frame in camera.capture_continuous(rawCapture , format = "bgr",use_video_port = True):
        image = frame.array
        cv2.imshow("Frame", image)
# clear the stream in preparation for the next frame
        rawCapture.truncate(0)
	

