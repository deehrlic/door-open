# door-open

This repository contains a the code for a personal project that allowed me and my roommate to set up a Raspberry Pi running a Node.js web server tunneled through ngrok to trigger a servo motor whenever the webpage associated with the server was accessed which opened our door to our room. The code for this portion of the project is contained in the doorPi folder of this repository.

We have since added the ability to ask an Amazon Echo to open our door with the command, 'Alexa, ask room door'. To set this up, you also need an Amazon developer account. Further details are in the remotePi folder of this repository.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

To run this project, you need:

Physical Components:
-2 Raspberry Pis with WiFi capability (only one if you aren't setting up the Alexa component or if you have a ngrok Pro account)
-1 Servo Motor, we used this one https://www.amazon.com/ANNIMOS-Digital-Waterproof-DS3218MG-Control/dp/B076CNKQX4?ref_=fsclp_pl_dp_1
-1 LED and some header cables to set up the circuit (diagram coming soon)

Digital Components:
-Node.js and npm installed on your computer and the Raspberry Pi connected to the servo motor: https://nodejs.org/
-ngrok installed on all the Raspberry Pis you are using for this project: https://ngrok.com/download
-PythonShell module for Node.js
```
npm install python-shell
```
-Express.js for Node.js
```
npm install express
```
-gpiozero for Python (for use on Raspberry Pi GPIO pins): https://gpiozero.readthedocs.io/en/stable/installing.html
-paho-mqtt for Pyhton (only if implementing Alexa functionality)
```
pip install paho-mqtt
```
or 
```
pip3 install paho-mqtt
```
-Flask-Ask for Python (only if implementing Alexa functionality)
```
pip install Flask-Ask
```
or
```
pip3 install paho-mqtt
```
-An Amazon developer account


### Installing

-To get this project up and running you need to create a directory on each Raspberry Pi you are using to keep your files
-Then all the files in the doorPi folder go on the Raspberry Pi you are connecting to the servo motor, and all the files except for Schema.JSON (it's for use in Amazon Alexa SDK) go on the other Raspberry Pi if you are implementing the Alexa functionality
-Node.js should add the node_modules and packagelock.json files into the directory automatically when you run the code for the first time

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

## ADD ALEXA PART
*
*
*
*
*

## Built In

*Node.js
*Python3
*JSON/Amazon Alexa SDK

## Contributing

This is a personal project which isn't really contribution-friendly since it requires a lot of hardware (2 Raspberry Pis, an Amazon Echo, and a servo motor) to run.

* **Drew Ehrlich** - *Codebase Developer* - [deehrlic](https://github.com/deehrlic)
* **Corey DuVal** - *Circuit Master/Development Assistance* - No Github

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Special thanks to:
https://www.hackster.io/nishit-patel/controlling-raspberry-pi-using-alexa-33715b
https://tutorials-raspberrypi.com/raspberry-pi-mqtt-broker-client-wireless-communication/
