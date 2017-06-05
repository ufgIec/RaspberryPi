import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

led = 27

GPIO.setup(led, GPIO.OUT)

button = 17

GPIO.setup(button, GPIO.IN)

GPIO.output(led, False)

while True:
    if GPIO.input(button) == 1:
        GPIO.output(led, True)
    else:
        GPIO.output(led, False)
        
