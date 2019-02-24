#include<LoRa.h>
#include<SPI.h>
void setup(){
  pinMode(A0,INPUT);
 pinMode(13,OUTPUT);
 digitalWrite(13,LOW);
 Serial.begin(9600);
 
}
void loop() {
   int  counter=0;


  Serial.print("Sending packet: ");
  Serial.println(counter);

  // send packet
  LoRa.beginPacket();
  
  
  

  counter++;

  delay(5000);
  int sens_val=analogRead(A0);
Serial.println(analogRead(A0));
delay(1000);
if(sens_val>500)
{
digitalWrite(13,HIGH);
delay(1000);
}

else
digitalWrite(13,LOW);

LoRa.print(sens_val);
LoRa.endPacket();
}
