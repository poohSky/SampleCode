#include "UbidotsMicroESP8266.h"

#define ID  "59bcd9f7c03f973a1e23cb56"  // Put here your Ubidots variable ID
#define TOKEN  "A1E-KT94OizDxK2v0IVdZGvOs6UQwLhtQI"  // Put here your Ubidots TOKEN
#define WIFISSID "sunmoon-402_2.4G" // Put here your Wi-Fi SSID
#define PASSWORD "sunmoon1234" // Put here your Wi-Fi password

Ubidots client(TOKEN);

void setup() {
    Serial.begin(115200);
    client.wifiConnection(WIFISSID, PASSWORD);
    //client.setDebug(true); // Uncomment this line to set DEBUG on
}

void loop() {
    float value = client.getValue(ID);
    int signalLevel = analogRead(A0);
    float voltage = signalLevel * 3.3/1024.0;
    Serial.print("Value: ");
    Serial.println(voltage, 4);
    delay(3000);
}

