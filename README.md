# door-open

This branch contains a the code for a personal project that allowed me and my roommate to set up a pair of Raspberry Pis in tandem with an Amazon Echo to allow us to say 'Alexa, ask room door', triggering a servo motor that would open our dorm room.  

## Getting Started

These instructions should allow you to be able set up the system allowing you to remotely open your door with an Amazon Echo.

### Prerequisites

To run this project, you need:

Physical Components:

-1 Raspberry Pi with WiFi capability

-1 free ngrok account

-1 Servo Motor, we used this one: https://www.amazon.com/ANNIMOS-Digital-Waterproof-DS3218MG-Control/dp/B076CNKQX4?ref_=fsclp_pl_dp_1

-1 LED and some header cables to set up the circuit (circuit diagram in doorPi folder)

-1 Amazon Echo (any should work, we used a Echo Dot)

Digital Components:

-ngrok installed on the Pi you are using for this project: https://ngrok.com/download

-gpiozero for Python (for use on Raspberry Pi GPIO pins)
```
sudo apt install python3-gpiozero
```
-paho-mqtt for Pyhton
```
pip install paho-mqtt
```
-Flask-Ask for Python
```
pip install Flask-Ask
```
-An Amazon developer account

### Installing

-Move all files in the alexaPi folder to the Pi except Schema.JSON

-Look at the circuit diagram to figure out how to set up the Raspberry Pi and servo motor, a picture of the finished product is in the doorPi folder (ignore the microphone in this case, the rest still applies)

-Create an Amazon developer account and use that same account to set up/connect to your Echo device.

-Following this tutorial (https://www.hackster.io/nishit-patel/controlling-raspberry-pi-using-alexa-33715b), set up a new Alexa skill (named room instead of raspberry) and replace the JSON code in the Interaction Model section with the Schema.JSON given in the remotePi folder.

-Before testing the Echo skill, do the following (it won't work if you don't do these things, it connects the Echo to the Pi):

-In separate terminals for each command,

```
python3 alexa.py
```

and then start a ngrok tunnel on port 5000 

```
ngrok http 5000
```

-You should now be able to use the Echo simulator in the Amazon developer console to say 'Alexa, ask room door' to trigger the servo motor

-If you named the skill something else, say 'Alexa ask {skillname} door' instead

## Built In

Python 3
JSON/Amazon Alexa SDK

## Contributing

This is a personal project which isn't really contribution-friendly since it requires a lot of hardware (2 Raspberry Pis, an Amazon Echo, and a servo motor) to run.

* **Drew Ehrlich** - *Codebase Developer* - [deehrlic](https://github.com/deehrlic)
* **Corey DuVal** - *Circuit Master/Development Assistance/Circuit Diagrams* - [coreyduval](https://github.com/coreyduval)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

Special thanks to:

**Justin Hinman**

