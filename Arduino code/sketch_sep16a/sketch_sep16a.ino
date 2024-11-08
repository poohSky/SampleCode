#include <SoftwareSerial.h>
SoftwareSerial BTSerial(2, 3);
void setup()
{
  BTSerial.begin(115200);
  Serial.begin(9600);
}
void loop()
{
  char c;
  if ( BTSerial.available() ) {
    c = BTSerial.read();
    if ( c == 'a') {
      digitalWrite(13, HIGH);
      BTSerial.println("LED ON");
    } 
    else {
      digitalWrite(13, LOW);
      BTSerial.println("LED OFF");
    }
  }
}
