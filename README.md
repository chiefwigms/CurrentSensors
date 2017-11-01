# CurrentSensors
CurrentSensor Plugin for CraftBeerPi 3.0

This plugin reads JSON formatted Current Sensor data from a serial port.

Serial Port data comes from an Arudino that uses EmonLib to monitor current for both 240V and 120V inputs - the Arduino Sketch is below:


#include "EmonLib.h"                   // Include Emon Library
EnergyMonitor emon240, emon120;        // Create an instance

void setup()
{ 
  analogReadResolution(12);
  for (int i = A0; i <= A11; i++)
  {
    if (i == A0 || i == A2)
    {
      pinMode(i, INPUT_PULLUP);
    }
    else
    {
      pinMode(i, OUTPUT);
      digitalWrite(i, LOW);
    }
  }
 
  Serial.begin(115200);
 
  delay(1000);
 
  emon240.current(0, 30);             // Current: input pin, calibration.
  emon120.current(2, 30);             // Current: input pin, calibration.
}

void loop()
{
  double Irms240 = emon240.calcIrms(1480);  // Calculate Irms only
  double Irms120 = emon120.calcIrms(1480);  // Calculate Irms only

  //JSON
  Serial.print("{\"CurrentSensors\":[{");
  Serial.print("\"240V\":\"");
  Serial.print(Irms240);
  Serial.print("\",");
  Serial.print("\"120V\":\"");
  Serial.print(Irms120);
  Serial.print("\"");
  Serial.print("}]}");
  Serial.println();
  delay(1000);
}

