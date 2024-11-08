import RPi.GPIO as GPIO

pin_left1 = 19
pin_left2 = 26
pin_right1 = 16 
pin_right2 = 20 

#pin_left_pwm = 6
#pin_right_pwm = 12
hz = 50  
dc = 50 #duty-cycle 0~100

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_left1, GPIO.OUT)
GPIO.setup(pin_left2, GPIO.OUT)
GPIO.setup(pin_right1, GPIO.OUT)
GPIO.setup(pin_right2, GPIO.OUT)
#GPIO.setup(pin_left_pwm, GPIO.OUT)
#GPIO.setup(pin_right_pwm, GPIO.OUT)

#lpwm = GPIO.PWM(pin_left_pwm, hz)
#rpwm = GPIO.PWM(pin_right_pwm, hz)
pwm_left1 = GPIO.PWM(pin_left1, hz)
pwm_left2 = GPIO.PWM(pin_left2, hz)
pwm_right1 = GPIO.PWM(pin_right1, hz)
pwm_right2 = GPIO.PWM(pin_right2, hz)
#lpwm.start(duty_cycle)
#rpwm.start(duty_cycle)

pwm_left1.start(0)
pwm_left2.start(0)
pwm_right1.start(0)
pwm_right2.start(0)

def setDC(value):
    global dc
    dc = value

def forward():
    pwm_left1.ChangeDutyCycle(dc)
    pwm_left2.ChangeDutyCycle(0)
    pwm_right1.ChangeDutyCycle(dc)
    pwm_right2.ChangeDutyCycle(0)

def stop():
    pwm_left1.ChangeDutyCycle(0)
    pwm_left2.ChangeDutyCycle(0)
    pwm_right1.ChangeDutyCycle(0)
    pwm_right2.ChangeDutyCycle(0)

def backward():
    pwm_left1.ChangeDutyCycle(0)
    pwm_left2.ChangeDutyCycle(dc)
    pwm_right1.ChangeDutyCycle(0)
    pwm_right2.ChangeDutyCycle(dc)

def turn_left():
    pwm_left1.ChangeDutyCycle(0)
    pwm_left2.ChangeDutyCycle(0)
    pwm_right1.ChangeDutyCycle(dc + 10)
    pwm_right2.ChangeDutyCycle(0)
    
def turn_right():
    pwm_left1.ChangeDutyCycle(dc + 10)
    pwm_left2.ChangeDutyCycle(0)
    pwm_right1.ChangeDutyCycle(0)
    pwm_right2.ChangeDutyCycle(0)

def cleanup():
    pwm_left1.stop()
    pwm_left2.stop()
    pwm_right1.stop()
    pwm_right2.stop()
    GPIO.cleanup()
    
    
if __name__ == '__main__':
    try:
        while True:
            print 'default speed is %d'%dc
            menu = input("0:stop, 8:go, 4:left, 6:right, 2:back, 5:speed>")
            if menu == 5:
                speed = input("speed (0 ~100) :")
                setDC(speed)
            elif menu == 8:
                forward()
            elif menu == 4:
                turn_left()
            elif menu == 6:
                turn_right()
            elif menu == 2:
                backward()
            elif menu == 0:
                stop()
    finally:
        cleanup()