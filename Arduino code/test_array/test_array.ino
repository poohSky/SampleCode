char data[7];

void setup()
{
    Serial.begin(9600);
    data[5]=4;
    data[6]=5;
}
void loop()
{int datahap = 0;
    datahap = data[5];
    datahap = datahap <<8;
    datahap = datahap + data[6];
    Serial.println(datahap,BIN);
    Serial.println(datahap,HEX);
    Serial.println(datahap,DEC);
    delay(3000);
}
