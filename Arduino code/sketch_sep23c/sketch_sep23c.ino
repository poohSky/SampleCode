#include <EEPROM.h>
#include <LiquidCrystal.h>
#include <Servo.h> //서보모터 라이브러리
#include "pitches.h"
LiquidCrystal lcd(13, 12, 11, 10, 9, 8);
Servo ser;
int thousand, hundred, ten, one, password, input;
int melody[] = {
  NOTE_C4, NOTE_G3, NOTE_G3, NOTE_A3, NOTE_G3, NOTE_B3, NOTE_C4
};
int noteDurations[] = {
  4,8,8,4,4,4,4,4
};
void setup() {
 Serial.begin(9600);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  lcd.begin(16,2);
  ser.attach(7);
  ser.write(0); //서보모터 초기값 0도
  thousand = 1000* EEPROM.read(0)
  hundred = 100* EEPROM.read(1)
  ten = 10* EEPROM.read(2)
  one = 1* EEPROM.read(3)
  password = thousand+hundred+ten+one;
  lcd.begin(16,2);
  lcd.print("LOCK ");
  myservo.write(0);
  delay(1000);
  digitalWrite(6, LOW);
  digitalWrite(7, HIGH);
}

void loop() {
  if(Serial.available()>0)
  {
    inpit = Serial.parselnt();
    Serial.println(input);
    if(input == password) {
      for ( int thisNote = 0; thisNote < 8; thisNote++) {
        int noteDurations = 1000/ noteDurations[thisnote];
        tone(8; melody[thisNOte], noteDurations);
        int pauseBetweenNotes = noteDurations * 1.30;
        delay(pauseBetweenNotes);
        noTone(8);
      }
      digitalWrite(6, HIGH);
    digitalWrite(7, LOW);
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
    digitalWrite(7, HIGH);
    lcd.setCursor(0,0);
    lcd.print("LOCK");
    lcd.setCursor(0,1);
    lcd.print(" ");
    myservo.write(0);
    }
    else{
      digitalWrite(6, LOW);
    digitalWrite(7, HIGH);
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
