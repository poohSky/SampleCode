#include <LiquidCrystal.h>
#include <Servo.h> //서보모터 라이브러리
LiquidCrystal lcd(13, 12, 11, 10, 9, 8);
Servo myservo;

float distanceCheck()
{
  int sensorValue= analogRead(A0);
  float distance = 12343.85 * pow( sensorValue, -1.15);
  if (distance < 10 ) {
  return 10;
  } else if ( distance > 100 ) {
  return 100;
  } else {
  return distance;
  }
}

void setup() {
  //pinMode(pushButtonPin, INPUT);
  //attachInterrupt(0, buttonRead, RISING);
  Serial.begin(9600);
  lcd.begin(16,2);
  ser.attach(7);
  ser.write(0); //서보모터 초기값 0도
}

void loop() {
  float distance = distanceCheck();
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("distance : "); //lcd에 불이 켜지고 'distance : '라는 문구 출력
  lcd.println(distance);   //거리값 출력
  lcd.setCursor(0,1);
  lcd.print("password : "); //lcd에 불이 켜지고 'password : '라는 문구 출력
  delay(300);
  if(distance<=30)
  {
    ser.write(90);
} else {
  for( int angle = ser.read(); angle >= 0 ; angle--) {
    ser.write(angle);
    delay(20);
}
  }
}


