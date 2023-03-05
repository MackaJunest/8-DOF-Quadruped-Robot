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
from  cmath import pi
import math
L1 = 150 #shank 
L2 = 106 #ham

#LEG1
def Angle1_calc(x,y):
    global leg1_ham
    global leg1_shank
    L3 = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
    theta1 = math.acos((math.pow(L1, 2) + math.pow(L2, 2) - math.pow(L3, 2)) / (2 * L1 * L2))
    theta1_2 = theta1 * 180 / pi
    leg1_shank =  (180 - theta1_2)
    L4 = math.sqrt(math.pow(L3, 2) - math.pow(x, 2))
    theta3 = math.asin((math.sin(theta1) / L3) * L1)
    theta3_2 = theta3 * 180 / pi
    theta4 = math.atan(L4 / x) 
    theta4_2 = theta4 * 180 / pi
    leg1_ham = theta4_2  - theta3_2 
def Coordinate1_calc(shank_deg,ham_deg):
    global x1
    global y1
    xh1=math.cos(leg1_shank)
    xh=math.degrees(xh1)*L2
    yh=math.sqrt(math.pow(L2,2)+math.pow(L2,2))
    theta4=180-leg1_shank
    L3=math.sqrt(math.pow(L1,2)+math.pow(L2,2)-2*L1*L2*(math.cos(math.radians(theta4))))
    theta3=math.degrees(math.asin(math.sin(math.radians(theta4))/L3*L1))
    theta5=theta3+leg1_ham
    x1=(math.cos(math.radians(theta5)))*L3
    y1=(math.sin(math.radians(theta5)))*L3
    x1=round(x1)
    y1=round(y1)
#LEG2
def Angle2_calc(x,y):
    global leg2_ham
    global leg2_shank
    L3 = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
    value = (math.pow(L1, 2) + math.pow(L2, 2) - math.pow(L3, 2)) / (2 * L1 * L2)
    if value >= -1 and value <= 1:
        theta1 = math.acos(value)
    else:
        raise ValueError("The argument passed to acos is not within the defined domain.")

    theta1_2 = theta1 * 180 / pi
    leg2_shank =  (180 - theta1_2)
    L4 = math.sqrt(math.pow(L3, 2) - math.pow(x, 2))
    theta3 = math.asin((math.sin(theta1) / L3) * L1)
    theta3_2 = theta3 * 180 / pi
    theta4 = math.atan(L4 / x) 
    theta4_2 = theta4 * 180 / pi
    leg2_ham = theta4_2  - theta3_2 
def Coordinate2_calc(shank_deg,ham_deg):
    global x2
    global y2
    xh1=math.cos(leg2_shank)
    xh=math.degrees(xh1)*L2
    yh=math.sqrt(math.pow(L2,2)+math.pow(L2,2))
    theta4=180-leg2_shank
    L3=math.sqrt(math.pow(L1,2)+math.pow(L2,2)-2*L1*L2*(math.cos(math.radians(theta4))))
    theta3=math.degrees(math.asin(math.sin(math.radians(theta4))/L3*L1))
    theta5=theta3+leg2_ham
    x2=(math.cos(math.radians(theta5)))*L3
    y2=(math.sin(math.radians(theta5)))*L3
    x2=round(x2)
    y2=round(y2)
#LEG3 
def Angle3_calc(x,y):
    global leg3_ham
    global leg3_shank
    L3 = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
    theta1 = math.acos((math.pow(L1, 2) + math.pow(L2, 2) - math.pow(L3, 2)) / (2 * L1 * L2))
    theta1_2 = theta1 * 180 / pi
    leg3_shank =  (180 - theta1_2)
    L4 = math.sqrt(math.pow(L3, 2) - math.pow(x, 2))
    theta3 = math.asin((math.sin(theta1) / L3) * L1)
    theta3_2 = theta3 * 180 / pi
    theta4 = math.atan(L4 / x) 
    theta4_2 = theta4 * 180 / pi
    leg3_ham = theta4_2  - theta3_2 
def Coordinate3_calc(shank_deg,ham_deg):
    global x3
    global y3
    xh1=math.cos(leg3_shank)
    xh=math.degrees(xh1)*L2
    yh=math.sqrt(math.pow(L2,2)+math.pow(L2,2))
    theta4=180-leg3_shank
    L3=math.sqrt(math.pow(L1,2)+math.pow(L2,2)-2*L1*L2*(math.cos(math.radians(theta4))))
    theta3=math.degrees(math.asin(math.sin(math.radians(theta4))/L3*L1))
    theta5=theta3+leg3_ham
    x3=(math.cos(math.radians(theta5)))*L3
    y3=(math.sin(math.radians(theta5)))*L3
    x3=round(x3)
    y3=round(y3)
#LEG4
def Angle4_calc(x,y):
    global leg4_ham
    global leg4_shank
    L3 = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
    theta1 = math.acos((math.pow(L1, 2) + math.pow(L2, 2) - math.pow(L3, 2)) / (2 * L1 * L2))
    theta1_2 = theta1 * 180 / pi
    leg4_shank =  (180 - theta1_2)
    L4 = math.sqrt(math.pow(L3, 2) - math.pow(x, 2))
    theta3 = math.asin((math.sin(theta1) / L3) * L1)
    theta3_2 = theta3 * 180 / pi
    theta4 = math.atan(L4 / x) 
    theta4_2 = theta4 * 180 / pi
    leg4_ham = theta4_2  - theta3_2 
def Coordinate4_calc(shank_deg,ham_deg):
    global x4
    global y4
    xh1=math.cos(leg4_shank)
    xh=math.degrees(xh1)*L2
    yh=math.sqrt(math.pow(L2,2)+math.pow(L2,2))
    theta4=180-leg4_shank
    L3=math.sqrt(math.pow(L1,2)+math.pow(L2,2)-2*L1*L2*(math.cos(math.radians(theta4))))
    theta3=math.degrees(math.asin(math.sin(math.radians(theta4))/L3*L1))
    theta5=theta3+leg4_ham
    x4=(math.cos(math.radians(theta5)))*L3
    y4=(math.sin(math.radians(theta5)))*L3
    x4=round(x4)
    y4=round(y4)

