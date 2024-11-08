import cv2, time

WIDTH = 64
HEIGHT = 64

cam = cv2.VideoCapture(0)
cam.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 64)
cam.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 64)
time.sleep(2) #time for camera warmup
while(True):
    # Capture frame-by-frame
    ret, frame = cam.read()
    print type(frame)
    rimg = cv2.flip(frame, 0)
    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    key = cv2.waitKey(1)
    
    if key & 0xFF == ord('q'): 
        break
    elif key & 0xFF == ord('h'):
        print 'left'
        cv2.imwrite('left.jpg', frame)
    elif key & 0xFF == ord('j'):
        print 'forward'
    elif key & 0xFF == ord('k'):
        print 'backward'
    elif key & 0xFF ==ord('l'):
        print 'left'
    elif key & 0xFF == ord(' '):
        print 'stop'
        

# When everything done, release the capture
cam.release()
cv2.destroyAllWindows()