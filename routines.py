import RPi.GPIO as GPIO
import sys
import os
import time

P1 = 17
P2 = 18
P3 = 20
P4 = 21

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

def readf(name):
    instruction = []
    with open(name, "r") as f:
        for curLine in f:
            #check if line starts with #

            if not curLine.startswith("#"):
                instruction.append(curLine.strip("\n"))

        return instruction

def performFile(l):
    for each in l:
        if each == "S":
            time.sleep(1)
        for i in each:
            if i == "0": pin17_18_20_21Off()
            if i == "1": pin17_18_20_21On()

def threeVoltShuffle():
    print("Setting all lights to red?")
    os.system("sudo python3 tester.py")

def cleanExit():
    GPIO.cleanup()
    print("GPIO CLEANUP")
    os.system("shutdown -h 1")
