from board import SCL, SDA
import busio
import time

import adafruit_ssd1306
import paho.mqtt.client as mqtt  # para mqtt communication

# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height. 
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
direccion = ""

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe([("casa/pi", 1)])

def on_message(client, userdata, message):
    global direccion
    mensaje = str(message.payload.decode("utf-8"))
    print("Message received: " + message.topic + " : " + mensaje)
    if mensaje == "derecha":
        direccion = "derecha"
    elif mensaje == "izquierda":
        direccion = "izquierda"
    elif mensaje == "arriba":
        direccion = "arriba"
    elif mensaje == "abajo":
        direccion = "abajo"

client = mqtt.Client()  # create new instance
# client.username_pw_set(user, password=password)    #set username and password
client.on_connect = on_connect  # attach function to callback
client.on_message = on_message  # attach function to callback


client.connect("3.232.232.178")  # connect to broker

x = 0
y = 32
speed = 5
client.loop_start()
client.loop_stop()
while(1):

    if (direccion == "derecha"):
        if(x>128):
            x=0
        x += speed
    elif (direccion == "izquierda"):
        if(x<0):
            x=128
        x -= speed
    elif (direccion == "arriba"):
        if(y<0):
            y=64
        y -= speed
    elif (direccion == "abajo"):
        if(y>64):
            y=0
        y += speed

    display.fill(0)
    display.circle(x, y, 15, 1)
    display.show()
