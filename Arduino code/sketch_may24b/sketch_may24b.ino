int ledPins[]={7,8};    // 배열을 이용하여, ledPins[0] = 7 , ledPins[1] = 8 번의 핀 넘버를 설정하였다.

void blick3()
{
   for(int index=0;index<2;index++)
 {
   digitalWrite(ledPins[index],HIGH);       // ledPins[0] 값에 HIGH (즉,1) 입력. 
   delay(1000);                              // 1000ms 동안 현 상태 유지.
   digitalWrite(ledPins[index],LOW);       // ledPins[0] 값에 LOW (즉,0)입력.
   delay(1000);                              // 1000ms 동안 현 상태 유지.
 }
}

void setup()
{
 for(int index=0;index<2;index ++)
 {
   pinMode(ledPins[index],OUTPUT);    // ledPins[0]과 ledPins[1] 의 Mode 설정. OUTPUT !!
 }
 Serial.begin(9600);      // 시리얼 포트 초기화 ( 나중에 자세하게 공부하도록 한다.)
}

void loop()
{
  blick3();       // 함수 호출

}
