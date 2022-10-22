from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep
import pickle
import cv2
import numpy as np


camera = PiCamera()
camera.resolution = (320,320)         # set camera resolution to (320, 320)
camera.color_effects = (128,128)  

# camera.start_preview() # 카메라 미리보기 시작

cv2.namedWindow('disp')
a = 0
sample = []
while a != 400:
# for direcao,velocidade,img in data:
    img = np.empty((320, 320, 3), dtype=np.uint8)
    camera.capture(img ,format='bgr')  # 캡쳐
    img = img[:,:,0]  
    threshold = int(np.mean(img))*0.5   
    # print(threshold)
    # Invert black and white with threshold
    ret, img2 = cv2.threshold(img.astype(np.uint8), threshold,255, cv2.THRESH_BINARY_INV)
    img2 = cv2.resize(img2,(16,16), interpolation=cv2.INTER_AREA )
    
    #print(str(a)+' : press ')
    #a = int(input())  -2       # 라벨링
    a+=1
    print(a)
    sample.append([0 , 1 , img2])

cv2.destroyAllWindows()

data = []

# data = pickle.load( open( "additonal_data.p", "rb" ), encoding="latin" )
data += sample
with open("new_additional_data2.p", "wb") as f:
    pickle.dump(data, f)
print('end')

