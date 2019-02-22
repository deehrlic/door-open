import paho.mqtt.publish as publish
 
#IP OF MACHINE YOU ARE SENDING TO GOES HERE, CHANGE IF USING
MQTT_SERVER = "YOUR.IP.HERE"
MQTT_PATH = "test_channel"
 
publish.single(MQTT_PATH, "opendoor", hostname=MQTT_SERVER)
