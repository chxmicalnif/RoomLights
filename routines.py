import RPi.GPIO as GPIO
import sys
import os

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


def pin17_18_20_21On():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(17,GPIO.OUT)
    GPIO.output(17,GPIO.HIGH)

    GPIO.setup(18,GPIO.OUT)
    GPIO.output(18,GPIO.HIGH)

    GPIO.setup(20,GPIO.OUT)
    GPIO.output(20,GPIO.HIGH)

    GPIO.setup(21,GPIO.OUT)
    GPIO.output(21,GPIO.HIGH)

def pin17_18_20_21Off():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(17,GPIO.OUT)
    GPIO.output(17,GPIO.LOW)

    GPIO.setup(18,GPIO.OUT)
    GPIO.output(18,GPIO.LOW)

    GPIO.setup(20,GPIO.OUT)
    GPIO.output(20,GPIO.LOW)

    GPIO.setup(21,GPIO.OUT)
    GPIO.output(21,GPIO.LOW)

    print("LEDs off")

def cleanExit():
    GPIO.cleanup()
    print("GPIO CLEANUP")
    os.system("shutdown -h 1")
