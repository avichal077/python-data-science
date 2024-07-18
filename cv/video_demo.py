import cv2

video = cv2.VideoCapture(r"c:\Users\Lenovo\AppData\Local\Packages\5319275A.WhatsAppDesktop_cv1g1gvanyjgm\TempState\B9460526DC7DAF0E629F28EFCA761E7A\WhatsApp Video 2024-07-18 at 10.47.36_86ed84e5.mp4")
while True:
    status , frame = video.read()
    print(status,frame)
    if not status:
        break
    cv2.imshow('video frame',frame)
    if cv2.waitKey(10) == 27:
        break
video.release()
cv2.destroyAllWindows()