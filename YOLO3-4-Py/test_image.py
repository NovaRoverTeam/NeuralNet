from io import BytesIO

import PIL.Image
import numpy as np
import requests

from pydarknet import Detector, Image


def test_image():

    assert r.status_code == 200
    img = PIL.Image.open('/home/nvidia/Desktop/download.jpg')

    img = np.array(img)
    img = img[:,:,::-1] # RGB to BGR

    cfg = bytes("/home/nvidia/Documents/yolov3-tiny-tennis/yolov3-tiny-tennis.cfg", encoding="utf-8")
    weights = bytes("/home/nvidia/Documents/yolov3-tiny-tennis/yolov3-tiny-tennis_last.weights", encoding="utf-8")
    data = bytes("/home/nvidia/Documents/darknet/data/obj.data", encoding="utf-8")

    net = Detector(cfg, weights, 0, data)


    img2 = Image(img)

    results = net.detect(img2)
    print(results)

    results_labels = [x[0].decode("utf-8") for x in results]

