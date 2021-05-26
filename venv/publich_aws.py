# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
from awsiot import mqtt_connection_builder
from awscrt import io, mqtt, auth, http
import time as t
import json
import datetime

# data from the robot
parameter = "productionParameter"
value = 3
robotID = "SBS01"
dateTime = str(datetime.datetime.now()) # "2017-02-03 11:29:37"

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

def publish_to_ASW(topic, parameter, value, robotID, dateTime):
    # Define ENDPOINT, CLIENT_ID, PATH_TO_CERT, PATH_TO_KEY, PATH_TO_ROOT, MESSAGE, TOPIC, and RANGE
    ENDPOINT = "a3bzszyut23ruj-ats.iot.us-east-1.amazonaws.com"
    CLIENT_ID = "testDevice"
    PATH_TO_CERT = "venv/certificates/7d271fd0c5-certificate.pem.crt"
    PATH_TO_KEY = "venv/certificates/7d271fd0c5-private.pem.key"
    PATH_TO_ROOT = "venv/certificates/root.pem"
    MESSAGE = "Hello World from python"
    TOPIC = topic
    RANGE = 20

    # Spin up resources
    event_loop_group = io.EventLoopGroup(1)
    host_resolver = io.DefaultHostResolver(event_loop_group)
    client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)
    mqtt_connection = mqtt_connection_builder.mtls_from_path(
                endpoint=ENDPOINT,
                cert_filepath=PATH_TO_CERT,
                pri_key_filepath=PATH_TO_KEY,
                client_bootstrap=client_bootstrap,
                ca_filepath=PATH_TO_ROOT,
                client_id=CLIENT_ID,
                clean_session=False,
                keep_alive_secs=6
                )
    print("Connecting to {} with client ID '{}'...".format(
            ENDPOINT, CLIENT_ID))
    # Make the connect() call
    connect_future = mqtt_connection.connect()
    # Future.result() waits until a result is available
    connect_future.result()
    print("Connected!")
    # Publish message to server desired number of times.
    print('Begin Publish')

    message=convert_python_json(value, parameter, robotID, dateTime)
    mqtt_connection.publish(topic=TOPIC, payload=message, qos=mqtt.QoS.AT_LEAST_ONCE)
    print("Published: '" + message + "' to the topic: " + topic)
    t.sleep(0.1)
    print('Publish End')
    disconnect_future = mqtt_connection.disconnect()
    disconnect_future.result()




