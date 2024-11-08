import RPi.GPIO as GPIO

pin_left1 = 19
pin_left2 = 26
pin_right1 = 16 
pin_right2 = 20 

pin_left_pwm = 6
pin_right_pwm = 12
hz = 50
duty_cycle = 50

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_left1, GPIO.OUT)
GPIO.setup(pin_left2, GPIO.OUT)
GPIO.setup(pin_right1, GPIO.OUT)
GPIO.setup(pin_right2, GPIO.OUT)
GPIO.setup(pin_left_pwm, GPIO.OUT)
GPIO.setup(pin_right_pwm, GPIO.OUT)

lpwm = GPIO.PWM(pin_left_pwm, hz)
rpwm = GPIO.PWM(pin_right_pwm, hz)

lpwm.start(duty_cycle)
rpwm.start(duty_cycle)

def setDC(dc):
    lpwm.ChangeDutyCycle(dc)
    rpwm.ChangeDutyCycle(dc)


def foward():
    GPIO.output(pin_left1, True)
    GPIO.output(pin_left2, False)
    GPIO.output(pin_right1, True)
    GPIO.output(pin_right2, False)
def stop():
    GPIO.output(pin_left1, False)
    GPIO.output(pin_left2, False)
    GPIO.output(pin_right1, False)
    GPIO.output(pin_right2, False)

def backward():
    GPIO.output(pin_left1, False)
    GPIO.output(pin_left2, True)
    GPIO.output(pin_right1, False)
    GPIO.output(pin_right2, True)

def turn_left():
    GPIO.output(pin_left1, False)
    GPIO.output(pin_left2, False)
    GPIO.output(pin_right1, True)
    GPIO.output(pin_right2, False)
    
def turn_right():
    GPIO.output(pin_left1, True)
    GPIO.output(pin_left2, False)
    GPIO.output(pin_right1, False)
    GPIO.output(pin_right2, False)

def cleanup():
    rpwm.stop()
    lpwm.stop()
    GPIO.cleanup()
    
    
if __name__ == '__main__':
    try:
        while True:
            menu = input("0:stop, 8:go, 4:left, 6:right, 2:back, 5:speed")
            if menu == 5:
                speed = input("speed (0 ~100) :")
                setDC(speed)
            elif menu == 8:
                foward()
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