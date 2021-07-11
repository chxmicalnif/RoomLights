import RPi.GPIO as GPIO

def pin17On():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(17,GPIO.OUT)
    GPIO.output(17,GPIO.HIGH)
    print("LED on")

def pin17Off():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(17,GPIO.OUT)
    GPIO.output(17,GPIO.LOW)
    print("LED off")
