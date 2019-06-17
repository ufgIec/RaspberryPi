from sense_emu import SenseHat
from urllib.request import urlopen

import time
import decimal

sense = SenseHat()
sense.clear()
sense.show_message("Olaaá mundo!")

while True:
    temp = sense.get_temperature()
    temp = round(temp,1)
    
    data = urlopen ("https://api.thingspeak.com/update?api_key=X1BUDYJZMO07DBO8&field1=0"+str(temp))
    
    
    pres = sense.get_pressure()
    pres = round(pres,1)
    
    data = urlopen ("https://api.thingspeak.com/update?api_key=X1BUDYJZMO07DBO8&field2=0"+str(pres))
    
    
    umid = sense.get_humidity()
    umid = round(umid,1)
    
    data = urlopen ("https://api.thingspeak.com/update?api_key=X1BUDYJZMO07DBO8&field3=0"+str(umid))

    
    print("Temperatura: " + str(temp)+" C")
    print("    Umidade: " + str(umid)+" %")
    print("    Pressão: " + str(pres) +" bar")
    print("---------------------")
    time.sleep(5)
    
    
