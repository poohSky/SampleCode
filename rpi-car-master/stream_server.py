from socket import  *
import cv2
import base64
import numpy as np


server = socket(AF_INET, SOCK_STREAM)
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server.bind(('', 1234))
server.listen(1)

print "server listening on 1234..."
conn, addr = server.accept()
print 'client connected.', addr

read = ''
try:
    while True:
        read += conn.recv(1024)
        first = read.find('^')
        last = read.find('$')
        print first, last
        if first != -1 and last != -1:
            b64 = read[first+1:last]
            read = read[last+1:]
            #print b64
            img = base64.decodestring(b64)
            image = cv2.imdecode(np.fromstring(img, dtype=np.uint8), cv2.CV_LOAD_IMAGE_UNCHANGED)
            cv2.imshow('server', image)
            cv2.waitKey(1)
            first = -1
            last = -1
finally:
    conn.close()