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


```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Built With

*Node.js
*Python3
*JSON/Amazon Alexa SDK

## Contributing

This is a personal project which isn't really contribution-friendly since it requires a lot of hardware (2 Raspberry Pis, an Amazon Echo, and a servo motor) to run.

* **Drew Ehrlich** - *Codebase Developer* - [deehrlic](https://github.com/deehrlic)
* **Corey DuVal** - *Circuitry/Development Assistance* - No Github

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Special thanks to:
https://www.hackster.io/nishit-patel/controlling-raspberry-pi-using-alexa-33715b
https://tutorials-raspberrypi.com/raspberry-pi-mqtt-broker-client-wireless-communication/
