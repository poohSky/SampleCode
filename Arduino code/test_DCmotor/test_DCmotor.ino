int motorPin = 11;
int pushButton1= 8;
int pushButton2= 9;
int pushButton3= 10;
int i = 0;
 
void setup() 
{ 
  pinMode(motorPin, OUTPUT);
  pinMode(pushButton1, INPUT_PULLUP);
  pinMode(pushButton2, INPUT_PULLUP);
  pinMode(pushButton3, INPUT_PULLUP);
  Serial.begin(9600);
  while (! Serial);
} 
 
void loop() 
{ 
  pushButton1 = digitalRead(8);
  pushButton2 = digitalRead(9);
  pushButton3 = digitalRead(10);
  
  if (pushButton1==0) {
      i += 10;
      analogWrite(motorPin,i);
      delay(50);
  }
 if (pushButton2==0) {
      i -= 10;
      analogWrite(motorPin,i);
      delay(50);
  }
  if (pushButton3==0) {
      i = 0;
      analogWrite(motorPin,i);
      delay(50);
  }
  if(i>255) {
    i=0;
    delay(50);
  }
  if(i<0) {
    i=255;
    delay(50);
  }
} 
  
