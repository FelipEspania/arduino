byte sensor = 7;
byte led = 13;

void setup() {
  // put your setup code here, to run once:
  pinMode(sensor, INPUT);
  pinMode(led, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(digitalRead(sensor) == HIGH)
  {
    Serial.println("Detectando movimiento");
    digitalWrite(led, HIGH);
    delay(1000);
    digitalWrite(led, LOW);
  }
}
