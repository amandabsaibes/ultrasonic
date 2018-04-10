#!/usr/bin/python

import spidev
import time
import os

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 1000000

# Read SPI data from MCP3008 chip
# Channel must be an integer 0-7
