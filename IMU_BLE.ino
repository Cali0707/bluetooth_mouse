#include <ArduinoBLE.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>


#define BNO055_SAMPLERATE_DELAY_MS (100)

Adafruit_BNO055 bno = Adafruit_BNO055(55, 0x28);
 // BLE Service
BLEService imuService("5c8e3119-d78e-4197-8a81-e7037b3ce16"); // Custom UUID

// BLE Characteristic
BLECharacteristic imuCharacteristic("6b90ba69-3581-4c91-9614-ccc1d2178103", BLERead | BLENotify, 12);

long previousMillis = 0;  // last timechecked, in ms

void setup() {
  Serial.begin(115200);    // initialize serial communication

  pinMode(LED_BUILTIN, OUTPUT); // initialize the built-in LED pin to indicate when a central is connected

// begin initialization
  
  if(!bno.begin())
  {
    /* There was a problem detecting the BNO055 ... check your connections */
    Serial.print("Ooops, no BNO055 detected ... Check your wiring or I2C ADDR!");
    while(1);
  }
  
  
  if (!BLE.begin()) {
    Serial.println("starting BLE failed!");
    while (1);
  }
  bno.setExtCrystalUse(true);

  // Setup bluetooth
  BLE.setLocalName("3dMouse");
  BLE.setAdvertisedService(imuService); 
  imuService.addCharacteristic(imuCharacteristic);
  BLE.addService(imuService); 
  
  // start advertising
  BLE.advertise();
  Serial.println("Bluetooth device active, waiting for connections...");
  Serial.println("Device name:");
}


// send IMU data
void sendSensorData() {

  sensors_event_t event; 
  bno.getEvent(&event);
// read acceleration x, y and z

  float distance[3] = {event.acceleration.x, event.acceleration.y, event.acceleration.z};
// Send 3x acceleration over bluetooth as 1x byte array
  imuCharacteristic.setValue((byte *) &distance, 16); 

} 

void loop() {
  // wait for a BLE central
  BLEDevice central = BLE.central();

  // if a BLE central is connected to the peripheral:
  if (central) {
    Serial.print("Connected to central: ");
    // print the central's BT address:
    Serial.println(central.address());
    // turn on the LED to indicate the connection:
    digitalWrite(LED_BUILTIN, HIGH);

    // while the central is connected:
    while (central.connected()) {
      long currentMillis = millis();

      if (currentMillis - previousMillis >= 50) {
        previousMillis = currentMillis;
        sendSensorData();
          
      }
    }
    // when the central disconnects, turn off the LED:
    digitalWrite(LED_BUILTIN, LOW);
    Serial.print("Disconnected from central: ");
    Serial.println(central.address());
  }
}
