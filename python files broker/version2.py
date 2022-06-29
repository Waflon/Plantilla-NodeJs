import adafruit_ssd1306  # Control de las prpiedades del oled
import board  #control de la comunicacion ic2
from PIL import Image, ImageDraw, ImageFont  # Biblioteca que permite el dibujo en la pantalla de forma simple

WIDTH = 128
HEIGHT = 64  # Change to 64 if needed
BORDER = 5

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
text = "Te amo Ia" # Draw Some Text
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