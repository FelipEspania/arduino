#!/usr/bin/python
# coding: utf-8

import serial
import MySQLdb

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = ''
DB_NAME = 'mydb'

# DB_HOST = '192.168.43.31'
# DB_USER = 'root'
# DB_PASS = ''
# DB_NAME = 'mydb'


ser = serial.Serial('/dev/ttyACM0')
valoresArd = ser.read(17)

# humedad = int(valoresArd[0:2])
temperatura = int(valoresArd[6:8])
gases = int(valoresArd[12:15])

# print(humedad)
# print(temperatura)
# print(gases)

refTemp = ''
refGas = ''

if temperatura < 10:
    refTemp = 'mucho frio'
elif temperatura < 20 and temperatura >= 10:
    refTemp = 'frio'
elif temperatura > 26 and temperatura <= 29:
    refTemp = 'calor'
elif temperatura >= 30:
    refTemp = 'mucho calor'
else:
    refTemp = 'agradable'

if gases <= 200:
    refGas = 'Gas xxx'
elif gases >= 201 and gases <= 400:
    refGas = 'Gas yyy'
else:
    refGas = 'Gas zzz'

# print(refTemp)

def setTemperatura(temperatura, refTemp):
    query="insert into temperatura (valor,timestamp,referencia) values ("+str(temperatura)+",current_timestamp(),'"+refTemp+"');"
    datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]
    conn = MySQLdb.connect(*datos) # Conectar a la base de datos
    cursor = conn.cursor()         # Crear un cursor
    cursor.execute(query)          # Ejecutar una consulta

    conn.commit()              # Hacer efectiva la escritura de datos
    cursor.close()             # Cerrar el cursor
    conn.close()               # Cerrar la conexión

setTemperatura(temperatura, refTemp)

def setMovimiento():
    query="insert into movimiento (valor,timestamp,referencia) values (1,current_timestamp(),'Movimiento Detectado');"
    # query = query + " insert into movimiento (valor,timestamp,referencia) values (1,current_timestamp(),'Movimiento Detectado');"
    datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]
    conn = MySQLdb.connect(*datos) # Conectar a la base de datos
    cursor = conn.cursor()         # Crear un cursor
    cursor.execute(query)          # Ejecutar una consulta

    conn.commit()              # Hacer efectiva la escritura de datos
    cursor.close()             # Cerrar el cursor
    conn.close()               # Cerrar la conexión

setMovimiento()

def setGases(gases, refGas):
    query="insert into humo (valor,timestamp,referencia) values ("+str(gases)+",current_timestamp(),'"+refGas+"');"
    # query = query + " insert into movimiento (valor,timestamp,referencia) values (1,current_timestamp(),'Movimiento Detectado');"
    datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]
    conn = MySQLdb.connect(*datos) # Conectar a la base de datos
    cursor = conn.cursor()         # Crear un cursor
    cursor.execute(query)          # Ejecutar una consulta

    conn.commit()              # Hacer efectiva la escritura de datos
    cursor.close()             # Cerrar el cursor
    conn.close()               # Cerrar la conexión

setGases(gases, refGas)
