from board import SCL, SDA
import busio
import time

import adafruit_ssd1306
import paho.mqtt.client as mqtt  # para mqtt communication

# Inicializaciones
i2c = busio.I2C(SCL, SDA) # Create the I2C interface.
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
direccion = ""
x = 0
y = 32
speed = 5

def on_connect(client, userdata, flags, rc):
    print("Conectado con codigo: " + str(rc))
    client.subscribe([("casa/pi", 1)])

def on_message(client, userdata, message):
    global direccion
    global loop_flag 
    mensaje = str(message.payload.decode("utf-8"))
    print("Mensaje Recibido bajo el Topic: " + message.topic + " : " + mensaje)
    if mensaje == "derecha":
        direccion = "derecha"
    elif mensaje == "izquierda":
        direccion = "izquierda"
    elif mensaje == "arriba":
        direccion = "arriba"
    elif mensaje == "abajo":
        direccion = "abajo"
    elif mensaje == "end":
        loop_flag = 0

client = mqtt.Client()  # create new instance
# client.username_pw_set(user, password=password)    #set username and password
client.on_connect = on_connect  # attach function to callback
client.on_message = on_message  # attach function to callback

client.connect("3.232.232.178")  # connect to broker
client.loop_start()

loop_flag = 1
while loop_flag == 1:  # si no es desactivado explicitamente por mi
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

client.disconnect()
client.loop_stop()

#limpiar pantalla
display.fill(0)
display.show()