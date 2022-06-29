#!/usr/bin/python

import adafruit_ssd1306  # Control de las prpiedades del oled
import board  #control de la comunicacion ic2
from PIL import Image, ImageDraw, ImageFont  # Biblioteca que permite el dibujo en la pantalla de forma simple

import time  
import paho.mqtt.client as mqtt  # para mqtt communication

WIDTH = 128
HEIGHT = 64  # Change to 64 if needed
BORDER = 5

def on_connect(client, userdata, flags, rc):
    print("Conectado con codigo: " + str(rc))
    client.subscribe([("casa/pi/oled", 1)])

def on_message(client, userdata, message):
    global mensaje
    global loop_flag 
    topic = message.topic
    mensaje = str(message.payload.decode("utf-8"))
    if mensaje == "exit":
        loop_flag = 0
    elif mensaje == "limpiar":
        limpiarPantalla()
    else:
        print("Mensaje Recibido bajo el Topic: " + topic + " : " + mensaje)
        dibujar(mensaje)
    
def limpiarPantalla():
    i2c = board.I2C()  # Use for I2C.
    oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)  #(alto, ancho, protocolo)
    oled.fill(0)  # Limpia pantalla y la deja en negro (0)
    oled.show()  # hace efecto de los cambios en la pantalla

def dibujar(mensaje):
    i2c = board.I2C()  # Use for I2C.
    oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)  #(alto, ancho, protocolo)
    oled.fill(0)  # Limpia pantalla y la deja en negro (0)
    oled.show()  # hace efecto de los cambios en la pantalla

    # Create blank image for drawing.
    image = Image.new("1", (oled.width, oled.height)) # Make sure to create image with mode '1' for 1-bit color.
    draw = ImageDraw.Draw(image) # Get drawing object to draw on image.
    draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255) # Draw a white background

    draw.rectangle( # Draw a smaller inner rectangle
        (BORDER, BORDER, oled.width - BORDER - 1, oled.height - BORDER - 1),
        outline=0,
        fill=0,
    )

    font = ImageFont.load_default() # Load default font.
    text = mensaje # Draw Some Text
    (font_width, font_height) = font.getsize(text)  # Obtener ancho y alto de la fuente y almacenarlos en 2 variables
    draw.text(
        (oled.width // 2 - font_width // 2, oled.height // 2 - font_height // 2),
        text,
        font=font,
        fill=255,
        size = 5,
    )
    oled.image(image) # Display image ( Solo lo carga en la memoria (en el buffer o band))
    oled.show() # hace que el efecto se manifieste en la pantalla

client = mqtt.Client()  # create new instance
# client.username_pw_set(user, password=password)    #set username and password
client.on_connect = on_connect  # attach function to callback
client.on_message = on_message  # attach function to callback

client.connect("3.232.232.178")  # connect to broker
client.loop_start()

loop_flag = 1
while loop_flag == 1:  # si no es desactivado explicitamente por mi
    #acá va el codigo a ejecutarse continuamente
    x = 0

client.disconnect()
client.loop_stop()