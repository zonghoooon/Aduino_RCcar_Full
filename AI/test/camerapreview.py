from picamera.array import PiRGBArray
from picamera import PiCamera
camera = PiCamera()
camera.resolution = (320,320)         # set camera resolution to (320, 320)
camera.color_effects = (128,128)
camera.start_preview(fullscreen=False, window=(200,200,480,480)) # 카메라 미리보기 시작