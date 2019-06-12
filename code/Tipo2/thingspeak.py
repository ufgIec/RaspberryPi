from sense_emu import SenseHat
import time
import thingspeak

# Coloque nessa variavel a ID do seu canal
iot_id = "763969"

# Coloque nessa variavel a chave da escrita do seu canal
iot_key = "dsafsd"

iot_chn = thingspeak.Channel(iot_id, iot_key)

sense = SenseHat()
sense.clear()
sense.show_message("Ola mundo IoT!")

while True:
    temp = sense.get_temperature()
    humid = sense.get_humidity()
    payload = {
        'field1' : temp,
        'field2' : humid
    }
    print("Temperatura: " + str(temp))
    print("Umidade: " + str(humid))
    if (iot_chn.update(payload)):
        print("Dados enviados para nuvem!")
    else:
        print("Falha ao enviar dados...")
    print("----------------------")
    time.sleep(15)
