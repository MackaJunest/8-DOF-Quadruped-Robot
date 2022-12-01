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
import kinematics as km
import math
import time
from Serial import ser

hp1=0
hp2=0
hp3=0
hp4=0

x1=0
x2=0
x3=0
x4=0

#func1=-0.04*math.pow(x1,2)+3*x1-235 #
#func1=-0.02*math.pow(x1,2)+2.15*x1-235#
#func2=-0.04*math.pow(x2,2)+3*x1-235 #
#func2=-0.02*math.pow(x2,2)+2.15*x1-235#
#func3=-0.04*math.pow(x3,2)+3*x1-235 #
#func3=-0.02*math.pow(x3,2)+2.15*x1-235#
#func4=-0.04*math.pow(x4,2)+3*x1-235 #
#func4=-0.02*math.pow(x4,2)+2.15*x1-235#

def set_function(function):
    global func1
    global func2
    global func3
    global func4
    if function==1:
        func1=-0.02*math.pow(x1,2)+2.15*x1-235#
        func2=-0.02*math.pow(x2,2)+2.15*x1-235#
        func3=-0.02*math.pow(x3,2)+2.15*x1-235#
        func4=-0.02*math.pow(x4,2)+2.15*x1-235#
    if function==0:
        func1=-0.04*math.pow(x1,2)+3*x1-235 #
        func2=-0.04*math.pow(x2,2)+3*x1-235 #
        func3=-0.04*math.pow(x3,2)+3*x1-235 #
        func4=-0.04*math.pow(x4,2)+3*x1-235 #

def set_range(xmaxium,xminimum):
    global xmax
    global xmini
    global x1
    global x2
    global x3
    global x4
    xmax=xmaxium
    xmini=xminimum
    x1=x3=xmini+1
    x2=x4=xmax-1

def height_adjust(L1,L2,L3,L4,adj):
    global aj1
    global aj2
    global aj3
    global aj4
    aj1=L1+adj
    aj2=L2+adj
    aj3=L3+adj
    aj4=L4+adj

def trotforward(speed):
    global x1
    global x2
    global x3
    global x4
    global hp1
    global hp2
    global hp3
    global hp4
    global aj1
    global aj2
    global aj3
    global aj4
#       leg1
    if x1<xmax and hp1 == 0 :
        y=func1+aj1
#           print(x1)
#           print(y)
        km.Angle1_calc(x1,y)
        km.Coordinate1_calc(km.leg1_shank,km.leg1_ham)
        s1= str(int(round(km.leg1_shank)))
        h1= str(int(round(km.leg1_ham)))
        x1+=speed
        if x1 >=xmax:
            hp1=1

    if x1>xmini and hp1 == 1:
        y=-210+aj1
#           print(x1)
#           print(y)
        km.Angle1_calc(x1,y)
        km.Coordinate1_calc(km.leg1_shank,km.leg1_ham)
        s1= str(int(round(km.leg1_shank)))
        h1= str(int(round(km.leg1_ham)))
        x1-=speed
        if x1 <=xmini:
            hp1=0



#       leg2
    if x2<xmax and hp2 == 0 :
        y=func2+aj2
#           print(x2)
#           print(y)
        km.Angle2_calc(x2,y)
        km.Coordinate2_calc(km.leg2_shank,km.leg2_ham)
        s2= str(int(round(km.leg2_shank)))
        h2= str(int(round(km.leg2_ham)))
        x2+=speed
        if x2 >=xmax:
            hp2=1

    if x2>xmini and hp2 == 1:
        y=-210+aj2
#           print(x2)
#           print(y)
        km.Angle2_calc(x2,y)
        km.Coordinate2_calc(km.leg2_shank,km.leg2_ham)
        s2= str(int(round(km.leg2_shank)))
        h2= str(int(round(km.leg2_ham)))
        x2-=speed
        if x2<=xmini:
            hp2=0



#       leg3
    if x3<xmax and hp3 == 0 :
        y=func3+aj3
#           print(x3)
#           print(y)
        km.Angle3_calc(x3,y)
        km.Coordinate3_calc(km.leg3_shank,km.leg3_ham)
        s3= str(int(round(km.leg3_shank)))
        h3= str(int(round(km.leg3_ham)))
        x3+=speed
        if x3 >=xmax:
            hp3=1

    if x3>xmini and hp3 == 1:
        y=-210+aj3
#           print(x3)
#           print(y)
        km.Angle3_calc(x3,y)
        km.Coordinate3_calc(km.leg3_shank,km.leg3_ham)
        s3= str(int(round(km.leg3_shank)))
        h3= str(int(round(km.leg3_ham)))
        x3-=speed
        if x3 <=xmini:
            hp3=0



#       leg4
    if x4<xmax and hp4 == 0 :
        y=func4+aj4
#           print(x4)
#           print(y)
        km.Angle4_calc(x4,y)
        km.Coordinate4_calc(km.leg4_shank,km.leg4_ham)
        s4= str(int(round(km.leg4_shank)))
        h4= str(int(round(km.leg4_ham)))
        x4+=speed
        if x4 >=xmax:
            hp4=1

    if x4>xmini and hp4 == 1:
        y=-210+aj4
#           print(x4)
#           print(y)
        km.Angle4_calc(x4,y)
        km.Coordinate4_calc(km.leg4_shank,km.leg4_ham)
        s4= str(int(round(km.leg4_shank)))
        h4= str(int(round(km.leg2_ham)))
        x4-=speed
        if x4<=xmini:
            hp4=0

    print(h1+','+s1+','+h2+','+s2+','+h3+','+s3+','+h4+','+s4)
    ser.write(h1+','+s1+','+h2+','+s2+','+h3+','+s3+','+h4+','+s4)
    time.sleep(0.0003)

def trotbackward(speed):
    global x1
    global x2
    global x3
    global x4
    global hp1
    global hp2
    global hp3
    global hp4
#       leg1
    if x1>xmini and hp1 == 0 :
        y=func1+aj1
#           print(x1)
#           print(y)
        km.Angle1_calc(x1,y)
        km.Coordinate1_calc(km.leg1_shank,km.leg1_ham)
        s1= str(int(round(km.leg1_shank)))
        h1= str(int(round(km.leg1_ham)))
        x1-=speed
        if x1 <=xmini:
            hp1=1

    if x1<xmax and hp1 == 1:
        y=-210+aj1
#           print(x1)
#           print(y)
        km.Angle1_calc(x1,y)
        km.Coordinate1_calc(km.leg1_shank,km.leg1_ham)
        s1= str(int(round(km.leg1_shank)))
        h1= str(int(round(km.leg1_ham)))
        x1+=speed
        if x1 >=xmax:
            hp1=0


#       leg2
    if x2>xmini and hp2 == 0 :
        y=func2+aj2
#           print(x2)
#           print(y)
        km.Angle2_calc(x2,y)
        km.Coordinate2_calc(km.leg2_shank,km.leg2_ham)
        s2= str(int(round(km.leg2_shank)))
        h2= str(int(round(km.leg2_ham)))
        x2-=speed
        if x2 <=xmini:
            hp2=1

    if x2<xmax and hp2 == 1:
        y=-210+aj2
#           print(x2)
#           print(y)
        km.Angle2_calc(x2,y)
        km.Coordinate2_calc(km.leg2_shank,km.leg2_ham)
        s2= str(int(round(km.leg2_shank)))
        h2= str(int(round(km.leg2_ham)))
        x2+=speed
        if x2 >=xmax:
            hp2=0



#       leg3
    if x3>xmini and hp3 == 0 :
        y=func3+aj3
#           print(x3)
#           print(y)
        km.Angle3_calc(x3,y)
        km.Coordinate3_calc(km.leg3_shank,km.leg3_ham)
        s3= str(int(round(km.leg3_shank)))
        h3= str(int(round(km.leg3_ham)))
        x3-=speed
        if x3 <=xmini:
            hp3=1

    if x3<xmax and hp3 == 1:
        y=-210+aj3
#           print(x3)
#           print(y)
        km.Angle3_calc(x3,y)
        km.Coordinate3_calc(km.leg3_shank,km.leg3_ham)
        s3= str(int(round(km.leg3_shank)))
        h3= str(int(round(km.leg3_ham)))
        x3+=speed
        if x3 >=xmax:
            hp3=0



#       leg4
    if x4>xmini and hp4 == 0 :
        y=func4+aj4
#           print(x4)
#           print(y)
        km.Angle4_calc(x4,y)
        km.Coordinate4_calc(km.leg4_shank,km.leg4_ham)
        s4= str(int(round(km.leg4_shank)))
        h4= str(int(round(km.leg4_ham)))
        x4-=speed
        if x4 <=xmini:
            hp4=1

    if x4<xmax and hp4 == 1:
        y=-210+aj4
#           print(x4)
#           print(y)
        km.Angle4_calc(x4,y)
        km.Coordinate4_calc(km.leg4_shank,km.leg4_ham)
        s4= str(int(round(km.leg4_shank)))
        h4= str(int(round(km.leg2_ham)))
        x4+=speed
        if x4 >=xmax:
            hp4=0


    print(h1+','+s1+','+h2+','+s2+','+h3+','+s3+','+h4+','+s4)
    ser.write(h1+','+s1+','+h2+','+s2+','+h3+','+s3+','+h4+','+s4)
    time.sleep(0.0003)

def trotturnleft(speed):
    global x1
    global x2
    global x3
    global x4
    global hp1
    global hp2
    global hp3
    global hp4
#       leg1 forward
    if x1<xmax and hp1 == 0 :
        y=func1+aj1
#           print(x1)
#           print(y)
        km.Angle1_calc(x1,y)
        km.Coordinate1_calc(km.leg1_shank,km.leg1_ham)
        s1= str(int(round(km.leg1_shank)))
        h1= str(int(round(km.leg1_ham)))
        x1+=speed
        if x1 >=xmax:
            hp1=1

    if x1>xmini and hp1 == 1:
        y=-210+aj1
#           print(x1)
#           print(y)
        km.Angle1_calc(x1,y)
        km.Coordinate1_calc(km.leg1_shank,km.leg1_ham)
        s1= str(int(round(km.leg1_shank)))
        h1= str(int(round(km.leg1_ham)))
        x1-=speed
        if x1 <=xmini:
            hp1=0


#       leg2 backward
    if x2>xmini and hp2 == 0 :
        y=func2+aj2
#           print(x2)
#           print(y)
        km.Angle2_calc(x2,y)
        km.Coordinate2_calc(km.leg2_shank,km.leg2_ham)
        s2= str(int(round(km.leg2_shank)))
        h2= str(int(round(km.leg2_ham)))
        x2-=speed
        if x2 <=xmini:
            hp2=1

    if x2<xmax and hp2 == 1:
        y=-210+aj2
#           print(x2)
#           print(y)
        km.Angle2_calc(x2,y)
        km.Coordinate2_calc(km.leg2_shank,km.leg2_ham)
        s2= str(int(round(km.leg2_shank)))
        h2= str(int(round(km.leg2_ham)))
        x2+=speed
        if x2 >=xmax:
            hp2=0



#       leg3 backward
    if x3>xmini and hp3 == 0 :
        y=func3+aj3
#           print(x3)
#           print(y)
        km.Angle3_calc(x3,y)
        km.Coordinate3_calc(km.leg3_shank,km.leg3_ham)
        s3= str(int(round(km.leg3_shank)))
        h3= str(int(round(km.leg3_ham)))
        x3-=speed
        if x3 <=xmini:
            hp3=1

    if x3<xmax and hp3 == 1:
        y=-210+aj3
#           print(x3)
#           print(y)
        km.Angle3_calc(x3,y)
        km.Coordinate3_calc(km.leg3_shank,km.leg3_ham)
        s3= str(int(round(km.leg3_shank)))
        h3= str(int(round(km.leg3_ham)))
        x3+=speed
        if x3 >=xmax:
            hp3=0


#       leg4 forward
    if x4<xmax and hp4 == 0 :
        y=func4+aj4
#           print(x4)
#           print(y)
        km.Angle4_calc(x4,y)
        km.Coordinate4_calc(km.leg4_shank,km.leg4_ham)
        s4= str(int(round(km.leg4_shank)))
        h4= str(int(round(km.leg4_ham)))
        x4+=speed
        if x4 >=xmax:
            hp4=1

    if x4>xmini and hp4 == 1:
        y=-210+aj4
#           print(x4)
#           print(y)
        km.Angle4_calc(x4,y)
        km.Coordinate4_calc(km.leg4_shank,km.leg4_ham)
        s4= str(int(round(km.leg4_shank)))
        h4= str(int(round(km.leg2_ham)))
        x4-=speed
        if x4<=xmini:
            hp4=0


    print(h1+','+s1+','+h2+','+s2+','+h3+','+s3+','+h4+','+s4)
    ser.write(h1+','+s1+','+h2+','+s2+','+h3+','+s3+','+h4+','+s4)
    time.sleep(0.0003)

def trotturnright(speed):
    global x1
    global x2
    global x3
    global x4
    global hp1
    global hp2
    global hp3
    global hp4
#       leg1 backward
    if x1>xmini and hp1 == 0 :
        y=func1+aj1
#           print(x1)
#           print(y)
        km.Angle1_calc(x1,y)
        km.Coordinate1_calc(km.leg1_shank,km.leg1_ham)
        s1= str(int(round(km.leg1_shank)))
        h1= str(int(round(km.leg1_ham)))
        x1-=speed
        if x1 <=xmini:
            hp1=1

    if x1<xmax and hp1 == 1:
        y=-210+aj1
#           print(x1)
#           print(y)
        km.Angle1_calc(x1,y)
        km.Coordinate1_calc(km.leg1_shank,km.leg1_ham)
        s1= str(int(round(km.leg1_shank)))
        h1= str(int(round(km.leg1_ham)))
        x1+=speed
        if x1 >=xmax:
            hp1=0


#       leg2 forward
    if x2<xmax and hp2 == 0 :
        y=func2+aj2
#           print(x2)
#           print(y)
        km.Angle2_calc(x2,y)
        km.Coordinate2_calc(km.leg2_shank,km.leg2_ham)
        s2= str(int(round(km.leg2_shank)))
        h2= str(int(round(km.leg2_ham)))
        x2+=speed
        if x2 >=xmax:
            hp2=1

    if x2>xmini and hp2 == 1:
        y=-210+aj2
#           print(x2)
#           print(y)
        km.Angle2_calc(x2,y)
        km.Coordinate2_calc(km.leg2_shank,km.leg2_ham)
        s2= str(int(round(km.leg2_shank)))
        h2= str(int(round(km.leg2_ham)))
        x2-=speed
        if x2<=xmini:
            hp2=0



#       leg3 forward
    if x3<xmax and hp3 == 0 :
        y=func3+aj3
#           print(x3)
#           print(y)
        km.Angle3_calc(x3,y)
        km.Coordinate3_calc(km.leg3_shank,km.leg3_ham)
        s3= str(int(round(km.leg3_shank)))
        h3= str(int(round(km.leg3_ham)))
        x3+=speed
        if x3 >=xmax:
            hp3=1

    if x3>xmini and hp3 == 1:
        y=-210+aj3
#           print(x3)
#           print(y)
        km.Angle3_calc(x3,y)
        km.Coordinate3_calc(km.leg3_shank,km.leg3_ham)
        s3= str(int(round(km.leg3_shank)))
        h3= str(int(round(km.leg3_ham)))
        x3-=speed
        if x3 <=xmini:
            hp3=0


#       leg4 backward
    if x4>xmini and hp4 == 0 :
        y=func4+aj4
#           print(x4)
#           print(y)
        km.Angle4_calc(x4,y)
        km.Coordinate4_calc(km.leg4_shank,km.leg4_ham)
        s4= str(int(round(km.leg4_shank)))
        h4= str(int(round(km.leg4_ham)))
        x4-=speed
        if x4 <=xmini:
            hp4=1

    if x4<xmax and hp4 == 1:
        y=-210+aj4
#           print(x4)
#           print(y)
        km.Angle4_calc(x4,y)
        km.Coordinate4_calc(km.leg4_shank,km.leg4_ham)
        s4= str(int(round(km.leg4_shank)))
        h4= str(int(round(km.leg2_ham)))
        x4+=speed
        if x4 >=xmax:
            hp4=0


    print(h1+','+s1+','+h2+','+s2+','+h3+','+s3+','+h4+','+s4)
    ser.write(h1+','+s1+','+h2+','+s2+','+h3+','+s3+','+h4+','+s4)
    time.sleep(0.01)
    
def return_0():
    ser.write('0'+','+'0'+','+'0'+','+'0'+','+'0'+','+'0'+','+'0'+','+'0')
#trotbackward(1)
#trotforward(1)
#trotturnright(1)
#trotturnleft(1)
#return_0()
