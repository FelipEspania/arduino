#include "DHT.h"
#define DHTPIN 2
#define DHTTYPE DHT11

DHT dht(DHTPIN,DHTTYPE);

void setup()
{
  Serial.begin(9600);
  pinMode(2,INPUT);
  dht.begin();
}
void loop()
{
  delay(1000);
  Serial.print("Humedad: ");
  Serial.println(dht.readHumidity());
  Serial.print("Temperatura: ");
  Serial.println(dht.readTemperature());
}
