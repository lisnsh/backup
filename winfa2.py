
import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BOARD)
gpio.setup(7,gpio.OUT)
gpio.setup(11,gpio.OUT)
gpio.setup(13,gpio.OUT)
gpio.setup(15,gpio.OUT)

gpio.setup(16,gpio.OUT)
gpio.setup(18,gpio.OUT)
gpio.setup(22,gpio.OUT)
gpio.setup(29,gpio.OUT)

gpio.output(7,True)
gpio.output(11,True)
gpio.output(16,True)
gpio.output(18,True)

gpio.output(13,False)
gpio.output(15,False)
gpio.output(22,False)
gpio.output(29,False)
time.sleep(2)
