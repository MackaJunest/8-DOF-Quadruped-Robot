#!/usr/bin/env python2
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
from tkinter import *
import time
import os
root = Tk()
root.overrideredirect(True)

def display_1():
    numIdx = 75# gif的帧数
    frames = [PhotoImage(file='display_1.gif', format='gif -index %i' %(i)) for i in range(numIdx)]

    def update(idx): # 定时器函数
        frame = frames[idx]
        idx += 1 # 下一帧的序号：在0,1,2,3,4,5之间循环(共6帧)
        label.configure(image=frame) # 显示当前帧的图片
        root.after(50, update, idx%numIdx) # 0.1秒(100毫秒)之后继续执行定时器函数(update)

    label = Label(root)
    label.pack()
    root.after(0, update, 0) # 立即启动定时器函数(update)
    root.mainloop()
