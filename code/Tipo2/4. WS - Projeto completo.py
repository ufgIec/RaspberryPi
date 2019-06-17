from sense_emu import SenseHat
import time
import thingspeak

#id do seu canal no thingspeak
iec_id = "798893"

#a chave de escrita do seu canal no thingspeak
iec_key = "X1BUDYJZMO07DBO8"

#cadeia com as variáveis para verificação do envio
iec_chn = thingspeak.Channel(iec_id, iec_key)

sense = SenseHat()
sense.clear()
sense.show_message("Ola mundo IoT!")

while True:
    temp = sense.get_temperature()
    pres = sense.get_pressure()
    umid = sense.get_humidity()
    
    payload = {'field1': temp, 'field2': pres, 'field3': umid}
    print("Temperatura: "+str(temp))
    print("    Pressão: "+str(pres))
    print("    Umidade: "+str(umid))
    
    if (iec_chn.update(payload)):
        print("Dados enviados com sucesso para a Nuvem! :)")
        print("")
    else:
        print("Falha ao enviar os dados para a Nuvem! :(")
    
    time.sleep(15)    

    
