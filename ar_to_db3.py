#!/usr/bin/env python
#!/usr/bin/python
# coding: utf-8

#Se esta utilizando el siguiente tipo de cURL
#curl -X POST -d '{ "fecha": "15/06/2016", "referencia": "humedad", "valor": "" }' \
#https://proyard2.firebaseio.com/humedad.json

import serial
#import pycurl
import json
import certifi
import datetime
import time
import requests

bEncontrado = False

for iPuerto in range(0, 9):
    try:
        # Puerto que voy a probar
        PUERTO = 'COM' + str(iPuerto)
        # Velocidad
        VELOCIDAD = '9600'
        # Intento abrir el puerto
        Arduino = serial.Serial(PUERTO, VELOCIDAD)
        # si no se ha producido un error, cierro el puerto
        Arduino.close()
        # cambio el estado del la variable para saber si lo he encontrado
        bEncontrado = True
        # Salgo del bucle
        break
    except:
        # Si hay error, no hace nada y continua con la busqueda
        pass

if bEncontrado:

	fecha = datetime.date.today().strftime('%Y-%m-%d')
	ser = serial.Serial(PUERTO)
	lectura = ''
	hora = datetime.datetime.now().time().strftime("%H:%M:%S")
	url_m = "https://proyard2.firebaseio.com/movimiento/"+fecha+".json"
	url_h = "https://proyard2.firebaseio.com/humedad/"+fecha+".json"
	url_t = "https://proyard2.firebaseio.com/temperatura/"+fecha+".json"
	url_hu = "https://proyard2.firebaseio.com/gases/"+fecha+".json"
	valor_ant_t = ''
	valor_ant_h = ''

	while True:
		#print ser.read(20)
		lectura = ser.read(15).split(",")

		print lectura
		for x in lectura:
			if lectura[0] == '1':
				r_m = requests.post(url_m, data = json.dumps({ "referencia": "movimiento", "valor":lectura[0], "hora": hora, "fecha": fecha}))
			
			if lectura[1] == '1':
				r_hu = requests.post(url_hu, data = json.dumps({ "referencia": "gas", "valor":lectura[1], "hora": hora, "fecha": fecha}))

			if valor_ant_h != lectura[2]:
				r_h = requests.post(url_h, data = json.dumps({ "referencia": "humedad", "valor":lectura[2], "hora": hora, "fecha": fecha}))
				#print ("H: " + str(r_h.status_code))
				valor_ant_h = lectura[2]

			if valor_ant_t != lectura[3]:
				r_t = requests.post(url_t, data = json.dumps({ "referencia": "temperatura", "valor":lectura[3], "hora": hora, "fecha": fecha}))
				#print ("T: " + str(r_t.status_code))
				valor_ant_t = lectura[3]

			#if lectura[0] == '1':

			#print ("M: " + str(r_m.status_code))
			#print ("H: " + str(r_h.status_code))
			#print ("T: " + str(r_t.status_code))
		r_m = requests.post(url_m, data = json.dumps({ "referencia": "movimiento", "valor":"0", "hora": hora, "fecha": fecha}))
		r_hu = requests.post(url_hu, data = json.dumps({ "referencia": "gas", "valor":"0", "hora": hora, "fecha": fecha}))
else:
    # Si no lo encuentra, muestra el mensaje de no encontrado
    print 'No se ha encontrado Ardunio   ' + str(time.asctime(time.localtime(time.time())))

    try:
        log = open('log.txt','a')
        log.write('No se ha encontrado Ardunio   ' + str(time.asctime(time.localtime(time.time()))) + '\n')
        log.close()
    except:
        log = open('log.txt','w')
        log.write('No se ha encontrado Ardunio   ' + str(time.asctime(time.localtime(time.time()))) + '\n')
        log.close()
