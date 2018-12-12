import RPi.GPIO as GPIO
import time

def watch():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(24, GPIO.IN) 
    
    try:
        while True:
            if GPIO.input(24) == GPIO.HIGH:
                break 
            time.sleep(0.1)
    
    except KeyboardInterrupt:
        pass
    
    GPIO.cleanup() 
