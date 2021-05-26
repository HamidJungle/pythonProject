
import paho.mqtt.client as mqtt
import time
import random

# he callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


def mqtt_test():  #
  client = mqtt.Client()
  client.on_connect = on_connect
  client.on_message = on_message

  client.connect("localhost", 1883, 60)


  robot_ID="Jungle Robot ID2642986"
  client.publish("robot",robot_ID)
  time_stamp=1
  for x in range(11):
    production= x*10;
    client.publish("production", production)
    fact=10
    payments=production * fact+3512;
    client.publish("payment", payments)
    axis_1=random.randint(0,180)
    axis_2=random.randint(0,180)
    axis_3=random.randint(0,180)
    axis_4=random.randint(0,180)
    axis_5=random.randint(0,180)
    axis_6=random.randint(0,180)

    client.publish("axis_1", axis_1)
    client.publish("axis_2", axis_2)
    client.publish("axis_3", axis_3)
    client.publish("axis_4", axis_4)
    client.publish("axis_5", axis_5)
    client.publish("axis_6", axis_6)
    time.sleep(time_stamp)
  # Blocking call that processes network traffic, dispatches callbacks and
  # handles reconnecting.
  # Other loop*() functions are available that give a threaded interface and a
  # manual interface.
  client.loop_forever()


mqtt_test()