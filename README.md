# door-open

This branch contains a the code for a personal project that allowed me and my roommate to set up a pair of Raspberry Pis in tandem with an Amazon Echo to allow us to say 'Alexa, ask room door', triggering a servo motor that would open our dorm room.  

## Getting Started

These instructions should allow you to be able set up the system allowing you to remotely open your door with an Amazon Echo.

### Prerequisites

To run this project, you need:

Physical Components:

-2 Raspberry Pis with WiFi capability

-2 free ngrok accounts

-1 Servo Motor, we used this one https://www.amazon.com/ANNIMOS-Digital-Waterproof-DS3218MG-Control/dp/B076CNKQX4?ref_=fsclp_pl_dp_1

-1 LED and some header cables to set up the circuit (circuit diagram in doorPi folder)

-1 Amazon Echo (any should work, we used a Echo Dot)

Digital Components:

-ngrok installed on all the Raspberry Pis you are using for this project: https://ngrok.com/download

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

-To get this project up and running you need to create a directory on each Raspberry Pi you are using to keep your files
-Then all the files in the doorPi folder go on the Raspberry Pi you are connecting to the servo motor, and all the files except for Schema.JSON (it's for use in Amazon Alexa SDK) go on the other Raspberry Pi if you are implementing the Alexa functionality
-Node.js should add the node_modules and packagelock.json files into the directory automatically when you run the code for the first time
-Also look at the circuit diagram in the doorPi folder to look at how to set up the Raspberry Pi and servo motor

*For running the web server that triggers the servo motor
```
node lockshell.js
```
Starts the Node.js server locally. Then in a different terminal window,
```
ngrok http 3000
```
Should give you a link to access the web server from anywhere. Accessing the link should trigger the python script that runs the servo motor.

Going to yourngroklink.ngrok.io/admin once your server is running will let you turn the ability to trigger the motor upon accessing the webpage on and off, creating a 'lock' of sorts. When someone attempts to unlock the door when it is in 'locked' mode, the LED should turn on for a few seconds and the user should be redirected.

*To implement Alexa activation after the inital circuit/server is set up

-To get the ability to say 'Alexa, ask room door' and open the door you need a second Raspberry Pi and a second ngrok account (or a Pro level ngrok account since you will need two active ngrok tunnels at once to use both the website and Alexa to open the door, and free ngrok accounts only allow one active ngrok tunnel per account), and some kind of Amazon Echo device.
-Create an Amazon developer account and use that same account to set up your Echo device.
-On the second Raspberry Pi, create a directory to store your work, and move all files from the remotePi folder into that directory except Schema.JSON. Following this tutorial (https://www.hackster.io/nishit-patel/controlling-raspberry-pi-using-alexa-33715b), set up a new Alexa skill (named room instead of raspberry) and replace the JSON code in the Interaction Model with Schema.JSON.

To enable the Alexa skill, do the following:
-In separate terminals for each,

```
python3 alexa.py
```

```
python3 mqtt_publisher.py
```

and then start a ngrok tunnel on port 5000 

```
ngrok http 5000
```

Important Note: Change the ip address in mqtt_publisher with the address of the Raspberry Pi that triggers the servo motor. On that pi, run 

```
python3 mqtt_subscriber.py
```

and replace the ip address field in that file with that device's internal IP address. After building the Alexa skill and making sure you have input the ngrok tunnel's address into the endpoint section of the Interaction Model and that the skill is enabled in the Alexa, app, you can test the skill in your browser with the built-in Alexa simulator. Once that's working, you should be able to test the whole thing by asking 'Alexa, ask room door'. If you have named your skill something different than 'room' instead say 'Alexa, ask {skill name} door.

## Built In

Node.js with Express.js
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

https://www.hackster.io/nishit-patel/controlling-raspberry-pi-using-alexa-33715b

https://tutorials-raspberrypi.com/raspberry-pi-mqtt-broker-client-wireless-communication/
