#!/usr/bin/python

import spidev
import time
import os
import RPI.GPIO as GPIO

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 1000000

# Read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
	adc = spi.xfer2([1,(8+channel)<<4,0])
	data = ((adc[1]&3) << 8) + adc[2]
	return data

# Convert data to voltage level
# Rounded to specified number
def ConvertVolts(data, places):
	volts = (data * 3.3) / float(1023)
	volts = round(volts, places)
	return volts

# Defines whether the voltage should be high or low
# to specify GPIO.HIGH or GPIO.LOW
def ConvertHighLow(voltage):
	if(voltage < 1.3):
		return 0
	else:
		return 1

def sensors:
	ultrasonic_channel = 0
	output_channel = 24
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(output_channel, GPIO)

def main:
	while True:
		# Read from ultrasonic data
		ultrasonic_reading = ReadChannel(ultrasonic_channel)
		ultrasonic_voltage = ConvertVolts(ultrasonic_reading, 2)
		# Decide if high or low
		highlow = ConvertHighLow(ultrasonic_voltage)
		GPIO.output(output_channel, highlow)
		time.sleep(.01)