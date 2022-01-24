Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-displayio_ssd1305/badge/?version=latest
    :target: https://docs.circuitpython.org/projects/displayio_ssd1305/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/adafruit/Adafruit_CircuitPython_DisplayIO_SSD1305/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_DisplayIO_SSD1305/actions
    :alt: Build Status

DisplayIO driver for SSD1305 monochrome displays

For the framebuf based driver see `Adafruit CircuitPython SSD1305 <https://github.com/adafruit/Adafruit_CircuitPython_SSD1305/>`_.


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython Version 5+ <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_.

Installing from PyPI
=====================

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-displayio_ssd1305/>`_. To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-displayio-ssd1305

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-displayio-ssd1305

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install adafruit-circuitpython-displayio-ssd1305

Usage Example
=============

.. code-block:: python

    import board
    import displayio
    import terminalio
    from adafruit_display_text import label
    import adafruit_displayio_ssd1305

    displayio.release_displays()

    # Use for SPI
    spi = board.SPI()
    oled_cs = board.D5
    oled_dc = board.D6
    display_bus = displayio.FourWire(spi, command=oled_dc, chip_select=oled_cs,
                                     baudrate=1000000, reset=board.D9)

    # Use for I2C
    # i2c = board.I2C()
    # display_bus = displayio.I2CDisplay(i2c, device_address=0x3c)

    WIDTH = 128
    HEIGHT = 64     # Change to 32 if needed
    BORDER = 8
    FONTSCALE = 1

    display = adafruit_displayio_ssd1305.SSD1305(display_bus, width=WIDTH, height=HEIGHT)

    # Make the display context
    splash = displayio.Group()
    display.show(splash)

    color_bitmap = displayio.Bitmap(display.width, display.height, 1)
    color_palette = displayio.Palette(1)
    color_palette[0] = 0xFFFFFF # White

    bg_sprite = displayio.TileGrid(color_bitmap,
                                   pixel_shader=color_palette,
                                   x=0, y=0)
    splash.append(bg_sprite)

    # Draw a smaller inner rectangle
    inner_bitmap = displayio.Bitmap(display.width - BORDER * 2, display.height - BORDER * 2, 1)
    inner_palette = displayio.Palette(1)
    inner_palette[0] = 0x000000 # Black
    inner_sprite = displayio.TileGrid(inner_bitmap,
                                      pixel_shader=inner_palette,
                                      x=BORDER, y=BORDER)
    splash.append(inner_sprite)

    # Draw a label
    text = "Hello World!"
    text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF)
    text_width = text_area.bounding_box[2] * FONTSCALE
    text_group = displayio.Group(scale=FONTSCALE, x=display.width // 2 - text_width // 2,
                                 y=display.height // 2)
    text_group.append(text_area) # Subgroup for text scaling
    splash.append(text_group)

    while True:
        pass

Documentation
=============

API documentation for this library can be found on `Read the Docs <https://docs.circuitpython.org/projects/displayio_ssd1305/en/latest/>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_DisplayIO_SSD1305/blob/main/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
