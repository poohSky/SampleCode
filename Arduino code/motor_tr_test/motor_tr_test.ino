int motorPin = 3;
int pushButton1= 8;
int pushButton2= 9;
int pushButton3= 10;

void setup() 
{ 
  pinMode(motorPin, OUTPUT);
  pinMode(pushButton1, INPUT_PULLUP);
  pinMode(pushButton2, INPUT_PULLUP);
  pinMode(pushButton3, INPUT_PULLUP);
  Serial.begin(9600);
  while (! Serial);
  Serial.println("Speed 100 to 255");
} 
 
void loop() 
{ 
  if (Serial.available())
  {
      pushButton1 = digitalRead(8);
     pushButton2 = digitalRead(9);
     pushButton3 = digitalRead(10);
    int i = Serial.parseInt();
    if (pushButton1==0) {
      i += 10;
      analogWrite(motorPin,i);
      Serial.println(i);
      delay(50);
     }
    if (pushButton2==0) {
      i -= 10;
      analogWrite(motorPin,i);
      Serial.println(i);
      delay(50);
     }
    if (pushButton3==0) {
      i = 0;
      analogWrite(motorPin,i);
      Serial.println(i);
      delay(50);
      }
   if(i>255) {
    i=0;
    Serial.println(i);
    delay(50);
     }
    if(i<0) {
    i=255;
    Serial.println(i);
    delay(50);
   }
  }
}
