# door-open snowboy

This branch contains a the code for a personal project that allows you to trigger a servo motor (in my case, being used to open my dorm door) by opening a door using Snowboy's wake word detection system.

## Getting Started

These instructions should allow you to trigger servo motors by using your voice.

### Prerequisites

To run this project, you need:

Physical Components:

-1 Raspberry Pi with WiFi capability

-1 Servo Motor, we used this one https://www.amazon.com/ANNIMOS-Digital-Waterproof-DS3218MG-Control/dp/B076CNKQX4?ref_=fsclp_pl_dp_1

-Some header cables to set up the circuit (circuit diagram in doorPi folder along with image of final product)

-1 USB Microphone or webcam

-A monitor and keyboard to connect to the Pi so you can see what you're doing

-A LOT of duct tape

Digital Components:
-Raspbian OS installed on your Pi (this whole README assumes you have it installed already)

-gpiozero for Python
```
sudo apt install python3-gpiozero
```

-Snowboy installed
https://snowboy.kitt.ai/

### Running

-Create a directory to hold the files and place Bloomie.pmdl and snowboy_door.py in it.

-Look at the circuit diagram in the doorPi folder to look at how to set up the Raspberry Pi, servo motor, and microphone

-Run 
```
python snowboy_door.py Bloomie.pmdl
```

The script should spit out a bunch of text and then continue running. When you say "Bloomie", the command line should display "hotword dectected" and the motor should run. If you don't want your hotword to be "Bloomie", go to Snowboy's website and make a free account and use their model creation tool to make your own with whatever word you want.


## Built In

Python

Minecraft

## Contributing

If you can think of something to add to this branch, reach out!

* **Drew Ehrlich** - *Codebase Developer* - [deehrlic](https://github.com/deehrlic)
* **Corey DuVal** - *Circuit Master/Development Assistance/Circuit Diagrams* - [coreyduval](https://github.com/coreyduval)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

Special thanks to:

**Steaven Ballesteros**

**Justin Hinman**


