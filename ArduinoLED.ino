#define LED 5
#define BUTTON 4
bool buttonState;
bool clickedFlag = false;
void setup() {
  // put your setup code here, to run once:

 Serial.begin(115200);
 pinMode(LED, OUTPUT);
 pinMode(BUTTON, INPUT);
  

}

void loop() {
  
  buttonState = digitalRead(BUTTON);
  if(buttonState == 1 ) {
    if(clickedFlag == false) {
      digitalWrite(LED, HIGH);
      clickedFlag = true;
      delay(1000);
      }else {
        digitalWrite(LED, LOW);
        clickedFlag = false;
        delay(1000);
        }
    }

}
