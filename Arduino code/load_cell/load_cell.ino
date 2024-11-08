#include "Hx711.h"
Hx711 scale(A2, A3);

void  setup() {
  Serial.begin(9600);
}
void loop(){
  float nZero,nLoad;

  nZero = 3800;
  nLoad = 2758000;

  Serial.println((scale.getValue()-nZero) / ( (nLoad-nZero) /20 ),3);
  delay(1);
 }

