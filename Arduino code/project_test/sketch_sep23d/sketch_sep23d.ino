#include <LiquidCrystal.h>
#include <Servo.h> //서보모터 라이브러리
#include "pitches.h"
LiquidCrystal lcd(13, 12, 11, 10, 9, 8);
Servo myservo;
int password, input;
int melody[] = {
  NOTE_C4, NOTE_G3, NOTE_G3, NOTE_A3, NOTE_G3, NOTE_B3, NOTE_C4
};
int noteDurations[] = {
  4,8,8,4,4,4,4,4
};
void setup() {
 Serial.begin(9600);
  pinMode(6, OUTPUT);
  pinMode(5, OUTPUT);
  lcd.begin(16,2);
  myservo.attach(7);
  myservo.write(0); //서보모터 초기값 0도
  password = 1234;
  lcd.begin(16,2);
  lcd.print("LOCK ");
  Serial.println("LOCK");
  myservo.write(0);
  delay(1000);
  digitalWrite(6, LOW);
  digitalWrite(5, HIGH);
}

void loop() {
  if(Serial.available()>0)
  {
    input = Serial.parseInt();
    Serial.println(input);
    if(input == password) {
      for ( int thisNote = 0; thisNote < 8; thisNote++) {
        int noteDuration = 1000/ noteDurations[thisNote];
        tone(4, melody[thisNote], noteDurations);
        int pauseBetweenNotes = noteDuration * 1.30;
        delay(pauseBetweenNotes);
        noTone(4);
      }
      digitalWrite(6, HIGH);
    digitalWrite(5, LOW);
    Serial.println("UNLOCK");
    lcd.setCursor(0,0);
    lcd.print("UNLOCK");
    lcd.setCursor(0,1);
    lcd.print("WELCOME");
    myservo.write(90);
    delay(5000);

    tone(8,800,500);
    delay(500);
    noTone(8);
    delay(500);
    digitalWrite(6, LOW);
    digitalWrite(5, HIGH);
    lcd.setCursor(0,0);
    lcd.print("LOCK");
    lcd.setCursor(0,1);
    lcd.print(" ");
    myservo.write(0);
    Serial.println("LOCK");
    }
    else{
      digitalWrite(6, LOW);
    digitalWrite(5, HIGH);
    lcd.setCursor(0,0);
    lcd.print("WRONG NUMBER");
    lcd.setCursor(0,1);
    lcd.print("LOCK");
    tone(8,300,500);
    delay(500);
    noTone(8);
    delay(500);
    myservo.write(0);
    delay(1000);
    }
  }
}
