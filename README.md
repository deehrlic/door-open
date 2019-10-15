# door-open master

This repository contains the code for the ways that my roommate and I have managed to open our door with a servo motor and a Raspberry Pi (being with an Amazon Echo, a Node.js http server, non-Echo offline voice recognition, and Minecraft). Each way to open our door is kept in its own branch (see Getting Started).

## Getting Started

Choose a branch to get to the code and method for setting up that system.

## open-door snowboy

Our current choice for voice control, this setup uses a combination of Snowboy's offline wake word detection technology and some Python code to enable faster response times on voice commands versus the Echo setup, which required going through Amazon's servers which took more time. 

## open-door nodeserver

The first way we opened our door was with a Node.js server tunneled through to the internet with ngrok, a free http tunneling service. We still actively use this setup.

https://github.com/deehrlic/door-open/tree/nodeserver

## open-door alexa

Our first addition to our setup, this branch will allow you to control a servo motor with an Amazon Echo and your voice. We have replaced this setup with the setup in the snowboy branch, but the code is here.

https://github.com/deehrlic/door-open/tree/alexa

## open-door minecraft

A more fun and casual setup, if you've ever wanted to have Minecraft have real life actions, this code is for you.

https://github.com/deehrlic/door-open/tree/minecraft

## open-door oldsetup 

This branch's setup is the code and methods for our previous setup, which consisted of using 2 Raspberry Pis to talk to each other to have the Node.js server and the Echo both being able to open the door. No longer our current setup, which is a combination of nodeserver and snowboy branches.

https://github.com/deehrlic/door-open/tree/oldsetup

## Built In

Node.js with Express.js

Python 3

JSON/Amazon Alexa SDK

## Contributing

* **Drew Ehrlich** - *Codebase Developer* - [deehrlic](https://github.com/deehrlic)
* **Corey DuVal** - *Circuit Master/Development Assistance/Circuit Diagrams* - [coreyduval](https://github.com/coreyduval)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

Special thanks to:

**Justin Hinman**
