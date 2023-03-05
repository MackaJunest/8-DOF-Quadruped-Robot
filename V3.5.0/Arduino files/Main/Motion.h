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
#ifndef __MOTION_H__
#define __MOTION_H__
#include <Servo.h>

long int motion[10];
int shank1, shank2, shank3, shank4, ham1, ham2, ham3, ham4, gimbalx, gimbaly;

Servo L1H;
Servo L1S;
Servo L2H;
Servo L2S;
Servo L3H;
Servo L3S;
Servo L4H;
Servo L4S;
Servo gimbalX;
Servo gimbalY;

void Motion()
{
  motion[0] = Serial.parseInt();
  motion[1] = Serial.parseInt();
  motion[2] = Serial.parseInt();
  motion[3] = Serial.parseInt();
  motion[4] = Serial.parseInt();
  motion[5] = Serial.parseInt();
  motion[6] = Serial.parseInt();
  motion[7] = Serial.parseInt();
  motion[8] = Serial.parseInt();
  motion[9] = Serial.parseInt();
  gimbalx = motion[8];
  gimbaly = motion[9];
  shank1 = (motion[0] + motion[1]);
  shank2 = (motion[2] + motion[3]);
  shank3 = (motion[4] + motion[5]);
  shank4 = (motion[6] + motion[7]);
  ham1 = motion[0];
  ham2 = motion[2];
  ham3 = motion[4];
  ham4 = motion[6];

  L1S.write((shank1) / 1.5); // "/1.5" for 270 degree servo
  L1H.write(ham1 / 1.5);
  L2S.write((shank2)   / 1.5);
  L2H.write(ham2 / 1.5);
  L3S.write((shank3) / 1.5);
  L3H.write(ham3 / 1.5);
  L4S.write((shank4) / 1.5);
  L4H.write(ham4 / 1.5);
  gimbalX.write(gimbalx);
  gimbalY.write(gimbaly);
}
#endif
