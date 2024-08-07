# library import 
# object  of videocapture class
# use it inside a while loop
import os
import cv2
import sys

path = r"c:\Users\Lenovo\AppData\Local\Packages\5319275A.WhatsAppDesktop_cv1g1gvanyjgm\TempState\9EC3CFF2FC5008DED145994EF2B906D7\UnifiedShareSheet.mp4"
if not os.path.exists(path):
    print(f"file not  found: {path}")
    sys.exit(1)
cam = cv2.VideoCapture(path)
while True:
    state,frame = cam.read()
    if not state:
        break
    # resize
    frame1= cv2.resize(frame ,(300,300))
    frame2= cv2.resize(frame ,(0,0),fx=.5,fy=.5)
    cv2.imshow('video resized',frame1)
    cv2.imshow('video resized by scale',frame2)
    if cv2.waitKey(10) == ord('q'):
        break
