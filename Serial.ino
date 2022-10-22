String Speed;
char  LorR;
int  i, s;
int motorA1 = 5;
int motorA2 = 6;
int motorB1 = 9;
int motorB2 = 10;
byte DataToRead[6];
int cnt=0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(motorA1, OUTPUT);
  pinMode(motorA2, OUTPUT);
  pinMode(motorB1, OUTPUT);
  pinMode(motorB2, OUTPUT);
}

void serialFlush(){
  while(Serial.available() > 0) {
    char t = Serial.read();
  }
}

void loop() {
  DataToRead[5] = '\n';
  Serial.readBytesUntil(char(13), DataToRead, 5);
  
/* For Debugging, send string to RPi */
/*for (i = 0; i < 6; i++) {
    Serial.write(DataToRead[i]);
    if (DataToRead[i] == '\n') break;
  }
/* End of Debugging */

;  LorR = DataToRead[0];
  Speed = "";
  for (i = 1; (DataToRead[i] != '\n') && (i < 6); i++) {
    Speed += char(DataToRead[i]);
  }
  s = Speed.toInt();
  
  if (LorR == 'R') {
    // Turn left wheel with speed s
	analogWrite(motorB1, s);
  analogWrite(motorB2, 0);
  analogWrite(motorA2, s);
  analogWrite(motorA1, 0);
  delay(110);

  }
  else if (LorR == 'L') {
    // Turn right wheel with speed s  
  analogWrite(motorA1, s);
	analogWrite(motorB1, 0);
  analogWrite(motorB2, s);
  analogWrite(motorA2, 0);
  delay(110);

  
  }
  else if (LorR == 'B') {
    // 
  analogWrite(motorB1, 0);
  analogWrite(motorB2, s);
  analogWrite(motorA2, s);
  analogWrite(motorA1, 0);
  delay(130);

  }
  else  {
    // 
  analogWrite(motorA1, s);
  analogWrite(motorB1, s);
  analogWrite(motorB2, 0);
  analogWrite(motorA2, 0);
  delay(130);

  }
  
  analogWrite(motorB1, 0);
  analogWrite(motorB2, 0);
  analogWrite(motorA2, 0);
  analogWrite(motorA1, 0);
  if(cnt ==10){
    serialFlush();
    cnt = 1;
    }
  else{cnt++;} 
  delay(10);
}
