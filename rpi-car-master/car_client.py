import cv2, time
from socket import  *
import motor_pwm as mt
import RPi.GPIO as GPIO
import threading
import base64
import picamera
import io

WIDTH = 128
HEIGHT = 128
host = '192.168.200.4'
stop_distance = 10
running = True

trig_pin = 24
echo_pin = 23 
distance = 0
start_time = 0
    
def recv():
    while running:
        read = socket.recv(1024)
        if len(read) <=0 :
            continue
        print 'cmd : [%s]'% read,
        if read  == 'h':
            print 'left'
            mt.turn_left()
        elif read == 'j':
            print 'forward'
            mt.forward()
        elif read == 'k':
            print 'back'
            mt.backward()
        elif read == 'l':
            print 'right'
            mt.turn_right()
        elif read == ' ':
            print 'stop'
            mt.stop()


def ultra_sonic():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(trig_pin, GPIO.OUT)
    GPIO.setup(echo_pin, GPIO.IN)
    
    while running:
        GPIO.output(trig_pin, False)
        print "ready for mesurement."
        time.sleep(0.2)
        GPIO.output(trig_pin, True)
        time.sleep(0.00001)  #set HIGH for 10us
        GPIO.output(trig_pin, False)
        while GPIO.input(echo_pin) == 0:
            start_time = time.time()
        while GPIO.input(echo_pin) == 1:
            end_time = time.time()
        travel_time = end_time - start_time;
        distance = travel_time * 17150 #32300/2
        distance = round(distance, 2)
        print 'Distance:%dcm' %distance
        if distance < stop_distance:
            mt.stop()


socket = socket(AF_INET, SOCK_STREAM)
socket.connect( (host, 1234))
print 'conneted to server : %s'%host

th = threading.Thread(target=recv)
th.start()

th2 = threading.Thread(target=ultra_sonic)
th2.start()
try:
    with picamera.PiCamera() as camera:
        camera.resolution = (WIDTH, HEIGHT)
        while(True):
            stream = io.BytesIO()   
            camera.capture(stream,  format='jpeg', use_video_port=True)
            img = stream.getvalue()
            b64 = base64.encodestring(img)
            b64 = '^'+b64 + '$'
            #print b64
            socket.send(b64)
            print 'sent!,', len(b64)
finally:
    running = False
    mt.cleanup()
    socket.close()
