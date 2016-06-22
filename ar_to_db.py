#!/usr/bin/env python
#!/usr/bin/python
# coding: utf-8

#Se esta utilizando el siguiente tipo de cURL
#curl -X POST -d '{ "fecha": "15/06/2016", "referencia": "humedad", "valor": "" }' \
#https://proyard2.firebaseio.com/humedad.json
#

import serial
#import pycurl
import json
import certifi
import datetime
import time
import requests

fecha = datetime.date.today().strftime('%Y-%m-%d')
ser = serial.Serial('COM5')
lectura = ''
hora = datetime.datetime.now().time().strftime("%H:%M:%S")
url_m = "https://proyard2.firebaseio.com/movimiento/"+fecha+".json"
url_h = "https://proyard2.firebaseio.com/humedad/"+fecha+".json"
url_t = "https://proyard2.firebaseio.com/temperatura/"+fecha+".json"

while True:
	#print ser.read(20)
	lectura = ser.read(13).split(",")

	print lectura
	for x in lectura:
		
		
		r_m = requests.post(url_m, data = json.dumps({ "referencia": "movimiento", "valor":lectura[0], "hora": hora, "fecha": fecha}))
		r_h = requests.post(url_h, data = json.dumps({ "referencia": "humedad", "valor":lectura[1], "hora": hora, "fecha": fecha}))
		r_t = requests.post(url_t, data = json.dumps({ "referencia": "temperatura", "valor":lectura[2], "hora": hora, "fecha": fecha}))
		
		#print ("M: " + str(r_m.status_code))
		#print ("H: " + str(r_h.status_code))
		#print ("T: " + str(r_t.status_code))
