import cv2, time, os
from datetime import datetime
#import motor_pwm_thread as m
import motor_pwm as m

WIDTH = 128
HEIGHT = 128

cam = cv2.VideoCapture(0)
cam.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, WIDTH)
cam.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, HEIGHT)
time.sleep(2) #time for camera warmup
basepath = './capture/'
if not os.path.exists(basepath):
    os.mkdir(basepath)

for dir in ['left', 'right', 'forward', 'backward', 'stop']:
    if not os.path.exists((basepath+dir)):
        os.mkdir(basepath + dir)
print 'h:left, j:forward, k:backward, l:right, space:stop, q:quit'
while(True):
    # Capture frame-by-frame
    ret, frame = cam.read()
    #rimg = cv2.flip(frame, 0)
    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv2.imshow('frame',frame)
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord('q'): 
        m.cleanup()
        break
    elif key in [ord('h') , ord('j'), ord('k'), ord('l'), ord(' ')] :
        now = datetime.now()
        now_str = now.strftime("%Y%m%d-%H%M%S.%f")
        if key  == ord('h'):
            print 'left'
            m.turn_left()
            path = basepath + 'left/%s.jpg'%now_str
        elif key == ord('j'):
            print 'forward'
            m.forward()
            path = basepath +'forward/%s.jpg'%now_str
        elif key == ord('k'):
            print 'backward'
            m.backward()
            path = basepath+ 'backward/%s.jpg'%now_str
        elif key ==ord('l'):
            print 'right'
            m.turn_right()
            path = basepath + 'right/%s.jpg' %now_str
        elif key == ord(' '):
            print 'stop'
            m.stop()
            path = basepath +'stop/%s.jpg' %now_str
        cv2.imwrite(path, frame)
# When everything done, release the capture
cam.release()
cv2.destroyAllWindows()