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
import pygame
pygame.init()
pygame.joystick.init()
val=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
def controller():
    global val
    for event in pygame.event.get(): # key events
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")
    joystick_count = pygame.joystick.get_count()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    x1=round(joystick.get_axis(0),2)#left joystick
    y1=round(joystick.get_axis(1),2)#left joystick
    x2=round(joystick.get_axis(2),2)#right joystick
    y2=round(joystick.get_axis(3),2)#right joystick
    L2=round(joystick.get_axis(4))#right joystick
    R2=round(joystick.get_axis(5))#right joystick
    b1 = joystick.get_button(0)
    b2 = joystick.get_button(1)
    b3 = joystick.get_button(2)
    b4 = joystick.get_button(3)
    b5 = joystick.get_button(4)
    b6 = joystick.get_button(5)
    b7 = joystick.get_button(6)
    b8 = joystick.get_button(7)
    b9 = joystick.get_button(8)
    b10 = joystick.get_button(9)
    b11 = joystick.get_button(10)
    h1 = joystick.get_hat(0)
    val=[x1,y1,x2,y2,L2,R2,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,h1[0],h1[1]]
