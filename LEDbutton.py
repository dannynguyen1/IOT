import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

#setup board
GPIO.setmode(GPIO.BCM)

#setup pin as input

GPIO.setup(21,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(18,GPIO.OUT)

#button not pressed
buttonPressed = False

#get button state
try:
    while(True):
        buttonState = GPIO.input(21)
        if buttonState:
            print("button pressed")
            if buttonPressed == False:
                GPIO.output(18,GPIO.HIGH)
                buttonPressed = True;
                sleep(1)
            else:
                GPIO.output(18,GPIO.LOW)
                buttonPressed = False;
                sleep(1)
finally:
    GPIO.cleanup()
    
  

        
        
        
        
