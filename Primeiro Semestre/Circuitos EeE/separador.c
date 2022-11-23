#include Servo servoid1;
Servo servoid2;

const int s0 = 8;
const int s1 = 9;
const int s2 = 12;
const int s3 = 11;
const int out = 10;

//Pinos do led RGB
int pinoledverm = 6;
int pinoledazul = 5;

//Variaveis cores
int red = 0;
int green = 0;
int blue = 0;

void setup()
{
  servoid1.attach(3);
  servoid2.attach(4);
  pinMode(s0, OUTPUT);
  pinMode(s1, OUTPUT);
  pinMode(s2, OUTPUT);
  pinMode(s3, OUTPUT);
  pinMode(out, INPUT);
  pinMode(pinoledverm, OUTPUT);
  pinMode(pinoledazul, OUTPUT);
  Serial.begin(9600);
  digitalWrite(s0, HIGH);
  digitalWrite(s1, LOW);
}

void loop()
{

//Detecta a cor
color();
servoid1.write(-90);
digitalWrite(pinoledverm, LOW);
digitalWrite(pinoledazul, LOW);

//Verifica se a cor vermelha foi detectada
if (red < blue && red < green && red < 100)
{
  Serial.println("Vermelho");
  digitalWrite(pinoledverm, HIGH);
  digitalWrite(pinoledazul, LOW);
  servoid1.write(90);
  servoid2.write(90);
  delay(3000);
  servoid1.write(-90);
  servoid2.write(0);
  digitalWrite(pinoledverm, LOW);
}
//Delay para apagar os leds e reiniciar o processo
else if (green < blue && green < blue && green < 100){
    digitalWrite(pinoledverm, LOW);
    digitalWrite(pinoledazul, HIGH);
    servoid1.write(90);
    delay(2000);
    servoid1.write(-90);
    digitalWrite(pinoledazul, LOW);
  }
}

void color()
{
  //Rotina que le o valor das cores
  digitalWrite(s2, LOW);
  digitalWrite(s3, LOW);
  //count OUT, pRed, RED
  red = pulseIn(out, digitalRead(out) == HIGH ? LOW : HIGH);
  digitalWrite(s3, HIGH);
  //count OUT, pBLUE, BLUE
  blue = pulseIn(out, digitalRead(out) == HIGH ? LOW : HIGH);
  digitalWrite(s2, HIGH);
  //count OUT, pGreen, GREEN
  green = pulseIn(out, digitalRead(out) == HIGH ? LOW : HIGH);
}