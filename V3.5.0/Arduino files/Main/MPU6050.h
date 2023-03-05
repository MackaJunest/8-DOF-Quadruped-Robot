/*
  Copyright © 2022 MackaJunest
  Permission is hereby granted, free of charge, to any person obtaining a copy of
  this software and associated documentation files (the “Software”), to deal in
  the Software without restriction, including without limitation the rights to
  use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
  of the Software, and to permit persons to whom the Software is furnished to do
  so, subject to the following conditions:

  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
  SOFTWARE.
**************************************************************************************

                 Front
                 ____
           Leg1 |    |Leg2
     left       |    |       right
                |    |
           Leg4  ---- Leg3
                 Back
    H=ham
    S=shank

    L1H ____
    L1S     LEG1

    L2H ____
    L2S     LEG2

    L3H ____
    L3S     LEG3

    L4H ____
    L4S     LEG4
*/
#ifndef __MPU6050_H__
#define __MPU6050_H__
#include "Wire.h"
#include <MPU6050_light.h>

MPU6050 mpu(Wire);

long timer = 0;
String MPU_VAL[7];//agx,agy,agz,ax,ay,az,temp


void MPU_Setup()
{
  Wire.begin();
  byte status = mpu.begin();
  while (status != 0) { } // stop everything if could not connect to MPU6050
  mpu.calcOffsets(true, true); // gyro and accelero
}

void MPU_Value()
{
  mpu.update();
  if (millis() - timer > 10)
  {
    MPU_VAL[0] = mpu.getAngleX();
    MPU_VAL[1] = mpu.getAngleY();
    MPU_VAL[2] = mpu.getAngleZ();
    MPU_VAL[3] = mpu.getAccX();
    MPU_VAL[4] = mpu.getAccY();
    MPU_VAL[5] = mpu.getAccZ();
    MPU_VAL[6] = mpu.getTemp();
    timer = millis();
  }
}


#endif
