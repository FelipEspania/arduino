#include "DHT.h"
#define DHTPIN 4
#define DHTTYPE DHT11

DHT dht(DHTPIN,DHTTYPE);

void setup()
{
  Serial.begin(9600);
  pinMode(2,INPUT);//movimiento
  pinMode(4,INPUT);//temp y hum
  pinMode(A1,INPUT);//humo
  
  dht.begin();
}

void loop()
{
  if(digitalRead(2) == HIGH)
  { 
    Serial.println("Movimiento Detectado");
    Serial.print("Humedad: ");
    Serial.println(dht.readHumidity());
    Serial.print("Temperatura: ");
    Serial.println(dht.readTemperature());
    Serial.print("Gases: ");
    Serial.println(analogRead(6));
  }
  else
  {
    Serial.println("Sin Movimiento");
  }
  
  
  
  delay(1000);
}
