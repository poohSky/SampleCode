import io
import picamera
import time
import cv2
import base64
import numpy as np

width=128
height = 128

with picamera.PiCamera() as camera:
    camera.resolution = (width, height) 
    stream = io.BytesIO()
    camera.capture(stream, format='jpeg', use_video_port=True)
    img = stream.getvalue()
    b64 = base64.encodestring(img)
    print b64
    
    img2 = base64.decodestring(b64)
    image = cv2.imdecode(np.fromstring(img2, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
    cv2.imshow('image', image)
    cv2.waitKey(0)
