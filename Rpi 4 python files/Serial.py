#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#JimmyChen V3.0 by MackaJunest COPYRIGHT 2022
'''
                            front
                   leg  leg1|    |leg2
    4 groups: 1,2  -|1      |    |
              3,4  -|2_____Jimmychen
              5,6  -|3      |    |
              7,8  -|4  leg4|    |leg3
                             back
'''
import serial
import time as t

global ser

print("JimmyChen V3.0 by MackaJunest COPYRIGHT 2022")
t.sleep(1)
try:
    ser=serial.Serial('/dev/ttyUSB0',115200,timeout=1)
    print("Connected!")
    t.sleep(1)
    print("Port:/dev/ttyUSB0")
    t.sleep(0.2)
    print("Baudrate:115200")
    t.sleep(0.5)
    print("Starting quadruped...")
    t.sleep(2)
except:
    ser=serial.Serial('/dev/ttyUSB1',115200,timeout=1)
    print("Connected!")
    t.sleep(1)
    print("Port:/dev/ttyUSB1")
    t.sleep(0.2)
    print("Baudrate:115200")
    t.sleep(0.5)
    print("Starting quadruped...")
    t.sleep(2)
