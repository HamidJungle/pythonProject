import hello_world as hello
import publich_aws as aws_pub
import publish_local_server as local_pub
import time as t

import datetime

# data from the robot
topic = "robot" #
parameter = "productionParameter"
value = 20 #
robotID = "Jungle 152145"
dateTime = str(datetime.datetime.now())  # "2017-02-03 11:29:37"


def main():
    # publish_to_aws
    aws_pub.publish_to_ASW(topic, parameter, value, robotID, dateTime)
    # publish to local webserver
    local_pub.publish(topic, parameter, value, robotID, dateTime)


if __name__ == "__main__":
    main()
