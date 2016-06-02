#!/usr/bin/env python

import serial

ser = serial.Serial('/dev/ttyACM0')
test = ser.readline()
print test
