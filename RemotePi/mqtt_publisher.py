import paho.mqtt.publish as publish
 
MQTT_SERVER = "100.64.59.42"
MQTT_PATH = "test_channel"
 
publish.single(MQTT_PATH, "opendoor", hostname=MQTT_SERVER)
