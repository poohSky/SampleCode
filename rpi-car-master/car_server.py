from socket import  *
import base64
import numpy as np
import cv2, time, os
from datetime import datetime

server = socket(AF_INET, SOCK_STREAM)
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server.bind(('', 1234))
server.listen(1)
print "server listening on 1234..."
conn, addr = server.accept()
print 'client connected.', addr

basepath = './capture_srv/'
if not os.path.exists(basepath):
    os.mkdir(basepath)

for dir in ['left', 'right', 'forward', 'backward', 'stop']:
    if not os.path.exists((basepath+dir)):
        os.mkdir(basepath + dir)
print 'h:left, j:forward, k:backward, l:right, space:stop, q:quit'

read = ''
try:
    while True:
        read += conn.recv(1024)
        first = read.find('^')
        last = read.find('$')
        #print first, last
        if first != -1 and last != -1:
            b64 = read[first+1:last]
            read = read[last+1:]
            #print b64
            img = base64.decodestring(b64)
            image = cv2.imdecode(np.fromstring(img, dtype=np.uint8), cv2.IMREAD_UNCHANGED )
            cv2.imshow('server', image)
            key = cv2.waitKey(0) & 0xFF
            if key == ord('q'): 
                break
            elif key in [ord('h') , ord('j'), ord('k'), ord('l'), ord(' ')] :
                now = datetime.now()
                now_str = now.strftime("%Y%m%d-%H%M%S.%f")
                if key  == ord('h'):
                    print 'left'
                    path = basepath + 'left/%s.jpg'%now_str
                    conn.send('h')
                elif key == ord('j'):
                    print 'forward'
                    path = basepath +'forward/%s.jpg'%now_str
                    conn.send('j')
                elif key == ord('k'):
                    print 'backward'
                    path = basepath+ 'backward/%s.jpg'%now_str
                    conn.send('k')
                elif key ==ord('l'):
                    print 'right'
                    path = basepath + 'right/%s.jpg' %now_str
                    conn.send('l')
                elif key == ord(' '):
                    print 'stop'
                    conn.send(' ')
                    path = basepath +'stop/%s.jpg' %now_str
                cv2.imwrite(path, image)
                first = -1
                last = -1
finally:
    conn.close()
    
    
        