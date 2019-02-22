#Base code from https://tutorials-raspberrypi.com/raspberry-pi-mqtt-broker-client-wireless-communication/
#Modified by Drew Ehrlich

import paho.mqtt.client as mqtt
import os

#IP OF THE DEVICE RUNNNING THIS CODE GOES HERE, CHANGE IF USING
MQTT_SERVER = "YOUR.IP.HERE"
MQTT_PATH = "test_channel"
 
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_PATH)
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(str(msg.payload))
    
    if str(msg.payload) == str(b'opendoor'):
    	os.system("python3 motor.py")    
    
# more callbacks, etc
 
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect(MQTT_SERVER, 1883, 60)
 
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.




client.loop_forever()
