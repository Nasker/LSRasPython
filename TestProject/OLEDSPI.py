from luma.core.interface.serial import spi
from luma.oled.device import sh1106
from PIL import Image

# Create an instance of the SPI interface
serial = spi(device=0, port=0)

# Create an instance of the ssh1106 class
device = sh1106(serial)

# Load an image
image = Image.open('path_to_your_image.png')

# Display the image on the OLED screen
device.display(image)