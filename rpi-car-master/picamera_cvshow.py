import numpy as np
import io
import picamera
import time
import cv2

stream = io.BytesIO()
with picamera.PiCamera() as camera:
    camera.resolution = (320, 240)
    camera.sleep(2) 
    camera.capture(stream, format='jpeg', use_video_port=True)
    imgdata = np.fromstring(stream.getvalue(), dtype=np.uint8)
    image = cv2.imdecode(imgdata, 1) 
    cv2.imshow('image', image)
    cv2.waitKey(0)
