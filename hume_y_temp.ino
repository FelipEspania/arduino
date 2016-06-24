#include <DHT.h>
#define DHTPIN 2
#define DHTTYPE DHT11

DHT dht(DHTPIN,DHTTYPE);
int movimiento = 0;
int humo = 0;

void setup()
{
  Serial.begin(9600);
  pinMode(2,INPUT);
  pinMode(4,INPUT);
  pinMode(7,INPUT);
  dht.begin();
}
void loop()
{
  if(digitalRead(4) == HIGH)
  {
    movimiento = 1;
  }
  if(digitalRead(7) == HIGH)
  {
    humo = 1;
  }
  Serial.print(movimiento);
  Serial.print(",");
  Serial.print(humo);
  Serial.print(",");
  Serial.print(dht.readHumidity());
  Serial.print(",");
  Serial.print(dht.readTemperature());
  delay(1000);
  
  movimiento = 0;
  humo = 0;
}
