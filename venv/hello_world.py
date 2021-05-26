
import json

MESSAGE = "Hello World from python"

def hello_wolrd_print():
    print("HEllo World from function")

def print_json():
    data = "{} [{}]".format(MESSAGE, 1)
    print("data is ", data)
    message = {"message": data}
    print(message)
    print("Published: '" + json.dumps(message) + "' to the topic: " + "'topic1'")
    print(json.dumps(message))


def convert_json_python():
    # some JSON:
    x = '{ "name":"John", "age":20, "city":"New York"}'

    # parse x:
    y = json.loads(x)

    # the result is a Python dictionary:
    print(y["name"])


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
