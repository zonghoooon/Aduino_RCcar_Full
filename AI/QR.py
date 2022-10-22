#pip install pyzbar
#pip install pillow


from pyzbar.pyzbar import decode
from PIL import Image
import cv2
import time

def is_qr(img):
    result = decode(img)
    for i in result:
        print(i.data.decode("utf-8")) #QR코드 사이트주소 출
        return True #QR코드가 인식된 경우 true return
    return False #QR코드 인식 X시 false return

def tst(): #테스트용 
    filePath ='C:/Users/hoon/Desktop/QRCode.png' #샘플QR코드 파일 위치 입력
    img = Image.open(filePath)
    res = decode(img)
    for i in res:
        print(i.data.decode("utf-8"))
        return True
    return False
