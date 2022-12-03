#!/usr/bin/env python
# -*- coding: utf-8 -*-
#JimmyChen V3.0 by MackaJunest COPYRIGHT 2022
'''
                            front
                   leg  leg1|    |leg2
    4 groups: 1,2  -|1      |    |
              3,4  -|2_____Jimmychen
              5,6  -|3      |    |
              7,8  -|4  leg3|    |leg4
                             back
'''
import threading
import motion
import display as dp
import cam
import pygame


motion.set_function(1)
motion.set_range(90,10)
motion.height_adjust(1,-2,1,-2,0)
pygame.init()
pygame.joystick.init()
cam=0

def thread1():
    while True:
        for event in pygame.event.get(): 
            if event.type == pygame.JOYBUTTONDOWN:
                print("Joystick button pressed.")
            if event.type == pygame.JOYBUTTONUP:
                print("Joystick button released.")
        joystick_count = pygame.joystick.get_count()
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        x1=round(joystick.get_axis(0),2)#left joystick
        y1=round(joystick.get_axis(1),2)#left joystick
        x2=round(joystick.get_axis(4),2)#right joystick
        y2=round(joystick.get_axis(3),2)#right joystick
        L2=round(joystick.get_axis(2),2)#right joystick
        R2=round(joystick.get_axis(5),2)#right joystick
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
        if val[1]<-0.5:
            motion.trotforward(4)
        if val[1]>0.5:
            motion.trotbackward(4)
        if val[0]<-0.5:
            motion.trotturnright(4)
        if val[0]>0.5:
            motion.trotturnleft(4)
        cam=val[5]
def thread2():
    while cam:
        cam.FD()
def main():
    t1 = threading.Thread(target=thread1)
    t1.start()
    t2 = threading.Thread(target=thread2)
    t2.start()
if __name__=='__main__':
    main()
dp.display_1()
