import socket
import sys
import os, time

server_address = '/tmp/tennis_loc_socket'

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

from pydarknet import Detector, Image
import cv2

debug = False
time.sleep(1)


if __name__ == "__main__":
    # Optional statement to configure preferred GPU. Available only in GPU version.
    #pydarknet.set_cuda_device(0)

    cfg = bytes("/home/nvidia/Documents/NeuralNet/Weights+CFG/OID_DIY_NOAUG2/yolov3-tiny-tennis.cfg", encoding="utf-8")
    weights = bytes("/home/nvidia/Documents/NeuralNet/Weights+CFG/V2_Foscm_2/yolov3-tiny-tennis_last.weights", encoding="utf-8")
    #weights = bytes("/home/nvidia/Documents/NeuralNet/Weights+CFG/OID_DIY_NOAUG2/yolov3-tiny-tennis_last.weights", encoding="utf-8")
    data = bytes("/home/nvidia/Documents/NeuralNet/Weights+CFG/OID_DIY_NOAUGMENT/yolov3-tiny-tennis.data", encoding="utf-8")

    net = Detector(cfg, weights, 0, data)

    cap = cv2.VideoCapture("udpsrc port=5002 ! application/x-rtp, encoding-name=JPEG,payload=26 ! rtpjpegdepay ! jpegdec ! videoconvert ! appsink", cv2.CAP_GSTREAMER)
    #cap = cv2.VideoCapture("rstp://nova:rovanova@192.168.1.53:88/videoMain")
    #cap = cv2.VideoCapture(1)


    try:
        sock.connect(server_address)
    except socket.error as msg:
        print(msg)
        sys.exit(1)

    while True:
        #print("trying")
        
        r, frame = cap.read()
        if r:
            #start_time = time.time()

            # Only measure the time taken by YOLO and API Call overhead

            dark_frame = Image(frame)
            results = net.detect(dark_frame)
            del dark_frame

            #end_time = time.time()
            #print("Elapsed Time:",end_time-start_time)
            if results:
              for cat, score, bounds in results:
                  x, y, w, h = bounds
                  st = time.time()
                  sock.sendall(str(list(bounds)).encode('ascii'))
                  time.sleep(max(1/5 - (time.time() - st),0))
                  print("x:", x, " y:", y)
                  if debug:
                    cv2.rectangle(frame, (int(x-w/2),int(y-h/2)),(int(x+w/2),int(y+h/2)),(255,105,180))
                    cv2.putText(frame, str(cat.decode("utf-8")), (int(x), int(y)), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0))
            else:
              sock.sendall(str('0').encode('ascii'))
              #print("no data")
            if debug:
              cv2.imshow("preview", frame)
         
            

        k = cv2.waitKey(1)
        if k == 0xFF & ord("q"):
            break
