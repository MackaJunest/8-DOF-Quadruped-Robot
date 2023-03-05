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
