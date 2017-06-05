import RPi.GPIO as GPIO
import pygame.midi
import time

# Distance Related Methods

def prepare(GPIO_ECHO, GPIO_TRIGGER):
    """ Initialize the Raspberry Pi GPIO  """
    # Set pins as output and input
    GPIO.setup(GPIO_TRIGGER,GPIO.OUT)    # Trigger
    GPIO.setup(GPIO_ECHO,GPIO.IN)        # Echo
    # Set trigger to False (Low)
    GPIO.output(GPIO_TRIGGER, False)
    # Allow module to settle
    time.sleep(0.5)

def get_distance(GPIO_ECHO, GPIO_TRIGGER):
    """ get the distance from the sensor, echo - the input from sensor """
    # Send 10us pulse to trigger
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    start = time.time()
    # Taking time
    while GPIO.input(GPIO_ECHO)==0:
        start = time.time()
    while GPIO.input(GPIO_ECHO)==1:
        stop = time.time()
    # Calculate pulse length
    elapsed = stop-start
    # Distance pulse travelled in that time is time
    # multiplied by the speed of sound (cm/s)
    distance = elapsed * 34300
    # That was the distance there and back so halve the value
    distance = distance / 2
    return distance

# Audio and MIDI Related Methods

def conf_midi():
    """ Initialize MIDI component """
    instrument = 79 # Whistle
    pygame.init()
    pygame.midi.init()
    port = 2
    global midiOutput   # It is used in other methods
    midiOutput = pygame.midi.Output(port, 1)
    midiOutput.set_instrument(instrument)

def play_midi(note, b4note, volume):
    """ Play a new MIDI note and turn off the last one """
    # use the last note to compare
    if (note != b4note):
        """ To-Do: smoother transitions between notes, use pitch bend. """
        midiOutput.note_off(b4note,volume)
        midiOutput.note_on(note,volume)
    # help to not consume all resources
    time.sleep(.15)

def get_note(dist=0):
    """ Compute the note based on the distance measurements, get percentages of each scale and compare """
    # Config
    # you can play with these settings
    minDist = 3    # Distance Scale
    maxDist = 21
    octaves = 1
    minNote = 48   # c4 middle c
    maxNote = minNote + 12*octaves
    # Percentage formula
    fup = (dist - minDist)*(maxNote-minNote)
    fdown = (maxDist - minDist)
    note = minNote + fup/fdown
    """ To-do: calculate trends form historical data to get a smoother transitions """
    return int(note)

# MAIN
GPIO.setwarnings(False)
# The pin number is the actual pin number
GPIO.setmode(GPIO.BCM)
# Set up the GPIO channels
trigger = 17
echo = 27
prepare(echo, trigger)
note = 0
conf_midi()
volume = 127
try:
    while True:
        b4note = note
        # get distance
        d = get_distance(echo, trigger)
        # calculate note
        note = get_note(d)
        # to-do, take a number of sample notes and average them, or any other statistical function. eg. Play just minor notes, ponderate average, etc. 
        # play the note
        play_midi(note, b4note, volume)
except KeyboardInterrupt:
    GPIO.cleanup()
    del midiOutput
    pygame.midi.quit()
GPIO.cleanup()
pygame.midi.quit()
