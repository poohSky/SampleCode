import cv2
import time
import socket
import base64
import threading
import pickle

WIDTH, HEIGHT = 64, 64
HOST = "192.168.1.4"
PORT = 1234
running = True

def recv():
    while running:
        read = conn.recv(1024)
        if len(read) <=0 :
            continue
        print 'cmd : [%s]'% read,
        if read  == 'h':
            print 'left'
        elif read == 'j':
            print 'forward'
        elif read == 'k':
            print 'back'
        elif read == 'l':
            print 'right'
        elif read == ' ':
            print 'stop'


cam = cv2.VideoCapture(0)
cam.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 64)
cam.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 64)
time.sleep(2) #time for camera warmup

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect( (HOST, PORT))

th = threading.Thread(target=recv)
th.start()

try:
    while True:
        ret, img = cam.read()
    
        cv2.imshow('frame',img)
        key = cv2.waitKey(10)
        ret, enc = cv2.imencode('.jpg',img)
        print type(enc), enc.shape
        data = base64.encodestring(img)
        #data = pickle.dumps(img)
        #data = enc.tostring()
        print len(data)
        data = '^'+ data + '$'
        #print b64
        conn.send(data)
        print 'sent!,'   
finally:
    running = False 
    cam.release()
    cv2.destroyAllWindows()