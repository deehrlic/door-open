from gpiozero import Servo
from time import sleep

servo = Servo(18)
servo.max()
sleep(3)
servo.min()
sleep(1)	
