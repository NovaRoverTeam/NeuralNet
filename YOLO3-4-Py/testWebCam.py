import cv2

cap = cv2.VideoCapture(1)

while True:
    #cap = cv2.VideoCapture('rstp://nova:rovanova@192.168.1.52:88/videoMain',cv2.CAP_GSTREAMER)
    
    r, frame = cap.read()
    cv2.imshow("preview", frame)
    k = cv2.waitKey(1)
    if k == 0xFF & ord("q"):
        break
