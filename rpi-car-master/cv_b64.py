import cv2
import time
import base64
import numpy as np
import pickle
import struct 

WIDTH, HEIGHT = 64, 64

cam = cv2.VideoCapture(0)
#cam.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 64)
#cam.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 64)
time.sleep(2) #time for camera warmup


try:
    ret, img1 = cam.read()
    print type(img1), img1.shape, img1.dtype
    ret, enc = cv2.imencode('.jpg', img1)
    print type(enc), len(enc)
    b64 = base64.encodestring(enc)
    print "b64", type(b64), len(b64),b64[0]
    pstr = enc.tostring()
    print "plain", len(pstr)

    dec = base64.decodestring(b64)
    #img_str = base64.b64decode(b64)
    #img_str = b64.decode('base64')
    #print type(img_str), len(img_str),  img_str[0]
    arr = np.fromstring(pstr, dtype=np.uint8)
    print type(arr), arr.shape, arr.dtype
    #ret, img2 = cv2.imdecode(np.fromstring(img_str, dtype=np.uint8), cv2.IMREAD_UNCHANGED )
    arr = np.frombuffer(dec, dtype=np.uint8)
    print type(arr), arr.shape, arr.dtype
    #img2 = pickle.loads(p)
    img2 = cv2.imdecode(arr, -1 ) #cv2.CV_LOAD_IMAGE_UNCHANGED)
    print type(img2), img2.shape, img2.dtype
    cv2.imshow('after',img2)
    key = cv2.waitKey(1)
finally:
    cam.release()
    cv2.destroyAllWindows()