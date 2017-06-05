#!/usr/bin/env python

#se o botao 24 foi pressionado
if (GPIO.input(24) == False):

    #abre um processo com a musica selecionada no index, com o mpg123
    subprocess.Popen(['mpg123', mp3_files[index]])

    print '--- Playing ' + mp3_files[index] + ' ---'
    print '--- Press button #3 to clear playing mp3s. ---'

    #sleep para nao abrir mais de um mp3 ao clicar no botao
    sleep(1)

#se o array de mp3 for vazio, retorna um erro
if not (len(mp3_files) > 0):
    print "No mp3 files found!"

#imprime todos os arquivos encontrados no diretorio
print '--- Available mp3 files ---'
print mp3_files
print '--- Press button #1 to select mp3, button #2 to play current. ---'

#variavel auxiliar para se usar no indice do vetor
index = 0

#importa bibliotecas
from os import listdir
import subprocess
from time import sleep
import RPi.GPIO as GPIO

#loop infinito
while True:

#se o botao 25 for pressionado
if (GPIO.input(25) == False):

    #termina todos processos que tiverem 'mpg123'
    subprocess.call(['killall', 'mpg123'])
    print '--- Cleared all existing mp3s. ---'
    
#sleep do loop
sleep(0.1);

#array mp3_files recebe o nome de todos arquivos mp3 do diretorio
mp3_files = [ f for f in listdir('.') if f[-4:] == '.mp3' ]

#se o botao 23 foi pressionado, 
if (GPIO.input(23) == False):
    index += 1
    if index >= len(mp3_files):
        index = 0

    #composicao de string em python            
    print "--- " + mp3_files[index] + " ---"

#seta pinos
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)
