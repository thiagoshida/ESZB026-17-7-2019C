import RPi.GPIO as GPIO
from time import sleep

x=0
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(24,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(25,GPIO.IN,pull_up_down=GPIO.PUD_UP)
sleep (0.1)



p = GPIO.PWM(18,100)
p.start(0)
while x<=90 :
    p.ChangeDutyCycle(x)
    print("x ",x)
    if GPIO.input(24) == GPIO.HIGH:
            x=x+1
            sleep(0.5)
    if GPIO.input(25) == GPIO.LOW:
        x=x-1
        sleep(0.5)
    

GPIO.cleanup()