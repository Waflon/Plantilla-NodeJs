#!/user/bin/python
import RPi.GPIO as io
import time

import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe([("casa/luz", 1), ("casa/pantalla", 1), ("casa/otro", 1)])


def on_message(client, userdata, message):
    print("Message received: " + message.topic + " : " + str(message.payload))
    print(str(message.payload.decode("utf-8")))
    if str(message.payload.decode("utf-8")) == '1':
        print("Led Encendido")
        io.output(led, True)
    elif str(message.payload.decode("utf-8")) == '0':
        print("Led Apagado")
        io.output(led, False)
    

try:
    io.setmode(io.BCM)
    led = 27
    io.setup(led, io.OUT)

    broker_address = "3.232.232.178" # AWS Broker de Waflon
    # broker_address = "localhost"  # Broker address
    port = 1883  # Broker port
    # user = "yourUser"                    #Connection username
    # password = "yourPassword"            #Connection password

    client = mqtt.Client()  # create new instance
    # client.username_pw_set(user, password=password)    #set username and password
    client.on_connect = on_connect  # attach function to callback
    client.on_message = on_message  # attach function to callback

    client.connect(broker_address, port=port)  # connect to broker
    client.loop_forever()

except KeyboardInterrupt:
        io.cleanup()