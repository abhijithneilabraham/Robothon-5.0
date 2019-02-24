
#include <SPI.h>
#include <LoRa.h>

int counter = 0;

void setup() {
  pinMode(A0,INPUT);
 pinMode(13,OUTPUT);
 digitalWrite(13,LOW);
  Serial.begin(9600);
  while (!Serial);

  Serial.println("LoRa Sender");

  if (!LoRa.begin(915E6)) {
    Serial.println("Starting LoRa failed!");
    while (1);
  }
}

void loop() {
  Serial.print("Sending packet: ");
  Serial.println(counter);
  
  int sens_val=analogRead(A0);
  Serial.println(sens_val);
  
  // send packet
  LoRa.beginPacket();
  
  
  LoRa.print(counter);
  LoRa.print(sens_val);
  LoRa.endPacket();

  counter++;

  delay(5000);
}
