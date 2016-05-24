// Codigo Fuente para plaqueta Arduino para simular el funcionamiento de un semaforo
// con pulsador para peatones
// Libre distribucion
// Cualquier consulta a Twitter --> @santiagosony

// Definiciones para evitar usar memoria con variables
#define VERDE 1
#define AMARILLOaROJO 2
#define AMARILLOaVERDE 3
#define ROJO 4

// Variables globales
const unsigned int tiempoRojo = 10000;         // 10 segundos
const unsigned int tiempoAmarillo = 1500;     // 1.5 segundos
const unsigned int tiempoVerde = 6000;        // 6 segundos
unsigned long varTiempo;
int colorActual;
int botonActivo = true;
unsigned long tiempoBoton;
unsigned long tiempoBotonParpadeo;

// Numero de pin de los leds
const int ledRojo = 12;
const int ledAmarillo = 11;
const int ledVerde = 10;
const int ledBoton = 13;
const int boton = 5;

void setup(void) {
  // Seteo los LEDs
  pinMode(ledRojo, OUTPUT);
  pinMode(ledAmarillo, OUTPUT);
  pinMode(ledVerde, OUTPUT);
  pinMode(ledBoton, OUTPUT);
  
  // Seteo el boton
  pinMode(boton, INPUT);
  
  // Inicio el semaforo (en ROJO)
  iniciaSemaforo();
  
  // Inicio el LED del boton
  digitalWrite(ledBoton, LOW);
  
  return;
}

void loop(void) {
  // Controlo los colores del semaforo
  controlSemaforo();
  
  // Controlo si se presiono el boton
  controlBoton();
}

void iniciaSemaforo(void) {
  digitalWrite(ledRojo, HIGH);
  digitalWrite(ledAmarillo, LOW);
  digitalWrite(ledVerde, LOW);
  colorActual = ROJO;
  varTiempo = millis();
  
  return;
}

void controlSemaforo(void) {
  
  if (colorActual == VERDE && tiempoConmutacion(tiempoVerde) ) {
    digitalWrite(ledVerde, LOW);
    digitalWrite(ledAmarillo, HIGH);
    varTiempo = millis();
    colorActual = AMARILLOaROJO;
  }
  else if (colorActual == AMARILLOaROJO && tiempoConmutacion(tiempoAmarillo) ) {
    digitalWrite(ledAmarillo, LOW);
    digitalWrite(ledRojo, HIGH);
    varTiempo = millis();
    colorActual = ROJO;
  }
  else if (colorActual == ROJO && tiempoConmutacion(tiempoRojo) ) {
    digitalWrite(ledAmarillo, HIGH);
    digitalWrite(ledRojo, LOW);
    varTiempo = millis();
    colorActual = AMARILLOaVERDE;
  }
  else if (colorActual == AMARILLOaVERDE && tiempoConmutacion(tiempoAmarillo) ) {
    digitalWrite(ledAmarillo, LOW);
    digitalWrite(ledVerde, HIGH);
    varTiempo = millis();
    colorActual = VERDE;
  }
  
  return;
}

int tiempoConmutacion(unsigned int tiempoColor)
{
  if ( (millis() - varTiempo) >= tiempoColor)
    return 1;
  else
    return 0;
}

void controlBoton(void)
{
  if ( (digitalRead(boton) == LOW) && botonActivo) {
    digitalWrite(ledBoton, HIGH);
    tiempoBoton = millis();
    tiempoBotonParpadeo = tiempoBoton;
    semaforoArojo();
    botonActivo = false; // Una vez que tomo que presione el boton, desactivo su funcionamiento por un tiempo
  }
  else {
    parpadeoLedBoton();
    if ( (millis() - tiempoBoton) > (tiempoRojo*2) ) {  // Espero 2 tiempos rojos antes de volver a habilitar el boton de cruce peaton
      botonActivo = true;
      digitalWrite(ledBoton, LOW);
    }
  }
    
  return;
}

void parpadeoLedBoton(void)
{
  if (!botonActivo) {
    if ( (millis() - tiempoBotonParpadeo) >= 500) { // Mientras el boton esta desactivado titilo el LED del pin 13 cada medio segundo
      tiempoBotonParpadeo = millis();
      if (digitalRead(ledBoton) == HIGH)
        digitalWrite(ledBoton, LOW);
      else
        digitalWrite(ledBoton, HIGH);
    }
  }
  
  return;
}

void semaforoArojo(void)
{
  if (colorActual == VERDE) {
    if ( (millis() - tiempoVerde) > 0) // Evito guardar (mas abajo en el codigo) un negativo en una variable unsigned
      varTiempo = (millis() - tiempoVerde); // Es el tiempo del verde, hago que el sistema piense que ya paso el tiempo para estar en VERDE y conmute a AMARILLO y luego a ROJO
  }   // Nunca deberia pasar la condicion del ELSE ya que arranca en ROJO, cuando llega al VERDE el contador deberia soportar la resta sin dar negativo
  else if (colorActual == ROJO)
    varTiempo = millis(); // Reinicio el contador de tiempo del rojo
  else if (colorActual == AMARILLOaVERDE) 
    colorActual = AMARILLOaROJO; // Le hago volver para el rojo
 
 return; 
}
