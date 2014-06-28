#include "Arduino.h"
class Ultrasonic {
  public:
    Ultrasonic(int pin);
    void DistanceMeasure(void);
    long microsecondsToCentimeters(void);
    long microsecondsToInches(void);
  private:
    int _pin;//pin number of Arduino that is connected with SIG pin of Ultrasonic Ranger.
    long duration;// the Pulse time received;
};

Ultrasonic::Ultrasonic(int pin) {
  _pin = pin;
}


void Ultrasonic::DistanceMeasure(void) {
  pinMode(_pin, OUTPUT);
  digitalWrite(_pin, LOW);
  delayMicroseconds(2);
  digitalWrite(_pin, HIGH);
  delayMicroseconds(5);
  digitalWrite(_pin,LOW);
  pinMode(_pin,INPUT);
  duration = pulseIn(_pin,HIGH);
}

long Ultrasonic::microsecondsToCentimeters(void) {
  return duration/29/2;	
}

Ultrasonic ultrasonic(7);

void setup() {
 Serial.begin(9600);
}

void loop() {
  long RangeInCentimeters;
  ultrasonic.DistanceMeasure();
  RangeInCentimeters = ultrasonic.microsecondsToCentimeters();
  Serial.println(RangeInCentimeters);
  delay(100);
}
