# door-open nodeserver

This branch contains the files necessary to run a web server (accessible through a URL) that, when accessed, triggers a servo motor, which in me and my roommate's case, opened our dorm room door.


## Getting Started

These instructions should allow you to set up a node.js web server and attach a URL to it which will trigger a servo motor when accessed.

### Prerequisites

To run this project, you need:

Physical Components:
-1 Raspberry Pis with WiFi capability 

-1 free ngrok account 

-1 Servo Motor, we used this one: https://www.amazon.com/ANNIMOS-Digital-Waterproof-DS3218MG-Control/dp/B076CNKQX4?ref_=fsclp_pl_dp_1

-1 LED and some header cables to set up the circuit (circuit diagram in doorPi folder, along with a image of the finished product, ignore the microphone)

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
-gpiozero for Python (for use on Raspberry Pi GPIO pins)
```
sudo apt install python3-gpiozero
```

### Installing

-Keep all the files in the doorPi folder together and set up the physical circuit (diagram and actual implementation in the folder, ignore the microphone)

*For running the web server that triggers the servo motor
```
node lockshell.js
```
Starts the Node.js server locally. Then in a different terminal window,
```
ngrok http 3000
```
Should give you a link to access the web server from anywhere. Accessing the link should trigger the python script that runs the servo motor.

## Built In

Node.js with Express.js
Python 3

## Contributing

* **Drew Ehrlich** - *Codebase Developer* - [deehrlic](https://github.com/deehrlic)
* **Corey DuVal** - *Circuit Master/Development Assistance/Circuit Diagrams* - [coreyduval](https://github.com/coreyduval)
## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

Special thanks to:

**Justin Hinman**


