#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
MIT License

Copyright (c) 2022 MackaJunest

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

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
try:
    ser=serial.Serial('/dev/ttyUSB0',115200,timeout=1)
    print("Connected!")
    t.sleep(0.5)
    print("Port:/dev/ttyUSB0")
    t.sleep(0.2)
    print("Baudrate:115200")
    t.sleep(0.5)
    print("Starting quadruped...")
except:
    ser=serial.Serial('/dev/ttyUSB1',115200,timeout=1)
    print("Connected!")
    t.sleep(0.5)
    print("Port:/dev/ttyUSB1")
    t.sleep(0.2)
    print("Baudrate:115200")
    t.sleep(0.5)
    print("Starting quadruped...")

def senddata(data):
#    ser.write(str.encode(h1+','+s1+','+h2+','+s2+','+h3+','+s3+','+h4+','+s4','+x+','+y))
    ser.write(data)