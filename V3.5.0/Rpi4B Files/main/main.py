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
import threading
from motion import *
import display as dp
import cam
import controller as ctl
import Serial

cam=0
GIMBAL_X=90
GIMBAL_Y=90
data =[35,100,35,100,35,100,35,100,90,90]
x=90
y=90
SWITCH=[0,0,0,0]
LegGait.GAIT_PLAN(1,50,10,50,-200)
LegGait.GAIT_PLAN(2,50,10,50,-200)
LegGait.GAIT_PLAN(3,50,10,50,-200)
LegGait.GAIT_PLAN(4,50,10,50,-200)
TROT_PLANNER.GAIT("TROT")

def thread1():
    global GIMBAL_X,GIMBAL_Y
    while True:
        ctl.controller()
       
        if ctl.val[1]>0.2 or ctl.val[1]<-0.2 or ctl.val[0]>0.6 or ctl.val[0]<-0.6:
            
            if ctl.val[1]>0.2 and ctl.val[0]>-0.6 and ctl.val[0]<0.6:# backward
                if GAIT_CONTROLL[0]==1:
                    LegGait.GAIT_PLAN(1,20,10,80,-220)
                if GAIT_CONTROLL[1]==1:
                    LegGait.GAIT_PLAN(2,20,10,80,-220)
                if GAIT_CONTROLL[2]==1:
                    LegGait.GAIT_PLAN(3,20,10,80,-220)
                if GAIT_CONTROLL[3]==1:
                    LegGait.GAIT_PLAN(4,20,10,80,-220)
                TROT_PLANNER.SPEED(10,-abs(ctl.val[1])+1.02)
            if ctl.val[1]<-0.2 and ctl.val[0]>-0.6 and ctl.val[0]<0.6:# forward
                if GAIT_CONTROLL[0]==1:
                    LegGait.GAIT_PLAN(1,20,80,10,-220)
                if GAIT_CONTROLL[1]==1:
                    LegGait.GAIT_PLAN(2,20,80,10,-220)
                if GAIT_CONTROLL[2]==1:
                    LegGait.GAIT_PLAN(3,20,80,10,-220)
                if GAIT_CONTROLL[3]==1:
                    LegGait.GAIT_PLAN(4,20,80,10,-220)
                TROT_PLANNER.SPEED(10,-abs(ctl.val[1])+1.02)
            if ctl.val[0]<-0.6 and ctl.val[1]>-0.2 and ctl.val[1]<0.2:# left
                if GAIT_CONTROLL[0]==1:
                    LegGait.GAIT_PLAN(1,20,60,10,-220)
                if GAIT_CONTROLL[1]==1:
                    LegGait.GAIT_PLAN(2,20,80,10,-220)
                if GAIT_CONTROLL[2]==1:
                    LegGait.GAIT_PLAN(3,20,80,10,-220)
                if GAIT_CONTROLL[3]==1:
                    LegGait.GAIT_PLAN(4,20,60,10,-220)
                TROT_PLANNER.SPEED(10,-abs(ctl.val[0])+1.02)
            if ctl.val[0]>0.6 and ctl.val[1]>-0.2 and ctl.val[1]<0.2:# right
                if GAIT_CONTROLL[0]==1:
                    LegGait.GAIT_PLAN(1,20,80,10,-220)
                if GAIT_CONTROLL[1]==1:
                    LegGait.GAIT_PLAN(2,20,60,10,-220)
                if GAIT_CONTROLL[2]==1:
                    LegGait.GAIT_PLAN(3,20,60,10,-220)
                if GAIT_CONTROLL[3]==1:
                    LegGait.GAIT_PLAN(4,20,80,10,-220)
                TROT_PLANNER.SPEED(10,-abs(ctl.val[0])+1.02)

            if ctl.val[3]>0.2:#GIMBAL_X
                GIMBAL_X-=abs(ctl.val[3])*3
                if GIMBAL_X<=0:
                    GIMBAL_X+=3
                
            if ctl.val[3]<-0.2:#GIMBAL_X
                GIMBAL_X+=abs(ctl.val[3])*3
                if GIMBAL_X>=180:
                    GIMBAL_X-=3
            if ctl.val[4]>0.2:#GIMBAL_Y
                GIMBAL_Y+=abs(ctl.val[4])*3
                if GIMBAL_Y>=180:
                    GIMBAL_Y-=3
            if ctl.val[4]<-0.2:#GIMBAL_Y
                GIMBAL_Y-=abs(ctl.val[4])*3
                if GIMBAL_Y<=0:
                    GIMBAL_Y+=3
            data = [ DATA[0], DATA[1], DATA[2], DATA[3], DATA[4], DATA[5], DATA[6], DATA[7], int(GIMBAL_X), int(GIMBAL_Y)]
            data_string = ",".join([str(i) for i in data])
            Serial.senddata(str.encode(data_string))

def thread2():
    while cam:
        cam.FD()

    t2 = threading.Thread(target=thread2)
    t2.start()
def main():
    t1 = threading.Thread(target=thread1)
    t1.start()
if __name__=='__main__':
    main()
dp.display_1()

