from luma.core.interface.serial import spi
from luma.oled.device import ssd1306
from luma.core.render import canvas
from PIL import ImageFont

# Create an instance of the SPI interface
serial = spi(device=0, port=0)

# Create an instance of the ssh1106 class
device = ssd1306(serial)

# Load a font
font = ImageFont.load_default()

# Create a canvas and draw the text
with canvas(device) as draw:
    draw.text((10, 10), "Hello, World!", font=font, fill="white")