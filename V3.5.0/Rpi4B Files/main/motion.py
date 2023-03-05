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
               legs     leg1|    |leg2
    4 groups: 1,2-|1        |    |
              3,4-|2       Jimmychen
              5,6-|3        |    |
              7,8-|4    leg4|    |leg3
                             back


'''
import kinematics as km #import IK Kinematics module
import math # import some necessary 
import time

#[leg:1,2,3,4]
x=[0,0,0,0]
PROGRESS_CHECKER=[1,0,1,0]
MINIMUM=[0,0,0,0]
MAXIMUM=[0,0,0,0]
Y_VALUES=[0,0,0,0]
STEP=[0,0,0,0]
GAIT_CONTROLL=[0,0,0,0]

DATA=[0,0,0,0,0,0,0,0]#[ham,shank,ham,shank,ham,shank,ham,shank]

class LegGait:
    
    A,B,C,D = (0, 0, 0, 0)
    
    def GAIT_PLAN(leg, height, start, end, v_shift):#(leg NO., the amplitude of the sin wave, starting point(horizontal shift), ending point(where the sinwave gets to the first turining point), vertical shift)
        
        LegGait.A = height
        LegGait.B = (2*math.pi) / (abs(end-start) * 2)
        if start< end:
            LegGait.C = start
        elif end< start:
            LegGait.C = end
        MINIMUM[leg-1] = start
        MAXIMUM[leg-1] = end
        LegGait.D = v_shift
        
        
        Y_VALUES[leg-1] = v_shift
    
    def calc(leg, x):
        return LegGait.A * math.sin(LegGait.B * (x - LegGait.C)) + LegGait.D # formular of sin wave f(x)=A*sin(B*(x-C))+D
    
    def MOTOR_CONTROLL(leg, x, switch):#(leg NO., x_value, 1:sinwave/2:linear equation)
        if switch == 0:
            y= LegGait.calc(leg,x)
        elif switch == 1:
            y=Y_VALUES[leg-1]

        if leg == 1:
            km.Angle1_calc(x, y)# use Angle(Leg NO.)_calc(x,y) function from kinematics to calculate the angle for each motor.
            s = int(round(km.leg1_shank))# use variable leg(Leg NO.)_shank/ham from kinematics for the result of the IK calculation 
            h = int(round(km.leg1_ham))
            if s < 0 :
                s=abs(180+s)# use abs(180+shank_value) to eliminate the negative value from calculation
            if h < 0 :
                h=abs(180+h)# use abs(180+ham_value) to eliminate the negative value from calculation
            DATA[0]=h#put the data into the list DATA{8} for further communication with the arduino MEGA 2560 board.
            DATA[1]=s#put the data into the list DATA{8} for further communication with the arduino MEGA 2560 board.
        
        elif leg == 2:
            km.Angle2_calc(x, y)
            s = int(round(km.leg2_shank))
            h = int(round(km.leg2_ham))
            if s < 0 :
                s=abs(180+s)
            if h < 0 :
                h=abs(180+h)
            DATA[2]=h
            DATA[3]=s

        elif leg == 3:
            km.Angle3_calc(x, y)
            s = int(round(km.leg3_shank))
            h = int(round(km.leg3_ham))
            if s < 0 :
                s=abs(180+s)
            if h < 0 :
                h=abs(180+h)
            DATA[4]=h
            DATA[5]=s

        elif leg == 4:
            km.Angle4_calc(x, y)
            s = int(round(km.leg4_shank))
            h = int(round(km.leg4_ham))
            if s < 0 :
                s=abs(180+s)
            if h < 0 :
                h=abs(180+h)
            DATA[6]=h
            DATA[7]=s
        return (s, h)

class TROT_PLANNER:
    
    def GAIT(GAIT):
        if GAIT=="TROT":
            x[0] = MAXIMUM[0]# with trot gait, the robot will move in a pattern of leg: (1,3)---(2,4) and I did this by using different starting points to get the different starting for my robot
            x[1] = MINIMUM[1]
            x[2] = MAXIMUM[2]
            x[3] = MINIMUM[3]
    
    def SPEED(CYCLE_TIME,PROCESSING_SPEED):
        for i in range (0,4):# the repeat here used to let the calculation run for each of the four legs            
            
            STEP[i]=(abs(MAXIMUM[i]-MINIMUM[i]))/CYCLE_TIME# the length of the step, used to keep sure that the movement of the legs are synchronized(finish their cycle in the same time)
            
            if MINIMUM[i]<MAXIMUM[i]:# the robot is moving backward
                if x[i]<=MAXIMUM[i] and PROGRESS_CHECKER[i]==0:# cycle:sinwave 
                    GAIT_CONTROLL[i]=0

                    LegGait.MOTOR_CONTROLL(i+1, x[i],0)
                    x[i]+=STEP[i]
                    if x[i] >=MAXIMUM[i]:
                        PROGRESS_CHECKER[i]=1# help the proramme to know the current coordinate is still in the range or not

                if x[i]>=MINIMUM[i] and PROGRESS_CHECKER[i]==1:# cycle:linear equation
                    LegGait.MOTOR_CONTROLL(i+1, x[i],1)
                    x[i]-=STEP[i]
                    if x[i] <=MINIMUM[i]:
                        PROGRESS_CHECKER[i]=0# help the proramme to know the current coordinate is still in the range or not
                        GAIT_CONTROLL[i]=1

            if MAXIMUM[i]<MINIMUM[i]:# the robot is moving forward
                if x[i]<=MINIMUM[i] and PROGRESS_CHECKER[i]==0:# cycle:linear equation 
                    GAIT_CONTROLL[i]=0
                    LegGait.MOTOR_CONTROLL(i+1, x[i],1)   
                    x[i]+=STEP[i]
                    if x[i] >=MINIMUM[i]:
                        PROGRESS_CHECKER[i]=1# help the proramme to know the current coordinate is still in the range or not

                if x[i]>=MAXIMUM[i] and PROGRESS_CHECKER[i]==1:# cycle:sinwave
                    LegGait.MOTOR_CONTROLL(i+1, x[i],0)
                    x[i]-=STEP[i]
                    if x[i] <=MAXIMUM[i]:
                        PROGRESS_CHECKER[i]=0# help the programme to know the current coordinate is still in the range or not
                        GAIT_CONTROLL[i]=1
        time.sleep(PROCESSING_SPEED)
        


'''
LegGait.GAIT_PLAN(1,50,10,50,-200)
LegGait.GAIT_PLAN(2,50,10,50,-200)
LegGait.GAIT_PLAN(3,50,10,50,-200)
LegGait.GAIT_PLAN(4,50,10,50,-200)
TROT_PLANNER.GAIT("TROT")

while 1:
    TROT_PLANNER.SPEED(50)
    if GAIT_CONTROLL[0]==1:
        LegGait.GAIT_PLAN(1,50,10,50,-200)
        print(1)
    if GAIT_CONTROLL[1]==1:
        LegGait.GAIT_PLAN(2,50,10,50,-200)
        print(2)
    if GAIT_CONTROLL[2]==1:
        LegGait.GAIT_PLAN(3,50,10,50,-200)
        print(3)
    if GAIT_CONTROLL[3]==1:
        LegGait.GAIT_PLAN(4,50,10,50,-200)
        print(4)
'''

    

        
        