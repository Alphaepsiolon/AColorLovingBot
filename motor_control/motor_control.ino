#include<Servo.h>

//Declaring the input pins for the 4 motors
enum MotorPin {FR1 = 46, FR2, BR1, BR2, FL1, FL2, BL1, BL2};
const int ENABLE = 12;

void setup() 
{
  //Setting all the pins to output mode. Use port register to do the same later.
  pinMode(FR1,OUTPUT);
  pinMode(FR2,OUTPUT);
  pinMode(FL1,OUTPUT);
  pinMode(FL2,OUTPUT);
  pinMode(BR1,OUTPUT);
  pinMode(BR2,OUTPUT);
  pinMode(BL1,OUTPUT);
  pinMode(BL2,OUTPUT);

  //Setting the PWM pin to OUPUT
  pinMode(ENABLE,OUTPUT);

  //Starting Serial communication at required baud rate
  Serial.begin(38400);
  
}
/*
void Motor_Contorl(int M_CMND)
{
  //This function contains the motors function or the Arduinos
  //Stop all motor functions
  if(M_CMND == 0)
  {
    digitalWrite(FR1,LOW);
    digitalWrite(FR2,LOW);
    digitalWrite(FL1,LOW);
    digitalWrite(FL2,LOW);
    digitalWrite(BR1,LOW);
    digitalWrite(BR2,LOW);
    digitalWrite(BL1,LOW);
    digitalWrite(BL2,LOW);
  }

  //Turn clockwise
  else if(M_CMND == 1)
  {
    digitalWrite(FR1,);
    digitalWrite(,);
    digitalWrite(,);
    digitalWrite(,);
    digitalWrite(,);
    digitalWrite(,);
    digitalWrite(,);
    digitalWrite(,);
  }

  //Turn anti-clockwise
  else if(M_CMND == 2)
  {
    digitalWrite(,);
    digitalWrite(,);
    digitalWrite(,);
    digitalWrite(,);
    digitalWrite(,);
    digitalWrite(,);
    digitalWrite(,);
    digitalWrite(,);
  }

  //Move forward
  else if(M_CMND == 3)
  {
    digitalWrite(,);
    digitalWrite(,);
    digitalWrite(,);
    digitalWrite(,);
    digitalWrite(,);
    digitalWrite(,);
    digitalWrite(,);
    digitalWrite(,);
  }

  //Move backward
  else if(M_CMND == 4)
  {
    digitalWrite(,);
    digitalWrite(,);
    digitalWrite(,);
    digitalWrite(,);
    digitalWrite(,);
    digitalWrite(,);
    digitalWrite(,);
    digitalWrite(,);
  }
}
*/
void loop() 
{/*
  if(Serial.available() > 0)
  {
    int cmd = int(Serial.read());
    M_CMND(cmd);
  }
  */
  analogWrite(ENABLE,60);

  // put your main code here, to run repeatedly:
  digitalWrite(FR1,LOW);
  digitalWrite(FR2,HIGH);
  digitalWrite(FL1,LOW);
  digitalWrite(FL2,HIGH);
  digitalWrite(BR1,HIGH);
  digitalWrite(BR2,LOW);
  digitalWrite(BL1,HIGH);
  digitalWrite(BL2,LOW);  
  delay(60);
}
