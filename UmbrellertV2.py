import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
 # need to set up every channel which are using as an input or an output
GPIO.setup(11, GPIO.OUT)
  
while True:
	GPIO.output(11, GPIO.HIGH) 
