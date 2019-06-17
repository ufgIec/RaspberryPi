from sense_emu import SenseHat

import time
import thingspeak
import decimal

sense = SenseHat()
sense.clear()

while True:
    print (sense.get_temperature())
    print (sense.get_pressure())
    print (sense.get_humidity())
    print ("-")
    
    time.sleep(5)