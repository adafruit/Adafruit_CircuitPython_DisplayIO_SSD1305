"""
This test will initialize the display using displayio and draw a solid white
background, a smaller black rectangle, and some white text.
"""

import board
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1305

displayio.release_displays()

oled_reset = board.D9

# Use for SPI
spi = board.SPI()
oled_cs = board.D5
oled_dc = board.D6
display_bus = displayio.FourWire(spi, command=oled_dc, chip_select=oled_cs,
                                 reset=oled_reset, baudrate=1000000)

# Use for I2C
#i2c = board.I2C()
#display_bus = displayio.I2CDisplay(i2c, device_address=0x3c, reset=oled_reset)

WIDTH = 128
HEIGHT = 64     # Change to 64 if needed
BORDER = 5

display = adafruit_displayio_ssd1305.SSD1305(display_bus, width=WIDTH, height=HEIGHT)

# Make the display context
splash = displayio.Group(max_size=10)
display.show(splash)

color_bitmap = displayio.Bitmap(WIDTH, HEIGHT, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFFFFFF # White

bg_sprite = displayio.TileGrid(color_bitmap,
                               pixel_shader=color_palette,
                               x=0, y=0)
splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(WIDTH-BORDER*2, HEIGHT-BORDER*2, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x000000 # Black
inner_sprite = displayio.TileGrid(inner_bitmap,
                                  pixel_shader=inner_palette,
                                  x=BORDER, y=BORDER)
splash.append(inner_sprite)

# Draw a label
text = "Hello World!"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=28, y=HEIGHT//2-1)
splash.append(text_area)

while True:
    pass