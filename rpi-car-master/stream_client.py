from socket import  *
import io
import picamera
import base64

socket = socket(AF_INET, SOCK_STREAM)
socket.connect( ('', 1234))

try:
    with picamera.PiCamera() as camera:
        camera.resolution = (320, 240)
        while True:
            raw_input('insert enter key when you are ready to take photo.')
            stream = io.BytesIO()
            camera.capture(stream,  format='jpeg', use_video_port=True)
            img = stream.getvalue()
            b64 = base64.encodestring(img)
            b64 = '^'+b64 + '$'
            #print b64
            socket.send(b64)
            print 'sent!'
finally:
    socket.close()

