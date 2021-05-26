import paho.mqtt.client as mqtt
import time
import random
import json

client = mqtt.Client()


def convert_python_json(value, parameter, robotID, dateTime):
    # a Python object (dict):
    x = {
    "robotParameter": parameter,
    "robotValue": value,
    "robotId": robotID,
     "dateTime":  dateTime
    }
    # convert into JSON:
    y=json.dumps(x)
    print(y)
    return y

# he callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


def publish(topic,parameter, value,  robotID, dateTime):  #

  client.on_connect = on_connect
  client.on_message = on_message
  client.connect("localhost", 1883, 60)
  message=convert_python_json(value, parameter, robotID, dateTime)
  client.publish(topic, message)
  #client.publish("robot",robotID)



def disconnect ():
  client.disconnect()