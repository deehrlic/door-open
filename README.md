# door-open

This branch contains a the code for a personal project that allows you to trigger a servo motor (in my case, being used to open my dorm door) by opening a door while playing Minecraft (Raspberry Pi edition).

## Getting Started

These instructions should allow you to trigger servo motors by having your Minecraft character standing at a certain position.

### Prerequisites

To run this project, you need:

Physical Components:
-1 Raspberry Pi with WiFi capability
-1 Servo Motor, we used this one https://www.amazon.com/ANNIMOS-Digital-Waterproof-DS3218MG-Control/dp/B076CNKQX4?ref_=fsclp_pl_dp_1
-Some header cables to set up the circuit (circuit diagram in doorPi folder)
-1 USB Microphone or webcam
-A monitor and keyboard to connect to the Pi so you can see what you're doing
-A LOT of duct tape

Digital Components:
-Raspbian OS installed on your Pi (this whole README assumes you have it installed already)
-Minecraft installed on your Pi (It should come installed by default on newer models)
-gpiozero for Python
```
sudo apt install python3-gpiozero
```

### Running

-Create a directory to hold the files and place mineDoor.py and mineMotor.py inside it
-Look at the circuit diagram in the doorPi folder to look at how to set up the Raspberry Pi and servo motor (image of the finished project will be there too for reference)
-Take the entire 'world' folder in doorPi and move it to where your Minecraft saves are stored on your Pi (google it if you don't know where)
-Open the imported 'world' in Minecraft (it should show up as option when you click the Play button)
-After you have the Minecraft world open, run mineDoor.py
```
python mineDoor.py
```
-Go back into Minecraft and navigate to the location (-5.5, 0, 12.5) (if you use the given world, the location is the block the door is on top of inside the house)
-If the servo is set up correctly, it should trigger once and give output in your terminal window
-You have now run a servo motor using Minecraft!

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


