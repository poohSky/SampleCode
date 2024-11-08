import io
import picamera
import time
import cv2
import base64
import numpy as np

try:
    with picamera.PiCamera() as camera:
        camera.resolution = (320, 240) 
        stream = io.BytesIO()
        camera.capture(stream, 'jpeg')
        img = stream.getvalue()
        b64 = base64.encodestring(img)
        print b64
        
        img2 = base64.decodestring(b64)
        image = cv2.imdecode(np.fromstring(img2, dtype=np.uint8), cv2.CV_LOAD_IMAGE_UNCHANGED)
        cv2.imshow('image', image)
        cv2.waitKey(0)
finally:
    pass