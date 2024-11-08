#include <LiquidCrystal.h>
#include <Password.h> //비밀번호 설정 라이브러리
#include <Servo.h> //서보모터 라이브러리
LiquidCrystal lcd(13, 12, 11, 10, 9, 8);
Servo ser;

Password password = Password( "121" ); //비밀번호 설정
int button[2] = {5, 6}; //버튼 핀 연결
int buttonState[2] = {0, 0};
int prevState[2] = {0, 0};
int number[3] = {0, 0, 0};
int sensor = 2;
int k;
char input;
char count;
int state1 = 0;
int state2 = 0;
int prevState1 = 0;
int prevState2 = 0;
byte currentLength = 0;
int buttonState1 = 0;

float distanceCheck()
{
  int sensorValue= analogRead(A0);
  float distance = 12343.85 * pow( sensorValue, -1.15);
  if (distance < 10 ) {
  return 10;
  } else if ( distance > 80 ) {
  return 80;
  } else {
  return distance;
  }
}

void setup() {
  for (int i=0; i<=3; i++) {
     pinMode(button[i], INPUT);
   }
  pinMode(sensor, INPUT);
  lcd.begin(16,2);
  ser.attach(7);
}

void loop() {
  float distance = distanceCheck();
  lcd.clear();
  lcd.setCursor(0,1);
  lcd.print("password : "); //lcd에 불이 켜지고 'password : '라는 문구 출력
  buttonState1 = digitalRead(sensor);
  for (int j=0; j<=3; j++) {
     buttonState[j] = digitalRead(button[j]);
   }
   for (k=0; k<=3; k++) {
     if (buttonState[k] != prevState[k]) {
       if (buttonState[k] == 1) {
         input = k+1;
         password.append(input);
         currentLength++;
         for (byte p=0; p<currentLength; p++) {
          lcd.setCursor(0,0);
           lcd.print("distance : "); //lcd에 불이 켜지고 'distance : '라는 문구 출력
           lcd.println(distance);   //거리값 출력
           lcd.setCursor(0,1);
           lcd.print("password : "); //lcd에 불이 켜지고 'password : '라는 문구 출력
           lcd.print('*');
         }
       }
       else {
       }
     prevState[k] = buttonState[k];
     delay(20);
     }
   } //비밀번호 함수

   if (buttonState1 != prevState1) {
     if (buttonState1 == 1) {
       state1 = 1;
     }
     else {
       state1 = 0;
     }
     prevState1 = buttonState1;
   } //터치센서1 디바운싱
   
  if (sensor) {
     if (password.evaluate()){
       lcd.clear();
       lcd.setCursor(0, 1);
       lcd.print("guessed!");
       ser.write(90);
       password.reset();
       delay(3000);
       lcd.clear();
       ser.write(0);
       currentLength = 0;
     }
     else  {
       lcd.clear();
       lcd.setCursor(0, 1);
       lcd.print("wrong!");
       password.reset();
       delay(3000);
       lcd.clear();
       currentLength = 0;
     }
   } //터치센서1이 입력되면 입력된 비밀번호가 맞는지 비교
}

