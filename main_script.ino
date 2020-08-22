/*Pin naming*/
const int trigPin = 9;
const int echoPin = 10;
const int ledPin = 4;

/*Defining the variables for calculating the distance*/
const int spd_sound = 0.034;
long duration;
long distance;


void setup()
{
    /*Setting pin modes*/
    pinMode(trigPin, OUTPUT);
    pinMode(echoPin, INPUT);
    pinMode(ledPin, OUTPUT);

    /*Opening the serial port at 9600 baud rate*/
    Serial.begin(9600);
    
}

void loop()
{
    /*Making sure both the trigPin and ledPin are cleared*/
    digitalWrite(trigPin, LOW);
    digitalWrite(ledPin, LOW);
    delayMicroseconds(2);

    /*Sending the echo burst*/
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);

    /*Assiging the returning pulse value to duration and calculating distance*/
    duration = pulseIn(echoPin, HIGH);
    distance= duration*0.034/2;

    /*Sending the distance to the serial port which allows it to be intercepted by the python script*/
    Serial.println(distance);

    /*Code for an LED that blinks when the door opens*/
    if (distance > 10)
    {
        digitalWrite(ledPin, HIGH);
        delay(500);
        digitalWrite(ledPin, LOW);
    }
    delayMicroseconds(60);
}