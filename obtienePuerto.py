import serial

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
    # Mostra el puerto donde esta el arduino
    print('el puerto del arduino es: ' + 'COM' + str(iPuerto))
else:
    # Si no lo encuentra, muestra el mensaje de no encontrado
    print('No se ha encontrado Ardunio')
